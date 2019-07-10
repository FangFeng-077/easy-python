"""
File: similarity.py
------------------------
This file should implement a console program that prompts users
for a DNA strand that they want to search through and a DNA target strand
that they want to search for. The program then outputs the closest match
to the target strand, as defined by the similarity metric presented in the
Assignment 2 Handout.
"""

def search_sequence(dna_to_match, subsequence):
    """
    This function takes in two DNA sequences, and calculates
    the number of spots at which the two sequences have the same
    base pairs.
    >>> search_sequence("GATC", "AATC")
    3
    >>> search_sequence("AGC", "TAG")
    0
    """

    return -1


def find_best_substrand(dna_to_match, dna_to_search):
    """
    This function takes in two DNA strands, one to search through and one
    for which you are trying to find a match. The function returns the closest
    match to the target sequence in the search sequence.
    >>> find_best_substrand("TCATA","ATGCCTGATA")
    'TGATA'
    >>> find_best_substrand("", "ATGCCTGATA")
    ''
    """

    return ''


def main():
    """
    Replace this comment with a more descriptive one.
    Don't forget to delete the pass statement below.
    """
    pass


if __name__ == "__main__":
    main()
