from TARGET import *
import sys
print '''
$1 | score_dir          |
$2 | random list length | 
$3 | permutation time   |
$4 | output_dir         | directory of p-value distribution files
$5 | cpu                |
'''


prepare_DIST(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], seed=12345, PROC_LIMIT=int(sys.argv[5]))



