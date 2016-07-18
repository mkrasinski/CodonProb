import ensembl
import sys, getopt
from collections import defaultdict

def compute_frequency( seq_id, codon_table, showtable):
    seq_id = seq_id.rstrip('\n')
    if not( seq_id.startswith("ENS") and len(seq_id) == 15):
        sys.stderr.write( seq_id + ' is not an Ensembl id' + '\n')
        return None
    client = ensembl.EnsemblRestClient()
    ref = client.get_sequence( seq_id )
    sequence = ref['seq']
    sequence = sequence.replace('T','U')

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
    if showtable == 'true':
        print "|-------------|-------------------|-----|------------------|-----------|-----------|---------|\n"+\
              "|  Amino-acid |   AA prob         |Codon|   Codon prob     | All AAs # | This AA # | Codon # |\n"+\
              "|-------------|-------------------|-----|------------------|-----------|-----------|---------|\n"
    display = '\n'.join(
            '\n'.join('%s   %-17s  %s   %-17s      %-9s   %-9s  %s' %
                      (aa.rjust(13),freq[codgrp],cod.rjust(4),freq[cod],sum(grp_count.values()),grp_count[siblings[cod]],cod_count[cod])
                      for i,cod in enumerate(codgrp) if grp_count[siblings[cod]] > 0 )
            for codgrp,aa in codon_table)
    print display

if __name__ == '__main__':
    usage_text = """This is a script for analysing frequency of amino-acid occurrence
Usage:
    python codon_frequency.py [-t] [-i input_file] [-o output_file] [ensembl_id]

        -h              print this help screen
        -t              adds table header to output
        -i              specify input file with list of Ensembl ids
        -o              specify output file (default is stdout)
        ensembl_id      run script for this specified Ensembl id only (while input file is not provided)

    For example:
    python codon_frequency.py -t ENSG00000157764
    python codon_frequency.py -i in.txt -o out.txt
"""

    if len(sys.argv) > 1:
        inputfile = ''
        outputfile = ''
        showtable = 'false'
        try:
            opts, args = getopt.getopt(sys.argv[1:],"hi:o:t",["ifile=","ofile="])
        except getopt.GetoptError:
            print usage_text
            sys.exit()

        for opt, arg in opts:
            if opt == '-h':
                print usage_text
                sys.exit()
            elif opt == '-t':
                showtable = 'true'
            elif opt in ("-i", "--ifile"):
                inputfile = arg
            elif opt in ("-o", "--ofile"):
                outputfile = arg
        if inputfile <> '':
            print 'Input file is ', inputfile
        else:
            print 'No input file provided, running script for Ensembl id ' + sys.argv[-1]

        if outputfile <> '':
            print 'Output file is ', outputfile
            sys.stdout = open(outputfile, 'w')

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
                       (('UAA', 'UGA', 'UAG'),  'STOP') )

        if inputfile <> '':
            with open(inputfile,'r') as f:
                content = f.readlines()
                for seq_id in content:
                    compute_frequency( seq_id, codon_table, showtable)
        else:
            compute_frequency( sys.argv[-1], codon_table, showtable)

    else:
        print usage_text