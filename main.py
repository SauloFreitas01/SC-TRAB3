#!/usr/bin/python3
import time
import os
import base64
import secrets
from pathlib import Path
from colorama import Fore, Style

import RSA
import AES

print("-" * 50)
print('Trabalho 3  - Segurança Computacional')
print('Gerador/Verificador de Assinaturas')
print('Aluno: Saulo Freitas - 211000176')
print("-" * 50)


init_keys = input('INICIAR AS CHAVES? (S/N) ')

if init_keys == 'S':
    pass
elif init_keys == 'N':
    exit('Encerrando...')
else:
    exit('Input incorreto. Encerrando...')

# GERA AS CHAVES PÚBLICAS E PRIVADAS

public_key, private_key = RSA.spawn_keys()

n, e = public_key #nonce, encrypt_key
n, d = private_key #nonce, decrypt_key

print(f'CHAVE PÚBLICA:\nN: {Fore.RED}{str(n)[:10]}...\n{Style.RESET_ALL}E: {Fore.GREEN}{str(e)[:10]}... {Style.RESET_ALL}\n')
print(f'CHAVE PRIVADA:\nN: {Fore.RED}{str(n)[:10]}...\n{Style.RESET_ALL}D: {Fore.GREEN}{str(d)[:10]}... {Style.RESET_ALL} \n')


# CIFRA E ASSINA A MSG
   
key, iv = secrets.token_bytes(16), secrets.token_bytes(16)

session_key = key + iv
session_key_cipher = RSA.cypher(public_key, session_key)
session_key_cipher = base64.b64encode(session_key_cipher).decode("ascii")

arq = input(f'\n{Fore.BLUE}NOME DO ARQUIVO A SER CIFRADO:{Style.RESET_ALL} ')
file = Path(__file__).absolute().parent / arq
with open(file, "rb") as f:
    msg = f.read()
    ciphered_msg = AES.ctr(msg, key, iv)
       
with open(file, "wb") as f:
    f.write(ciphered_msg)

signature = RSA.sign(private_key, msg)
signature = base64.b64encode(signature).decode("ascii")

print(f'\n{Fore.YELLOW}MENSAGEM:{Style.RESET_ALL} {msg}\n')
print(f'\n{Fore.YELLOW}MENSAGEM CIFRADA:{Style.RESET_ALL}{ciphered_msg}\n')
print(f'\n{Fore.YELLOW}CHAVE DA SESSÃO:{Style.RESET_ALL}{session_key}\n')
print(f'\n{Fore.YELLOW}CHAVE DA SESSÃO CIFRADA:{Style.RESET_ALL}{session_key_cipher}\n')
print(f'\n{Fore.YELLOW}ASSINATURA:{Style.RESET_ALL}{signature}\n')


init_keys = input('Deseja decifrar? (S/N) ')

if init_keys == 'S':
    pass
elif init_keys == 'N':
    exit('Encerrando...')
else:
    exit('Input incorreto. Encerrando...')


# DECIFRA E VERIFICA ASSINATURA DA CIFRA
arq = input('\nNOME DO ARQUIVO A SER DECIFRADO: ')
file = Path(__file__).absolute().parent / arq
with open(file, "rb") as f:
    ciphered_msg = f.read()
       
signature = base64.b64decode(signature)
session_key_cipher = base64.b64decode(session_key_cipher)
        
session_key = RSA.decypher(private_key, session_key_cipher)
chave, iv = session_key[:16], session_key[16:]

msg = AES.ctr(ciphered_msg, chave, iv)
signature_ok = RSA.signature_check(public_key, msg, signature)

print("Verificando assinatura...\n")
time.sleep(3)
if signature_ok:
    print("\nAssinatura confere\n")
    print('MENSAGEM:\n')
    print(msg)
       
    with open(arq, "wb") as f:
            f.write(msg)
else:
        print("\nAssinatura não confere. Encerrando...\n")



