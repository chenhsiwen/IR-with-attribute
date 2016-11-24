#encoding=utf-8
import main
import csv
import sys

sys.setdefaultencoding('utf-8')
reload(sys)
Doclist = open('doclist4.txt', 'w')

querieslist = main.querieslist
documentlist = main.documentlist
qdlist = main.qdlist

ranklist = main.ranklist
num_query = len(querieslist)
method = 4

temp = []
IDliststr =''
IDlist = [] 
IDstr = ''
CHAR =[]


#build the rel new list for top 100
col  = ['Id', 'Rel_News']  
IDlist.append(col)
for q in range(num_query):
	for j in range(100):
		rid = ranklist[q][j][0]
		did = qdlist[q][rid]
		for i in range(len(documentlist[did])):
			if documentlist[did][i] == "\t" :
				CHAR.append(' ')
				break
			else:
				CHAR.append(documentlist[did][i])
	IDstr = ''.join(CHAR) 
	CHAR = []
	IDlist.append([q+1,IDstr])
	temp=[]


output = open("test17.csv","w")
w = csv.writer(output)
w.writerows(IDlist)
output.close()


# 11 1 + 2 
# 12 1 + 2 + 3
# max123 1 + 2 + 3 max
# temp 1+2+3 no weight max