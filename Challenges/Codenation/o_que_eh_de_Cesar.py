print("Importando libs e criando metodos... ", end="")
#imports
import requests
import json
import string
import hashlib

#minhas funcoes
def translate(x, n):
    x = x - n
    while(x > 122):
        x = x - 26
    while(x < 97):
        x = x + 26
    return x

def encr(char, num):
    x = ord(char)
    if(x >= 65 and x <= 90):
        return encr(char.toLower(), num)
    if(x >= 97 and x <= 122):
        return chr(translate(x, num))
    return char
print("Ok")
print("Realizando requisição... ", end="")

url_request = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=2447422f85d6d8dceea4439c347f3071eec5f5a8'
response = requests.get(url_request)

if (200 == response.status_code):
    print("Sucesso")
else:
    print("ERRO: " + response.text)
    
print("Decifrando texto... ", end="")
jsonString = response.text

quantidade = int(json_obj["numero_casas"])
lista_de_chars = [encr(x, quantidade) for x in json_obj["cifrado"]]
json_obj["decifrado"] = "".join(lista_de_chars)

print("pronto!")

print("Encriptando com SHA-1... ", end="")
hashe = hashlib.sha1()
hashe.update(json_obj["decifrado"].encode('utf-8'))
json_obj["resumo_criptografico"] = str(hashe.hexdigest())
print("pronto!!")

print("Salvando a J... ", end="")
jstr = json.dumps(json_obj)
File_object = open("answer.json","w") 
File_object.write(jstr)
File_object.close() 
print("pronto!!!")

print("Enviando essa Joça... ", end="")
url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=2447422f85d6d8dceea4439c347f3071eec5f5a8'
files = {'answer': ('answer.json', open('answer.json', 'rb'))}
resposta = requests.post(url, files=files)
print("pronto!!!\nSua nota de espião: " + resposta.text)