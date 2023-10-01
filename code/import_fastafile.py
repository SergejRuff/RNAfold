"""
This code demonstrates how to import fasta files into Python
and use them as DATAFRAMES.
you need biopython package and pandas
"""

from Bio import SeqIO
import pandas as pd

virus_list = []  # create empty list to store values inside.


for virus in SeqIO.parse("../data/nido_roniviruses_n6.fasta", "fasta"):
    # append a list with what you want to list
    virus_list.append([virus.id, str(virus.seq)])
    # biopython imports sequences as Class Bioseq (see print-command).
    # need to change type to string.
    print(type(virus.seq))

# convert lists to dataframe.
virus_df = pd.DataFrame(virus_list, columns=["id", "sequences"])
# you can also use directories.

print(virus_df)

# same thing but with dictionaries, not lists.

# create empty dictionary
virus_dict = {"id": [], "seq": []}

for virus in SeqIO.parse("../data/nido_roniviruses_n6.fasta", "fasta"):
    # append dictionary
    virus_dict["id"].append(virus.id)
    virus_dict["seq"].append(str(virus.seq))

print("virus dictionary\n", virus_dict)
virus_df_ = pd.DataFrame(virus_dict)  # advantage: dont need to set col-names

print(virus_df_)
