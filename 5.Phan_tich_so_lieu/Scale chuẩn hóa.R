library(ggplot2)    # Vẽ hình
library(readxl)     # đọc file excel
library(factoextra) # tìm chỉ số Silhouette, Hopkin
library(cluster)

# IMPORT DỮ LIỆU 
Fifa20 <- read_excel("football.xlsx")
attach(Fifa20)

k.Fifa = Fifa20[,c(44:77)]
k.Fifa = scale(k.Fifa)

# Đánh giá chất lượng cụm
# Phương pháp Silhouette


sil =silhouette(cluster$cluster, dist(k.Fifa))
fviz_silhouette(sil)
View(fviz_silhouette(sil)$data)