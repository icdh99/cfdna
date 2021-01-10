import collections
import pysam
import random

def get_motif_bamfile(bamfile_path, last_n, subsample = False):
    fwd3 = collections.Counter()
    fwd5 = collections.Counter()
    samfile = pysam.AlignmentFile(bamfile_path, "rb" )
    i = 0
    for read in samfile:
        if read.is_reverse:
            fwd3[complement(read.get_forward_sequence()[0:last_n])] += 1 
            n = len(read.get_forward_sequence()) - last_n
            fwd5[complement(read.get_forward_sequence()[:n-1:-1])] += 1 
        else:
            fwd5[read.get_forward_sequence()[0:last_n]] += 1 
            n = len(read.get_forward_sequence())-last_n
            fwd3[read.get_forward_sequence()[:n-1:-1]] += 1
        i += 1
        if subsample:
            if i > subsample:
                break
    motif = {"fwd3":fwd3,"fwd5":fwd5}
    return motif

def get_motif_random(last_n, subsample = False):             
    fwd3 = collections.Counter()
    fwd5 = collections.Counter()
    sequences = get_random_sequences(1000000, 10)
    i = 0
    for read in sequences:                                
        if i%2==0:  
            fwd3[complement(read[0:last_n])] += 1
            n = len(read) - last_n
            fwd5[complement(read[:n-1:-1])] += 1   
        else:
            fwd5[read[0:last_n]] += 1 
            # from 5' to 3' direction
            n = len(read)- last_n
            fwd3[read[:n-1:-1]] += 1
        i += 1                                                         
        if subsample:                                           
            if i > subsample:                                          
                break
    motif = {"fwd3":fwd3, "fwd5":fwd5}  
    return motif


def get_motif_fastafile(fastafile_path, last_n, subsample = False):
    fwd3 = collections.Counter()
    fwd5 = collections.Counter()
    i = 0
    with open(fastafile_path, "r") as file:
        for line in file:
            if ">" in line:
                continue
            else:
                fwd5[line[0:last_n]] += 1
                n = len(line) - last_n
                fwd3[line[-2:n-2:-1]] += 1
            i += 1
            if subsample:
                if i > subsample:
                    break 
    motif = {"fwd3":fwd3, "fwd5":fwd5}
    return motif

#function from Buys
complement_translate = str.maketrans('ATCGNatcgn', 'TAGCNtagcn')            

#function from Buys
def complement(seq):
    """Obtain complement of seq
    returns:
        complement (str)
    """
    return seq.translate(complement_translate)

#generate a completely random sequence
def get_random_sequences(number, length_seq):
    """
    >>>len(get_random_sequences(10, 5))
    10
    >>>len(get_random_sequences(10, 5)[1])
    5
    """
    sequences = []
    for i in range(number):
        seq = []
        for j in range(length_seq):
            seq+=random.choice(['A', 'T', 'C', 'G'])
        sequence = "".join(seq)
        sequences += [sequence]
    return sequences