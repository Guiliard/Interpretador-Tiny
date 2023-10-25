# Associação dos tokens com seus respectivos tipos

from Tipos_de_Tokens import TipoToken

tabela_de_tokens = {
    
    # Símbolos
	';': TipoToken.SEMICOLON,
	'=': TipoToken.ASSIGN,

	# Operadores lógicos de comparação
	'==': TipoToken.EQUAL,
	'!=': TipoToken.NOT_EQUAL,
	'<':  TipoToken.LOWER,
	'<=': TipoToken.LOWER_EQUAL,
	'>':  TipoToken.GREATER,
	'>=': TipoToken.GREATER_EQUAL,

	# Operadores Aritméticos
	'+': TipoToken.ADD,
	'-': TipoToken.SUB,
	'*': TipoToken.MUL,
	'/': TipoToken.DIV,
	'^': TipoToken.POW,
	'%': TipoToken.MOD,

	# Palavras-chave da linguagem Tiny
	'program': TipoToken.PROGRAM,
	'while': TipoToken.WHILE,
	'do': TipoToken.DO,
	'done': TipoToken.DONE,
	'if': TipoToken.IF,
	'then': TipoToken.THEN,
	'else': TipoToken.ELSE,
	'output': TipoToken.OUTPUT,
	'true': TipoToken.TRUE,
	'false': TipoToken.FALSE,
	'read': TipoToken.READ,
	'not': TipoToken.NOT,
}