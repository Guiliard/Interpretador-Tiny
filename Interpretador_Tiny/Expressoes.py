#Expressões retornam informações

from enum import Enum

class Expr:
    
    def __init__(self,linha):
        self.linha = linha
        
    def retorna_linha(self):
        return self.linha

    def executar(): # Método abstrato da classe Expr, será implementado nas classes filhas
        pass 
    

class Const_Bool_Expr (Expr):
    
    def __init__(self, linha, booleano):
        super().__init__(linha)
        self.booleano = booleano
        
    def executar(self):
        return self.booleano
    

class Single_Bool_Expr (Expr):
    
    Log_Operators = Enum('Log_Operators', ['EQUAL','NOT_EQUAL','LOWER','LOWER_EQUAL','GREATER', 'GREATER_EQUAL'])       
    
    def __init__(self, linha, left, log_operation, right):
        super().__init__(linha)
        self.left = left
        self.log_operation = log_operation
        self.right = right
        
    def __del__(self):
        del self.left
        del self.right
        
    def executar(self):
        expr1 = int(self.left.executar())
        expr2 = int(self.right.executar())
        
        if self.log_operation == self.Log_Operators.EQUAL:
            return expr1 == expr2
        elif self.log_operation == self.Log_Operators.NOT_EQUAL:
            return expr1 != expr2
        elif self.log_operation == self.Log_Operators.LOWER:
            return expr1 < expr2
        elif self.log_operation == self.Log_Operators.LOWER_EQUAL:
            return expr1 <= expr2
        elif self.log_operation == self.Log_Operators.GREATER:
            return expr1 > expr2
        elif self.log_operation == self.Log_Operators.GREATER_EQUAL:
            return expr1 >= expr2
    
    
class Not_Bool_Expr (Expr):
    
    def __init__(self, linha, bool_expr):
        super().__init__(linha)
        self.bool_expr = bool_expr
        
    def executar(self):
        return not self.bool_expr.executar()
    
class Const_Int_Expr (Expr):
    
    def __init__(self, linha, valor):
        super().__init__(linha)
        self.valor = valor
    
    def executar(self):
        return self.valor
    
class Neg_Int_Expr (Expr):
    
    def __init__(self, linha, int_expr):
        super().__init__(linha)
        self.int_expr = int_expr
        
    def executar(self):
        return -self.int_expr.executar()
        
    
class Read_Int_Expr (Expr):
    
    def __init__(self, linha):
        super().__init__(linha)
        
    def executar(self):
        var = int(input())
        return var
    
class Binary_Int_Expr (Expr):
    
    Operators = Enum('Operators', ['ADD','SUB','MUL','DIV','POW','MOD'])       
    
    def __init__(self, linha, left, operation, right):
        super().__init__(linha)
        self.left = left
        self.operation = operation
        self.right = right
        
    def __del__(self):
        del self.left
        del self.right
        
    def executar(self):
        expr1 = int(self.left.executar())
        expr2 = int(self.right.executar())
        
        if self.operation == self.Operators.ADD:
            return expr1 + expr2
        elif self.operation == self.Operators.SUB:
            return expr1 - expr2
        elif self.operation == self.Operators.MUL:
            return expr1 * expr2
        elif self.operation == self.Operators.DIV:
            return int(expr1 / expr2)
        elif self.operation == self.Operators.POW:
            return expr1 ** expr2
        elif self.operation == self.Operators.MOD:
            return expr1 % expr2
            
                      
class Variable (Expr):	
    
    variables_map = {}
    
    def __init__(self, nome):
        super().__init__(-1)
        self.nome = nome
        self.valor = 0 
        
    def retorna_variavel(self, nome):
        var = self.variables_map.get(nome)
        
        if var is None:  
            
            var = Variable (nome)
            self.variables_map[nome] = var
        
        return var
        
    def set_valor(self, valor):
        self.valor = valor
    
    def retorna_nome (self):
        return self.nome
    
    def executar(self):
        return self.valor
