####Sudoku Geral####

quantLinhas <- readline(prompt = 'insira o número de linhas do sudoku: ')
quantLinhas <- as.numeric(quantLinhas)


####Construtor de matriz sudoku####

n <- 1
construcaoSudoku <- function(){
  matrizSudoku <- NA
  
  for(i in seq(1, quantLinhas)){
    linhaEntrada <- scan()
    matrizSudoku <- rbind(matrizSudoku, linhaEntrada)
    }
  }
  matrizSudoku <- matrizSudoku[-1,]
}

construtoSudoku <- construcaoSudoku() #a função gera o objeto construtoSudoku

####Verificador de NAs####

#o programa pega a matriz retornada pelo construtor e verifica a quantidade de 
#NAs que ela possui (NAs são os valores em branco do sudoku)

contadorNAs <- function(){
  n <- 0
  for(i in construtoSudoku){
    if(is.na(i)){
      n <- n + 1
      return(construtoSudoku)
    }
  }
  return(n)
}

n <- 1
a <- while(n >= 3){
  if(is.na(construtoSudoku[n,1:3])){
    return(n)
  }
  n <- n + 1
}
  
which(is.na(construtoSudoku)) #retorna os índices para os quais a condição é verdadeira


  
  
  
