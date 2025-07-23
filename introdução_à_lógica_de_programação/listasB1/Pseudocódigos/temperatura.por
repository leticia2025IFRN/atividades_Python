programa {
  funcao inicio() {
    real temperatura, fahrenheit

    escreva ("\nSeja bem-vindo ao conversor de temperatura.\n")

    escreva ("\nDigite uma temperatura em graus Celsius (°C) para começar a aplicação e convertê-la para Fahrenheit (°F).\nTEMPERATURA: ")
    leia (temperatura)
    fahrenheit = ((9/5) * temperatura) + 32

    escreva ("\nA conversão de "+ temperatura +"°C para Fahrenheit é "+ fahrenheit +"°F.")
  }
}
