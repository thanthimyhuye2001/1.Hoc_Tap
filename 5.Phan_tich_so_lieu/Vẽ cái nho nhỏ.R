ggplot(k.Fifa, aes(x=defending_standing_tackle, 
                   y= attacking_finishing)) + 
  geom_point(shape=16, color="green3",size=2,fill="green3")+
  labs(x    ="Tắc Bóng", 
       y    ="Tấn công _ Dứt điểm") +
  theme(axis.text.x  = element_text(face="bold", size=10),
        axis.text.y  = element_text(face="bold", size=10),
        axis.title.x = element_text(face="bold", size=14),
        axis.title.y = element_text(face="bold", size=14),
        legend.title = element_text(face="bold", size=14),
        legend.text  = element_text(face="bold", size=12))
