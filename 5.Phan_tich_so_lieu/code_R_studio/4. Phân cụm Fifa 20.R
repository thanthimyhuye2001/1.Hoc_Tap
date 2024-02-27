library(ggplot2)    # Vẽ hình
library(readxl)     # đọc file excel
library(factoextra) # tìm chỉ số Silhouette, Hopkin

# IMPORT DỮ LIỆU 
Fifa20 <- read_excel("football.xlsx")
attach(Fifa20)
View(Fifa20)

# Hiển thị danh sách tên các thuộc tính
name = data.frame(c(names(Fifa20)))
View(name)
View(head(Fifa20,15))


# Tệp có nhiều thông tin không cần để phân cụm
# Chọn dữ liệu để phân tích K-Mean
k.Fifa = Fifa20[,c(44:77)]
View(head(k.Fifa,25))

# Tên thuộc tính có thể mở file Excel giải thích
View(data.frame(c(names(k.Fifa))) )

# Kiểm tra xem dữ liệu mk lấy có ô nào trống ko? 
# Vì K-Mean ko đọc được các biến NA
names(which(colSums(is.na(k.Fifa))>0))

            
# Số liệu được chọn có chung thang đo là thang điểm 100
# Nhưng vẫn phải chuẩn hóa -> Kết quả ko đẹp như bản gốc TT^TT
kk.Fifa = scale(k.Fifa)
View(head(kk.Fifa,25))

# Đo chỉ số Hopkin
get_clust_tendency(kk.Fifa, n=25, graph=F)


#________________________________________________________________________________
# Tìm K phù hợp theo phương pháp Eo-Bồ

library(purrr) #Để dùng hàm map_dbl
set.seed(123)
# function to compute total within-cluster sum of square 
wss <- function(k) {
  kmeans(kk.Fifa, k, nstart=20 )$tot.withinss  #Cái này là TSS
}

# Compute and plot wss for k = 1 to k = 10
k.values <- 1:10

# extract wss for 1-10 clusters
wss_values <- map_dbl(k.values, wss)
wss_values
plot(k.values, wss_values, col="#4683b7",
     type="b", pch = 19, frame = FALSE, ylim=c(1.5*10^5,7*10^5),cex=1.5,xaxt='n',
     xlab="Giá trị K",
     ylab="TSS",
     main= "Elbow Methor - Phương pháp khuỷa tay")
axis(side = 1, at=1:10)
text(x= c(1,4), y = wss_values[c(1,4)]+10^7,round( wss_values[c(1,4)]))
abline(v=c(round(4,wss_values[1])), lty=2, lwd=3)



#__________________________________________________________________________________________________
# Thực hiện Phân tích Cụm

cluster <- kmeans(kk.Fifa,4, nstart=20)
cluster
# Đưa ra luôn kết quả hàm K-mean or nói 3 cái dưới
View(cluster)

# Tổng bình phương khoảng cách trong mỗi cụm
data.frame(cluster$withinss)
# Tổng bình phương khoảng cách trong các cụm
cluster$tot.withinss
# Số lượng cầu thủ trong mỗi cụm
So.Luong = table(cluster$cluster)
View(So.Luong)
Pie = function(){
  cat("Số lượng mỗi cụm:",So.Luong)
  piepercent= round(100*So.Luong/sum(So.Luong), 1)
  pie(So.Luong, 
      cex = 1.4,
      labels = paste0(piepercent, "%"),
      radius= 0.8,
      col=c("#3366FF","#FF0033",
            "#FCA510","green3"),
      main = "TỈ lệ % số lượng cầu thủ mỗi cụm")
  legend("topright", title="Cụm",
         legend = c(1:4), 
         fill = c("#3366FF","#FF0033",
                  "#FCA510","green3"),
         cex = 1.2)
}
Pie()

cbind(So.Luong)

# Gắn dữ liệu gốc với kết quả phân cụm
Full.Fifa <- as.data.frame(cbind(Fifa20[c(3,5:110)],
                                 cluster=cluster$cluster))

