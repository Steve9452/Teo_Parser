import re

f = open('fuente.cpp','r')


#Lista de tipos de tokens
operators = { '=': 'Asignacion',
             '+': 'Operador suma',
             '-' : 'Operador resta',
             '/' : 'Division Operador',
             '*': 'Multiplicacion Operador',
             '++' : 'Operador incremento',
             '--' : 'Operador decremento'}
optr_keys = operators.keys()

comments = {r'//' : 'Comentario de línea',
            r'/*' : 'Inicia comentario multilinea',
            r'*/' : 'Termina comentario multilinea',
            '/**/' : 'Comentario vacio'}
comment_keys = comments.keys()

header = {'.h': 'archivo de encabezado'}
header_keys = header.keys()

sp_header_files = {'<cstdio>':'Standard Input Output'
                   ,'<string>':'String Manipulation'
                   , '<iostream>' : 'Input Output Stream'}
sp_header_files_keys = sp_header_files.keys()

macros = {r'#\w+' : 'macro'}
macros_keys = macros.keys()

datatype = {'void': 'Void',
            'int': 'Integer',
            'float' : 'Floating Point',
            'char': 'Character',
            'long': 'long int',
            'short': 'short int',
            'string':'Character String',
            'double':'Double number',
            'bool':'Boolean'}
datatype_keys = datatype.keys()

keyword = {'return' : 'Palabra clave que retorna al SO',
           'if' : 'Palabra clave para evaluar una condicion',
           'else' : 'Palabra clave para cuando una condicion evaluada retorna false',
           'for' : 'Palabra clave para iterar n veces',
           'while' : 'Palabra clave para iterar mientras una condicion se cumpla',
           'do' : 'Palabra clave para ejecutar un bloque de instrucciones 1 vez antes de evaluar una condicion',
           'switch' : 'Palabra clave para evaluar un valor',
           'case' : 'Palabra clave que se ejecuta dependiendo del valor en switch',
           'break' : 'Palabra clave que detiene la ejecucion de un case',
           'struct' : 'Palabra clave para iniciar la delcaracion de una estructura de datos',
           'class' : 'Palabra clave para la delcaracion de una clase',
           'this' : 'Palabra clave para un puntero que apunta a la instancia de una clase',
           'malloc' : 'Palabra clave para reservar espacio en memoria',
           'new' : 'Palabra clave para instanciar una clase',
           'free' : 'Palabra clave para liberar el espacio en memoria ocupado por un dato o estructura de datos'}
keyword_keys = keyword.keys()

delimiter = {';':'Fin de instruccion'}
delimiter_keys = delimiter.keys()

blocks = {'{' : 'Inicia bloque de instrucciones', '}':'Fin de bloque de instrucciones'}
block_keys = blocks.keys()

builtin_functions = {'printf':'Imprime en consola',
                     'cout':'Imprime en consola',
                     'scanf':'Lee en consola',
                     'cin':'Lee en consola'}
builtin_functions_keys = builtin_functions.keys()

non_identifiers = ['_','-','+','/','*','`','~','!','@','#','$','%','^','&','*','(',')','=','|','"',':',';','{'
,'}','[',']','<','>','?','/']

numerals = ['0','1','2','3','4','5','6','7','8','9','10']

# banderas
dataFlag = False


i = f.read()

count = 0
program =  i.split('\n')

for line in program:
    count = count+1
    print ("Linea #",count,"\n",line)
    
     
    tokens = line.split(' ')#asumiendo el espacio //no deberia ser
    print ("Tokens son",tokens)
    print ("Linea #",count,'propiedades \n')
    for token in tokens:
        
        if '\r' in token:
            position = token.find('\r')
            token=token[:position]
        # print 1
        
        if token in block_keys:
            print (blocks[token])
        if token in optr_keys:
            print ("Operador es: ", operators[token])
        if token in comment_keys:
            print ("Comentario: ", comments[token])
        if token in macros_keys:
            print ("Macro es: ", macros[token])
        if '.h' in token:
            print ("Archivo de encabezado: ",token)
        if token in sp_header_files_keys:
            print ("Liberia: ",token, sp_header_files[token])
        if '()' in token:
            print ("Función:", token)
        
        if '"' in token:
            print ("Cadena de texto: ", token)

        if dataFlag == True and (token not in non_identifiers) and ('()' not in token):
            print ("Identificador: ",token)
        if token in datatype_keys:
            print ("Tipo es: ", datatype[token])
            dataFlag = True
        
        if token in keyword_keys:
            print (keyword[token])
        if token in builtin_functions_keys:
            print (builtin_functions[token])
            
        if token in delimiter:
            print ("Delimitador" , delimiter[token])
        if '#' in token:
            match = re.search(r'#\w+', token)
            print ("Encabezado", match.group())
        if token in numerals:
            print (token,type(int(token)))
            
    dataFlag = False   
            
    
    print ("________________________")
    

f.close()