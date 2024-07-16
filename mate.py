#!/usr/bin/env python3
import argparse
from mate.workflow.pipeline import pipeline


def get_opts():
    groups = argparse.ArgumentParser()

    groups.add_argument('-r', '--ref', help='Reference cds file', required=True)
    mut_group = groups.add_mutually_exclusive_group(required=True)
    mut_group.add_argument('-g', '--genome', help="Directory contain all genomes")
    mut_group.add_argument('-b', '--bam', help="Directory contain all bam files by mapping Reseq reads to "
                                               "reference cds")
    # groups.add_argument('-g', '--genome', help="Directory contain all genomes", required=True)
    groups.add_argument('-l', '--ploidy', help="Ploidy of genomes, only effect with -g default=2", type=int, default=2)
    groups.add_argument('-p', '--pheno', help="Directory contain phenotypes for association, if the "
                                              "filename of phenotype starts with \"LOW-\", means lower value is better"
                        , required=True)
    groups.add_argument('-k', '--kmer', help="kmer length for cleanup mafft result, default=5",
                        type=int, default=5)
    groups.add_argument('--filter', help="Threshold string, "
                                         "\"lower_threshold:upper_threshold:missing_threshold:min_allele\",\n"
                                         "lower_threshold means if one allele with less than this ratio of "
                                         "samples supported, it would be dropped; "
                                         "upper_threshold means if one allele with more than this ratio of "
                                         "samples supported, it would be dropped; "
                                         "missing_threshold means if one gene with more than this ratio of "
                                         "samples marked as absence, it would be dropped; "
                                         "min_allele means if one gene with less than this count of alleles "
                                         "(ignore absence), it would be dropped; "
                                         "default=0.05:1:0.25:1", default="0.05:1:0.25:1")
    groups.add_argument('-o', '--output', help="Output directory", required=True)
    groups.add_argument('-s', '--show', help="The multi-alignment of variants would be stored as pdf "
                                             "file if this parameter is set", action="store_true")
    groups.add_argument('-t', '--thread', help="Thread number, default=10", type=int, default=10)

    return groups.parse_args()


if __name__ == "__main__":
    opts = get_opts()
    pipeline(opts)
