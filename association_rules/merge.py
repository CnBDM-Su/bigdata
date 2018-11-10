fout=open("merge.csv","a")

for line in open("text_choose_2009.csv"):
	fout.write(line)
for num in range(2010,2018):
	f = open("text_choose_"+str(num)+".csv")
	for line in f:
		fout.write(line)
	f.close()
fout.close()
