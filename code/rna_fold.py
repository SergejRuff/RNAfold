"""
a script to apply the things I did during my
3 weeks of work for Chris Lauber in Python.
Goal: get used to Python programming
translate the R script into Python

"""
from Bio import SeqIO
import pandas as pd

virus_list = []

for virus in SeqIO.parse("data/nido_roniviruses_n6.fasta", "fasta"):
    virus_list.append([virus.id, str(virus.seq)])

virus_df = pd.DataFrame(virus_list, columns=["id", "sequences"])
