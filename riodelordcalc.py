# https://github.com/riodelord
import math
import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'NAME',
    'NUMBER_INT', 'NUMBER_DOUBLE',
    'PLUS','MINUS','TIMES','DIVIDE',
    'EQUALS','COLON',
    'LPAREN','RPAREN',
)
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_COLON   = r','
t_EQUALS  = r'='
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_ignore = ' \t'

def t_NUMBER_DOUBLE(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print('Integer value too large %d', t.value)
        t.value = 0
    return t

def t_NUMBER_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print('Integer value too large %d', t.value)
        t.value = 0
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')
    
def t_error(t):
    print('Illegal character \'%s\'' % t.value[0])
    t.lexer.skip(1)

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
)

variables = {
    'pi': math.pi,
    'e': math.e,
}
start='statement'

def p_statement_assign(t):
    '''
    statement : NAME EQUALS expression
    '''
    variables[t[1]] = t[3]

def p_statement_expression(t):
    '''
    statement : expression
    '''
    print(t[1])

def p_expression_binop(t):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression DIVIDE expression
               | expression TIMES expression
    '''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]

def p_expression_uminus(t):
    '''
    expression : MINUS expression %prec UMINUS
    '''
    t[0] = -t[2]

def p_expression_group(t):
    '''
    expression : LPAREN expression RPAREN
    '''
    t[0] = t[2]

def p_expressions(t):
    '''
    expressions : expressions COLON expression
               | expression
               |
    '''
    if len(t) == 0:
        t[0]=None
        return
    t[0] = [t[1]] if len(t) == 2 else t[1] + [t[3]]

def p_expression_function(t):
    '''
    expression : NAME LPAREN expressions RPAREN
    '''
    if t[1] == 'sin':
        if len(t[3]) == 1:
            t[0]=math.sin(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'cos':
        if len(t[3]) == 1:
            t[0]=math.cos(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'log':
        if len(t[3]) == 1:
            t[0]=math.log(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'log10':
        if len(t[3]) == 1:
            t[0]=math.log10(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'log2':
        if len(t[3]) == 1:
            t[0]=math.log2(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'exp':
        if len(t[3]) == 1:
            t[0]=math.exp(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return




    elif t[1] == 'sqrt':
        if len(t[3]) == 1:
            t[0]=math.sqrt(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'acos':
        if len(t[3]) == 1:
            t[0]=math.acos(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'atan':
        if len(t[3]) == 1:
            t[0]=math.atan(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'radians':
        if len(t[3]) == 1:
            t[0]=math.radians(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'sinh':
        if len(t[3]) == 1:
            t[0]=math.sinh(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'cosh':
        if len(t[3]) == 1:
            t[0]=math.cosh(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'tanh':
        if len(t[3]) == 1:
            t[0]=math.tanh(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'asin':
        if len(t[3]) == 1:
            t[0]=math.asin(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return



    elif t[1] == 'ceil':
        if len(t[3]) == 1:
            t[0]=math.ceil(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'fabs':
        if len(t[3]) == 1:
            t[0]=math.fabs(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'factorial':
        if len(t[3]) == 1:
            t[0]=math.factorial(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'floor':
        if len(t[3]) == 1:
            t[0]=math.floor(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'copysign':
        if len(t[3]) == 2:
            t[0]=math.copysign(int(t[3][0]), int(t[3][1]))
        else:
            print('%s() function need two arguments' % t[1])
        return
    elif t[1] == 'pow':
        if len(t[3]) == 2:
            t[0]=math.pow(int(t[3][0]), int(t[3][1]))
        else:
            print('%s() function need two arguments' % t[1])
        return
    print('Undefined function \'%s\'' % t[1])
    t[0] = None

def p_expression_number(t):
    '''
    expression : NUMBER_INT
               | NUMBER_DOUBLE
    '''
    t[0] = t[1]

def p_expression_name(t):
    '''
    expression : NAME
    '''
    try:
        t[0] = variables[t[1]]
    except LookupError:
        print('Undefined name \'%s\'' % t[1])
        t[0] = None

def p_error(t):
    print('Syntax error at \'%s\'' % t.value)

# lexer = lex.lex()
lexer = lex.lex(optimize=1)
# parser = yacc.yacc()
parser = yacc.yacc(debug=0, write_tables=0)
while True:
    try:
        s = input('> ')
    except EOFError:
        break
    parser.parse(s)