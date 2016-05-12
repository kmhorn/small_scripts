##mas_converter README

Written by Kevin Horn and released as is.
You are free to use, copy, or modify this script however you wish.

This will convert a multiple sequence alignment from one format to another. 
Any format recognized by Biopython's SeqIO can be used as input or output. 
For a full list of file types see the biopython documentation. 

Formats that require more information than the input format contains can not be used for the output.
For example, nexus files need the type of sequence, but fasta files do not explicitly contain that information. 
So you can go from a nexus file to a fasta file, but not a fasta file to a nexus file.

#Usage: python msa_converter.py input_file input_format output_file output_format

#Example: msa_converter.py sequences.fasta fasta sequences.phylip phylip-relaxed