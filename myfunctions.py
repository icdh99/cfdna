import pysam
import collections 
import matplotlib.pyplot as plt
import random

#function from Buys
complement_translate = str.maketrans('ATCGNatcgn', 'TAGCNtagcn')            

#function from Buys
def complement(seq):
    """Obtain complement of seq
    returns:
        complement (str)
    """
    return seq.translate(complement_translate)

#adjusted from Liting
def get_motif(bam, last_n, subsample = False):
    fwd3= collections.Counter()
    fwd5= collections.Counter()
    samfile = pysam.AlignmentFile(bam, "rb" )
    i = 0
    for read in samfile:
        if read.is_reverse:
            fwd3[complement(read.get_forward_sequence()[0:last_n])] += 1 
            n =len(read.get_forward_sequence()) - last_n
            fwd5[complement(read.get_forward_sequence()[:n-1:-1])] += 1 
        else:
            fwd5[read.get_forward_sequence()[0:last_n]] += 1 
            n =len(read.get_forward_sequence())-last_n
            fwd3[read.get_forward_sequence()[:n-1:-1]] += 1
        i += 1
        if subsample:
            if i > subsample:
                break
    motif = {"fwd3":fwd3,"fwd5":fwd5}
    return motif

#function from Liting
def plot_kmer_dist(motifs, ind, colors=['blue', "red", "teal", "yellow"], relative = True, figsize = (10,4)):
    plt.figure(figsize=figsize)
    for i, x in enumerate(motifs):
        if relative:
            sum_total = sum(x.values())
            print(x.keys())                      #see how the dictionary is structured
            print(x.values())
        else:
            sum_total = 1
        # x labels should be predefined. (combination of ATGC sorted with alphabetical orders.)
        plt.bar([k for k,v in  sorted(x.items())],[v/sum_total for k,v in  sorted(x.items())], 
                label = f"{ind[i]}", 
                alpha=0.3, 
                color = colors[i]) 
    plt.xticks( rotation='vertical')
    plt.legend()
    plt.show()
    
#function from liting
def plot_all(df, figsize= (10,4)):    
    plot_kmer_dist([df['fwd5']], ["fwd 5 prime end"], [ "red", "yellow"], figsize= figsize)
    plot_kmer_dist([df['fwd3']], ["fwd 3 prime end"], [ "blue", "teal"], figsize= figsize)
    plot_kmer_dist([df['fwd5'], df['fwd3']],["fwd 5 prime end", "fwd 3' prime end"], [ "red", "blue"], figsize= figsize)

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

#adjusted from Liting
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
            fwd5[read[0:last_n]] +=1 
            # from 5' to 3' direction
            n = len(read)- last_n
            fwd3[read[:n-1:-1]] +=1
        i += 1                                                         
        if subsample:                                           
            if i > subsample:                                          
                break
    motif = {"fwd3":fwd3,"fwd5":fwd5}  
    return motif

#small difference with plot_all
def plot_all_random(df, figsize= (10,4)):    
    plot_kmer_dist([df['fwd5']],["fwd 5' end"], [ "red", "yellow"], figsize= figsize)
    plot_kmer_dist([df['fwd3']],["fwd 3'end"], [ "blue", "teal"], figsize= figsize)
    plot_kmer_dist([df['fwd5'],df['fwd3']],["fwd 5' end", "fwd 3' end"], [ "red", "blue"], figsize= figsize)
    
#function to extract a random sequence with a specified length and an original sequence to extract from
def generate_random_sequence(length, fc):
    n = random.randint(0 + length, len(fc) - length)
    s = fc[n : int(n) + int (length)]
    return s.upper()

#function to create a file with the lenghts of all the sequences in a bamfile
def make_file_with_freq_lengths(filename, dataset, filepath = '/mnt/c/Users/icden/Data_practical/'):
    file = f"/mnt/c/Users/icden/Data_practical/{filename}"
    bamfile = pysam.AlignmentFile(file, "rb")
    filename_new = f"lengths_{dataset}.txt"
    seq = ""
    for read in bamfile:
        seq += str(f"{len(read.get_forward_sequence())}\n")
    with open(filename_new, "w") as new_file:
        new_file.write(seq)

#function to make a "clean" fasta file: that means the whole sequence on one line for easy usage 
def make_clean_fasta(a):
    name1 = "/mnt/c/Users/icden/Data_practical/" + a + ".fa"
    name2 = "/mnt/c/Users/icden/Data_practical/fasta_clean_" + a + ".txt"
    with open(name1, "r") as fasta:
        with open(name2, "w") as fasta_clean:
            for line in fasta:
                if ">" in line:
                    pass
                else:
                    line = line.strip("\n")
                    line = line.replace("N", "")
                    line = line.replace("n", "")
                    fasta_clean.write(line)      

#function from week3_analyse_freqfiles but never called
def make_dict_with_freqs(filename, dataset):
    n = ["chr", "counts"]
    filepath = f"/mnt/c/Users/icden/Data_practical/{filename}"
    df = pd.read_csv(filepath, sep = "\t", names = n, nrows = 23)
    df.index = df["chr"]
    df = df.reindex(index = natsorted(df["chr"]))
    return df["counts"].to_dict()

#function from week 4 to analyse sequence motifs from textfiles 
def get_motif_txtfile(txtfile, last_n, subsample = False):
    fwd3 = collections.Counter()
    fwd5 = collections.Counter()
    i = 0
    with open(txtfile, "r") as file:
        for line in file:
            if ">" in line:
                pass
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

