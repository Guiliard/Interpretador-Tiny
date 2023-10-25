# Arquivo de Execução 

from Parser import Parser

def main ():
    nome_arq = 'Testes_Interpretador/pow_ot.tiny'
    Interpretador = Parser()
    object_interpretador = Interpretador.inicio(nome_arq)
    object_interpretador.executar()
    
main()