# Módulos
import random

# Variáveis
cpf = ''; cpfFormatado = ''

# Código
numAleatorio = random.randrange(0, 10)
numAleatorio = str(numAleatorio)
cpf = cpf + numAleatorio
numAleatorio = random.randrange(0, 10)
numAleatorio = str(numAleatorio)
cpf = cpf + numAleatorio
numAleatorio = random.randrange(0, 10)
numAleatorio = str(numAleatorio)
cpf = cpf + numAleatorio
cpf = cpf + '.'
numAleatorio = random.randrange(0, 10)
numAleatorio = str(numAleatorio)
cpf = cpf + numAleatorio
numAleatorio = random.randrange(0, 10)
numAleatorio = str(numAleatorio)
cpf = cpf + numAleatorio
numAleatorio = random.randrange(0, 10)
numAleatorio = str(numAleatorio)
cpf = cpf + numAleatorio
cpf = cpf + '.'
numAleatorio = random.randrange(0, 10)
numAleatorio = str(numAleatorio)
cpf = cpf + numAleatorio
numAleatorio = random.randrange(0, 10)
numAleatorio = str(numAleatorio)
cpf = cpf + numAleatorio
numAleatorio = random.randrange(0, 10)
numAleatorio = str(numAleatorio)
cpf = cpf + numAleatorio
cpf = cpf + '-'
numAleatorio = random.randrange(0, 10)
numAleatorio = str(numAleatorio)
cpf = cpf + numAleatorio
numAleatorio = random.randrange(0, 10)
numAleatorio = str(numAleatorio)
cpf = cpf + numAleatorio
cpfFormatado = 'O CPF gerado foi {}'
cpfFormatado = cpfFormatado.format(cpf)
print(cpfFormatado)