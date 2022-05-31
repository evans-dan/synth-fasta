# synth-fasta
A tool to create synthetic fasta files

# Description
This tool will create a controllable number of arbitrarily long sequence entries. By default, it will create 24 (extremely) short sequences, to mimic a human reference genome. It is meant to act as a tool to create "test" reference genomes for early software tool development purposes. What you do with it is up to you; I'm not the bioinformatics police.

# Usage examples
- To be provided later.

# Future development
- a switch to create synthetic protein sequences (default is nucleotide sequences)
- a switch to turn on/off the creation of multi-N sequence telomeres (default on)
- a switch to turn on/off the creation of multi-N sequence centromeres (default on)
- tunable GC percentage (default equal probability A/C/G/T)
- motif inclusion: STRs, oligonucleotide sequences, etc.
- "other" reference sequence inclusion (i.e., the ability to salt in "real" reference sequence, either randomly or on a specific "chromosome")
