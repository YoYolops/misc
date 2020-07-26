####Pacotes Usados####
library(stringr)



####Sudoku Geral####

quantLinhas <- readline(prompt = 'insira o número de linhas do sudoku: ')
quantLinhas <- as.numeric(quantLinhas)

posicoesNA <- which(is.na(construtoSudoku)) #retorna os índices para os quais a 
                              #condição é verdadeira e salva 
quantNA <- length(posicoesNA)

quantTeste <- 10^81


####Construtor de matriz sudoku####

n <- 1
construcaoSudoku <- function(){
  matrizSudoku <- NA
  
  for(i in seq(1, quantLinhas)){
    linhaEntrada <- scan()
    matrizSudoku <- rbind(matrizSudoku, linhaEntrada)
  }
  matrizSudoku <- matrizSudoku[-1,]
}

construtoSudoku <- construcaoSudoku() #a função gera o objeto construtoSudoku

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


for(i in seq(1, length(construtoSudoku))){
  if(construtoSudoku[i] == 0){ #as posições em brancos são representadas por 0
    construtoSudoku[i] <- construtoSudoku[i] + 1
  }
}


  

  
  
  
