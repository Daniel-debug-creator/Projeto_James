# **Interface de Codificação e Decodificação de textos por Criptografia**

Referências de decodificação por Frequência de Letras:

- [Exemplo](http://numaboa.com.br/criptografia/criptoanalise/1051-exemplo)
- [Frequência de Letras em Espanhol](http://numaboa.com.br/criptografia/criptoanalise/1049-freq-espanhol)
- [Letter Frequency](https://en.wikipedia.org/wiki/Letter_frequency)
- [Frecuencia de aparición de letras](https://es.wikipedia.org/wiki/Frecuencia_de_aparici%C3%B3n_de_letras)
- [Frequência de letras](https://pt.wikipedia.org/wiki/Frequ%C3%AAncia_de_letras)

Referências de codificação por cifra de César:

- [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher)

Referências de codificação por Morse:

- [Morse code](https://en.wikipedia.org/wiki/Morse_code)

Referências de codificação por Morse:

- [Enigm Machine](https://www.youtube.com/watch?v=2D2bJWHvqJo)

O objetivo do código é montar uma interface e fazer capítulos com seções sobre **decodificação e codificação**. Como decodificação, a principal será utilizar estudos estatísticos sobre **frequência de letras**. Neste caso, a decodificação pode não sair perfeita, então deve-se fazer pequenas modificações, manuais e/ou automáticas por código. Na parte de codificação, terá seções sobre codificação e decodificação (vice-versa) com as criptografias de **Cifra de César**, **associação caracter por caracter** **Máquina Enigma (Alan Turing)**. Como o objetivo da parte de decodificação é analisar por frequência de letras, iremos apenas considerar a parte textual das strings, deixando a parte numérica inalterada. A inserção de caracteres para fazermos o processamento por string será por input e no decorrer da interface, haverá instruções escritas em markdown de como utilizar este sistema.

**OBS: Até a data final do projeto, podem haver criptografias a serem inseridas ou retiradas. Além disso, pequenas alterações estruturais do projeto como interface e dinâmica entre as criptografias pode mudar, não saindo do escopo principal do projeto**

O que foi feito até agora:

- Função de precessamento de texto, transformando os textos em minúsculo, sem sinais, números e caracteres especiais (**formata**)
- Função para Cripitografia de César (**cesar**)
- Função para identificação da frequência de caracteres no texto(**conta**)
