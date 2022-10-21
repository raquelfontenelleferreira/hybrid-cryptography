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
    with open('03/keys/chPub.pem', 'rb') as p:
        chPub = rsa.PublicKey.load_pkcs1(p.read())
    with open('03/keys/chPriv.pem', 'rb') as p:
        chPriv = rsa.PrivateKey.load_pkcs1(p.read())
    return chPub, chPriv

#assinatura
def assinatura(mensagem, chave):
    return rsa.sign(mensagem.encode('ascii'), chave, 'SHA-1')

mensagem_Verdadeira = "Mensagem super secreta!"
mensagem_Falsa = "Mensagem não tão secreta" #para fins de teste

gerarChaves()
chPub, chPriv = carregarChaves()

with open("03/files/arquivo_texto.txt", "w") as arquivo_vazio:
    arquivo_vazio.write(".")

hashMensagem = assinatura(mensagem_Verdadeira, chPriv)

with open("03/files/arquivo_texto_assinado.txt", "wb") as caminho:
    caminho.write(hashMensagem)