Group_1 = Full.Fifa[Full.Fifa$cluster ==1,]
Group_2 = Full.Fifa[Full.Fifa$cluster ==2,]
Group_3 = Full.Fifa[Full.Fifa$cluster ==3,]
Group_4 = Full.Fifa[Full.Fifa$cluster ==4,]

View(head(Group_1[,c(1,2,108)],10))
View(head(Group_2[,c(1,2,108)],10))
View(head(Group_3[,c(1,2,108)],10))
View(head(Group_4[,c(1,2,108)],10))


# Hiển thị Tâm cụm
View(aggregate(kk.Fifa, by=list(cluster=cluster$cluster), mean))

# Ma trận khoảng cách euclidean giữa các tâm cụm 
dist(cluster$centers)


#__________________________________________________________________________________________________
# Đánh giá chất lượng cụm
# Phương pháp Silhouette

library(cluster)
library(factoextra)

sil =silhouette(cluster$cluster, dist(kk.Fifa))
fviz_silhouette(sil)
View(fviz_silhouette(sil)$data)


#__________________________________________________________________________________________________
# Vẽ hình trực quan hóa

color = c("#FCA510","green3", "#3366FF", "#FF0033")
group = as.factor(cluster$cluster)

ggplot(k.Fifa, aes(x=defending_standing_tackle, 
                   y= attacking_finishing, 
                   col= group)) + 
      geom_point(size=2)+
  
      scale_color_manual(values=color)+
  
      labs(x    ="Tắc Bóng", 
           y    ="Tấn công _ Dứt điểm",
           colour ="Cụm") +
      theme(axis.text.x  = element_text(face="bold", size=10),
            axis.text.y  = element_text(face="bold", size=10),
            axis.title.x = element_text(face="bold", size=14),
            axis.title.y = element_text(face="bold", size=14),
            legend.title = element_text(face="bold", size=14),
            legend.text  = element_text(face="bold", size=12))



# Vẽ biểu đồ hộp với các thuộc tính trong k.Fifa
draw_box = function(column = k.Fifa$attacking_finishing , vietsub = "Tốc độ"){
  
  ggplot(k.Fifa, aes(x=group, y=column, fill= group)) +
    
    # geom_boxplot is used to plot the boxplot
    geom_boxplot() +
    scale_fill_manual(values=color ) +
    # stat_summary computes the statistics summary
    # fun.y arguments as mean determines that
    # statistical summary will be mean of y-axis
    stat_summary(fun.y="mean",shape=16, size=0.8,color="white")+
    scale_y_continuous(breaks = seq(from = 0, 
                                    to = 100, 
                                    by = 20))+
    theme_void()+
    labs(x    ="Cụm",
         y    ="",
         title=vietsub,
         fill ="Cụm")
}
draw_box(k.Fifa$physic,   "Thể chất")
draw_box(k.Fifa$dribbling, "Rê bóng")
draw_box(k.Fifa$pace,  "Tốc độ chạy")
draw_box(k.Fifa$defending, "Phòng thủ")
draw_box(k.Fifa$passing, "Chuyền bóng")
draw_box(k.Fifa$shooting, "Sút bóng")           
           


# So sánh chiều cao giữa các cụm
ggplot(Full.Fifa)+
  geom_boxplot(mapping = aes(y = height_cm , 
                             x = group, 
                             fill= group))+
  scale_fill_manual(values=color ) +
  labs(x    ="Cụm", 
       y    ="Chiều cao",
       fill ="Cụm")


# Điểm tổng thể (BXH Fifa xếp thứ tự theo Overall)
ggplot(Full.Fifa)+
  geom_boxplot(mapping = aes(y = overall , 
                             x = group, 
                             fill= group))+
  scale_fill_manual(values=color ) +
  labs(x    ="Cụm", 
       y    ="Overall",
       fill ="Cụm")


# Giá trị cầu thủ (đồng Ơ rô )
ggplot(Full.Fifa)+
  geom_boxplot(mapping = aes(y = wage_eur , 
                             x = group, 
                             fill= group))+
  scale_fill_manual(values=color ) +
  labs(x    ="Cụm", 
       y    ="Tiền lương",
       fill ="Cụm")

