import ensembl
import requests
import sys
import json
import time

if __name__ == '__main__':
    if len(sys.argv) == 3:

        architectures = (('1.10','Orthogonal Bundle'),
                        ('1.20','Up-down Bundle'),
                        ('1.25','Alpha Horseshoe'),
                        ('1.40','Alpha solenoid'),
                        ('1.50','Alpha/alpha barrel'),
                        ('2.10','Ribbon '),
                        ('2.100','Aligned Prism'),
                        ('2.102','3-layer Sandwich'),
                        ('2.105','3 Propellor'),
                        ('2.110','4 Propellor'),
                        ('2.115','5 Propellor'),
                        ('2.120','6 Propellor'),
                        ('2.130','7 Propellor'),
                        ('2.140','8 Propellor'),
                        ('2.150','2 Solenoid'),
                        ('2.160','3 Solenoid'),
                        ('2.170','Beta Complex'),
                        ('2.20','Single Sheet'),
                        ('2.30','Roll '),
                        ('2.40','Beta Barrel'),
                        ('2.50','Clam '),
                        ('2.60','Sandwich '),
                        ('2.70','Distorted Sandwich'),
                        ('2.80','Trefoil '),
                        ('2.90','Orthogonal Prism'),
                        ('3.10','Roll '),
                        ('3.100','Ribosomal Protein'),
                        ('3.15','Super Roll'),
                        ('3.20','Alpha-Beta Barrel'),
                        ('3.30','2-Layer Sandwich'),
                        ('3.40','3-Layer(aba) Sandwich'),
                        ('3.50','3-Layer(bba) Sandwich'),
                        ('3.55','3-Layer(bab) Sandwich'),
                        ('3.60','4-Layer Sandwich'),
                        ('3.65','Alpha-beta prism'),
                        ('3.70','Box '),
                        ('3.75','5-stranded Propeller'),
                        ('3.80','Alpha-Beta Horseshoe'),
                        ('3.90','Alpha-Beta Complex'),
                        ('4.10','Irregular '))

        client = ensembl.EnsemblRestClient()
        species = sys.argv[1]
        symbol = sys.argv[2]
        ref = client.get_xrefs_symbol(species = species, symbol = symbol)
        for obj in ref:
            print obj['type'] + ' ' + obj['id']
            if obj['type'] == "translation":
                seq_id = obj['id']
        ref = client.get_sequence( seq_id )
        sequence = ref['seq']

        cath_url = 'http://www.cathdb.info/search/by_fasta'

        param = {}
        param['fasta'] = '>QUERY\n' + sequence
        query = param

        headers={ "Accept" : "application/json"}
        r = requests.post(cath_url, headers=headers, data=query)

        if not r.ok:
            r.raise_for_status()
            sys.exit()
        if r.status_code == 202:
            print 'Query is being processed ...'
        else:
            print 'Unexpected response code - > ' + r.status_code

        cath_response =  r.json()
        task_id = cath_response['task_id']
        cath_url = 'http://www.cathdb.info' + '/search/by_fasta/check/' + task_id

        task_completed = 0
        while task_completed == 0:
            r = requests.get(cath_url, headers=headers)
            cath_response = r.json()
            task_completed = cath_response['success']
            if task_completed != 1:
                print 'Still waiting ...'
                time.sleep(0.5)
            else:
                print 'Results are ready ! Retrieving results ...'

        cath_url = 'http://www.cathdb.info' + '/search/by_fasta/results/' + task_id
        r = requests.get(cath_url, headers=headers)
        parsed = json.loads(r.content)

        superfamily_id = parsed["signatures_by_id"]["QUERY"]["matches"][0]["data"]["superfamily_id"]
        print "Superfamily :" + "\n" + superfamily_id

        prefix = superfamily_id.split(".",2)[0] + "." + superfamily_id.split(".",2)[1]

        print "Architecture :"
        for symbol,arch in architectures:
            if symbol == prefix:
                print arch

    else:
        print """This script scans the query protein sequence against a library of CATH domains to find the most likely structural domain matches.
                    Query is based on translation sequence for provided species and symbol.

                    Usage: python get_cath_domain [species] [symbol]
                    For example:
                    python get_cath_domain.py homo_sapiens NP_055040
              """

