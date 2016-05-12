#!/usr/bin/env python

## Written by Kevin M Horn and released "as is". You are free to use, modify, or copy this script in any manner you like.
## This will read a multiple sequence alignment file, and for each entry print the name of the sequence, aligned length, number of gap positions, and sequence length with no gaps.
## Any file format recognized by Biopython's SeqIO module can be used as input. 
## Note, this uses the '-', 'x', 'X', and '?' as a gap characters and will count all others. To change which characters are counted as gap characters, modify the list of gap characters in line 15.
## Usage:   fasta_seq_length.py alignment_file file_format
## Example: python sequences.phy phylip-relaxed
## Example: python sequences.fa fasta

from Bio import SeqIO
import sys
print("Name\tAligned_length\tGaps\tNongap_Length")
for seq_record in SeqIO.parse(str(sys.argv[1]), sys.argv[2]):
    gaps = sum((seq_record.seq).count(x) for x in '-xX?')
    output_line = '%s\t%i\t%i\t%i' % \
    (seq_record.id, len(seq_record.seq), gaps, len(seq_record.seq) - int(gaps))
    print(output_line)