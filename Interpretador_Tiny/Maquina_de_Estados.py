# Analizador Léxico 

from Tabela_de_Tokens import tabela_de_tokens
from Tipos_de_Tokens import TipoToken
from Lexema import Lexema

class Maquina_de_Estados:
    
    def __init__ (self, existe, token):
        self.existe = existe
        self.token = token
        self.arquivo_em_linhas  = []
        self.lista_de_Tokens = []

    def ler_arquivo(self, nome):
        try:
            with open(nome, 'r') as arquivo:
                self.conteudo = arquivo.read()
                arquivo.seek(0)
                self.arquivo_em_linhas = arquivo.readlines()
                return self.conteudo
        except FileNotFoundError:
            print(f"O arquivo {sum.tiny} não foi encontrado.")
            
    def analizador_lexico(self, conteudo):
        string_token = ''
        estado = 1
        controle = 0
        linhas = 1
        existe = False
        tamanho_do_arquivo = len(conteudo)
        lexema_final = Lexema (' ', ' ', 0)
        while controle <= tamanho_do_arquivo:
            
                if estado == 1:
                    
                    if controle == tamanho_do_arquivo:
                        lexema_final = Lexema('', TipoToken.END_OF_FILE, linhas)
                        #print(f"(_{lexema_final.token}_, {lexema_final.tipo_token}), linha: {lexema_final.linha}")
                        self.lista_de_Tokens.append(lexema_final)
                        break
                        
                    elif conteudo[controle] == '\t' or  conteudo[controle] == '\r' or conteudo[controle] == '\n' or conteudo[controle] == ' ':
                        if conteudo[controle] == '\n':
                            linhas += 1
                        controle = controle + 1 
                        estado = 1
                        
                    elif conteudo[controle] == '#':
                        controle = controle + 1
                        estado = 2
                        
                    elif conteudo[controle] == '<' or conteudo[controle] == '>' or conteudo[controle] == '=':
                        string_token = string_token + conteudo[controle]
                        controle = controle + 1 
                        estado = 3
                        
                    elif conteudo[controle] == '!':
                        string_token = string_token + conteudo[controle]
                        controle = controle + 1
                        estado = 4
                    
                    elif conteudo[controle] == ';' or conteudo[controle] == '+' or  conteudo[controle] == '-' or conteudo[controle] == '*' or conteudo[controle] == '%' or conteudo[controle] == '/' or conteudo[controle] == '^':
                        string_token = string_token + conteudo[controle]
                        controle = controle + 1
                        estado = 7
                    
                    elif conteudo[controle].isalpha() == True:
                        string_token = string_token + conteudo[controle]
                        controle = controle + 1
                        estado = 5
                    
                    elif conteudo[controle].isdigit() == True:
                        string_token = string_token + conteudo[controle]
                        controle =  controle + 1
                        estado = 6
                    
                    else:
                        string_token = string_token + conteudo[controle]
                        lexema_final = Lexema (string_token, TipoToken.INVALID_TOKEN, linhas)
                        print(f"(_{lexema_final.token}_, {lexema_final.tipo_token}, linha: {lexema_final.linha})")
                        self.lista_de_Tokens.append(lexema_final)
                        print('\nQuebra de execução......')
                        exit()
                        
                elif estado == 2:
                    
                    if conteudo[controle] != '\n':
                        controle = controle + 1
                        estado = 2
                        
                    elif conteudo[controle] == '\n':
                        if conteudo[controle] == '\n':
                            linhas += 1
                        controle =  controle + 1
                        estado = 1
                
                elif estado == 3:
                    
                    if conteudo[controle] == '=':
                        string_token = string_token + conteudo[controle]
                        controle = controle + 1
                        estado = 7
                    
                    elif conteudo[controle] != '=':
                        estado = 7

                elif estado == 4:
                    
                    if conteudo[controle] == '=':
                        string_token = string_token + conteudo[controle]
                        controle = controle + 1
                        estado = 7 
                        
                    elif controle == tamanho_do_arquivo - 1:
                        string_token = string_token + conteudo[controle]
                        lexema_final = Lexema (string_token, TipoToken.UNEXPECTED_EOF, linhas)
                        print(f"(_{lexema_final.token}_, {lexema_final.tipo_token}), linha: {lexema_final.linha}")
                        self.lista_de_Tokens.append(lexema_final)                        
                        print('\nQuebra de execução......')
                        exit()
                        
                    else:
                        string_token = string_token + conteudo[controle]
                        lexema_final = Lexema (string_token, TipoToken.INVALID_TOKEN, linhas)
                        print(f"(_{lexema_final.token}_, {lexema_final.tipo_token}, linha: {lexema_final.linha})")
                        self.lista_de_Tokens.append(lexema_final)
                        print('\nQuebra de execução......')
                        exit()
                        

                elif estado == 5:
                    
                    if conteudo[controle].isalpha() == True:
                        string_token = string_token + conteudo[controle]
                        controle = controle + 1
                        estado = 5
                    
                    elif conteudo[controle].isalpha() == False:
                        estado = 7

                elif estado == 6:
                    
                    if conteudo[controle].isdigit() == True:
                        string_token = string_token + conteudo[controle]
                        controle = controle + 1
                        estado = 6
                    
                    elif conteudo[controle].isdigit() == False:
                        estado = 8

                elif estado == 7:
                    
                    existe = string_token in tabela_de_tokens
                    lexema_final = Lexema (string_token, TipoToken.VAR if not existe else tabela_de_tokens[string_token], linhas)
                    #print(f"(_{lexema_final.token}_, {lexema_final.tipo_token}, linha: {lexema_final.linha})")
                    self.lista_de_Tokens.append(lexema_final)
                    string_token = ''
                    estado = 1

                elif estado == 8:
                    
                    existe = string_token in tabela_de_tokens
                    lexema_final = Lexema (string_token, TipoToken.NUMBER if not existe else tabela_de_tokens[string_token], linhas)
                    #print(f"(_{lexema_final.token}_, {lexema_final.tipo_token}, linha: {lexema_final.linha})")
                    self.lista_de_Tokens.append(lexema_final)
                    string_token = ''
                    estado = 1