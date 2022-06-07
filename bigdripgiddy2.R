library(tidyverse)

inmycloset <- function(mypants = NULL, myshirts = NULL, mysocks = NULL, 
                       myshoes = NULL, myhat = NULL, myhoodie = NULL, 
                       mylayer = NULL, myjacket = NULL, myshorts = NULL){
  pants <<- mypants %>% 
    as.data.frame() %>% 
    rename('pantsname' = ".")
  if (is.null(pants) == T){
    rm(pants, envir = globalenv())
  }
  socks <<- mysocks %>% 
    as.data.frame() %>% 
    rename('sockname' = ".")
  if (is.null(socks) == T){
    rm(socks, envir = globalenv())
  }
  shoes <<- myshoes %>% 
    as.data.frame() %>% 
    rename('shoename' = ".")
  if (is.null(shoes) == T){
    rm(shoes, envir = globalenv())
  }
  hats <<- myhat %>% 
    as.data.frame() %>% 
    rename('hatname' = ".")
  if (is.null(hats) == T){
    rm(hats, envir = globalenv())
  }
  hoodies <<- myhoodie %>% 
    as.data.frame() %>% 
    rename('hoodiename' = ".")
  if (is.null(hoodies) == T){
    rm(hoodies, envir = globalenv())
  }
  layers <<- mylayer %>% 
    as.data.frame() %>% 
    rename('layername' = ".")
  if (is.null(layers) == T){
    rm(layers, envir = globalenv())
  }
  jackets <<- myjacket %>% 
    as.data.frame() %>% 
    rename('jacketname' = ".")
  if (is.null(jackets) == T){
    rm(jackets, envir = globalenv())
  }
  shorts <<- myshorts %>% 
    as.data.frame() %>% 
    rename('shortsname' = ".")
  if (is.null(shorts) == T){
    rm(shorts, envir = globalenv())
  }
  shirts <<- myshirts %>% 
      as.data.frame() %>%
      rename('shirtname' = ".")
  if (is.null(shirts) == T){
    rm(shirts, envir = globalenv())
  }
  if(exists("dirty") == T){
    rm(dirty, envir = globalenv())
  }
}


