import ensembl
import sys

if __name__ == '__main__':
    if len(sys.argv) == 3:
        client = ensembl.EnsemblRestClient()
        species = sys.argv[1]
        symbol = sys.argv[2]
        ref = client.get_xrefs_symbol(species = species, symbol = symbol)
        for obj in ref:
            print obj['type'] + ' ' + obj['id']
    else:
        print """This is a client for Ensembl REST API resource 'GET xrefs/symbol/:species/:symbol'

                    Usage: python get_xrefs_symbol.py [species] [symbol]
                    For example:
                    python get_xrefs_symbol.py homo_sapiens BRCA2
              """