import click 
import myfunctions as mf
import motif_analysis as m
import plot_motifs as p
import random_sequences as r

@click.group()
def main():
    """
    This is the script I made as part of my research project. It can be used to analyse and plot cfDNA sequences. The motif dictionaries are not saved into a file so make sure to write down the outcome. 
    """
    pass

@main.command()
@click.option('--bamfile', '-b', help = 'provide a .bam file')
@click.option('--fastafile', '-f', help = 'provide a .fa file')
@click.option('--saveplot', '-s', default = False, help = 'set to True if you want to save a plot of the analysis')
@click.option('--motifsize', '-m', default = 2, help = 'size of the end motif, default is 2')
@click.option('--path', '-p', default = '/mnt/c/Users/icden/Data_practical', help = 'give a path to where to save the plot figure')

def motif_analysis(bamfile, fastafile, saveplot, motifsize, path):
    """
    This subcommand performs the motif analysis. It returns a dictionary with the frequency of each motif and a plot of these frequencies. 
    """
    if bamfile != None:
        print('there is a bamfile')
        analyse_bamfile(bamfile, motifsize, saveplot, path)
    if fastafile != None:
        print('there is a fastafile')
        analyse_fastafile(fastafile, motifsize, saveplot, path)

def analyse_bamfile(bamfile, motifsize, saveplot, path):
    a = m.get_motif_bamfile(bamfile, motifsize)
    print(a)
    if saveplot != False:
        print('take a look in your folder! There should be a file named \'fig\'. Make sure to save it properly before you do the next analysis.')
        p.plot_all(a, path)

def analyse_fastafile(fastafile, motifsize, saveplot, path): 
    a = m.get_motif_fastafile(fastafile, motifsize)
    print(a)
    if saveplot != False:
        print('take a look in your folder! There should be a file named \'fig\'. Make sure to save it properly before you do the next analysis.')
        p.plot_all(a, path)

@main.command()
@click.option('--dataset', '-d', help = 'enter the name of the dataset')
@click.option('--freqfile', '-f', help = 'give a file with the frequencies of all sequences of a dataset per chromosome')
@click.option('--lenfile', '-l', help = 'give a file with the frequences of each length per dataset')
@click.option('--path', '-p',  default  = "/mnt/c/Users/icden/Data_practical/", help = 'give the path to the files if the default filepath is insufficient')
@click.option('--random', '-r', default = None, help = 'set to True if you want to generate random sequences')
@click.option('--number', '-n', default = 100000, help = 'set the number of sequences you want to randomly generate')

def generate_fasta(dataset, freqfile, lenfile, path, random, number):
    """
    This subcommand generates a file in fasta format, with sequences created according to information provided by the user or with randomly generated sequences.
    """
    print('a fastafile will be generated')
    if dataset != None and freqfile != None and lenfile != None:
        generate_fasta_from_files(dataset, freqfile, lenfile, path)
        print('a fasta file is generated from a frequency file')
    if random !=  None:
        print('a random fasta file is generated')
        generate_random_fasta(number, path)

def generate_fasta_from_files(dataset, freqfile, lenfile, path):
    r.generate_random_sequence_from_freqfile(dataset, freqfile, lenfile, path)
    print('look in your folder! There should be a file named \'DATASET_random_seq.fa\'')

def generate_random_fasta(number, path):
    r.make_fasta_file_from_random_sequences(number, path)
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
    
    





