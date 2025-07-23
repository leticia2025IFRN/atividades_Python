programa {
  funcao real tabuada(real n, inteiro i) {
    retorne n * i
  }
  funcao inicio() {
    // QUESTÃO 10
    real n
    inteiro i

    escreva ("\nDigite um número para saber a sua tabuada.\nN° = ")
    leia (n)

    para (inteiro i = 1; i <= 10; i++) {
      escreva ("■ ", n, "x", i, " = ", tabuada(n ,i), "\n")
    }
  }
}
