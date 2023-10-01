""""
function for finding Open Reading Frames.
Could not find a module for that in Python.
So i had to implement it myself.
"""
from Bio.Seq import Seq


def find_orf(sequence_):

    startcodon = "ATG"
    stopcodon = ["TAA", "TAG", "TGA"]

    orf_seq = Seq(sequence_.upper().replace("U", "T"))
    print(orf_seq)
    print(orf_seq.translate())


find_orf("uaa")
