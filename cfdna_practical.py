import click 
import myfunctions as mf
import motif_analysis as m
import plot_motifs as p
import random_sequences as r

@click.group()
def main():
    pass

@main.command()
@click.option('--bamfile')
@click.option('--fastafile')
@click.option('--plot', default = False)
@click.option('--motifsize', default = 2)

def motif_analysis(bamfile, fastafile, plot, motifsize):
    if bamfile != None:
        print('there is a bamfile')
        analyse_bamfile(bamfile, motifsize, plot)
    if fastafile != None:
        print('there is a fastafile')
        analyse_fastafile(fastafile, motifsize, plot)

def analyse_bamfile(bamfile, motifsize, plot):
    a = m.get_motif_bamfile(bamfile, motifsize)
    print(a)
    if plot != False:
        print('a plot will be made')
        p.plot_all(a)

def analyse_fastafile(fastafile, motifsize, plot): 
    a = m.get_motif_fastafile(fastafile, motifsize, plot)
    print(a)
    if plot != False:
        print('a plot will be made')
        p.plot_all(a)

@main.command()
@click.option('--dataset')
@click.option('--freqfile')
@click.option('--lenfile')
@click.option('--filepath', default  = "mnt/c/Users/icden/Data_practical/")
@click.option('--random')
@click.option('--number', default = 100000)

def generate_fasta(dataset, freqfile, lenfile, filepath, random, number):
    print('a fastafile will be generated')
    if dataset != None and freqfile != None and lenfile != None:
        generate_fasta_from_files(dataset, freqfile, lenfile, filepath)
        print('a fasta file is generated from a frequency file')
    if random !=  None:
        generate_random_fasta(number)

def generate_fasta_from_files(dataset, freqfile, lenfile, filepath):
    r.generate_random_sequence_from_freqfile(dataset, freqfile, lenfile, filepath)
    print('look in your folder! There should be a file named \'DATASET_random_seq.fa\'')

def generate_random_fasta(number):
    r.make_fasta_file_from_random_sequences(number)
    print('look in your folder! There should be a file named \'random_sequences.fa\'')

if __name__ == '__main__':
    print('the script is being executed')
    main()
    print('execution finished') #never happens



#
#@click.command()     #dit zijn allemaal decorators
#@click.option('--bamfile', help = 'Give the path of a bamfile')
#@click.option('--random', default = False, help = 'Set to True (or something else) to generate random motifs')
#@click.option('--fastafile', help = 'Give the path of a fastafile')
#@click.option('--motifsize', default = 2, help = 'Give the motif size')
#@click.option('--dataset', help = 'Give the dataset\'s name')
#@click.option('--freqfile', help = 'Give a file with chromosome frequencies')
#@click.option('--lenfile', help = 'Give a file with lengths')



#def main(bamfile, random, fastafile, motifsize, dataset, freqfile, lenfile):          
 #if you add a docstring here that will be given when you run help  
 #main: code you want to 
#be run when you execute the script
#    if bamfile != None:                                                     #option to analyse and plot motifs from a bamfile
#        print('there is a bamfile')
#        plot_motifs_bamfile(bamfile, motifsize)
#    if random != False:
#        r.make_fasta_file_from_random_sequences()                                                     #option to analyse and plot randomly generated sequences#
	#plot_random_motifs(motifsize)
#        print('random is True')
#    if fastafile != None:                                                   #option to analyse and plot motifs from a fastafile
#        print('there is a fastafile')
#        plot_motifs_fastafile(fastafile, motifsize)
#    if ((dataset != None) and (freqfile != None) and (lenfile != None)):    #option to generate random sequences from fasta chromosome files
#        print('random sequences are generated and saved into a new file')
#        generate_random_sequence_from_freqfile(dataset, freqfile, lenfile)
#    print('main finished')
#    
#def plot_motifs_bamfile(bamfile, motifsize):
#    p.plot_all(m.get_motif_bamfile(bamfile, motifsize))
#    
#def plot_random_motifs(motifsize):
#    p.plot_all(m.get_motif_random(motifsize))#

#def plot_motifs_fastafile(fastafile, motifsize):
#    p.plot_all(m.get_motif_fastafile(fastafile, motifsize))
#    
#def generate_random_sequence_from_freqfile(dataset, freqfile, lenfile):
#    r.generate_random_sequence_from_freqfile(dataset, freqfile, lenfile)#

#if __name__ == '__main__':
#    print('the script is being executed')
#    main()
#    print('execution finished')
    #als je iets import is deze conditional false dus dan niet uitgevoerd!!
    
    
    
    
#def get_motif(file):
#    click.echo(file)#

#def analyse_plot_motifs():
#    pass
    
#def get_plot_random_seq():
#    a= m.get_random_seq(parameters)
#    plot(a)
    
#def plot_all(filetype, file, last_n):
#    get_motif
#    plot_motif
    
    





