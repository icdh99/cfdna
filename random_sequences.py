import random
import pandas as pd
from natsort import natsorted

def generate_random_sequence_from_freqfile(dataset, freqfile, lenfile, filepath = "/mnt/c/Users/icden/Data_practical/"):
    with open(f'{filepath}{dataset}_random_seq.fa', "w") as newfile:
        with open(f'{filepath}{lenfile}', 'r') as lengths:
            i = 1
            b = []
            for line in lengths:
                b += [line]
        dic = make_dict_with_freqs(freqfile)
        for x , y in dic.items():
            a = f'{filepath}fasta_clean_{x}.txt'
            with open(a, "r") as fasta:
                n = fasta.readline()
                for j in range(1, y+1):
                    c = random.choice(b)
                    s = generate_random_sequence(int(c), n)
                    newfile.write(f'>seq{i}_{x}\n{s}\n')
                    i += 1
def make_dict_with_freqs(filename, filepath = "/mnt/c/Users/icden/Data_practical/"):
    n = ["chr", "counts"]
    df = pd.read_csv(f"{filepath}{filename}", sep = "\t", names = n, nrows = 23)
    df.index = df["chr"]
    df = df.reindex(index = natsorted(df["chr"]))
    return df["counts"].to_dict()

#function to generate a random sequence with a specified length and a sequence
def generate_random_sequence(length, fc):
    n = random.randint(0 + length, len(fc) - length)
    s = fc[n : int(n) + int (length)]
    return s.upper()

def make_fasta_file_from_random_sequences(number = 100000, filepath = "/mnt/c/Users/icden/Data_practical/"):
    with open(f'{filepath}random_sequences.fa', 'w') as newfile:
        for i in range(number):
            a = get_random_sequences(167)
            newfile.write(f'>seq{i+1}\n{a}\n')

#function to generate completely random sequences with a specified length
def get_random_sequences(length_seq):
    seq = ""
    for j in range(length_seq):
        seq += random.choice(['A', 'T', 'C', 'G'])
    #sequence = "".join(seq)
    #seq += sequence
    return seq
