countdata <- as.data.frame(read.csv("/Users/lipeiyu/Desktop/countdata.csv"))
kmdata <- as.matrix(countdata[1:2087,])
count <- 1
year <- c(2009:2018)
nextyear <- data.frame(year=2019)
while(count<2088){
  number <- as.vector(kmdata[count,2:11]) #把第count个单词的每年次数读入number 
  lm.reg <- lm(number~year)   #做线性回归
  result <- predict(lm.reg,nextyear,interval = "prediction",level = 0.95)
  rowname <- as.vector(kmdata[count,1])
  write.table(result, file = "/Users/lipeiyu/Desktop/predict2019.csv", sep =",",row.names = rowname,append = TRUE,col.names =FALSE) #把预测结果写入csv文件
  count=count+1
}


