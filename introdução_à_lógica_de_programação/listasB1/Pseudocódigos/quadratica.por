programa {
  //inclua biblioteca Matematica -->  mat
  
  funcao real y(real a, real b, real c, real x) {
    retorne (a * (x * x)) + (b * x) + c
  }
  
  funcao inicio() {
    // QUESTÃO 08
    real a, b, c, x

    escreva ("\nSeja bem-vindo à aplicação de Equação de Segundo Grau.\n")

    escreva ("\nDigite quatro valores (a, b, c e x) para montar uma equação quadrática e você receberá a resolução (y) em poucos instantes.\n a = ")
    leia (a)
    escreva (" b = ")
    leia (b)
    escreva (" c = ")
    leia (c)
    escreva (" x = ")
    leia (x)

    escreva ("O resultado da equação montada é "+ y(a, b, c, x) +".")
    //y = (a * (x * x)) + (b * x) + c
    //y = (a * mat.potencia(x, 2)) + (b * x) + c
    //escreva("O resultado da equação montada é "+ y +".")
  }
}
