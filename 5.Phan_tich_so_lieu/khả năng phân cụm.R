library(factoextra)
library(cluster)
library(NbClust)
library(datasets)
library(factoextra)
df = k.Fifa
df= scale(df)
df[2]
View(df)

for(i in 1:2){
  cat(typeof(df[1]),"\n")
}



get_clust_tendency(k.Fifa, n=25,graph =F)
km = kmeans(k.Fifa,2)
class(k.Fifa$a)
View(km)
fviz_cluster(km, k.Fifa)
k.Fifa = scale(k.Fifa)
fviz_nbclust(k.Fifa, FUN= kmeans, method = "wss",k.max =10)


mean(k.Fifa$goalkeeping_reflexes)
mean(k.Fifa$movement_reactions)
