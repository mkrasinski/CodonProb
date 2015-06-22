import ensembl
import sys
import json

if __name__ == '__main__':
    if len(sys.argv) == 3:
        client = ensembl.EnsemblRestClient()
        id = sys.argv[1]
        external_db = sys.argv[2]
        ref = client.get_xrefs_id(id = id, external_db = external_db)

        parsed = json.loads(ref)
        print json.dumps(parsed, indent=4, sort_keys=True)
    else:
        print """This is a client for Ensembl REST API resource 'GET xrefs/id/:id'

                    Usage: python get_xrefs_id.py [Ensembl ID] [external_db]
                    For example:
                    python get_xrefs_id.py ENST00000322088 PDB
              """