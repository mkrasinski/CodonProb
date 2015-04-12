import requests 
import sys
 
class EnsemblRestClient():
    def __init__(self, server='http://rest.ensembl.org', endpoint='/archive/id/'):
        self.server = server
        self.endpoint = endpoint

    def get_sequence(self, id):		
		r = requests.get(self.server+self.endpoint+id+'?', headers={ "Content-Type" : "application/json"})
		
		if not r.ok:
		    r.raise_for_status()
		else: 
			decoded = r.json()
			print repr(decoded)
		return None
	


if __name__ == '__main__':
    if len(sys.argv) == 2:
        client = EnsemblRestClient()
        id = sys.argv[1]
        client.get_sequence(id = id)
    else:
        print """Usage: python get_sequence.py [id]
                    For example:
                    python get_sequence.py ENSG00000157764
              """