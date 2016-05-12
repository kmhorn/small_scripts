#!/usr/bin/env python

from Bio import SeqIO
import sys

"""
Written by Kevin Horn and released as is.
You are free to use, copy, or modify this script however you wish.
Usage: python msa_converter.py input_file input_format output_file output_format
"""

few_arguments = """
Missing arguments
Usage: msa_converter.py input_file input_format output_file output_format
Example: msa_converter.py sequences.fasta fasta sequences.phylip phylip-relaxed
Input and output formats can be any format recognized by biopython's SeqIO, for full list see biopython documentation.
All sequences must be same length.
"""

if len(sys.argv) < 5:
    print few_arguments

if len(sys.argv) > 5:
    print "Extra arguments will be ignored."

count = SeqIO.convert(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

print "Converted %i records from" % count , str(sys.argv[2]), "to", str(sys.argv[4])
print "Saved to", str(sys.argv[3])
