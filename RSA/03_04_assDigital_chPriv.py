#3 - Implemente um sistema que receba pela linha de comando o caminho de 2 arquivos: 
# uma chave privada e um arquivo de texto. Seu sistema deve gerar uma assinatura digital para o arquivo,
# tendo como resultado um novo arquivo assinado. Esse arquivo deve ser armazenado no mesmo diretório do arquivo original, 
# com nome terminando em "_assinado".
import rsa
import os

def gerarChaves():
    (chPub, chPriv) = rsa.newkeys(1024)
    with open('03/keys/chPub.pem', 'wb') as p:
        p.write(chPub.save_pkcs1('PEM'))
    with open('03/keys/chPriv.pem', 'wb') as p:
        p.write(chPriv.save_pkcs1('PEM'))

def carregarChaves():
    with open(caminhoChavePublica(), 'rb') as p:
        chPub = rsa.PublicKey.load_pkcs1(p.read())
    with open(caminhoChavePrivada(), 'rb') as p:
        chPriv = rsa.PrivateKey.load_pkcs1(p.read())
    return chPub, chPriv

def caminhoChavePublica():
    try:
        chave_publica = input("Insira o caminho da chave pública: ") #03/keys/chPub.pem
        return chave_publica
    except:
        print("Não foi possível encontrar o caminho da chave pública")

def caminhoChavePrivada():
    try: 
        chave_privada = input("Insira o caminho da chave privada: ") #03/keys/chPriv.pem
        return chave_privada
    except:
        print("Não foi possível encontrar o caminho da chave privada.")

def caminhoOriginal():
    try: 
        cam_original = input("Insira o caminho do arquivo original: ") #03/files/arquivo_texto.txt
        return cam_original
    except:
        print("Não foi possível encontrar o caminho do arquivo.")

def caminhoVerificado():
    try:
        cam_assinado = input("Insira o caminho do arquivo assinado a se verificar: ") #'03/files/arquivo_texto_assinado.txt'
        return cam_assinado
    except:
        print("Não foi possível encontrar o caminho do arquivo.")

gerarChaves()
chPub, chPriv = carregarChaves()

#03 questão

with open(caminhoOriginal(), 'rb') as msg: 
    assinatura = rsa.sign(msg, chPriv, 'SHA-1')

with open(caminhoVerificado(), 'wb') as arqAss:
    arqAss.write(assinatura)
    print("Arquivo assinado com sucesso!")
    arqAss.close()

#04 questão
try:
    with open(caminhoOriginal(), 'rb') as msg:
        rsa.verify(msg, assinatura, chPub)
    print("A assinatura é válida.")
except:
    print("Não foi possível verificar a assinatura.")