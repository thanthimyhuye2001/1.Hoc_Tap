# Chọn K = ?

library(purrr) #Để dùng hàm map_dbl
set.seed(123)
a=c(1.5,3.5,1,2,4)
b =c(3,0,4,1,2)
k.Fifa=data.frame(a,b)

View(aa)
k.Fifa
plot(a,b)
3*(3.166667-2.4)^2+2*(2.4- 1.25)^2 +3*(1-2)^2+2*(3.5-2)^2
mean(b)
# function to compute total within-cluster sum of square 
wss <- function(k) {
  kmeans(k.Fifa, k, nstart = 2 )$tot.withinss
}

# Compute and plot wss for k = 1 to k = 15
k.values <- 1:4

# extract wss for 2-15 clusters
wss_values <- map_dbl(k.values, wss)
wss_values

plot(k.values, wss_values,
     type="b", pch = 19, cex=1.5, frame = FALSE, ylim=c(0,20),
     xlab="Giá trị K",
     ylab="Total within-clusters sum of squares",
     main= "Elbow Methor")
text(x= k.values, y = wss_values+1,round( wss_values,2) ,cex=1.5)

library(cluster)
library(factoextra)
aa = kmeans(k.Fifa,4)
sil =silhouette(aa$cluster, dist(k.Fifa))
View(fviz_silhouette(sil))

fviz_cluster ( aa, data = k.Fifa )
