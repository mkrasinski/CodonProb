import ensembl
import sys

if __name__ == '__main__':
    if len(sys.argv) > 3:
        species = sys.argv[1]
        region = sys.argv[2]
        features = sys.argv[3:]

        client = ensembl.EnsemblRestClient()
        print client.get_region_feature(species, region, features)
    else:
        print """This is a client for Ensembl REST API resource 'GET overlap/region/:species/:region'

                    Usage: python get_region_features.py [species] [region] [features]
                    For example:
                    python get_region_features.py human 7:140424943-140624564 gene exon

                    Available features : gene, transcript, cds, exon, repeat, simple, misc,
                                         variation, somatic_variation, structural_variation,
                                         somatic_structural_variation, constrained, regulatory,
                                         segmentation, motif, chipseq, array_probe
              """