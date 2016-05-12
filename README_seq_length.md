##seq_length.py README

Written by Kevin M Horn and released "as is". You are free to use, modify, or copy this script in any manner you like.
This will read a multiple sequence alignment file, and for each entry print the name of the sequence, aligned length, number of gap positions, and sequence length with no gaps.
Any file format recognized by Biopython's SeqIO module can be used as input. 
Note, this uses the '-', 'x', 'X', and '?' as a gap characters and will count all others. To change which characters are counted as gap characters, modify the list of gap characters in line 15.
 
#Usage:   fasta_seq_length.py alignment_file file_format

Example: python sequences.phy phylip-relaxed
Example: python sequences.fa fasta