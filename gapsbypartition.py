#!/usr/bin/env python
""""
Written by Kevin M Horn and released "as is". You are free to use, modify, or copy this script in any manner you like.
Given a multiple sequence alignment file and a file identifying the partions in the alignment, this script will output a tab file indicating missing data by partition.
The user's partition file must have tab separated values, with partition name in the first column, start position in the second column and end position in the third column.
Flags: -msa alignment file -f format of alignment file -p partition file -o output file
The alignment format can be any format allowed by biopython's SeqIO and is specified with the '-f' flag. Default is fasta.
Example usage:
python gapsbypartition.py -msa seq.phylip -p partitionfile.txt -f phylip-relaxed -o outputfile.txt
""""
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
