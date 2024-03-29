#!/usr/bin/env python

# written by Adam Lopez

import optparse
import sys

import bleu
delim = '\t'

def compute_bleu(hyp, refs):
    # print "computing bleu between {} and {}".format(hyp, ref)
  stats = [0 for i in xrange(10)]
  for (r,h) in zip(refs, hyp):
    stats = [sum(scores) for scores in zip(stats, bleu.bleu_stats(h,r))]
    # print "stats {} hyp {} ref {}".format(stats, h, r)
  return bleu.bleu(stats)

if __name__=="__main__":
    optparser = optparse.OptionParser()
    optparser.add_option("-r", "--reference", dest="reference", default="../data-train/LDCtranslations.tsv", help="Target language reference sentences")
    (opts,_) = optparser.parse_args()

    # ref assumes references to be in tab separated format, all references for the same sentence to be in same line
    ref = [[ reference.strip().split() for reference in line.split(delim)[1:] ] for line in open(opts.reference)]
    ref = ref[1:];
    hyp = [line.strip().split() for line in sys.stdin]

    print compute_bleu(hyp, ref)
