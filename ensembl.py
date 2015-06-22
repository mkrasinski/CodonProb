import requests
import sys
 
class EnsemblRestClient():
    """EnsemblRestClient class definition."""
    def __init__(self, server='http://rest.ensembl.org'):
        self.server = server

    def get_sequence(self, id):
        """Return archived sequence for specified identifier."""
        self.endpoint = '/sequence/id/'
        url = self.server + self.endpoint + id + '?'
        r = requests.get(url, headers={ "Content-Type" : "application/json"})

        if not r.ok:
            r.raise_for_status()
            sys.exit()
        decoded = r.json()
        return decoded

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
        return r.text

    def get_xrefs_symbol(self, species, symbol):
        """Lookup all Ensembl objects linked to provided symbol."""
        self.endpoint = '/xrefs/symbol/'
        url = self.server + self.endpoint + species + '/' + symbol + '?'

        r = requests.get(url, headers={ "Content-Type" : "application/json"})

        if not r.ok:
            r.raise_for_status()
            sys.exit()
        return r.json()

    def get_xrefs_id(self, id, external_db):
        """Lookup all IDs in external_db for provided Ensembl ID."""
        self.endpoint = '/xrefs/id/'
        url = self.server + self.endpoint + id + '?external_db=' + external_db + ';all_levels=1'

        r = requests.get(url, headers={ "Content-Type" : "application/json"})

        if not r.ok:
            r.raise_for_status()
            sys.exit()
        return r.text

if __name__ == '__main__':
    print """This package implements client for Ensembl REST API"""