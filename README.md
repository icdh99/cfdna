# cfDNA End Motif Analysis
This script is aimed at end motif analysis of DNA reads, it was build specifically for cell-free DNA (cfDNA) reads. Given a certain dataset, this script can build a random control dataset for you to identify any difference in end motif distribution between your dataset and the generated control. 

## Getting Started


### Prerequisites
Required packages:
- click, pysam, matplotlib, pandas, natsort

  `pip install click pysam matplotlib pandas natsort`

- Other default packages used in this package: collections, random

### Installing
Create a new conda environment and install all the required python packages as listed above. The package is tested with python 3.6.

## Usage
The script can work with both .bam and .fa files. There are two main functionalities: (1) generation of a simulated cfdna .fa file by random choice from A,T,G,C or by random sampling fragments from a genome. (2) cfdna end motif analysis. The two functionalities are selected using subcommands `generate-fasta` and `motif-analysis`. Below we demonstrate how to use the subcommands, what options and arguments to supply, and what output will be generated. 

### Getting started:

`python cfdna_practical.py --help` gives a general overview of the usage of the script and the subcommands

`python cfdna_practical.py generate-fasta --help` lists the options for the subcommand generate-fasta, as will be described below.

`python cfdna_practical.py motif-analysis --help` lists the options for the subcommand motif-analysis, as will be described below.

### Fasta file generation
This subcommand can either generate a .fa file according to provided information about a dataset, or it can generate a .fa file with randomly generated sequences. 

#### Simulate cfdna reads by random sampling from a genome based on given cfdna length distribution and frequency per chromosome: Control .fa file
The required arguments of this subcommand are:
`python cfdna_practical.py generate-fasta --dataset 'name of dataset' --freqfile 'file.txt' --lenfile 'file.txt'`

Freqfile indicates a file that harbours the frequencies of reads per chromosome. It is a .txt file and looks the following: 

chr1    473764

chr2    734635

...

Lenfile indicates a file that harbours the length of each sequence, each written on a newline. 

Dataset indicates the name of the dataset that you are analysing so that this can be used to write new filenames.

Further options are:
`--path` 

This gives the path to the folder where the files are located and saved, if the default path is not sufficient (which will be the case on another computer than my own).

The output is a .fa file named DATASET_random_seq.fa.

#### Simulate cfdna reads of set length by random selecting from A,T,G,C: Random .fa file
The required arguments of this subcommand are:
`python cfdna_practical.py generate-fasta --random True`

Set --random to True. 

Further options are:
`--number` (default = 100,000)

This sets the amount of sequences the .fa file should contain.

This results in a .fa file named 'random_sequences.fa'. 

### End motif analysis
This subcommand analyses the end motifs of the read supplied in either a .fa or a .bam file. Optionally it generates a histogram with the counts per k-mer. 

#### .bam file analysis
`python cfdna_practical.py motif-analysis --bamfile 'file.bam'`

The required argument is --bamfile with the name of the bamfile that has to be analysed.

Optional arguments are:
`--motifsize` 

This is an integer that indicates the k-mer size of the end motif, default is 2.

`--saveplot`

Set to True if you want to save a figure of the plot, it will be saved in a file named 'fig'. 

#### .fa file analysis
`python cfdna_practical.py motif-analysis --fastafile 'file.fa'`

The required argument is --fastafile with the name of the fastafile that has to be analysed. 

Optional arguments are:
`--motifsize` 

This is an integer that indicates the k-mer size of the end motif, default is 2.

`--saveplot`

Set to True if you want to save a figure of the plot, it will be saved in a file named 'fig'. 

`--path`

This is the path to the location the plot is saved. 

The output of the subcommand `motif-analysis` is a dictionary printed in the command line which harbours how many times each end motif occurs. Optionally, a histogram which visualizes the dictionary can be saved. 

## License
This project is licensed under the MIT license. 
