
import ply.lex as lex

reservado = {
    'se' : 'SE',
    'então' : 'ENTAO',
    'senão' : 'SENAO',
    'fim' : 'FIM',
    'repita' : 'REPITA',
    'flutuante' : 'FLUTUANTE',
    'retorna' : 'RETORNA',
    'até' : 'ATE',
    'leia': 'LEIA',
    'escreva' : 'ESCREVA',
    'inteiro' : 'INTEIRO'
}



tokens = [
    'SOMA',
    'SUBTRACAO',
    'DIVISAO',
    'MULTIPLICACAO',
    'IGUALDADE',
    'VIRGULA',
    'ATRIBUICAO',
    'MENOR',
    'MAIOR',
    'MENOR_IGUAL',
    'MAIOR_IGUAL',
    'ABRE_PAR',
    'FECHA_PAR',
    'DOIS_PONTOS',
    'ABRE_COL',
    'FECHA_COL',
    'E_LOGICO',
    'OU_LOGICO',
    'NEGACAO',
    'COMENTARIO',
    'NUMERO_FLUTUANTE',
    'NUMERO_INTEIRO',
    'NOTACAO_CIENTIFICA',
    'ID',
    'NUM_NOTACAO_CIENTIFICA',
    
] + list(reservado.values())

t_SOMA = r'\+'
t_SUBTRACAO = r'\-'
t_DIVISAO = r'/'
t_MULTIPLICACAO = r'\*'
t_IGUALDADE = r'\='
t_VIRGULA = r','    
t_ATRIBUICAO = r':='
t_MENOR = r'<'
t_MAIOR = r'>'
t_MENOR_IGUAL = r'<='
t_MAIOR_IGUAL = r'>='
t_ABRE_PAR = r'\('
t_FECHA_PAR = r'\)'
t_DOIS_PONTOS = r':'
t_ABRE_COL = r'\['
t_FECHA_COL = r'\]'
t_E_LOGICO = r'&&'
t_OU_LOGICO = r'\|\|'
t_NEGACAO = r'!'
#t_COMENTARIO = r'\{[^}]*[^{]*\}'

t_ignore = ' \t'


def t_COMENTARIO(t):
    r'\{[^}]*[^{]*\}'
    pass



def t_ID(t):
    r'[a-zA-Z_][a-zà-úA-ZÀ-Ú0-9_]*'
    t.type = reservado.get(t.value, 'ID')
    return t

def t_NOVA_LINHA(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)


def t_NUM_NOTACAO_CIENTIFICA(t):
    r'[0-9]+[\.[0-9]*]?e\+?\-?[0-9]+'   
    return t
    

def t_NUMERO_FLUTUANTE(t):
    r'[0-9]+\.[0-9]*'
    t.value = float(t.value)    
    return t

def t_NUMERO_INTEIRO(t):
    r'[0-9]+'
    t.value = int(t.value)    
    return t


teste = lex.lex()

#filename = './lexica-testes/teste-1.tpp'
#filename = './lexica-testes/teste-2.tpp'
#filename = './lexica-testes/Busca_Linear_1061992.tpp'
filename = './lexica-testes/fat.tpp'
#filename = './lexica-testes/multiplicavetor.tpp'
#filename = './lexica-testes/primo.tpp'
#filename = './lexica-testes/bubble_sort.tpp'


file = open(filename,'r', encoding = 'utf8')

codigo = file.read()
file.close()

teste.input(codigo)


cont = 1
while True :
    token = teste.token()
    if not token:
        break
    print(cont,'(', token.type,',' ,token.value , ')')
    cont+=1



