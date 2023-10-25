# Analizador Sintático - Interpretador

from Tabela_de_Tokens import tabela_de_tokens
from Tipos_de_Tokens import TipoToken
from Lexema import Lexema
from Maquina_de_Estados import Maquina_de_Estados
from Comandos import *
from Expressoes import *

class Parser:
    
    def __init__(self):
        self.Maquina = None
        self.lista = []
        self.controle = 0
        self.token_aux = None
        
    def erro(self):
        if self.token_aux.tipo_token == TipoToken.INVALID_TOKEN:
            print(f"Linha {self.token_aux.linha}: {self.Maquina.arquivo_em_linhas[self.token_aux.linha-1]}")
            print(f"Lexema Inválido: _{self.token_aux.token}_")
        elif self.token_aux.tipo_token in [TipoToken.UNEXPECTED_EOF, TipoToken.END_OF_FILE]:
            print(f"Linha {self.token_aux.linha}: {self.Maquina.arquivo_em_linhas[self.token_aux.linha-1]}")
            print("Fim de arquivo inesperado")
        else:
            print(f"Linha {self.token_aux.linha}: {self.Maquina.arquivo_em_linhas[self.token_aux.linha-1]}")
            print(f"Lexema não esperado: _{self.token_aux.token}_")
        exit()
    
    def progredir(self, tipo_token_esperado):
        if self.token_aux.tipo_token == tipo_token_esperado:
            self.controle += 1
            if self.controle < self.tamanho_lista:
                self.token_aux = self.lista[self.controle]
        else:
            self.erro()
    
    def incrementar(self):
        self.controle += 1  
        self.token_aux = self.lista[self.controle]

    def iniciar_maquina_de_estados(self, nome_arq):
        self.Maquina = Maquina_de_Estados(False, ' ')
        self.Maquina.analizador_lexico(self.Maquina.ler_arquivo(nome_arq))
        self.lista = self.Maquina.lista_de_Tokens
        self.token_aux = self.lista[self.controle]
    
    def inicio(self, nome_arq):
        self.iniciar_maquina_de_estados(nome_arq)
        self.tamanho_lista = len(self.lista)
        object_command = self.procProgram()
        self.progredir(TipoToken.END_OF_FILE)
        return object_command
        
    # <program> ::= program <cmdlist>    
    def procProgram(self):
        self.progredir(TipoToken.PROGRAM)
        object_command = self.procCmdList()
        return object_command 

    # <cmdlist> ::= <cmd> { <cmd> }        
    def procCmdList(self):
        line = int(self.token_aux.linha)
        object_blocks_commands = Blocks_Command(line)
        object_command = self.procCmd()
        object_blocks_commands.add_commands(object_command)
        
        while self.token_aux.tipo_token in [TipoToken.VAR, TipoToken.OUTPUT, TipoToken.IF, TipoToken.WHILE]:
            object_command = self.procCmd()
            object_blocks_commands.add_commands(object_command)
        
        return object_blocks_commands

    # <cmd> ::= (<assign> | <output> | <if> | <while>) ;
    def procCmd(self):
        object_command = None
        
        if self.token_aux.tipo_token == TipoToken.VAR:
            object_command = self.procAssign()
        elif self.token_aux.tipo_token == TipoToken.OUTPUT:
            object_command = self.procOutput()
        elif self.token_aux.tipo_token == TipoToken.IF:
            object_command = self.procIf()
        elif self.token_aux.tipo_token == TipoToken.WHILE:
            object_command = self.procWhile()
        else:
            self.erro()
            
        self.progredir(TipoToken.SEMICOLON)
        return object_command 

    # <assign> ::= <var> = <intexpr>
    def procAssign(self):
        object_var = self.procVar()
        line = int(self.token_aux.linha)
        self.progredir(TipoToken.ASSIGN)
        object_expr = self.procIntExpr()
        object_assigned_command = Assign_Command (line, object_var, object_expr)
        return object_assigned_command

    # <output> ::= output <intexpr>
    def procOutput(self):
        self.progredir(TipoToken.OUTPUT)
        linha = int(self.token_aux.linha)
        object_expr = self.procIntExpr()
        object_output_command = Output_Command (linha, object_expr)
        return object_output_command

    # <if> ::= if <boolexpr> then <cmdlist> [ else <cmdlist> ] done
    def procIf(self):
        self.progredir(TipoToken.IF)
        line = int(self.token_aux.linha)
        
        object_bool_expr = self.procBoolExpr()
        self.progredir(TipoToken.THEN)
        
        object_command_then = self.procCmdList()
        object_command_else = None
        
        if self.token_aux.tipo_token == TipoToken.ELSE:
            self.incrementar()
            object_command_else = self.procCmdList()
        self.progredir(TipoToken.DONE)
        
        object_if_command = If_Command(line, object_bool_expr, object_command_then, object_command_else)
        return object_if_command

    # <while> ::= while <boolexpr> do <cmdlist> done
    def procWhile(self):
        self.progredir(TipoToken.WHILE)
        line = int(self.token_aux.linha)
        
        object_bool_expr = self.procBoolExpr()
        
        self.progredir(TipoToken.DO)
        
        object_command = self.procCmdList()
        self.progredir(TipoToken.DONE)
        
        object_while_command = While_Command(line, object_bool_expr, object_command)
        
        return object_while_command

    # <boolexpr> ::= false | true |
    #                not <boolexpr> |
    #                <intterm> (== | != | < | > | <= | >=) <intterm>
    def procBoolExpr(self):
        if self.token_aux.tipo_token == TipoToken.FALSE:
            self.incrementar()
            line = int(self.token_aux.linha)
            object_const_bool_expr = Const_Bool_Expr(line, False)
            return object_const_bool_expr
        
        elif self.token_aux.tipo_token == TipoToken.TRUE:
            self.incrementar()
            line = int(self.token_aux.linha)
            object_const_bool_expr = Const_Bool_Expr(line, False)
            return object_const_bool_expr
        
        elif self.token_aux.tipo_token == TipoToken.NOT:
            self.incrementar()
            line = int(self.token_aux.linha)
            object_bool_expr = self.procBoolExpr()
            object_not_bool_expr = Not_Bool_Expr (line, object_bool_expr)
            return object_not_bool_expr
        
        else:
            line = int(self.token_aux.linha)
            object_expr_left = self.procIntTerm()
            log_op = None
            
            if self.token_aux.tipo_token == TipoToken.EQUAL:
                log_op = Single_Bool_Expr.Log_Operators.EQUAL
                self.incrementar()
                
            elif self.token_aux.tipo_token == TipoToken.NOT_EQUAL:       
                log_op = Single_Bool_Expr.Log_Operators.NOT_EQUAL
                self.incrementar()
                                   
            elif self.token_aux.tipo_token ==TipoToken.LOWER: 
                log_op = Single_Bool_Expr.Log_Operators.LOWER
                self.incrementar()
                
            elif self.token_aux.tipo_token == TipoToken.LOWER_EQUAL:
                log_op = Single_Bool_Expr.Log_Operators.LOWER_EQUAL
                self.incrementar()
                
            elif self.token_aux.tipo_token == TipoToken.GREATER: 
                log_op = Single_Bool_Expr.Log_Operators.GREATER
                self.incrementar()
                
            elif self.token_aux.tipo_token == TipoToken.GREATER_EQUAL: 
                log_op = Single_Bool_Expr.Log_Operators.GREATER_EQUAL
                self.incrementar()
                
            else:
                self.erro()
                
            object_expr_right = self.procIntTerm()
            
            Bool_Expr = Single_Bool_Expr (line, object_expr_left, log_op, object_expr_right)
            return Bool_Expr

    # <intexpr> ::= [ + | - ] <intterm> [ (+ | - | * | / | ^ | %) <intterm> ]
    def procIntExpr(self):
        boolean = False 
        
        if self.token_aux.tipo_token == TipoToken.ADD:
            self.incrementar()
        elif self.token_aux.tipo_token == TipoToken.SUB:
            self.incrementar()
            boolean = True
        
        object_left = None
        
        if boolean:    
            line = int(self.token_aux.linha)
            object_int_expr = self.procIntTerm()
            object_left = Neg_Int_Expr(line, object_int_expr)
        else:
            line = int(self.token_aux.linha)
            object_left = self.procIntTerm()
        
        op = None
        
        if self.token_aux.tipo_token == TipoToken.ADD:
            op = Binary_Int_Expr.Operators.ADD
            
            self.incrementar()
            object_right = self.procIntTerm()
            object_left = Binary_Int_Expr (line, object_left, op, object_right)
            
        elif self.token_aux.tipo_token == TipoToken.SUB:
            op = Binary_Int_Expr.Operators.SUB
            
            self.incrementar()
            object_right = self.procIntTerm()
            object_left = Binary_Int_Expr (line, object_left, op, object_right)
            
        elif self.token_aux.tipo_token == TipoToken.MUL:
            op = Binary_Int_Expr.Operators.MUL
            
            self.incrementar()
            object_right = self.procIntTerm()
            object_left = Binary_Int_Expr (line, object_left, op, object_right)
            
        elif self.token_aux.tipo_token == TipoToken.DIV:
            op = Binary_Int_Expr.Operators.DIV
            
            self.incrementar()
            object_right = self.procIntTerm()
            object_left = Binary_Int_Expr (line, object_left, op, object_right)
        
        elif self.token_aux.tipo_token == TipoToken.POW:
            op = Binary_Int_Expr.Operators.POW
            
            self.incrementar()
            object_right = self.procIntTerm()
            object_left = Binary_Int_Expr (line, object_left, op, object_right)
        
        elif self.token_aux.tipo_token == TipoToken.MOD:
            op = Binary_Int_Expr.Operators.MOD
            
            self.incrementar()
            object_right = self.procIntTerm()
            object_left = Binary_Int_Expr (line, object_left, op, object_right)
        
        return object_left

    # <intterm> ::= <var> | <const> | read
    def procIntTerm(self):
        if self.token_aux.tipo_token == TipoToken.VAR:
            return self.procVar()
        
        elif self.token_aux.tipo_token == TipoToken.NUMBER:
            return self.procConst()
        
        else:
            self.progredir(TipoToken.READ)
            line = int(self.token_aux.linha)
            object_read_int_expr = Read_Int_Expr(line)
            return object_read_int_expr

    # <var> ::= id
    def procVar(self):
        name = self.token_aux.token
        self.progredir(TipoToken.VAR)
        
        object_var = Variable (name)
        object_return_var = object_var.retorna_variavel(name)
        
        return object_return_var

    # <const> ::= number
    def procConst(self):
        name = self.token_aux.token
        self.progredir(TipoToken.NUMBER)
        line = int(self.token_aux.linha)
        num = int(name)
        object_const_int_expr = Const_Int_Expr (line, num)
        
        return object_const_int_expr
