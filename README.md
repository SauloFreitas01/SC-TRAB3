# CIC0201 - Segurança Computacional - Turma 01

### Saulo Oliveira de Freitas - 211000176

## Gerador/Verificador de Assinaturas

### 1. Introdução

O processo de  assinatura é um método de autenticação de documentos e mensagens. Ele permite que o signatário prove que é a pessoa que criou o documento ou que valida seu conteúdo, e que o documento ou mensagem não foi alterado desde que foi assinado.Com o a digitalização da informação, tornou-se necessário criar um recurso que exerça as mesmas funções da assinatura analógica, isto é uma validação de identidade única, rastreável e de difícil falsificação. Baseado na dificuldade de fatorar números primos grandes, o algoritmo RSA é um dos algoritmos de assinatura digital mais usados para este fim. Este relatório descreve a implementação de um gerador e verificador de assinaturas RSA em arquivos.


### 1.1 Objetivos
Este relatório descreve a implementação de um gerador e verificador de assinaturas RSA em arquivos. O programa implementa as seguintes funcionalidades:

- Geração de chaves RSA

- Cifração e decifração assimétrica RSA

- Cálculo de hashes da mensagem em claro

- Assinatura da mensagem

- Verificação da assinatura

### 2. Metodologia

A linguagem adotada para este projeto foi Python, devido a sua simplicidade de uso e sintaxe familiar. Além do RSA e OAEP, foi também desenvolvido uma implementação dos algoritmo de Advanced Encryption Standard (AES) para viabilizar o processo de criptografia.

#### OAEP.py
A função do OAEP é prover o preenchimento e formatação dos dados que serão utilizado pelo algoritmo de RSA, garantindo maior segurança ao resultado final do processo de cifragem. Pontos principais de sua implementação são:

- A mensagem é preenchida com valores randômicos para aumentar seu tamanho e entropia

- A mensagem então é cifrada utilizando a chave pública, obtida através do RSA.

- Para a decifragem, a chave privada é utilizada, realizando o processo de cifragem no sentido inverso.

- Os preenchimentos são extraidos e a mensagem original é recuperada.

#### RSA.py
O RSA é um algoritmo de cifragem assimétrico amplamente utilizado para a transmissão segura de dados. Sua implementação envolve o uso de números primos para geração de um par de chaves público-privada. Sua implementação pode ser dividida em:

- Gere um par de chaves público-privada utilizando a função `spawn_keys()` e as extraia

- Converta a mensagem em formato textual para uma representação numérica.

- Cifre o resultado utilizando a chave pública e a função `cypher(key, msg)`

- Decifre utilizando a chave privada e a função `decypher(key,ciphered_text)`

- Converta a representação numérica resultante para seu formato original


#### AES.py
A AES será implementada no tamanho de 128 bits para bloco e chave. Um processo de implementação convencional geralmente envolve os seguintes passos:

- Geração de chave no tamanho desejado através da função `expand_key(key)`

- Geração do vetor de inicialização

- Aplicar os paddings e conversões necessárias

- Cifrar e/ou decifrar utilizando a função `cipher(block, keys)`



### 3. Resultados

![](https://raw.githubusercontent.com/SauloFreitas01/SC-TRAB3/main/imgs/1.png)




![Geração de chaves](https://raw.githubusercontent.com/SauloFreitas01/SC-TRAB3/main/imgs/2.png)


![Cifragem do arquivo](https://raw.githubusercontent.com/SauloFreitas01/SC-TRAB3/main/imgs/3.png)


![Produtos do processo de cifragem ](https://raw.githubusercontent.com/SauloFreitas01/SC-TRAB3/main/imgs/2.png)




![Decifragem do arquivo](https://raw.githubusercontent.com/SauloFreitas01/SC-TRAB3/main/imgs/4.PNG)


