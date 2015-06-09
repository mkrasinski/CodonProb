import sys
import SOAPpy
from SOAPpy import WSDL

if __name__ == '__main__':
    if len(sys.argv) == 3:
        input_type = sys.argv[1]
        input_value = sys.argv[2]

        if input_type == 'gene':
            input_type = 'Ensembl Gene ID'
        elif input_type == 'protein':
            input_type = 'Ensembl Protein ID'
        elif input_type == 'transcript':
            input_type = 'Ensembl Transcript ID'
        else:
            print "Incorrect parameter " + input_type
            sys.exit(0)

        outputs = 'UniGene ID, PDB ID'

        biodbnet = WSDL.Proxy('http://biodbnet.abcc.ncifcrf.gov/webServices/bioDBnet.wsdl')
        #inputResult = biodbnet.getInputs()
        #print "inputResult  :  " + inputResult

        #outputResult = biodbnet.getOutputsForInput(input_type)
        #print "outputResult  :  " + outputResult

        #directOutputResult = biodbnet.getDirectOutputsForInput(input_type)
        #print "directOutputResult  :  " + directOutputResult

        db2dbParams = SOAPpy.structType({'input': input_type, 'inputValues': input_value, 'outputs': outputs})
        db2dbResult = biodbnet.db2db(db2dbParams)
        result = db2dbResult.split("\n")
        result[0] = result[0].split("\t")
        result[1] = result[1].split("\t")
        for a,b,c in result[0:2]:
            print a.ljust(25) + b.ljust(25) + c.ljust(25)

    else:
        print """This is a script for converting Ensembl IDs to Uniprot and/or PDB
                    Please specify what type of input Ensembl ID is provided (gene, protein or transcript).

                    Usage: python db2db_converter.py [gene|protein|transcript] [Ensembl ID]

                    For example:
                    python db2db_converter.py transcript ENST00000248342
              """








