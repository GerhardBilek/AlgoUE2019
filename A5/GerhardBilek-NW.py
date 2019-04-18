#!/Users/gerhardbilek/anaconda3/bin/python3

import argparse
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
#from Bio.SeqRecord import SeqRecord
#from Bio.Align import Applications

#__ARGPARSER
parser=argparse.ArgumentParser(description="Global sequence alignment of two fasta sequences using Needleman-Wunsch alogorithm. Enter a multi-sequence file containing two fasta squences via STDIN. CLI example: python3 nw.py < short_mulitseq.fa ")
parser.add_argument('-m','--match', type=int, default= 1, required=False, help='change default scoring value "1" for matches')
parser.add_argument('-mm','--mismatch', type=int, default= -1, required=False, help='change defazkt scoring value "-1" for mismatches')
parser.add_argument('-g','--gap', type=int, default = -2, required=False, help='change default scoring value "-2" for gaps')
args = parser.parse_args()
 
matchScore = args.match         # diagonal score
mismatchScore = args.mismatch   # diagonal score
gapScore = args.gap             # right & bottom score

#__PARSING ID and Sequence of the FASTA FILE
fastaFiles = sys.stdin
seqFiles = SeqIO.parse(fastaFiles,"fasta", generic_dna)     
seqList = []
idList = []
for sequence in seqFiles:
    seqList.append(sequence.seq)
    idList.append(sequence.id)
id1 = idList[0]
seq1 = seqList[0]
id2 = idList[1]
seq2 = seqList[1]

#__INITIALIZE Scoring and Path Matrix
scoringMatrix = [[0]]
pathMatrix = [[" "]]
nrow = len(seq1) + 1    # +1 ... first gap row
ncol = len(seq2) + 1

for i in range(1,ncol,1):   # adds gap score to first column
    scoringMatrix[0].append(scoringMatrix[0][i - 1] + gapScore)  # adds score to prev. cell and appends
    pathMatrix[0].append("h")

#__FILL MATRICES
s1 = 0
s2 = 0
for row in range(1,nrow,1):         #  initialize the row; Start with 1 to skip gap row
    scoringMatrix.append([scoringMatrix[row - 1][0] + gapScore]) # new row with add gapscore form prev. row start cell
    pathMatrix.append(["v"])        # gamp column contains only "v" ... vertical
    for col in range(1,ncol,1):     # fill the row by walking through columns; Start at 1 to skip gap column 
        
        #__Calculate weight from vertical, horizontal and diagonal by using Scores
        vertical = scoringMatrix[row - 1][col] + gapScore
        horizontal = scoringMatrix[row][col - 1] + gapScore
        if (seq1[s1] == seq2[s2]):
            diagonal = scoringMatrix[row - 1][col - 1] + matchScore
        else:
            diagonal = scoringMatrix[row - 1][col - 1] + mismatchScore
        
        #__Path Decision - Adding heighest weight to scoring Matrix
        if horizontal >= vertical and horizontal > diagonal:
            scoringMatrix[row].append(horizontal)
            pathMatrix[row].append("h")
        elif vertical > horizontal and vertical > diagonal:
            scoringMatrix[row].append(vertical)
            pathMatrix[row].append("v")
        elif diagonal >= horizontal and diagonal >= vertical:
            scoringMatrix[row].append(diagonal)
            pathMatrix[row].append("x")
        s2 += 1   # iterating the rows     
    s1 +=1
    s2 = 0  # Reseting the squence counter to start new row

#__Dimensions for path Matrix
col = ncol - 1
row = nrow - 1
#print(col, row) #TEST
p = ""                # store backward path

#__PATH development
while(row > 0 or col > 0):
    if pathMatrix[row][col] == "x":
        p += "x"
        row -= 1
        col -= 1
    elif pathMatrix[row][col] == "v":
        p += "v"
        row -= 1
    elif pathMatrix[row][col] == "h":
        p += "h"
        col -= 1
path = p[::-1]  # convert to forward path
#print(path) #TEST

#__ALIGNMENTS
align1 = ""         # build 1st alignment
align2 = ""         # build 2nd alignment
align3 = ""         # build symbol line
s1 = 0
s2 = 0
for step in path:
    if step == "x":
        align1 += seq1[s1]
        align2 += seq2[s2]
        if seq1[s1] == seq2[s2]:
            align3 += "*"     # BOOM: add symbol for proper bp alignment
        else:
            align3 += " "     # Mismatch
        s1 += 1
        s2 += 1
    elif step == "v":         # Keep base of 1st seq
        align1 += seq1[s1]    # Keep base
        align2 += "-"         # Insert Gap in 2nd seq
        align3 += " "
        s1 += 1
    elif step == "h":         # Keep base of 2nd seq if horizontal gap was included
        align1 += "-"
        align2 += seq2[s2]
        align3 += " "
        s2 += 1

#print(align1)  #TEST
#print(align2)  #TEST
#print(align3)  #TEST
#print(len(seq1)//linelength)   #TEST

#__CLUSTAL Outputs to STDOUT
def niceOutput(linelength, ID1, seq1, ID2, seq2, seq3):
    if len(seq1) <= linelength and len(seq2) <= linelength:
        print('{:18}'.format(ID1), seq1)
        print('{:18}'.format(ID2), seq2)
        print('{:18}'.format(""),seq3)
    else:
        print('{:18}'.format(ID1), seq1[0:linelength])
        print('{:18}'.format(ID2), seq2[0:linelength])
        print('{:18}'.format(""), seq3[0:linelength])
        print("")
        start=linelength
        for i in range(len(seq1)//linelength): 
            print('{:18}'.format(ID1), seq1[start:start+linelength])
            print('{:18}'.format(ID2), seq2[start:start+linelength])
            print('{:18}'.format(""),seq3[start:start+linelength])
            print("")
            start=start+linelength

linelength = 60
niceOutput(linelength, id1, align1, id2, align2, align3)

#__SIMILARITY VALUE to STDERR
print(scoringMatrix[len(seq1)][len(seq2)], file=sys.stderr)

'''

#__TEST
for row in scoringMatrix:
    print(row)
for row in pathMatrix:
    print(row)

#SeqIO.write(rec_temp, "outputGer.fa", "clustal")
#AlignIO.write(rec_temp, "outputGer.fa", "clustal")
#print(fastaFiles)

'''