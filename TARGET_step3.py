from TARGET import *
import sys

print '''
$1 | score_dir       |
$2 | dist dir        | 
$3 | gene list file  |
$4 | output_dir      |
$5 | cpu             |
'''

enrich_MAIN(sys.argv[1],sys.argv[2], sys.argv[3],  sys.argv[4], PROC_LIMIT=int(sys.argv[5]))



