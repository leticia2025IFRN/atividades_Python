programa {
  funcao inicio() {
    real raio, area
    real PI = 3.14

    escreva ("\nSeja bem-vindo à aplicação.\n")

    escreva ("\nPara saber a área de um cículo, digite um raio para começar a aplicação.\nRAIO: ")
    leia (raio)
    area = PI * (raio * raio)

    se (raio > 0)
      escreva ("\nA área do cículo com raio de "+ raio +" unidades é "+ area +" unidades ao quadrado.")
    senao
      escreva ("Ops! Para formar a área da figura, é necessário que a medida do raio seja maior que 0 (zero).")
  }
}
