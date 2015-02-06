# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

Jee Hyun Kim
Olin College Class of 2018
Software Design Spring 15'
Mini Project 1: Gene Finder

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, aa_table
import random
from load import load_seq

def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###
def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    """
    nuc=['A','T','C','G']
    com_nuc=['T','A','G','C']
    for i in range (4):
        if nucleotide == nuc[i]:
            return com_nuc[i]
    raise ValueError
    return None

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """
    rc=''
    for nucleotide in dna:
        rc=get_complement(nucleotide)+rc
    return rc

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'
    """
    #stop codon: TAG, TAA, TGA
    for i in range(3,len(dna),3):
        if dna[i:i+3]in('TAG','TAA','TGA'):
            return dna[:i]
    return dna

def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    """
    ind=0
    ORF=[]
    for i in range(0,len(dna),3):
        if dna[i:i+3]=='ATG':
            dna=dna[i:]
            ORF.insert(ind,rest_of_ORF(dna))
            dna=dna[len(rest_of_ORF(dna)):]
            ind+=1
            continue
    return ORF

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs

    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    """
    ORFs=[]
    for i in range(3):
        ORFs.extend(find_all_ORFs_oneframe(dna[i:]))
    return ORFs

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    ORFb=[]
    ORFb.extend(find_all_ORFs(dna))
    ORFb.extend(find_all_ORFs(get_reverse_complement(dna)))
    return ORFb

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF()
    'ATGCTACATTCGCAT'
    """
    #Returns the first longest ORF if there are more than one longest ORF
    ORFl=""
    for ORF in find_all_ORFs_both_strands(dna):
            if len(ORF)>len(ORFl):
                ORFl=ORF
    return ORFl

def longest_ORF_noncoding(dna,num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    l=0
    dnal=0
    dnalist=list(dna)
    for i in range(num_trials):
        random.shuffle(dnalist)
        l=len(longest_ORF(dnalist))
        if l>dnal:
            dnal=l
    return dnal

def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    aa=''
    for i in range(0,len(dna),3):
        if i<len(dna)-2:
            aa=aa+aa_table[dna[i:i+3]]
    return aa

def gene_finder(dna):
    """ Returns the amino acid sequences that are likely coded by the specified dna
        
        dna: a DNA sequence
        returns: a list of all amino acid sequences coded by the sequence dna.
    """
    threshold=longest_ORF_noncoding(dna,1500)
    ORFb=find_all_ORFs_both_strands(dna)
    aa=[]
    for ORF in ORFb:
        if len(ORF)>threshold:
            aa.extend(coding_strand_to_AA(ORF))
    return aa


if __name__ == "__main__":
    import doctest
    doctest.testmod()