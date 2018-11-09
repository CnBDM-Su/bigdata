import csv
with open('/Users/xuxinpin/Desktop/bbproject/wordcount/part-r-2018.csv') as f:
    rows = csv.reader(f)

    with open('/Users/xuxinpin/Desktop/bbproject/wordcount/2018.csv','w') as f1:
        writer = csv.writer(f1)
        for line in rows:
            line.append(2018)
            writer.writerow(line)

