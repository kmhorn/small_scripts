##gapsbypartition.py README

 Written by Kevin M Horn and released "as is". You are free to use, modify, or copy this script in any manner you like.

Given a multiple sequence alignment file and a file identifying the partions in the alignment, this script will output a tab file indicating missing data by partition. 

The user's partition file must have tab separated values, with partition name in the first column, start position in the second column and end position in the third column.

Required dependancies are Biopython and argparse.

Flags: 
-msa alignment file
-f format of alignment file
-p partition file
-o output file  

The alignment format can be any format allowed by biopython's SeqIO and is specified with the '-f' flag. Default is fasta.

#Example usage:

python gapsbypartition.py -msa seq.fasta -p partitionfile.txt -f fasta -o outputfile.txt

or

python gapsbypartition.py -msa seq.phylip -p partitionfile.txt -f phylip-relaxed -o outputfile.txt
