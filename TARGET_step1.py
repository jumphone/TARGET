from TARGET import *
import sys
print '''
$1 | network file | col1: gene, col2: gene
$2 | geneset file | col1: gene, col2: geneset
$3 | output_dir   | directory of score files
$4 | max step     | 
$5 | cpu          |
'''


prepare_STEP(sys.argv[1], sys.argv[2], sys.argv[3], max_step=int(sys.argv[4]), PROC_LIMIT=int(sys.argv[5]))