ootd <- function(mypants = T, myshirts = T, mysocks = T, myshoes = T, 
                 myhat = F, myhoodie = F, mylayer = F, myjacket = F, 
                 myshorts = F){
  pantsOfTheDay <- sample(pants$pantsname, 1)
  shirtOfTheDay <- sample(shirts$shirtname, 1)
  socksOfTheDay <- sample(socks$sockname, 1)
  shoesOfTheDay <- sample(shoes$shoename, 1)
  hatOfTheDay <- sample(hats$hatname, 1)
  hoodieOfTheDay <- sample(hoodies$hoodiename, 1)
  layerOfTheDay <- sample(layers$layername, 1)
  jacketOfTheDay <- sample(jackets$jacketname, 1)
  shortsOfTheDay <- sample(shorts$shortsname, 1)
  
  # SELECT THE ITEMS OF CLOTHING
  if (mypants == T){
    pantsOfTheDay <- sample(pants$pantsname, 1)
  } else {
    pantsOfTheDay <- NA
  }
  
  shirtOfTheDay <- sample(shirts$shirtname, 1)
  
  socksOfTheDay <- sample(socks$sockname, 1)
  
  shoesOfTheDay <- sample(shoes$shoename, 1)
  
  if (myhat == T) {
    hatOfTheDay <- sample(hats$hatname, 1)
  } else {
    hatOfTheDay <- NA
  }
  
  if (myhoodie == T) {
    hoodieOfTheDay <- sample(hoodies$hoodiename, 1)
  } else {
    hoodieOfTheDay <- NA
  }
  
  if (mylayer == T) {
    layerOfTheDay <- sample(layers$layername, 1)
  } else {
    layerOfTheDay <- NA
  }
  
  if (myjacket == T) {
    jacketOfTheDay <- sample(jackets$jacketname, 1)
  } else {
    jacketOfTheDay <- NA
  }
  
  if (myshorts == T) {
    shortsOfTheDay <- sample(shorts$shortsname, 1)
  } else {
    shortsOfTheDay <- NA
  }
  
  # DISQUALIFY CERTAIN COMBOS
  # tons of if statments about sock and shoe combos
  if (socksOfTheDay == "spongebob" & shoesOfTheDay == "timbs"){
    socksOfTheDay <- sample(socks$sockname, 1)
    shoesOfTheDay <- sample(shoes$shoename, 1)
  }
  if (socksOfTheDay == "black sauconys" & shoesOfTheDay == "timbs"){
    socksOfTheDay <- sample(socks$sockname, 1)
    shoesOfTheDay <- sample(shoes$shoename, 1)
  }
  if (socksOfTheDay == "hawks" & shoesOfTheDay == "timbs"){
    socksOfTheDay <- sample(socks$sockname, 1)
    shoesOfTheDay <- sample(shoes$shoename, 1)
  }
  if (socksOfTheDay == "spongebob" & shoesOfTheDay == "am95s"){
    socksOfTheDay <- sample(socks$sockname, 1)
    shoesOfTheDay <- sample(shoes$shoename, 1)
  }
  if (socksOfTheDay == "spongebob" & shoesOfTheDay == "desert boots"){
    socksOfTheDay <- sample(socks$sockname, 1)
    shoesOfTheDay <- sample(shoes$shoename, 1)
  }
  if (socksOfTheDay == "hawks" & shoesOfTheDay == "desert boots"){
    socksOfTheDay <- sample(socks$sockname, 1)
    shoesOfTheDay <- sample(shoes$shoename, 1)
  }
  if (socksOfTheDay == "black sauconys" & shoesOfTheDay == "desert boots"){
    socksOfTheDay <- sample(socks$sockname, 1)
    shoesOfTheDay <- sample(shoes$shoename, 1)
  }
  if (socksOfTheDay == "tiger" & shoesOfTheDay == "timbs"){
    socksOfTheDay <- sample(socks$sockname, 1)
    shoesOfTheDay <- sample(shoes$shoename, 1)
  }
  
  # other illegal combos
  if (shirtOfTheDay == "red, white, and black ss button-up" & 
      shoesOfTheDay == "desert boots"){
    shirtOfTheDay <- sample(shirts$shirtname, 1)
    shoesOfTheDay <- sample(shoes$shoename, 1)
  }
  # no shorts and boots combos
  if (myshorts == TRUE & shoesOfTheDay == "desert boots"){
    shoesOfTheDay <- sample(shoes$shoename, 1)
  }
  if (myshorts == TRUE & shoesOfTheDay == "timbs"){
    shoesOfTheDay <- sample(shoes$shoename, 1)
  }
    
  no1 <- as_tibble(c("pants", "shirt", "socks", "shoes", "hat", "hoodie", "layer", 
                     "jacket", "shorts")) %>% 
    rename("type" = "value")
  
  no2 <- as_tibble(c(pantsOfTheDay, shirtOfTheDay, socksOfTheDay, shoesOfTheDay, 
                     hatOfTheDay, hoodieOfTheDay, layerOfTheDay, 
                     jacketOfTheDay, shortsOfTheDay)) %>% 
    rename("item" = "value")
  
  no3 <- cbind(no1, no2) %>% 
    as_tibble() %>% 
    drop_na()
  
  if(exists("dirty") == F){
    dirty <<- as_tibble(matrix(c(NA, NA), nrow = 1)) %>% 
      rename("type" = "V1", "item" = "V2")  
  }
  
  dirty1 <- no3 %>% 
    filter(type %in% c("shirt", "socks", "shorts"))
  
  dirty <<- rbind(dirty, dirty1) %>% 
    drop_na()
  
  dirtyShirts <- dirty %>%
    filter(type == 'shirt') %>%
    select(item) %>%
    rename('shirtname' = 'item')

  # shirts <<- anti_join(shirtsDF, dirtyShirts)
  
  shirts <<- suppressMessages(anti_join(shirts, dirtyShirts))
  
  # socksDF <- as.data.frame(socks) %>% 
  #   rename('sockname' = 'socks')
  
  dirtySocks <- dirty %>% 
    filter(type == 'socks') %>% 
    select(item) %>% 
    rename('sockname' = 'item')
  
  socks <<- suppressMessages(anti_join(socks, dirtySocks))
  
  dirtyShorts <- dirty %>% 
    filter(type == 'shorts') %>% 
    select(item) %>% 
    rename('shortsname' = 'item')
  
  shorts <<- suppressMessages(anti_join(shorts, dirtyShorts))
  
  no3

}


inmycloset(mypants = #####
           c("light blue jeans", "dark blue jeans", "camo pants", 
             'calvin klein joggers', 'brixton chinos', 'rvca chinos', 
             'calvin klein chinos'), 
           myshirts = c("grey nike", "black oakley", "black brixton", 
                        "grey rvca", "white tnf", "pizza my heart", 
                        "stan jersey", "boca jersey", "melo jersey", 
                        "iverson jersey", "grey stan long sleeve", 
                        "red stan long sleeve", "the bike lane", 
                        "honduras jersey", "lingo sense", "warrior basketball", 
                        "byu stats", "steve jobs", 
                        "red, white, and black ss button-up", "hawaiian polo",
                        "blue striped ls button-up", 'green tenet polo', 
                        'light blue striped ls button-up'), 
           mysocks = c(rep("black nikes", 6), rep("white nikes", 6), 
                       "black sauconys", "cactus", "spongebob", "tiger", 
                       "gonzo", "beaker", "animal", "fozzy", "qr code", "hawks",
                       "sportotal"), 
           myshoes = c("am95s", "lebrons", "flyknits", "timbs", 
                       "alphabounces"), 
           myhat = c("staple", "rexel norcal valley", "pocket dhi-plus", 
                     "hbll"), 
           myhoodie = c("but at what cost", "grey zip-up", "navy fleece", 
                        "wesc plants", "kirkland signature"), 
           mylayer = c("columbia windbreaker", "stan windbreaker", 
                       "red flannel", "blue eb jacket", "yellow sf vest", 
                       "navy sf vest"), 
           myjacket = c("cowboy jacket", "grey gerry jacket", 
                        "brown 686 liner", "brown 686 shell + liner", 
                        "yellow sf jacket"), 
           myshorts = c("black o'neill", "grey volcom", "camo nba", 
                        "grey asics", "grey amazon")
           #####
)

ootd()
