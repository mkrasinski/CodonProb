from Bio.PDB.PDBParser import PDBParser
from Bio import pairwise2
import ensembl
import time
import sys
import urllib,urllib2
import requests
import xml.etree.ElementTree as ET

def dedup(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def pdb_seq_mapping( pdb_id ):
        # amino acids codes dictionary definition
        aaCodes = dict()
        aaCodes['GLY'] = 'G' #GLYCINE
        aaCodes['PRO'] = 'P' #PROLINE
        aaCodes['ALA'] = 'A' #ALANINE
        aaCodes['VAL'] = 'V' #VALINE
        aaCodes['LEU'] = 'L' #LEUCINE
        aaCodes['ILE'] = 'I' #ISOLEUCINE
        aaCodes['MET'] = 'M' #METHIONINE
        aaCodes['CYS'] = 'C' #CYSTEINE
        aaCodes['PHE'] = 'F' #PHENYLALANINE
        aaCodes['TYR'] = 'Y' #TYROSINE
        aaCodes['TRP'] = 'W' #TRYPTOPHAN
        aaCodes['HIS'] = 'H' #HISTIDINE
        aaCodes['LYS'] = 'K' #LYSINE
        aaCodes['ARG'] = 'R' #ARGININE
        aaCodes['GLN'] = 'Q' #GLUTAMINE
        aaCodes['ASN'] = 'N' #ASPARAGINE
        aaCodes['GLU'] = 'E' #GLUTAMIC ACID
        aaCodes['ASP'] = 'D' #ASPARTIC ACID
        aaCodes['SER'] = 'S' #SERINE
        aaCodes['THR'] = 'T' #THREONINE

        pdbId = pdb_id

        parser = PDBParser()  #new parser
        pdb = parser.get_structure(pdbId, pdbId + '.pdb')

        result = [] #empty list for storing results
        processed_chains = []

        for chain in pdb.get_chains():                 #iterating per each chain
            chainId = chain.get_id()                   #id
            if chainId not in processed_chains:
                processed_chains.append(chainId)
                residuesObj =  chain.get_unpacked_list()   #residues

                chainSeq =''                               #getting AA sequence for this chain
                                  #getting AA sequence for this chain
                for res in residuesObj:
                    if res.get_resname() in aaCodes.keys():
                        chainSeq = chainSeq + aaCodes[res.get_resname()]

                #getting uniprotid for this chain
                rcsb_url = 'http://www.rcsb.org/pdb/rest/customReport?pdbids=' + pdbId + '.' + chainId + '&customReportColumns=chainId,db_id,db_name&service=wsdisplay&format=text'
                headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
                r = requests.get(rcsb_url, headers=headers)
                e = ET.ElementTree(ET.fromstring(r.content))
                root = e.getroot()

                uniprotId = ''
                for elem in root.getiterator('dimEntity.db_id'):
                    uniprotId = elem.text   #UniprotId found
                if uniprotId == '':         #this should never happen
                    print 'UniprotId not found !'
                    sys.exit()

                #translating uniprotId to Ensembl transcripts
                url = 'http://www.uniprot.org/mapping/'
                paramsStep2 = {
                'from':'ACC',
                'to':'ENSEMBL_TRS_ID',
                'format':'tab',
                'query':uniprotId
                }

                data = urllib.urlencode(paramsStep2)
                request = urllib2.Request(url, data)
                user = 'krasinskimaciek@gmail.com'
                request.add_header('User-Agent', user )
                try:
                    response = urllib2.urlopen(request)
                except urllib2.HTTPError, err:
                    if err.code == 503:
                        response = urllib2.urlopen(request)
                page = response.read()
                lines = page.split('\n')

                transcriptIds = []
                for line in lines:          #building list of transcripts for uniprotId
                    if len(line.split('\t')[0]) > 0 and (line.split('\t')[0]) <> 'From':
                        transcriptIds.append(line.split('\t')[1])

                #checking Ensembl reanscriptIds to find one with sequence that is the best match for processed chain
                client = ensembl.EnsemblRestClient()
                best_score = 0
                best_match_tid = ''
                best_match_seq = ''
                best_alignment = ''
                for transcriptId in transcriptIds:
                    ref = client.get_sequence( transcriptId , type="protein")
                    sequence = ref['seq']
                    alns = pairwise2.align.globalxs(chainSeq, sequence, -5, 0)
                    if alns[0][2] > best_score:
                        best_score = alns[0][2]
                        best_match_tid = transcriptId
                        best_match_seq = sequence
                        best_alignment = alns[0][0]
                result.append([pdbId + '.' + chainId, best_match_tid, best_alignment])
        return result

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print pdb_seq_mapping( sys.argv[1] )
    else:
        print "Please provide a single argument - pdb id"
