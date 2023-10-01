"""
module: re for work with regular expressions.
using search function to match Poly-A-requirement in poly_a_pattern variable
with input sequence.
"""
import re


def has_poly_a_tail(sequence_):
    """
    has_poly_a_tail function
    define poly A Tail as having 5 or more As at the end of teh nucleotide sequence.
    use search function to match pattern.
    search returns pattern-object (the As at the end).
    I need True or False depending if As are there or not.
    Use bool to convert to True or False.
    search is case sensitive -> .upper to convert sequence.
    Args:
        sequence_ (str): The DNA sequence to check.

    Returns:
        bool: True if a poly-A tail is found at the end of the sequence
        (with at least 5 consecutive 'A' characters), False otherwise.
    """
    poly_a_pattern = "A{5,}$"
    return bool(re.search(poly_a_pattern, sequence_.upper()))
