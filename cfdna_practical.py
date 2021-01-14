import click 
import myfunctions as mf
import motif_analysis as m
import plot_motifs as p
import random_sequences as r

@click.command()     #dit zijn allemaal decorators
@click.option('--bamfile', help = 'Give the path of a bamfile')
@click.option('--random', default = False, help = 'Set to True (or something else) to generate random motifs')
@click.option('--fastafile', help = 'Give the path of a fastafile')
@click.option('--motifsize', default = 2, help = 'Give the motif size')
@click.option('--dataset', help = 'Give the dataset\'s name')
@click.option('--freqfile', help = 'Give a file with chromosome frequencies')
@click.option('--lenfile', help = 'Give a file with lengths')



def main(bamfile, random, fastafile, motifsize, dataset, freqfile, lenfile):          
 #if you add a docstring here that will be given when you run help  
 #main: code you want to 
#be run when you execute the script
    if bamfile != None:                                                     #option to analyse and plot motifs from a bamfile
        print('there is a bamfile')
        plot_motifs_bamfile(bamfile, motifsize)
    if random != False:                                                     #option to analyse and plot randomly generated sequences
        plot_random_motifs(motifsize)
        print('random is True')
    if fastafile != None:                                                   #option to analyse and plot motifs from a fastafile
        print('there is a fastafile')
        plot_motifs_fastafile(fastafile, motifsize)
    if ((dataset != None) and (freqfile != None) and (lenfile != None)):    #option to generate random sequences from fasta chromosome files
        print('random sequences are generated and saved into a new file')
        generate_random_sequence_from_freqfile(dataset, freqfile, lenfile)
    print('main finished')
    
def plot_motifs_bamfile(bamfile, motifsize):
    p.plot_all(m.get_motif_bamfile(bamfile, motifsize))
    
def plot_random_motifs(motifsize):
    p.plot_all(m.get_motif_random(motifsize))

def plot_motifs_fastafile(fastafile, motifsize):
    p.plot_all(m.get_motif_fastafile(fastafile, motifsize))
    
def generate_random_sequence_from_freqfile(dataset, freqfile, lenfile):
    r.generate_random_sequence_from_freqfile(dataset, freqfile, lenfile)

if __name__ == '__main__':
    print('the script is being executed')
    main()
    print('execution finished')
    #als je iets import is deze conditional false dus dan niet uitgevoerd!!
    
    
    
    
def get_motif(file):
    click.echo(file)

def analyse_plot_motifs():
    pass
    
def get_plot_random_seq():
    a= m.get_random_seq(parameters)
    plot(a)
    
def plot_all(filetype, file, last_n):
    get_motif
    plot_motif
    
    





