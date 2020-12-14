
[![N|Solid](https://eventos.ifg.edu.br/semanai2c/wp-content/uploads/sites/7/2016/08/marca-ifg-2015-todas-as-verses.png)](https://www.ifg.edu.br/goiania)

# Shannon (Criptografia de mensagens)

Shannon é um algoritmo de criptografia militar desenvolvido pos discentes do IFG, e leva consigo este nome em homenagem a Claude Shannon, considerado o pai da criptografia moderna.
#### Caracteristicas do Shannon:

  - Conversão de strings para binario por meio de um modelo baseado em ASCII
  - Chave de segurança criptografada em SHA256, sendo este um algoritmo disgestivo, é impossivel descriptografar a mensagem sem que tenha em posse a chave de segurança.
  - Embaralhamento aleatorio da mensagem criptografada (mesmo que consiga converter o binario a mensagem ainda será ilegivel)
  - Texto final da mensagem em binario (podendo facilmente ser transmitida por diversos meios de comunicação por mais legados e simplorios que sejam, já que se trata de um sistema de base 2) 

#### Tecnologias empregadas:

  - Python 3
  - Tkinter (Lib para randerizaçao de interfaces graficas em Python)
  - SHA256 Para digestão da chave de segurança
  - Tabela ASCII


#### Instalação:

Shannon requer python [python](https://www.python.org/) versão 3 ou superior para rodar

##### Windows:

  - Baixe e instale o execultavel do [python3](https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe) ou superior
  
  ![](https://python.robasworld.com/wp-content/uploads/2017/09/pythonInstallationDir.gif)

##### Linux:
 Para ver a versão do python3 instalada no seu sistema, abra o terminal e execulte:
```sh
$ python3 --version
```
Se você estiver usando o Ubuntu 16.10 ou mais recente, poderá instalar facilmente o Python 3.6 com os seguintes comandos:
```sh
$ sudo apt-get update
$ sudo apt-get install python3.6
```
Se você estiver usando outra versão do Ubuntu (por exemplo, a versão mais recente do LTS) ou quiser usar um Python mais atual, recomendamos o uso do Deadsnakes PPA para instalar o Python 3.8:

```sh
$ sudo apt-get install software-properties-common
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get update
$ sudo apt-get install python3.8
```

Se você estiver usando outra distribuição Linux, é provável que já tenha o Python 3 pré-instalado também. Caso contrário, use o gerenciador de pacotes da sua distribuição. Por exemplo, no Fedora, você usaria dnf:

```sh
$ sudo dnf install python3
```
##### Clonando o repositorio:
Para clonar o diretorio execute no terminal ou no prompt:
(É necessario ter um cliente [git](https://git-scm.com/) instalado )
```sh
$ git clone https://github.com/LucasRangelSSouza/criptografiaMsgs.git
```
#### Execultando o Shannon:

##### Windows
  - Clique duas vezes sobre o arquivo Shannon.pyw e aguarde a interface grafica iniciar
 
##### Linux
- Abra o termina no diretorio do arquivo e execute no terminal:
```sh
$ python Shannon.pyw
```

### Utilizando o Shannon:

Apos iniciar o Shanonn e a interface grafica iniciada basta inserir o texto desejado em uma das areas, digitar a chave e clicar na ação desejada.

##### Criptografando
- Execute o Shannon
- Digite a chave de criptografia no campo CHAVE
- Digite a mensagem a qual deseja criptografar no campo MENSAGEM DESCRIPTOGRAFADA
- Clique no botão CRIPTOGRAFAR
- A mensagem criptografada sera exibida no campo MENSAGEM CRIPTOGRAFADA
- Basta copiar a mensagem e transmiti-la

 ![](/gifs/howCrypt.gif)
##### Descriptografando
- Execute o Shannon
- Digite a chave de criptografia no campo CHAVE
- Digite a mensagem a qual deseja descriptografar no campo MENSAGEM CRIPTOGRAFADA
- Clique no botão DESCRIPTOGRAFAR
- A mensagem decriptografada sera exibida no campo MENSAGEM DESCRIPTOGRAFADA (se a chave informada for correta)

 ![](/gifs/howDecrypt.gif)

### Como o Shannon trabalha:
A criptografia é realizada de string para binario com base na tabela ASCII pos gerado o binario da mensagem, a chave de segurança é submetida ao algoritmo SHA256 que é uma especie de algoritmo digestivo.
O algoritmo digestivo gera um hash unico de 256 bits para a chave de segurança, a chave de segurança nao é contida neste hash de forma que é impossivel descriptografar a chave de segurança.
Em posse da mensagem em binario e do hash da chave de segurança, o hash tambem é convertido em binario, o binario do hash e da mensagem é embaralhado randomicamente, de forma que ao tentar traduzir o binario da mensagem em algum tradutor qualquer se obtem uma mensagem completamente ilegivel

**Por exemplo:**
Ao criptogafar a mensagem: ```Navios a 4km da costa```
Utilizando a chave: ```lagos verdes```
É gerado o seguinte binario criptografado:
```
01100101001110010110011000111000001101010011100100110101001100110110000100110001011001000011011000
11010100110101011001100011010000111000001100100011011100110010001101100110010100111001001101010011
00100011011101100100001100110011100101100101001100000011000101001110011001010011100101100110001110
00001101010011100100110101001100110110000100110010001101110110010000110011001110010110010100110000
00110001011101100110010100111001011001100011100000110101001110010011010100110011011010010110000100
11010000110101011000010011000101100101001100010110000101101111001100100011000001100110011000100011
00010110011000110011001100010111001101100001001100010110010000110110001101010011010101100110001101
00001000000011100000110010001101110011001000110110011001010011100100110101011000010011001000110000
01100110011000100011000101100110001100110011000100100000011001010011100101100110001110000011010100
11100100110101001100110011010001100001001100000011100000111001001100110110001000111000011000100110
10110011100000110010001101110011001000110110011001010011100100110101011011010011100000110010001101
11001100100011011001100101001110010011010100100000001100100011000001100110011000100011000101100110
00110011001100010110010000111000001100100011011100110010001101100110010100111001001101010110000101
10001100110001001101010011010101100110001101000110000101100001001000000011100000110010001101110011
00100011011001100101001110010011010101100011011000010011000101100100001101100011010100110101011001
10001101000110111100111000001100100011011100110010001101100110010100111001001101010111001100110010
00110000011001100110001000110001011001100011001100110001011101000110010100111001011001100011100000
11010100111001001101010011001101100001011000010011010000110101011000010011000101100101001100010110
00010011001000110000011001100110001000110001011001100011001100110001011000110011000100110101001101
01011001100011010001100001011000010110000100110000001110000011100100110011011000100011100001100010
```
Ao tentar decodificar em um tradutor binario comum o seguinte texto é obtido:
```
e9f85953a1d655f482726e9527d39e01Ne9f85953a27d39e01ve9f85953ia45a1e1ao20fb1f31
sa1d655f4 82726e95a20fb1f31 e9f859534a0893b8bk82726e95m82726e95 20fb1f31d8272
6e95ac155f4aa 82726e95ca1d655f4o82726e95s20fb1f31te9f85953aa45a1e1a20fb1f31c1
55f4aaa0893b8b
```
Algo que continua sem sentido e mantem a mensagem segura e secreta

Outra coisa que dificulta a quebra da mensagem, é o fato que logo apos o binario ser gerado toda a string é concatenada, sendo impossivel decodificar com exatidao algum texto minimamente util sem antes saber com quantos bits cada palavra foi codificada

No momento da descriptografia a string binaria é quebrada em tuplas de 8bits, e é convertido para texto todo o binario no entando o texto ainda continua embaralhado com o hash, como é impossivel decriptografar o hash criptografado em sha256 é necessario que o usuario insira a chave de segurança no qual serviu de base para criptografar a mensagem desta forma a chave é novamente convertida em sha256, e o hash gereado é usado para desembaralhar o corpo do hash do corpo da mensagem, separando assim a mensagem do hash e exibindo a mensagem ao usurio


### Licença:


MIT
**Free Software, Hell Yeah!**
