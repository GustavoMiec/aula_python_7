import re

def is_valid_email(email):

    pattern = r'^[a-zA-Z][a-zA-Z0-9._]*@[a-zA-Z]+\.[a-zA-Z]{2,3}$'
    if re.match(pattern, email):
        return True
    else:
        return False

while True:
    email = input("Digite o e-mail: ")
    if is_valid_email(email):
        break
    else:
        print("E-mail inválido, digite outro correto!")

numero_rm = input("Digite o número do RM: ")

nome_arquivo = f"RM{numero_rm}.txt"

with open(nome_arquivo, 'w') as arquivo:
    arquivo.write(email)

print("Gravado com sucesso!")
