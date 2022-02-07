import json
import re

file = open("read.txt")

operators = {'=': 'Assignment op', '+': 'Addition op', '-': 'Subtraction op', '/': 'Division op',
             '*': 'Multiplication op', '<': 'Lessthan op', '>': 'Greaterthan op'}
operators_key = operators.keys()

data_type = {'ent': 'integer type', 'flot': 'Floating point', 'car': 'Character type', 'grande': 'long int'}
data_type_key = data_type.keys()

punctuation_symbol = {':': 'colon', ';': 'semi-colon', '.': 'dot', ',': 'comma',
                      '(': 'Open round bracket', ')': 'Close round bracket',
                      '[': 'Open square bracket', ']': 'Close square bracket',
                      '{': 'Open curly bracket', '}': 'Close curly bracket'}
punctuation_symbol_key = punctuation_symbol.keys()

identifier = {'print': 'function'}
identifier_key = identifier.keys()

reserved = ['mientras', 'para', 'romper', 'continuar', 'retorna', 'si', 'funcion']

a = file.read()

count = 0
program = a.split("\n")
tokend = []
for line in program:
    tokend.append([])
    count = count + 1
    # print("line#" , count, "\n" , line)

    tokens = line.split(' ')
    # print("Tokens are " , tokens)
    # print("Line#", count, "properties \n")

    if tokens[0] in data_type_key:
        if tokens[1] not in identifier:
            identifier[tokens[1]] = 'id'
            identifier_key = identifier.keys()

    for token in tokens:
        if token in operators:
            # print("operator is ", operators[token])
            tokend[-1].append({'Tipo': operators[token], 'Valor': token})
        elif token in data_type:
            # print("datatype is", data_type[token])
            tokend[-1].append({'Tipo': data_type[token], 'Valor': token})
        elif token in punctuation_symbol:
            # print (token, "Punctuation symbol is" , punctuation_symbol[token])
            tokend[-1].append({'Tipo': punctuation_symbol[token], 'Valor': token})
        elif token in identifier:
            # print (token, "Identifier is" , identifier[token])
            tokend[-1].append({'Tipo': 'id', 'Valor': token})
        elif re.match('^[0-9]+$', token):
            tokend[-1].append({'Tipo': 'entero', 'Valor': token})
        elif re.match('^"[0-9 a-z A-Z]*"$', token):
            tokend[-1].append({'Tipo': 'caracteres', 'Valor': token})
        elif re.match('^[0-9]+.[0-9]+$', token):
            tokend[-1].append({'Tipo': 'flotante', 'Valor': token})
        elif token in punctuation_symbol:
            tokend[-1].append({'Tipo': punctuation_symbol[token], 'Valor': token})
        elif token in reserved:
            tokend[-1].append({'Tipo': 'reserved', 'Valor': token})

    # print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _")

json_object = json.dumps(tokend, indent=4)
with open("tokens.json", "w") as outfile:
    outfile.write(json_object)
