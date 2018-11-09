Lines = LOAD '/Users/xuxinpin/Desktop/bbproject/text_choose_2018.txt' AS (line: chararray);
Groups = GROUP Lines BY ', ';
Words = FOREACH Groups GENERATE (TOKENIZE(line)) AS word;
STORE Words INTO '/Users/xuxinpin/Desktop/20183';
