library(dplyr)


Fifa20 %>% group_by(nationality_name) %>% 
  summarise(count = n())%>%
  arrange(desc(count))


Group_1 %>% group_by(nationality_name) %>% 
  summarise(count = n())%>%
  arrange(desc(count))

library(tidyverse)
library(here)
library(visdat)


Draw_Map = function(fifa20_map = Group_1 ){
  
  if(fifa20_map[1,108] == 1){ text = "Cụm 1"}
  if(fifa20_map[1,108] == 2){ text = "Cụm 2"}
  if(fifa20_map[1,108] == 3){ text = "Cụm 3"}
  if(fifa20_map[1,108] == 4){ text = "Cụm 4"}
  
  fifa20_map$nationality_name[fifa20_map$nationality_name=="United States"] = "USA"
  fifa20_map$nationality_name[fifa20_map$nationality_name=="England"] = "UK"
  fifa20_map$nationality_name[fifa20_map$nationality_name=="China PR"] = "China"
  fifa20_map$nationality_name[fifa20_map$nationality_name=="Korea Republic"] = "South Korea"
  fifa20_map$nationality_name[fifa20_map$nationality_name=="Republic of Ireland"] = "Ireland"
  
  world_map = map_data("world")
  names(world_map)[names(world_map) == 'region'] = 'nationality_name'
  
  numofplayers = world_map %>%
    left_join((fifa20_map %>% 
                 dplyr::count(nationality_name)), by = "nationality_name")
  
  
  ggplot(numofplayers, aes(long, lat, group = group))+
    geom_polygon(aes(fill = n), color = "black", show.legend = TRUE)+
    scale_fill_gradient(low="#FFEF00", high="red", na.value = "#dcdcdc" )+
    
    labs(fill = text,
         title = "Cầu thủ ở các quốc gia")+
    theme_void()+
    
    theme(panel.background = element_rect(fill = "steelblue1",
                                          colour = "steelblue1",
                                          size = 0.5, linetype = "solid"),
          panel.grid.major = element_line(size = 0.5, linetype = 'solid',
                                          colour = "steelblue1"), 
          panel.grid.minor = element_line(size = 0.25, linetype = 'solid',
                                          colour = "steelblue1")
    )+
    theme(legend.title = element_text(face="bold", size=20),
          legend.text  = element_text(face="bold", size=20),
          plot.title   = element_text(face="bold", size=20))
}

Draw_Map(Group_1 )
Draw_Map(Group_2 )
Draw_Map(Group_3 )
Draw_Map(Group_4 )





Chan_Foot = rbind(table(Group_1$preferred_foot),
                 table(Group_2$preferred_foot),
                 table(Group_3$preferred_foot),
                 table(Group_4$preferred_foot))

barplot(Chan_Foot,
        ylim = c(0,5000),
        col = color,
        main = "Preferred Foot Comparison of all Players",
        beside = TRUE )
legend(2,4700, 
       legend = c(1:4), 
       fill = color,
       cex = 1.45)
