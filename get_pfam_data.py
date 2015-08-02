import requests
import sys
import xml.etree.ElementTree as ET

if __name__ == '__main__':
    if len(sys.argv) == 2:
        pdb_id = sys.argv[1]
        url = 'http://www.rcsb.org/pdb/rest/hmmer?structureId=' + pdb_id
        r = requests.get(url)
        if not r.ok:
            r.raise_for_status()
            sys.exit()
        else:
            root = ET.fromstring(r.content)
            for child in root:
                print "pfamName = " + child.attrib["pfamName"] + " , " + "pfamAcc = " + child.attrib["pfamAcc"]

    else:
        print """This script retrieves Pfam data for provided PDB ID

                    Usage: python get_pfam_data.py [PDB_ID]
                    For example:
                    python get_pfam_data.py 4lac
              """