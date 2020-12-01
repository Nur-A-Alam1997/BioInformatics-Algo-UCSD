from Bio import SeqIO
for record in SeqIO.parse("dna2.fasta", "fasta"):
    print(record.id)
    
    