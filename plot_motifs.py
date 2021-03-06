import matplotlib.pyplot as plt

def plot_kmer_dist(motifs, ind, colors=['blue', "red", "teal", "yellow"],path = "/mnt/c/Users/icden/Data_practical", relative = True, figsize = (10,4)):
    plt.figure(figsize=figsize)
    for i, x in enumerate(motifs):
        if relative:
            sum_total = sum(x.values())
        else:
            sum_total = 1
        plt.bar([k for k,v in  sorted(x.items())],[v/sum_total for k,v in  sorted(x.items())],
                label = f"{ind[i]}", 
                alpha=0.3, 
                color = colors[i]) 
    plt.xticks( rotation='vertical')
    plt.legend()
    a = f"{path}/fig"
    plt.savefig(a, dpi = 100)
    #plt.show()
    
def plot_all(df, path, figsize = (10,4)):
    plot_kmer_dist([df['fwd5'], df['fwd3']], ["fwd 5' end", "fwd 3' end"], [ "red", "blue"], path, figsize = figsize)


def plot_all_random(df, path, figsize = (10,4)):         #to give the randomly generated .fa files a different colour scheme 
    plot_kmer_dist([df['fwd5'], df['fwd3']], ["fwd 5' end", "fwd 3' end"], [ "goldenrod", "teal"], path, figsize = figsize)

