
#from rpy2.robjects.packages import importr
#from rpy2.robjects.vectors import FloatVector


import sys
from statsmodels.sandbox.stats.multicomp import multipletests

fi=open(sys.argv[1])
pvalue_list=[]
for line in fi:
    seq=line.rstrip().split('\t')
    p=float(seq[2])
    #if p<1:
    pvalue_list.append(p)

#stats = importr('stats')
#print pvalue_list #FloatVector(pvalue_list)
p_adjust =     multipletests(pvalue_list, alpha=0.05, method='fdr_bh', is_sorted=False, returnsorted=False)[1] #stats.p_adjust(FloatVector(pvalue_list), method = 'fdr')
#print p_adjust
fi.close()


fi=open(sys.argv[1])
fo=open(sys.argv[1]+'.adjust','w')
output=[]
i=0
for line in fi:
    seq=line.rstrip().split('\t')
    p=float(seq[2])
    #if p<1:
    #pa = p_adjust[i]
    output.append([p_adjust[i],p , line.rstrip()+'\t'+str(p_adjust[i]) +'\n'])
    i=i+1
    #else:
        #pa = 1.0
    #fo.write(line.rstrip()+'\t'+str(pa) +'\n')
output.sort()
i=1
for out in output:
    fo.write(str(i)+'\t'+'\t'.join(out[2].split('\t')[1:]))
    i+=1
