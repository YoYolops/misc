####Pacotes Usados####
library(stringr)


backup <- construtoSudoku
####Sudoku Geral####
jaRodou <- FALSE

quantLinhas <- readline(prompt = 'insira o número de linhas do sudoku: ')
quantLinhas <- as.numeric(quantLinhas)

posicoes0 <- which(construtoSudoku == 0) #retorna os índices para os quais a 
                              #condição é verdadeira e salva 
quant0 <- length(posicoes0)

quantTeste <- 10^81

####Construtor de matriz sudoku####

construcaoSudoku <- function(n) t(replicate(n, scan()))

construtoSudoku <- construcaoSudoku(9) #a função gera o objeto construtoSudoku

####Verificador de núcleos####

#indices dos núcleos:

#  1  2  3     4  5  6     7  8  9
# 10 11 12    13 14 15    16 17 18
# 19 20 21    22 23 24    25 26 27
# 
# 28 29 30    31 32 33    34 35 36
# 37 38 39    40 41 42    43 44 45
# 46 47 48    49 50 51    52 53 54
# 
# 55 56 57    58 59 60    61 62 63
# 64 65 66    67 68 69    70 71 72
# 73 74 75    76 77 78    79 80 81

indiceNucleo1 <- c(1,2,3,10,11,12,19,20,21)
indiceNucleo2 <- c(4,5,6,13,14,15,22,23,24)
indiceNucleo3 <- c(7,8,9,16,17,18,25,26,27)
indiceNucleo4 <- c(28,29,30,37,38,39,46,47,48)
indiceNucleo5 <- c(31,32,33,40,41,42,49,50,51)
indiceNucleo6 <- c(34,35,36,43,44,45,52,53,54)
indiceNucleo7 <- c(55,56,57,64,65,66,73,74,75)
indiceNucleo8 <- c(58,59,60,67,68,69,76,77,78)
indiceNucleo9 <- c(61,62,63,70,71,72,79,80,81)

valorNucleo1 <- NULL
valorNucleo2 <- NULL
valorNucleo3 <- NULL
valorNucleo4 <- NULL
valorNucleo5 <- NULL
valorNucleo6 <- NULL
valorNucleo7 <- NULL
valorNucleo8 <- NULL
valorNucleo9 <- NULL


valorNucleo1
valorNucleo2
valorNucleo3
valorNucleo4
valorNucleo5
valorNucleo6
valorNucleo7
valorNucleo8
valorNucleo9


for(i in indiceNucleo1){
  valorNucleo1 <- c(valorNucleo1, construtoSudoku[i])
}
for(i in indiceNucleo2){
  valorNucleo2 <- c(valorNucleo2, construtoSudoku[i])
}
for(i in indiceNucleo3){
  valorNucleo3 <- c(valorNucleo3, construtoSudoku[i])
}
for(i in indiceNucleo4){
  valorNucleo4 <- c(valorNucleo4, construtoSudoku[i])
}
for(i in indiceNucleo5){
  valorNucleo5 <- c(valorNucleo5, construtoSudoku[i])
}
for(i in indiceNucleo6){
  valorNucleo6 <- c(valorNucleo6, construtoSudoku[i])
}
for(i in indiceNucleo7){
  valorNucleo7 <- c(valorNucleo7, construtoSudoku[i])
}
for(i in indiceNucleo8){
  valorNucleo8 <- c(valorNucleo8, construtoSudoku[i])
}
for(i in indiceNucleo9){
  valorNucleo9 <- c(valorNucleo9, construtoSudoku[i])
}








jaRodou <- FALSE
funcaoCompletora <- function(){
  c <- 1 #contador que passeia pela stringTeste
  n <- 1 #contador para gerar o teste inicial com 1
  casoTeste <- 0
  quantTeste <- 10^quant0
  
  for(i in posicoes0){ #loop que adiciona o primeiro teste
    construtoSudoku[i] <- algarismoCasoTeste[c]
    c <- c + 1
  }
  jaRodou <- TRUE
  return(construtoSudoku)
}










rm(dale)



#a função acima deve invocar o fiscal

#https://pt.stackoverflow.com/questions/463039/problemas-com-na-em-r






