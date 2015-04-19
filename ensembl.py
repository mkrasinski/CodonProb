import requests
import sys
 
class EnsemblRestClient():
    """EnsemblRestClient class definition."""
    def __init__(self, server='http://rest.ensembl.org'):
        self.server = server

    def get_sequence(self, id):
        """Return archived sequence for specified identifier."""
        self.endpoint = '/archive/id/'
        url = self.server + self.endpoint + id + '?'
        r = requests.get(url, headers={ "Content-Type" : "application/json"})

        if not r.ok:
            r.raise_for_status()
        else:
            decoded = r.json()
            print repr(decoded)
        return None

    def get_region_feature(self, species, region, features):
        """Return requested features for specified species and region."""
        self.endpoint = '/overlap/region/'
        url = self.server + self.endpoint + species + '/' + region + '?'

        for f in features:
            url = url + 'feature=' + f + ';'

        r = requests.get(url, headers={ "Content-Type" : "text/x-gff3"})

        if not r.ok:
            r.raise_for_status()
            sys.exit()
        print r.text
        return None

if __name__ == '__main__':
    print """This package implements client for Ensembl REST API"""