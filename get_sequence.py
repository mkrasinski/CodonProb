import ensembl
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        client = ensembl.EnsemblRestClient()
        id = sys.argv[1]
        print client.get_sequence(id = id)
    else:
        print """This is a client for Ensembl REST API resource 'GET archive/id/:id'

                    Usage: python get_sequence.py [id]
                    For example:
                    python get_sequence.py ENSG00000157764
              """