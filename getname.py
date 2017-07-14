import sys,os
path=os.path.split(os.path.realpath(__file__))[0]
path=path+'/yeast_data/GeneSet_des.txt'
fa=open(path)

go2name={}
for line in fa:
    seq=line.split('\t')
    go2name[seq[0]]=seq[1]
fi=open(sys.argv[1])
fo=open(sys.argv[1]+'.name','w')

for line in fi:
    seq=line.split('\t')
    name=go2name[seq[1]]
    fo.write(name+'\t'+line)

