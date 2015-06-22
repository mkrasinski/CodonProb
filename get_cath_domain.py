import ensembl
import requests
import sys
import json
import time

if __name__ == '__main__':
    if len(sys.argv) == 3:
        client = ensembl.EnsemblRestClient()
        species = sys.argv[1]
        symbol = sys.argv[2]
        ref = client.get_xrefs_symbol(species = species, symbol = symbol)
        for obj in ref:
            #print obj['type'] + ' ' + obj['id']
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
        print json.dumps(parsed, indent=4, sort_keys=True)

    else:
        print """This script scans the query protein sequence against a library of CATH domains to find the most likely structural domain matches.
                    Query is based on translation sequence for provided species and symbol.

                    Usage: python get_cath_domain [species] [symbol]
                    For example:
                    python get_cath_domain.py human NP_055040.2
              """

