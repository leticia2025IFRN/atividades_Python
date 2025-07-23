programa {
  funcao inicio() {
    real input_segundos, hora, minutos, segundos

    escreva("\nSeja bem-vindo ao conversor de tempo.\nDigite um número em segundos para aparecer no formato 'HORA:MINUTO:SEGUNDO'.\nSEGUNDOS: ")
    
    leia(input_segundos)
    
    se (input_segundos < 0)
    {
      escreva("Temos um problema! Não estamos considerando princípios e teorias da física para aceitar o valor de tempo negativo, além de que o resultado apresente-se totalmente diferente do valor esperado.\nPor favor, digite o valor novamente.")
    }
    senao
    {
      hora = input_segundos / 3600
      minutos = (input_segundos % 3600) / 60
      segundos = (input_segundos % 3600) % 60

      escreva("O tempo, "+input_segundos+" segundos, corresponde a "+hora+":"+minutos+":"+segundos)
    }
  }
}
