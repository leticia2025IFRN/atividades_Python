programa {
  funcao inicio() {
    real base, altura, area

    escreva ("\nSeja bem-vindo à aplicação.\n")

    escreva ("\nPara saber a área de um triângulo, digite o valor da base e da altura para começar a aplicação.\nBASE: ")
    leia (base)
    escreva ("ALTURA: ")
    leia (altura)
    area = (base * altura)/2

    se (base > 0 e altura > 0)
      escreva ("\nA área do triângulo que possui "+ base +" unidades de base e "+ altura +" unidades de altura é "+ area +" unidades ao quadrado.")
    senao se (base <= 0)
      escreva ("\nOps! Para formar a área da figura, é necessário que a base seja maior que 0 (zero).")
    senao
      escreva ("\nOps! Para formar a área da figura, é necessário que a altura seja maior que 0 (zero).")
  }
}
