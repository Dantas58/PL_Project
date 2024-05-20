# compilador de forth
import ply.yacc as yacc
from Tokens import *



def p_inicio(p):
    '''inicio : Comandos'''
    p[0] = p[1]
    
def p_Comandos(p):
    '''Comandos : Comando Comandos
                | Comando'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

        

def p_Comando(p):
    '''Comando : Valores
               | Operadores 
               | Declaracao
               | Print
               | Operacao
               | Condicional
               | Ciclo
               | DEFINED_WORD
    '''
    p[0] = p[1]


def p_Condicional(p):
    '''Condicional : IF Comandos ELSE Comandos THEN
                   | IF Comandos ELSE THEN
                   | IF Comandos THEN
                   | IF THEN'''
    
    global contador_ifs
    local = contador_ifs
    contador_ifs += 1
    if len(p) == 6:
        p[0] = "jz else" + str(local) + "\n" + '\n'.join(p[2]) + "\njump endif" + str(local) + "\nelse" + str(local) + ":\n" + '\n'.join(p[4]) + "\nendif" + str(local) + ":\n"
    elif len(p) == 4:
        p[0] = "jz else" + str(local) + "\n" + '\n'.join(p[2]) + "\nelse" + str(local) + ":\n"
    elif len(p) == 3:
        p[0] = "jz else" + str(local) + "\n" + '\n'.join(p[2]) + "\nelse" + str(local) + ":\n"
    else:
        p[0] = ""

def p_Ciclo(p):
    '''Ciclo : DO Comandos LOOP'''
    p[0] = p[1] + '\n'.join(p[2]) + '\n' + p[3]
    global contador_whiles
    contador_whiles += 1

def p_Operacao(p):
    '''Operacao : KEY
                | DUP
                | 2DUP
                | SWAP
                | DROP'''
    p[0] = p[1]

def p_Print(p):
    '''Print : STRING
             | EMIT
             | DOT
             | CHAR
             | SPACE
             | SPACES
             | CR'''
    p[0] = p[1]

def p_Valores(p):
    '''Valores : INT'''

    p[0] = p[1]

def p_Declaracao(p):
    '''Declaracao : DeclaracaoF
                  | DeclaracaoV'''
    p[0] = p[1]


def p_DeclaracaoF(p):
    '''DeclaracaoF : NAME Comandos SEMICOLON'''
    final = ""
    if(defined_words[p[1]][0] > 0):

        for i in range(defined_words[p[1]][0], 0 , -1):
            final += "pushfp\nload -" + str(i) + "\n"
                
    final = (p[1] + ":\n" + final + '\n'.join(p[2]))
    if(defined_words[p[1]][1] == True):
        final += "\nstoreg 0"
    word_list.append(final + "\nreturn")
    p[0] = ""

def p_DeclaracaoV(p):
    '''DeclaracaoV : VARIABLE
                   | EXCLAMATION
                   | AT'''

    p[0] = p[1]
    
def p_Operadores(p):
    '''Operadores :  PLUS
                    | MINUS
                    | TIMES
                    | DIVIDE
                    | MOD
                    | SUPEQ
                    | INFEQ
                    | INFERIOR
                    | SUPERIOR
                    | EQUALS
        '''
    p[0] = p[1]


def p_error(p):
    if p:
        print(f"Erro de sintaxe na posição {p.lineno}: {p.value}")
    else:
        print("Erro de sintaxe no fim do input!")

# Constrói o parser
parser = yacc.yacc()


print("1. Read from input")
print("2. Read from file")
choice = input("Enter your choice: ")

if choice == '1':
    entrada = input("Enter your input: ")
elif choice == '2':
    filename = input("Enter the filename: ")
    with open(filename, 'r') as file:
        entrada = file.read()
else:
    print("Invalid choice")
    exit(1)

res = parser.parse(entrada)


with open("output.txt", "w") as f: 
    for v in range(vars.contador_vars):
        f.write("pushi 0\n")
    f.write("start\n")
    for i in res:
        f.write(i + "\n")
    f.write("stop\n\n")
    for word in word_list:
        f.write(word + "\n\n")
    f.close()

