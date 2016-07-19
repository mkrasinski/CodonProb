from Bio.PDB.PDBParser import PDBParser
import ensembl
from pdb_seq_mapping import pdb_seq_mapping
from Bio import pairwise2
import urllib,urllib2
import requests
import xml.etree.ElementTree as ET
import os.path, sys, getopt

def cod_vr_mapping( pdb_chain_id, vr_filename, transcriptId, alignment ):
        # amino acids codes dictionary definition
        aaCodes = dict()
        aaCodes['G'] = 'Gly' #GLYCINE
        aaCodes['P'] = 'Pro' #PROLINE
        aaCodes['A'] = 'Ala' #ALANINE
        aaCodes['V'] = 'Val' #VALINE
        aaCodes['L'] = 'Leu' #LEUCINE
        aaCodes['I'] = 'Ile' #ISOLEUCINE
        aaCodes['M'] = 'Met' #METHIONINE
        aaCodes['C'] = 'Cys' #CYSTEINE
        aaCodes['F'] = 'Phe' #PHENYLALANINE
        aaCodes['Y'] = 'Tyr' #TYROSINE
        aaCodes['W'] = 'Trp' #TRYPTOPHAN
        aaCodes['H'] = 'His' #HISTIDINE
        aaCodes['K'] = 'Lys' #LYSINE
        aaCodes['R'] = 'Arg' #ARGININE
        aaCodes['Q'] = 'Gln' #GLUTAMINE
        aaCodes['N'] = 'Asn' #ASPARAGINE
        aaCodes['E'] = 'Glu' #GLUTAMIC ACID
        aaCodes['D'] = 'Asp' #ASPARTIC ACID
        aaCodes['S'] = 'Ser' #SERINE
        aaCodes['T'] = 'Thr' #THREONINE

        client = ensembl.EnsemblRestClient()

        ref = client.get_sequence( transcriptId , type="protein")
        ensembl_protein_seq = ref['seq']
        #print ensembl_protein_seq
        #print alignment
        ref = client.get_sequence( transcriptId , type="cds")
        cod_seq = ref['seq']
        cod_seq = cod_seq.replace('T','U')
        cod_seq = [cod_seq[i:i+3] for i in range(0, len(cod_seq), 3)]
        #print cod_seq

        if os.path.exists(vr_filename):
            with open(vr_filename) as vr_file:
                content = vr_file.readlines()
            vr_file.close()

            VR = []
            for line in content:
                VR.append(line.split())

            #print VR
            i = 0
            j = 0
            for k in alignment:
                    #print 'k:' + str(k) +' l:' + ensembl_protein_seq[j]
                    if j < len(ensembl_protein_seq):
                        if k == ensembl_protein_seq[j]:
                            i = i + 1
                            for row in VR:
                                if int(row[0]) == i:
                                    #print row
                                    print pdb_chain_id + ' ' + aaCodes[k] + ' ' + cod_seq[j] + ' ' +  row[0] + ' ' + row[1] + ' ' + row[2] + ' ' + row[3]
                        j = j + 1

            #pdbId = sys.argv[1]

            #parser = PDBParser()  #new parser
            #pdb = parser.get_structure(pdbId, pdbId + '.pdb')

        result = []
        return result

if __name__ == '__main__':
    usage_text = """This is a script for analysing frequency of amino-acid occurrence
Usage:
    python cod_vr_mapping.py [-i input_file] [-o output_file]

        -h              print this help screen
        -i              specify input file with list of PDB ids
        -o              specify output file (default output is stdout)

    For example:
    python cod_vr_mapping.py -i in.txt -o out.txt
"""

    #if len(sys.argv) == 5:
    #    cod_vr_mapping( sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] )

    if len(sys.argv) > 2:

        inputfile = ''
        outputfile = ''
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

        if inputfile <> '':
            with open(inputfile,'r') as f:
                content = f.readlines()
                for pdb_id in content:
                    pdb_id = pdb_id.rstrip('\n')
                    input = pdb_seq_mapping( pdb_id )
                    for set in input:
                        if set[1] == '':
                            pass
                            #print 'Nie znaleziono kompatybilnej sekwencji w Ensembl'
                        else:
                            cod_vr_mapping( set[0], set[0][0:4] + '.pdb_' + set[0][5] + '.pdb.01.vr', set[1], set[2])
        else:
            print 'NO INPUT FILE ?'
            compute_frequency( sys.argv[-1], codon_table, showtable)

    else:
        print usage_text
