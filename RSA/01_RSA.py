import rsa

#cria as chaves
def gerarChaves():
    (chPub, chPriv) = rsa.newkeys(1024)
    with open('keys/chPub.pem', 'wb') as p:
        p.write(chPub.save_pkcs1('PEM'))
    with open('keys/chPriv.pem', 'wb') as p:
        p.write(chPriv.save_pkcs1('PEM'))
    
#carrega as chaves
def carregarChaves():
    with open('keys/chPub.pem', 'rb') as p:
        chPub = rsa.PublicKey.load_pkcs1(p.read())
    with open('keys/chPriv.pem', 'rb') as p:
        chPriv = rsa.PrivateKey.load_pkcs1(p.read())
    return chPub, chPriv

#cifrar a mensagem
def cifrar(mensagem, chave):
    return rsa.encrypt(mensagem.encode('ascii'), chave)

#decrifrar a mensagem
def decifrar(mensagemCifrada, chave):
    try:
        return rsa.decrypt(mensagemCifrada, chave).decode('ascii')
    except:
        return False

#assinatura
def assinatura(mensagem, chave):
    return rsa.sign(mensagem.encode('ascii'), chave, 'SHA-1')

#verificar se a mensagem é autêntica
def verificar(mensagem, assinatura, chave):
    try: 
        return rsa.verify(mensagem.encode('ascii'), assinatura, chave) =='SHA-1'
    except:
        return False


#gerar chaves
gerarChaves()
chPubA, chPrivA = carregarChaves()

#mensagem e cifra usando a chave pública
mensagem = 'Mensagem super secreta!'
textoCifrado = cifrar(mensagem, chPubA)

#gerando assinatura
assinaturaA = assinatura(mensagem, chPrivA)

texto = decifrar(textoCifrado, chPrivA)

print(f'Texto Cifrado: {textoCifrado}')
print(f'Assinatura: {assinaturaA}')

if texto:
    print(f'Mensagem: {texto}')
else:
    print(f'Não foi possível decifrar a mensagem.')

if verificar(texto, assinaturaA, chPrivA):
    print('Assinatura verificada com sucesso.')
else:
    print('Não foi possível verificar a assinatura.')

