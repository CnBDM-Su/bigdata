library("ggplot2")
classified1 <- read.csv("/Users/lipeiyu/Desktop/classified1.csv")
png("/Users/lipeiyu/Desktop/classified1.png")
p1 <- ggplot(classified1, aes(x = year, y = number, colour = name))+geom_point(alpha = .5)+scale_size_area()+ylim(0,1000)+geom_smooth(method=lm)
p1
dev.off()