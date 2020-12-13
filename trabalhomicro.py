# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def ascii_to_bin(b):
    binario = bin(b)[2:]
    binario = binario.rjust(8, '0')
    return binario
 
 
def run():
    parar = False;
    while not parar:
        opcao = input('''
Escolha uma opção:
    1 - criptografar
    2 - decriptografar
    3 - sair\n''')
        if opcao == '1':
            texto = input('digite o texto\n')
            texto_ascii = [ord(l) for l in texto]
            texto_binario = [ascii_to_bin(b) for b in texto_ascii]
            print(''.join(texto_binario))
        elif opcao == '2':
            texto = input('digite o texto\n')
            texto_binario = []
            for i in range(0, len(texto), 8):
                texto_binario.append(texto[i: i + 8])
            texto_ascii = [int(b, 2) for b in texto_binario]
            texto_decriptado = [chr(asc) for asc in texto_ascii]
            print(''.join(texto_decriptado))
        elif opcao == '3':
            break
        else:
            print('opção inválida')
            continue
 
 
if __name__ == '__main__':
    run()
    