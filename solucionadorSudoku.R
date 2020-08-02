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

iNuc <- list(
  indiceNucleo1 <- c(1,2,3,10,11,12,19,20,21),
  indiceNucleo2 <- c(4,5,6,13,14,15,22,23,24),
  indiceNucleo3 <- c(7,8,9,16,17,18,25,26,27),
  indiceNucleo4 <- c(28,29,30,37,38,39,46,47,48),
  indiceNucleo5 <- c(31,32,33,40,41,42,49,50,51),
  indiceNucleo6 <- c(34,35,36,43,44,45,52,53,54),
  indiceNucleo7 <- c(55,56,57,64,65,66,73,74,75),
  indiceNucleo8 <- c(58,59,60,67,68,69,76,77,78),
  indiceNucleo9 <- c(61,62,63,70,71,72,79,80,81)
)

iLin <- list(
  indiceLinha1 <- c(1:9),
  indiceLinha2 <- c(10:18),
  indiceLinha3 <- c(19:27),
  indiceLinha4 <- c(28:36),
  indiceLinha5 <- c(37:45),
  indiceLinha6 <- c(46:54),
  indiceLinha7 <- c(55:63),
  indiceLinha8 <- c(64:72),
  indiceLinha9 <- c(73:81)
)


iCol <- list(
  indiceColuna1,
  indiceColuna2,
  indiceColuna3,
  indiceColuna4,
  indiceColuna5,
  indiceColuna6,
  indiceColuna7,
  indiceColuna8,
  indiceColuna9
)
indiceColuna1 <- c(1,10,19,28,37,46,55,64,73)
indiceColuna2 <- c(2,11,20,29,38,47,56,65,74)
indiceColuna3 <- c(3,12,21,30,39,48,57,66,75)
indiceColuna4 <- c(4,13,22,31,40,49,58,67,76)
indiceColuna5 <- NULL
indiceColuna6 <- NULL
indiceColuna7 <- NULL
indiceColuna8 <- NULL
indiceColuna9 <- NULL




for(i in indiceColuna4){
  indiceColuna5 <- append(indiceColuna5, i+1)
}
for(i in indiceColuna5){
  indiceColuna6 <- append(indiceColuna6, i+1)
}
for(i in indiceColuna6){
  indiceColuna7 <- append(indiceColuna7, i+1)
}
for(i in indiceColuna7){
  indiceColuna8 <- append(indiceColuna8, i+1)
}
for(i in indiceColuna8){
  indiceColuna9 <- append(indiceColuna9, i+1)
}



cg <- 1

funcaoCompletora <- function(){
 posicoes0[cg] <- 1
 return(construtoSudoku)
}


funcaoFiscal <- function(){
  
}

#ESTUDAR COMO PESQUISAR EM LISTAS
posicoes0[6]



#a função acima deve invocar o fiscal

#https://pt.stackoverflow.com/questions/463039/problemas-com-na-em-r



