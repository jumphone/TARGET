##################################################################
!<<!

TARGET - neTwork bAsed enRichment of Gene sETs

Author: Feng ZHANG - 2017-07-14

Email: 15110700005@fudan.edu.cn

!
##################################################################


CPU=10

#Preparation

NETWORK=yeast_data/Yeast_TF_net.txt
GENESET=yeast_data/Gene_Set_yeast.txt
SCORE=yeast_data/SCORE/
DIST=yeast_data/DIST/
LIST_LENGTH=70
PERMUTATION_TIME=100
STEP=5
python TARGET_step1.py $NETWORK $GENESET $SCORE $STEP $CPU
python TARGET_step2.py $SCORE $LIST_LENGTH $PERMUTATION_TIME $DIST $CPU


#Enrichment

sporilation
GENE_LIST=yeast_data/sporulation.id.TF_list.txt
OUT=yeast_data/SP_OUT
python TARGET_step3.py $SCORE $DIST $GENE_LIST $OUT $CPU
cat $OUT\/* > $GENE_LIST\.enrich
python Padjust.py $GENE_LIST\.enrich
python getname.py $GENE_LIST\.enrich.adjust

#cellcycle
GENE_LIST=yeast_data/cellcycle.id.TF_list.txt
OUT=yeast_data/CC_OUT
python TARGET_step3.py $SCORE $DIST $GENE_LIST $OUT $CPU
cat $OUT\/* > $GENE_LIST\.enrich
python Padjust.py $GENE_LIST\.enrich
python getname.py $GENE_LIST\.enrich.adjust

#Result
echo ""
echo "##############################################################"
echo ""
echo "DEMO RESULT (Top 10 of 183 gene sets):"
echo ""
echo "-------------------------------------------------------------"
echo ""
echo "TARGET:   Sporulation"
echo ""
echo "col 1: Gene Set   |   col 2: Rank   |   col 3: P-value   |   col 4: FDR"
echo ""
GENE_LIST=yeast_data/sporulation.id.TF_list.txt
cat $GENE_LIST\.enrich.adjust.name | cut -f 1,2,4,11 | head -n 10
echo ""
echo ""
echo "-------------------------------------------------------------"
echo ""
echo "TARGET:   Cell cycle"
echo ""
echo "col 1: Gene Set   |   col 2: Rank   |   col 3: P-value   |   col 4: FDR"
echo ""
GENE_LIST=yeast_data/cellcycle.id.TF_list.txt
cat $GENE_LIST\.enrich.adjust.name | cut -f 1,2,4,11 | head -n 10
echo ""
echo ""
echo "##############################################################"
echo ""
