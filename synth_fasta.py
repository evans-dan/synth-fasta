#
# synth_fasta.py - create FASTA-format files that are completely fake.
#
# Theory of operation: this script will read the passed-in arguments and
#   create FASTA-formatted files as defined here:
#   https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=BlastHelp
#

#
# libraries
#

import sys
import argparse
import random

#
# default values - move this into a config file?
#

DEFAULT_CONTIGS = 24
DEFAULT_CONTIG_LEN = 10000
DEFAULT_OUT = 'synth_fasta' # default output file prefix; i.e. 'synth_fasta.fa'
DEFAULT_TELOMERES = True
DEFAULT_CENTROMERES = True
DEFAULT_CONTIG_NAME = 'lcl|synth_fasta_contig'
DEFAULT_TELOMERES = True
DEFAULT_CENTROMERES = True
DEFAULT_CENTROMERE_SHARE = 0.03
DEFAULT_TELOMERE_SHARE = 0.001
DEFAULT_PROTEIN = False
DEFAULT_GC = 0.5
DEFAULT_SEED = 112358 # the first few Fibonacci numbers
DEFAULT_FASTA_LINE_LEN = 80 # fasta files are "recommended" to be shorter than 80 characters

#
# read in and deal with command-line arguments
#

parser = argparse.ArgumentParser(description="Processing synth_fasta arguments")
parser.add_argument('-c', '--contigs', help='Number of contigs to create, int', type=int, default=DEFAULT_CONTIGS)
parser.add_argument('-l', '--contig_len', help='Length of created contigs, int', type=int, default=DEFAULT_CONTIG_LEN)
parser.add_argument('-o', '--out', help='Output prefix, default synth_fasta', default=DEFAULT_OUT)
parser.add_argument('-s', '--seed', help=f"Random number seed, default {DEFAULT_SEED}", default=DEFAULT_SEED)
parser.add_argument('-z', '--compress', help='Create gz-compressed output file (not implemented)', action='store_true')
parser.add_argument('-v', '--verbose', help='Increase runtime output', action='store_true')
parser.add_argument('--contig_name', help='Base name for created contigs, string', default=DEFAULT_CONTIG_NAME)
parser.add_argument('--telomeres', help=f"Include proportional telomere Ns, default amount = {DEFAULT_TELOMERE_SHARE} (not implemented)", default=DEFAULT_TELOMERE_SHARE)
parser.add_argument('--centromeres', help=f"Include absolute centromere Ns, default amount = {DEFAULT_CENTROMERE_SHARE} (not implemented)", default=DEFAULT_CENTROMERE_SHARE)
parser.add_argument('--protein', help='Create protein sequence instead of nucleotide, default false (not implemented)', action='store_true', default=False)
parser.add_argument('--gc', help=f"Define a GC percentage (approximate), default {DEFAULT_GC}", type=float, default=DEFAULT_GC)

args = parser.parse_args()
arg_str = ''
for (k, v) in vars(args).items():
    arg_str = arg_str + f"\t{k} = {v}\n"

if args.verbose:
    print(f"MESSAGE: {sys.argv[0]} beginning execution", file=sys.stderr)
    print(f"MESSAGE: runtime argument values are: \n{arg_str}")

# what are we calling output?

out_fname = args.out

if args.protein is True:
    out_fname = out_fname + '.faa'
else:
    out_fname = out_fname + '.fna'

base_weights = [(1-args.gc)/2, args.gc/2, args.gc/2, (1-args.gc)/2]

#
# begin writing contigs
#

random.seed(args.seed) # set the random seed value

if args.verbose:
    print(f"MESSAGE: writing out {args.contigs} contigs of length {args.contig_len} to {out_fname}")

with open(out_fname, "w") as out_fh:

    for i in range(args.contigs):

        #contig_id = f"{args.contig_name}{i+1}"
        out_fh.write(f">{args.contig_name}{i+1} synth_fasta synthetic contig\n") # write the header

        for base_count in range(0, args.contig_len, DEFAULT_FASTA_LINE_LEN):

            if base_count + DEFAULT_FASTA_LINE_LEN < args.contig_len:
                out_fh.write(''.join(random.choices(['A','C','G','T'], weights=base_weights, k=DEFAULT_FASTA_LINE_LEN)) + "\n")
                # write out a line at a time

        out_fh.write(''.join(random.choices(['A','C','G','T'], weights=base_weights, k= args.contig_len - base_count)) + "\n")
        # get the last bit of the contig Length
        base_count = 0

        if args.verbose:
            print(f"MESSAGE: contig {args.contig_name}{i+1} complete\n")

out_fh.close()
