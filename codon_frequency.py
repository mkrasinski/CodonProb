import ensembl
import sys
from collections import defaultdict

if __name__ == '__main__':
    if len(sys.argv) == 2:
        client = ensembl.EnsemblRestClient()
        seq_id = sys.argv[1]
        ref = client.get_sequence( seq_id )
        sequence = ref['seq']
        sequence = sequence.replace('T','U')

        #RNA codon table from http://en.wikipedia.org/wiki/Genetic_code
        codon_table = ((('GCU', 'GCC', 'GCA', 'GCG'),  'Alanine'),
               (('UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'),  'Leucine'),
               (('CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'),  'Arginine'),
               (('AAA', 'AAG'),  'Lysine'),
               (('AAU', 'AAC'),  'Asparagine'),
               (('AUG',),  'Methionine'),
               (('GAU', 'GAC'),  'Aspartic_acid' ),
               (('UUU', 'UUC'),  'Phenylalanine'),
               (('UGU', 'UGC'),  'Cysteine'),
               (('CCU', 'CCC', 'CCA', 'CCG'),  'Proline') ,
               (('CAA', 'CAG'),  'Glutamine'),
               (('UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'),  'Serine'),
               (('GAA', 'GAG'),  'Glutamic_acid'),
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
        print "|-------------|-------------------|-----|------------------|-----------|-----------|---------|\n"+\
              "|  Amino-acid |   AA prob         |Codon|   Codon prob     | All AAs # | This AA # | Codon # |\n"+\
              "|-------------|-------------------|-----|------------------|-----------|-----------|---------|\n"
        display = '\n'.join(
                '\n'.join('%s   %-17s  %s   %-17s      %-9s   %-9s  %s' %
                          (aa.rjust(13),freq[codgrp],cod.rjust(4),freq[cod],sum(grp_count.values()),grp_count[siblings[cod]],cod_count[cod])
                          for i,cod in enumerate(codgrp) if grp_count[siblings[cod]] > 0 )
                for codgrp,aa in codon_table)

        print display

    else:
        print """This is a script for analysing frequency of amino-acid occurrence
                    Usage: python codon_frequency.py [ensembl_id]
                        [ensembl_id] is expected to have Ensembl object linked to it.
                    For example:
                    python codon_frequency.py ENSG00000157764
              """