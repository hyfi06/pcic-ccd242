library(ggplot2)

data <- read.table("./data.txt",header = TRUE, stringsAsFactors = FALSE)
data
d10k <- data[data$works=="10k",]
d10k
d1k <- data[data$works=="1k",]
d1k


a10k <- data.frame(cores= as.integer(names(table(d10k$cores))))
for (i in a10k$cores){
  a10k$mean[a10k$cores == i] <- mean(d10k$time[d10k$cores==i])
  a10k$sd[a10k$cores == i] <- sd(d10k$time[d10k$cores==i])
}

a10k

ggplot(d10k, aes(x=cores, y=time),xlab("# Cores"),ylab("Time [s]")) +
  geom_jitter(position = position_jitter(0.3), color = "darkgray")+
  stat_summary(fun.data=mean_sdl, fun.args = list(mult=1),
               geom="pointrange", color="red",size=0.2)+
  stat_summary(aes(label=round(..y..,2)),fun.data=mean_sdl, geom="text",hjust=-0.5,vjust=-1,angle=45)





