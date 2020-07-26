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

# 1  2  3     4  5  6     7  8  9
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






  

  
  
  
