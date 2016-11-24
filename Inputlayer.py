#encoding=utf-8
import jieba
import jieba.posseg as pseg
import sys
import tool 
reload(sys)
sys.setdefaultencoding('utf-8')

Input = open('queries.txt', 'r').read()
Output = open('output.txt', 'w')
Doc = open('document.txt', 'r')


jieba.load_userdict("mydict.txt")
words = pseg.cut(Input)

Queriesset = []
querieslist = []
queries = []
querie = [] 
count = 0 
count2 = 0



term = []
hfterm = open('hfterm.txt', 'r').read()
hftermlist = []
hfterm = hfterm.decode('utf8')
for i in range(len(hfterm)):
	if hfterm[i] == ' ':
		termstr = ''.join(term) 
		term = []
		hftermlist.append(termstr)
	else :
		term.append(hfterm[i])

for word in words:
	if (word.word == '。') &  (count % 3  == 0):
		queries.append(querie)
		querie = [] 
		querieslist.append(queries)
		queries = []
		count2 +=1
	else:
		if word.word == '\t':
			queries.append(querie)
			querie = [] 
			count +=1
		else :
			token = 0
			for i in range (len(hftermlist)) :
				if word.word == hftermlist[i] :
					token = 1
			if token != 1 :	
				weight = 0;
				if word.flag == 'm':
					weight = 2.5
				elif word.flag == 'n':
					weight = 2
				elif word.flag == 'eng':
					weight = 1.5
				elif word.flag == 'v':
					weight = 1
				else :
					weight = 0
				querie.append([word.word,weight])

documentlist = []
temp = Doc.readline()
while temp != '':
	temp=Doc.readline()
	documentlist.append(temp)

for i in range(len(querieslist)) :
	Q4 = []
	for k in range(len(querieslist[i][2])) :
		if len(querieslist[i][2][k][0]) > 2 :
			Q4.append(querieslist[i][2][k])
	Q4 = tool.combinequery(Q4, querieslist[i][1])
	Q4 = tool.combinequery(Q4, querieslist[i][3])
	querieslist[i].append(Q4)
count = 0


for i in range(len(querieslist)) :
	print i
	for j in range(4,5) :
		for k in range(len(querieslist[i][j])) :
			print querieslist[i][j][k][1]
			print querieslist[i][j][k][0]
			count +=1
print count		

