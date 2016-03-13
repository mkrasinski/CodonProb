from Bio.PDB.PDBParser import PDBParser
import ensembl
from pdb_seq_mapping import pdb_seq_mapping
from Bio import pairwise2
import urllib,urllib2
import requests
import xml.etree.ElementTree as ET
import sys

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
                if k == ensembl_protein_seq[j]:
                    i = i + 1
                    for row in VR:
                        if int(row[0]) == i:
                            #print row
                            print pdb_chain_id + ' ' + aaCodes[k] + ' ' + k + ' ' + cod_seq[j] + ' ' +  row[0] + ' ' + row[1] + ' ' + row[2] + ' ' + row[3]
                j = j + 1

        #pdbId = sys.argv[1]

        #parser = PDBParser()  #new parser
        #pdb = parser.get_structure(pdbId, pdbId + '.pdb')

        result = []
        return result

if __name__ == '__main__':
    if len(sys.argv) == 5:
        cod_vr_mapping( sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] )
    if len(sys.argv) == 2:
        input = pdb_seq_mapping( sys.argv[1] )
        #print input
        for set in input:
            #print set[0], set[0][0:3] + '.pdb_' + set[0][5] + '.pdb.01.vr' , set[1], set[2]
            cod_vr_mapping( set[0], set[0][0:4] + '.pdb_' + set[0][5] + '.pdb.01.vr', set[1], set[2])
    else:
        print "Please provide pdb chain id, VR filename, ENST and alignment"
