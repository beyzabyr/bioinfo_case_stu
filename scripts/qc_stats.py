import sys
import pandas as pd
import numpy as np
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

def calculate_fastq_stats(input_fastq, output_csv):
    records = []
    
    # using Biopython 
    for record in SeqIO.parse(input_fastq, "fastq"):
        read_id = record.id
        seq = record.seq
        quality_scores = record.letter_annotations["phred_quality"]
        
        gc_content = gc_fraction(seq) * 100
        read_length = len(seq)
        mean_quality = np.mean(quality_scores)
        
        records.append([read_id, gc_content, read_length, mean_quality])
    
    df = pd.DataFrame(records, columns=["Read_ID", "GC_Content_Percent", "Read_Length", "Mean_Quality"])
    df.to_csv(output_csv, index=False)

if __name__ == "__main__":
   
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    calculate_fastq_stats(input_file, output_file)
