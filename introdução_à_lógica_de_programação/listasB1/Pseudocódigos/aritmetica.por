programa {
  //inclua biblioteca Matematica-->mat

  funcao inicio() {
    real nota1, nota2, nota3, media

    escreva ("\nSeja bem-vindo à aplicação de média aritmética.\n")

    escreva ("\nDigite três notas para calcular sua média.\n1° NOTA: ")
    leia (nota1)
    escreva ("2° NOTA: ")
    leia (nota2)
    escreva ("3° NOTA: ")
    leia (nota3)
    media = (nota1 + nota2 + nota3)/3

    se (nota1 < 0 ou nota1 > 10)
      escreva ("\nTemos um problema! Para se ter resultado, é necessário que sua primeira nota esteja entre 0 (zero) e 10 (dez).")
    senao se (nota2 < 0 ou nota2 > 10)
      escreva ("\nTemos um problema! Para se ter resultado, é necessário que sua segunda nota esteja entre 0 (zero) e 10 (dez).")
    senao se (nota3 < 0 ou nota3 > 10)
      escreva ("\nTemos um problema! Para se ter resultado, é necessário que sua terceira nota esteja entre 0 (zero) e 10 (dez).")
    senao
      escreva ("\nSua média com a soma das notas "+ nota1 +", "+ nota2 +" e "+ nota3 +", dividida por 3, é "+ media +".")
    //  escreva ("\nSua média com a soma das notas "+ nota1 +", "+ nota2 +" e "+ nota3 +", dividida por 3, é "+ mat.arredondar(media, 2) +".")
  }
}
