#This module recovers an assembly graph
#by overlapping contigs
################################################

from collections import namedtuple
import logging

from Bio import SeqIO

from ragout.shared import config
from ragout.coverlap import _build_overlap_graph

logger = logging.getLogger()

#PUBLIC:
#################################################

#builds assembly graph and outputs it in "dot" format
def make_overlap_graph(contigs_file, dot_file):
    logger.info("Building overlap graph...")
    res = _build_overlap_graph(contigs_file, dot_file,
                               config.ASSEMBLY_MIN_OVERLAP,
                               config.ASSEMBLY_MAX_OVERLAP,
                               config.ASSEMBLY_EXACTLY_K)
    return res
