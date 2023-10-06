# ------------------------------------------------------------
# Lexer para C
# ------------------------------------------------------------
import ply.lex as lex

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
   'Asignacion',
   'Comentario_linea',
   'comentario_bloque',
   'Cadena',
   'Coma',
   'Punto',
   'Macro'
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
t_Asignacion = r'\='
t_Coma= r'\,'
t_Punto= r'\.'
t_Macro= r'\#'

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

def t_comentario_bloque(t):
    r'\/\*(.|\n)*\*\/'
    return t

# Error handling rule
def t_error(t):
    print("Caracter Ilegal '%s'" % t.value[0])
    t.lexer.skip(1)    
    return t

# Build the lexer
lexer = lex.lex()

def Lexer():
    f = open('fuente.cpp','r')
    lexer.input(f.read())
    while True:
        tok=lexer.token()
        if not tok:
            break
        if (tok.type == 'error'):
            continue
        print(tok.type, ' Valor: (', tok.value, ') Linea: ', tok.lineno, ' Posicion: ', tok.lexpos)

Lexer()