import ply.lex as lex
import re


tokens =  ('INT', 'STRING', 'DOT', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD', 'EMIT', 'CHAR', 'KEY', 'SPACE', 
           'SPACES', 'CR', 'DEFINED_WORD', 'SEMICOLON', 'DUP', '2DUP', 'SWAP','SUPEQ', 'SUPERIOR','INFEQ', 'INFERIOR', 'EQUALS', 'DROP',
           'IF', 'ELSE', 'THEN', 'NAME', 'VARIABLE', 'EXCLAMATION', 'AT','DO', 'LOOP')

class Counters:
    def __init__(self):
        self.contador_vars = 1

ult_tipo = ""
ult_valor = ""
contador_ifs = 1
contador_whiles = 1

vars = Counters()


def extract_stack_comment(stack_comment):
    #print(stack_comment)
    if stack_comment == "(--)":
        return 0, False
    if '--' in stack_comment:
        inputs, outputs = stack_comment.split('--')
        num_inputs = len(inputs.strip().split()) if inputs.strip() else 0
        num_outputs = len(outputs.strip().split()) if outputs.strip() else 0
        has_output = num_outputs > 0
    else:
        num_inputs = len(stack_comment.split())
        has_output = False  # Cannot determine without '--', assuming no output

    return num_inputs, has_output

defined_words = {}
defined_vars = {}
# numero do while -> contador
defined_whiles = {}
word_list = []

def t_2DUP(t):
    r'2dup'
    t.value = "dup 2"
    return t

def t_INT(t):
    r'\d+'
    global ult_valor
    global ult_tipo
    ult_tipo = "INT"
    ult_valor = (t.value)
    t.value = "pushi" + " " + str(t.value)
    return t

def t_MOD(t):
    r'MOD'
    t.value = "mod"
    return t

def t_SPACES(t):
    r'SPACES'
    t.value = 'pushs "' 
    for i in range(int(ult_valor)):    
        t.value += " "
    t.value += '"\nwrites'
    return t

def t_SPACE(t):
    r'SPACE'
    t.value = 'pushs " "\nwrites'
    return t

def t_CR(t):
    r'CR'
    t.value = r'pushs "\n"' + "\nwrites"
    return t

def t_DUP(t):
    r'DUP'
    t.value = "dup 1"
    return t

def t_SWAP(t):
    r'swap'
    return t

def t_EMIT(t):
    r'EMIT'
    t.value = "writechr\n" 
    return t

def t_CHAR(t):
    r'CHAR\s(.)'
    t.value = 'pushs "' + str(t.value[5:]) + '"\nchrcode'
    global ult_tipo 
    ult_tipo = "INT"
    return t

def t_KEY(t):
    r'KEY'
    t.value = "read\nchrcode\n"
    global ult_tipo
    ult_tipo = "INT"
    return t

def t_DROP(t):
    r'drop'
    t.value = "pop 1"
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_THEN(t):
    r'then'
    return t

def t_VARIABLE(t):
    r'VARIABLE\s([a-zA-Z0-9]+)'
    match = re.match(r'VARIABLE\s([a-zA-Z0-9]+)', t.value, re.IGNORECASE)
    global defined_vars
    if match:
        defined_vars[match.group(1)] = vars.contador_vars
        vars.contador_vars += 1
        t.value = "alloc 1\nstoreg " + str(defined_vars[match.group(1)]) + "\n"
    return t

def t_NAME(t):
    r':\s([a-zA-Z0-9\-]+)\s\((.*)\)'
    match = re.match(r':\s([a-zA-Z0-9]+)\s\((.*)\)', t.value)
    if match:
        if match.group(1) not in defined_words:
            defined_words[match.group(1)] = extract_stack_comment(match.group(2))

    t.value = match.group(1)
    return t

def t_DO(t):
    r'do'
    global contador_whiles
    # contador
    t.value = "storeg " + str(vars.contador_vars) + "\n"
    global defined_whiles
    defined_whiles[contador_whiles] = vars.contador_vars
    vars.contador_vars += 1
    # caso de paragem 
    t.value += "storeg " + str(vars.contador_vars) + "\n"
    vars.contador_vars += 1
    t.value += "WHILE" + str(contador_whiles) + ":\n"
    t.value += "pushg " + str(vars.contador_vars-2) + "\n"
    t.value += "pushg " + str(vars.contador_vars-1) + "\n"
    t.value += "inf\n"
    t.value += "jz ENDWHILE" + str(contador_whiles) + "\n"
    return t

def t_LOOP(t):
    r'loop'
    global defined_whiles
    t.value = "pushg " + str(defined_whiles[contador_whiles]) + "\n"
    t.value += "pushi 1\n"
    t.value += "add\n"
    t.value += "storeg " + str(defined_whiles[contador_whiles]) + "\n"
    t.value += "jump WHILE" + str(contador_whiles) + "\n"
    t.value += "ENDWHILE" + str(contador_whiles) + ":\n"
    return t

def t_DEFINED_WORD(t):
    r'[a-zA-Z0-9]+'

    if t.value in defined_words:
        final = "pusha " + t.value + "\ncall"
        if defined_words[t.value][0] > 0:
            final += "\npop " + str(defined_words[t.value][0])
        if(defined_words[t.value][1] == True):
            final += "\npushg 0"
        t.value = final
    elif t.value in defined_vars:
        t.value = "pushg " + str(defined_vars[t.value])
    
    elif t.value == "i" and contador_whiles > 0:
        t.value = "pushg " + str(defined_whiles[contador_whiles])
    else:
        t.value = ""

    return t

def t_EXCLAMATION(t):
    r'!'
    t.value = "swap\nstore 0"
    return t

def t_AT(t):
    r'@'
    t.value = "load 0"
    return t

def t_SEMICOLON(t):
    r';'
    return t

def t_PLUS(t):
    r'\+'
    t.value = "add"
    return t

def t_MINUS(t):
    r'\-'
    t.value = "sub"
    return t

def t_TIMES(t):
    r'\*'
    t.value = "mul"
    return t

def t_DIVIDE(t):
    r'\/'
    t.value = "div"
    return t

def t_STRING(t):
    r'\.\"\s.*?\"'
    t.value = 'pushs "' + t.value[3:-1] + '"\nwrites'
    return t

def t_DOT(t):
    r'\.'
    t.value = "writei\n"
    return t

def t_SUPEQ(t):
    r'>='
    t.value = "supeq"
    return t

def t_SUPERIOR(t):
    r'>'
    t.value = "sup"
    return t

def t_INFEQ(t):
    r'<='
    t.value = "infeq"
    return t

def t_INFERIOR(t):
    r'<'
    ult_tipo == "INT"
    t.value = "inf"
    return t

def t_EQUALS(t):
    r'='
    t.value = "equal"
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    pass

def t_error(t):
    print("Caracter ilegal: ", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex(reflags=re.IGNORECASE)