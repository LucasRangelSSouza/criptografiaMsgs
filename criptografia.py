'''
Ete modulo é responsavel por realizar a criptografia
Alem da mensagem a ser criptografada/descriptografada é necessario inserir uma chave de segurança,

A criptografia é realizada de string para binario com base na tabela ASCII
apos gerado o binario da mensagem, a chave de segurança é submetida ao algoritmo SHA256
que é uma especie de algoritmo digestivo.
O algoritmo digestivo gera um hash unico de 256 bits para a chave de segurança, a chave de segurança nao é contida neste hash
de forma que é impossivel descriptografar a chave de segurança.

Em posse da mensagem em binario e do hash da chave de segurança, o hash tambem é convertido em binario, o binario do hash e da mensagem 
é embaralhado randomicamente, de forma que ao tentar traduzir o binario da mensagem em algum tradutor qualquer se obtem uma mensagem
completamente ilegivel
Por exemplo:
Ao criptogafar a mensagem: "Navios a 4km da costa"
Utilizando a chave: "lagos verdes"
É gerado o seguinte binario criptografado:

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

Ao tentar decodificar em um tradutor binario comum o seguinte texto é obtido:

e9f85953a1d655f482726e9527d39e01Ne9f85953a27d39e01ve9f85953ia45a1e1ao20fb1f31
sa1d655f4 82726e95a20fb1f31 e9f859534a0893b8bk82726e95m82726e95 20fb1f31d8272
6e95ac155f4aa 82726e95ca1d655f4o82726e95s20fb1f31te9f85953aa45a1e1a20fb1f31c1
55f4aaa0893b8b

Algo que continua sem sentido e mantem a mensagem segura e secreta

Outra coisa que dificulta a quebra da mensagem, é o fato que logo apos o binario ser gerado
toda a string é concatenada, sendo impossivel decodificar com exatidao algum texto minimamente util
sem antes saber com quantos bits cada palavra foi codificada

No momento da descriptografia a string binaria é quebrada em tuplas de 8bits, e é convertido para texto todo o binario
no entando o texto ainda continua embaralhado com o hash, como é impossivel decriptografar o hash criptografado em sha256
é necessario que o usuario insira a chave de segurança no qual serviu de base para criptografar a mensagem

desa forma a chave é novamente convertida em sha256, e o hash gereado é usado para desembaralhar o corpo do hash do corpo
da mensagem, separando assim a mensagem do hash e exibindo a mensagem ao usurio



'''
import sha256
import random

asciiChars = [' ', '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{',
              '|', '}', '~','á','é','í','ó','ú','Á','É','Í','Ó','Ú','à','è','ì','ò','ù','À','È','Ì','Ò','Ù','â','ê','î','ô','û','ã','õ','ñ']


def decToBin(n):
    ''''''
    binario = ""
    while(True):
        binario = binario + str(n % 2)
        n = n//2
        if n == 0:
            break
    binario = binario[::-1]
    binario = str(binario).zfill(8)
    return binario


def binToDec(n):
    decimal = 0
    n = str(n)
    n = n[::-1]
    tam = len(n)
    for i in range(tam):
        if n[i] == "1":
            decimal = decimal + 2**i
    return decimal


def strToBin(texto):
    cryptMsg = []
    for charOfMsg in texto:
        for index in range(len(asciiChars)):
            if(charOfMsg == asciiChars[index]):
                cryptMsg.append(decToBin(index+32))
                break
    return cryptMsg


def binToStr(binaryArray):
    decryptedMsg = ''

    for binary in binaryArray:
        decryptedMsg += asciiChars[int(binToDec(binary))-32]
    return decryptedMsg


def crypt(mensagem, key):
    cryptedKey = sha256.digest(key)
    binMsg = strToBin(mensagem)
    binCryptedKey = []
    for partOfKey in cryptedKey:
        binCryptedKey.append(strToBin(partOfKey))
    indiceCalculado = 1
    for i in range(len(binMsg)-1):
        binMsg[indiceCalculado:indiceCalculado] = binCryptedKey[random.randrange(0, 8)]
        indiceCalculado += 9
    binCryptedKeyA = [binCryptedKey[0], binCryptedKey[1], binCryptedKey[2], binCryptedKey[3]]
    binCryptedKeyB = [binCryptedKey[4],binCryptedKey[5],binCryptedKey[6],binCryptedKey[7]]
    
    binMsg[0:0] = binCryptedKeyA
    binMsg.append(binCryptedKeyB)
    cryptedMsg= str(binMsg).replace('[', '').replace(']', '').replace(' ','').replace("','",'').replace("'",'')
    return cryptedMsg


def decrypt(mensagem, key):
    msgList= eval(splitBin(mensagem))
    decryptedMsg = binToStr(msgList)
    keyDigested = sha256.digest(key)
    sha256Str = str(keyDigested).replace("', '", '').replace("('", '').replace("')", '')
    
    tamanhoA =len(keyDigested[0]+keyDigested[1]+keyDigested[2]+keyDigested[3])
    tamanhoB =len(keyDigested[4]+keyDigested[5]+keyDigested[6]+keyDigested[7])
    extractedKey= ''
    extractedKey+=decryptedMsg[0:tamanhoA]
    extractedKey+=((decryptedMsg[::-1])[0:tamanhoB])[::-1] 
    
    if(sha256Str==extractedKey):
        
        for partOfKey in keyDigested:
            decryptedMsg = decryptedMsg.replace(partOfKey,'')
        return(decryptedMsg)
    else:
        return('Chave invalida')

def splitBin(textoBinario):
    binStr=textoBinario.replace("\n", '')
    splitedStr = "['"
    controlVar =0
    for char in binStr:
        if(controlVar==8):
            splitedStr+="','"+char
            controlVar =1
        else:
            splitedStr+=char
            controlVar+=1
    splitedStr+="']"
    return splitedStr
     
# mensagem= input('Mensagem: ')
# key= input('Chave de segurança: ')

# mensagemCriptografada = crypt(mensagem,key)
# print('Mensagem Criptografada: ',mensagemCriptografada)

# mensagemDescriptografada = decrypt(mensagemCriptografada, key)
# print('Mensagem descriptografada: ',mensagemDescriptografada)
