#!/usr/bin/env python

from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-msa", dest="userMSA", help="Input fasta formatted multiple sequence alignment", default=None)
parser.add_argument("-p", dest="userPartition", help="Input partition file.", required=True)
parser.add_argument("-o", dest="userOUT", help="Specify the name of your output file.", required=True)
parser.add_argument("-f", dest="userFormat", help="Specify the format of your msa file in quotes. Any format name allowed by Biopython's SeqIO is okay.", default="fasta")
args = parser.parse_args()

out_headers = ["Names"]
with open(args.userPartition) as pfile:
    partition_file = [row.strip().split('\t') for row in pfile]

for row in partition_file:
    out_headers.append(row[0])
with open(args.userOUT, "a") as outfile:
    outfile.write('\t'.join([str(x) for x in out_headers]))
    outfile.write('\n')
  
with open(args.userMSA, "r") as msa:  
    for record in SeqIO.parse(msa, args.userFormat):
        seq_list = []
        seq_list.append(record.name)
        for row in partition_file:
            partition_seq = record.seq[(int(row[1]) - 1):(int(row[2]))]
            gaps = sum(partition_seq.count(x) for x in '-xX?')
            portion = gaps / float(len(partition_seq))
            seq_list.append(portion)
        with open(args.userOUT, "a") as outfile:
            outfile.write('\t'.join([str(x) for x in seq_list]))
            outfile.write('\n')
