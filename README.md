# synth-fasta
A tool to create synthetic fasta files

# Description
This tool will create a controllable number of arbitrarily long sequence entries. By default, it will create 24 (extremely) short sequences, to mimic a human reference genome. It is meant to act as a tool to create "test" reference genomes for early software tool development purposes. What you do with it is up to you; I'm not the bioinformatics police.

# Usage examples
- `python3 synth_fasta.py`
This will create a file called synth_fasta.fna which contains 24 10-kb records (included in this repo)

- `python3 synth_fasta.py -l 100000 -c 11 -o test`
This will create a file called test.fna which contains 11 100-kb records

- `python3 synth_fasta.py -h`
Prints the following:
```
usage: synth_fasta.py [-h] [-c CONTIGS] [-l CONTIG_LEN] [-o OUT] [-s SEED] [-z] [-v] [--contig_name CONTIG_NAME]
                      [--telomeres TELOMERES] [--centromeres CENTROMERES] [--protein] [--gc GC]

Processing synth_fasta arguments

optional arguments:
  -h, --help            show this help message and exit
  -c CONTIGS, --contigs CONTIGS
                        Number of contigs to create, int
  -l CONTIG_LEN, --contig_len CONTIG_LEN
                        Length of created contigs, int
  -o OUT, --out OUT     Output prefix, default synth_fasta
  -s SEED, --seed SEED  Random number seed, default 112358
  -z, --compress        Create gz-compressed output file (not implemented)
  -v, --verbose         Increase runtime output
  --contig_name CONTIG_NAME
                        Base name for created contigs, string
  --telomeres TELOMERES
                        Include proportional telomere Ns, default amount = 0.001 (not implemented)
  --centromeres CENTROMERES
                        Include absolute centromere Ns, default amount = 0.03 (not implemented)
  --protein             Create protein sequence instead of nucleotide, default false (not implemented)
  --gc GC               Define a GC percentage (approximate), default 0.5
```

# Argument notes
Some of the arguments in "future development" exist in the help, but do not yet have an effect.

# Future development
- a switch to create synthetic protein sequences (default is nucleotide sequences)
- an argument to control an amount on telomere added to each record
- an argument to control an amount of centromere added to each record
- tunable GC percentage (default equal probability A/C/G/T)
- motif inclusion: STRs, oligonucleotide sequences, etc.
- "other" reference sequence inclusion (i.e., the ability to salt in "real" reference sequence, either randomly or in a specific record)
