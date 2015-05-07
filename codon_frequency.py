import ensembl
import sys
from collections import defaultdict

if __name__ == '__main__':
    if len(sys.argv) == 3:
        client = ensembl.EnsemblRestClient()
        species = sys.argv[1]
        symbol = sys.argv[2]
        ref = client.get_xrefs_symbol(species = species, symbol = symbol)
        #add verification if ref came back non-empty
        for obj in ref:
            print obj['type'] + ' ' + obj['id']
        ref = client.get_sequence( ref["type" == "gene"]["id"] )
        sequence = ref['seq']
        sequence = sequence.replace('T','U')
        #print "Sequence: " + sequence

        #RNA codon table from http://en.wikipedia.org/wiki/Genetic_code
        codon_table = ((('GCU', 'GCC', 'GCA', 'GCG'),  'Alanine'),
               (('UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'),  'Leucine'),
               (('CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'),  'Arginine'),
               (('AAA', 'AAG'),  'Lysine'),
               (('AAU', 'AAC'),  'Asparagine'),
               (('AUG',),  'Methionine'),
               (('GAU', 'GAC'),  'Aspartic acid' ),
               (('UUU', 'UUC'),  'Phenylalanine'),
               (('UGU', 'UGC'),  'Cysteine'),
               (('CCU', 'CCC', 'CCA', 'CCG'),  'Proline') ,
               (('CAA', 'CAG'),  'Glutamine'),
               (('UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'),  'Serine'),
               (('GAA', 'GAG'),  'Glutamic acid'),
               (('ACU', 'ACC', 'ACA', 'ACG'),  'Threonine'),
               (('GGU', 'GGC', 'GGA', 'GGG'),  'Glycine'),
               (('UGG',),  'Tryptophane'),
               (('CAU', 'CAC'),  'Histidine'),
               (('UAU', 'UAC'),  'Tyrosine'),
               (('AUU', 'AUC', 'AUA'),  'Isoleucine'),
               (('GUU', 'GUC', 'GUA', 'GUG'),  'Valine'),
               (('UAA', 'UGA', 'UAG'),  'STOP')            )
        #for each codon siblings points a list of other codons for the same aa
        siblings = dict( (cod, codgroup) for codgroup,aa in codon_table for cod in codgroup )

        cod_count, grp_count, freq = defaultdict(int), defaultdict(int), {}

        #counting each codon and each aa
        for cod in (sequence[i:i+3] for i in xrange(0,len(sequence),3)):
            if len(cod) == 3:
                cod_count[cod] += 1
                grp_count[siblings[cod]] += 1

        for cod in siblings.iterkeys(): # the keys of siblings are the 64 codons
            if siblings[cod] in grp_count: #grp_count has value only if aa occurred
                freq[cod] = float(cod_count[cod])/grp_count[siblings[cod]]
                freq[siblings[cod]] = float(grp_count[siblings[cod]])/sum(grp_count.values())
            else:
                freq[cod] = '-* Missing *-'
                freq[siblings[cod]] = '-* Missing *-'
        print "|-------------|-----|---------------|-----------------|\n"+\
              "|  Amino-acid |Codon|  Codon prob   |   AA prob       |\n"+\
              "|-------------|-----|---------------|-----------------|\n"
        display = '\n'.join(aa.rjust(13)+' '+\
                '\n'.join('%s  %-16s %-16s' % (cod.rjust(19 if i else 5),freq[cod],freq[codgrp])
                          for i,cod in enumerate(codgrp))
                for codgrp,aa in codon_table)

        print display

    else:
        print """This is a script for analysing frequency of amino-acid occurrence

                    Usage: python codon_frequency.py [species] [symbol]
                        [symbol] is expected to have Ensembl object linked to it.
                    For example:
                    python get_xrefs_symbol.py homo_sapiens BRCA2
              """