import json

operators = {'=' : 'Assignment op','+' : 'Addition op','-' : 'Subtraction op','/' : 'Division op','*' : 'Multiplication op','<' : 'Lessthan op','>' : 'Greaterthan op' }
operators_key = operators.keys()

data_type = {'ent' : 'integer type', 'flot': 'Floating point' , 'car' : 'Character type', 'grande' : 'long int' }
data_type_key = data_type.keys()

punctuation_symbol = { ':' : 'colon', ';' : 'semi-colon', '.' : 'dot' , ',' : 'comma' }
punctuation_symbol_key = punctuation_symbol.keys()

identifier = { }
identifier_key = identifier.keys()

symbol_table = {}

with open('tokens.json', 'r') as openfile:
    program = json.load(openfile)
    
    count = 0
    for line in program:
        count += 1
        #print('Line# ', count, '\n')
        
        if(line[-1]['Valor'] not in punctuation_symbol_key):
            print('Error al final de la linea #', count, 'No se usaron los simbolos de puntuación correctos \n')
            break
        if(line[0]['Valor'] not in identifier_key and line[0]['Valor'] not in data_type_key):
            print('Error al principio de la linea #', count, 'No se reconoce la variable o el tipo de datos')
            break
        if line[0]['Valor'] in data_type_key:
            if line[1]['Valor'] not in identifier:
                identifier[line[1]['Valor']] = 'id'
                identifier_key = identifier.keys()
                symbol_table[line[1]['Valor']] = line[0]['Valor']
        elif line[0]['Valor'] == 'funcion':
            if line[1] not in identifier:
                identifier[line[1]['Valor']] = 'id'
                identifier_key = identifier.keys()
                symbol_table[line[1]['Valor']] = line[0]['Valor']
                
        first_id = False
        for token in line:
            if token['Valor'] in identifier.keys():
                if first_id == True:
                    #print('Error, se esperaba un signo de asignacion')
                    break
                first_id = True
            elif first_id == True:
                first_id = False
           
json_object = json.dumps(symbol_table, indent = 4)
with open('symbol_table.json', 'w') as st:
    st.write(json_object)
    
        
