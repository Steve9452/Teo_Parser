# ------------------------------------------------------------
# Lexer para C
# ------------------------------------------------------------
import ply.lex as lex

S=0
S2=1
T=2
T2=3
F=4

# List of token names.   This is always required
tokens = (
   'Numero',
   'Suma',
   'Resta',
   'Multiplicacion',
   'Division',
   'Menor_que',
   'Mayor_que',
   'Parentesis_izquierdo',
   'Parentesis_derecho',
   'Corchete_izquierdo',
   'Corchete_derecho',
   'Tipo_dato',
   'Palabra_revervada',
   'Entrada',
   'Imprimir',
   'Identificador',
   'Inicio_bloque',
   'Fin_bloque',
   'Fin_instruccion',
   'Ligamiento',
   'Asignacion',
   'Comentario_linea',
   'Comentario_bloque',
   'Cadena',
   'Coma',
   'Punto',
   'Macro',
   'eof'
   
)

# Regular expression rules for simple tokens
t_Suma    = r'\+'
t_Resta   = r'-'
t_Multiplicacion   = r'\*'
t_Division  = r'/'
t_Menor_que  = r'\<'
t_Mayor_que  = r'\>'
t_Parentesis_izquierdo  = r'\('
t_Parentesis_derecho  = r'\)'
t_Corchete_izquierdo  = r'\['
t_Corchete_derecho  = r'\]'
t_Inicio_bloque = r'\{'
t_Fin_bloque = r'\}'
t_Fin_instruccion = r'\;'
t_Ligamiento = r'\:'
t_Asignacion = r'\='
t_Coma= r'\,'
t_Punto= r'\.'
t_Macro= r'\#'
t_eof= r'\$'

#t_vacia= r'\'  


# A regular expression rule with some action code
def t_Numero(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_Tipo_dato(t):
    r'(int)|(float)|(char)|(long)|(short)|(string)|(double)|(bool)|(void)'
    return t

def t_Palabra_revervada(t):
    r'(return)|(if)|(else)|(do)|(while)|(for)|(switch)|(case)|(break)|(struct)|(class)|(this)|(malloc)|(new)|(free)'
    return t

def t_Entrada(t):
    r'(cin)|(scanf)'
    return t

def t_Imprimir(t):
    r'(cout)|(printf)'
    return t

def t_Identificador(t):
    r'([a-z]|[A-Z]|_)([a-z]|[A-Z]|\d|_)*'
    return t

def t_Cadena(t):
    r'\".*\"'
    return t

def t_Comentario_linea(t):
    r'\/\/.*'
    return t

def t_Comentario_bloque(t):
    r'\/\*(.|\n)*\*\/'
    return t

# Error handling rule
def t_error(t):
    print("Error. Caracter ilegal: '%s'" % t.value[0])
    t.lexer.skip(1)    
    return t

TT=5
D=6

tabla2 = [[S, 'Identificador', [T,S2] ],
         [S, 'Suma', None ],
         [S, 'Multiplicacion', None ],
         [S, 'Parentesis_izquierdo', [T,S2]],
         [S, 'Parentesis_derecho', None],
         [S, 'eof', None],
         [S2, 'Identificador', None ],
         [S2, 'Suma', ['Suma',T,S2] ],
         [S2, 'Multiplicacion', None ],
         [S2, 'Parentesis_izquierdo', None],
         [S2, 'Parentesis_derecho', ['vacia']],
         [S2, 'eof', ['vacia']],
         [T, 'Identificador', [F,T2] ],
         [T, 'Suma', None ],
         [T, 'Multiplicacion', None ],
         [T, 'Parentesis_izquierdo', [F,T2]],
         [T, 'Parentesis_derecho', None],
         [T, 'eof', None],
         [T2, 'Identificador', None ],
         [T2, 'Suma', ['vacia'] ],
         [T2, 'Multiplicacion', ['Multiplicacion',F,T2] ],
         [T2, 'Parentesis_izquierdo', None],
         [T2, 'Parentesis_derecho', ['vacia']],
         [T2, 'eof', ['vacia']],
         [F, 'Identificador', ['Identificador'] ],
         [F, 'Suma', None ],
         [F, 'Multiplicacion', None ],
         [F, 'Parentesis_izquierdo', ['Parentesis_izquierdo',S,'Parentesis_derecho']],
         [F, 'Parentesis_derecho', None],
         [F, 'eof', None],
         [S, 'Identificador', None ],
         [S, 'Tipo_dato', [TT,'Identificador',D] ],
         [S, 'Tipo_dato', [TT,'Identificador',D] ],
         [S, 'Coma', None],
         [S, 'Fin_instruccion', None],
         [TT, 'Identificador', None ],
         [TT, 'Tipo_dato', ['Tipo_dato'] ],
         [TT, 'Tipo_dato', ['Tipo_dato'] ],
         [TT, 'Coma', None],
         [TT, 'Fin_instruccion', None],
         [D, 'Identificador', None ],
         [D, 'Tipo_dato', None ],
         [D, 'Tipo_dato', None ],
         [D, 'Coma', ['Coma','Identificador',D]],
         [D, 'Fin_instruccion', ['Fin_instruccion']],
         ]


tabla = [[S, 'identificador', None ],
         [S, 'int', [TT,'identificador',D] ],
         [S, 'float', [TT,'identificador',D] ],
         [S, 'coma', None],
         [S, 'finInstruccion', None],
         [TT, 'identificador', None ],
         [TT, 'int', ['int'] ],
         [TT, 'float', ['float'] ],
         [TT, 'coma', None],
         [TT, 'finInstruccion', None],
         [D, 'identificador', None ],
         [D, 'int', None ],
         [D, 'float', None ],
         [D, 'coma', ['coma','identificador',D]],
         [D, 'finInstruccion', ['finInstruccion']],
         ]

stack = ['eof', 0]


# Build the lexer
lexer = lex.lex()

def miParser():
    f = open('fuente2.cpp','r')
    lexer.input(f.read())
    #lexer.input('total_mujeres+total_hombres$')
    

    tok=lexer.token()
    x=stack[-1] #primer elemento de der a izq
    while True:
        print(tok.type)
        print(x)
        if x == tok.type and x == 'eof':
            print("Cadena reconocida exitosamente")
            return #aceptar
        else:
            if x == tok.type and x != 'eof':#llegué a un camino de derivación completo
                stack.pop()
                x=stack[-1]
                tok=lexer.token()                
            if x in tokens and x != tok.type:
                print("Error: se esperaba ", tok.type)
                print('en la posicion: ', tok.lexpos);
                return 0;
            if x not in tokens: #es no terminal      
                celda=buscar_en_tabla(x,tok.type)                            
                if  celda is None:
                    print("Error: NO se esperaba", tok.type)
                    print('en la posicion: ', tok.lexpos);
                    return 0;
                else:                    
                    stack.pop()
                    agregar_pila(celda)
                    x=stack[-1]
        print(stack)
        print()

            
        #if not tok:
            #break
        #print(tok)
        #print(tok.type, tok.value, tok.lineno, tok.lexpos)

def buscar_en_tabla(no_terminal, terminal):
    for i in range(len(tabla2)):
        if( tabla2[i][0] == no_terminal and tabla2[i][1] == terminal):
            return tabla2[i][2] #retorno la celda

def agregar_pila(produccion):
    for elemento in reversed(produccion):
        if elemento != 'vacia': #la vacía no la inserta
            stack.append(elemento)
    

miParser()