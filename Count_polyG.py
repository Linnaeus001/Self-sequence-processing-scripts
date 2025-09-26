import os
from Bio import SeqIO

# Sequence to search for
sequence_to_find = "GGGGGGGG"

# Output file
output_file = "8G_read_counts.txt"

# Open the output file for writing
with open(output_file, "w") as output:
    # Write the header
    output.write("File\tCount\n")
    
    # Process each FASTQ file in the current directory
    for filename in os.listdir("."):
        if filename.endswith(".fq"):
            count = 0
            # Count reads containing the sequence in the current file
            for record in SeqIO.parse(filename, "fastq"):
                if sequence_to_find in str(record.seq):
                    count += 1
            # Write the result to the output file
            output.write(f"{filename}\t{count}\n")
            print(f"Processed {filename}: {count} reads containing '{sequence_to_find}'")

print(f"Results saved to {output_file}")
