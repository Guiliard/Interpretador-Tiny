# Comandos não retornam informações, apenas processamento

from Expressoes import Expr
from Expressoes import Variable

class Command:
    
    def __init__(self, linha):
        self.linha = linha
    
    def retorna_linha(self):
        return self.linha
    
    def executar(): #Método abstrato da classe Command, será implementado nas classes filhas
        pass
    

class Blocks_Command(Command):
    
    def __init__(self, linha):
        super().__init__(linha)
        self.commands_list = []
        
    def __del__(self):
       for object in self.commands_list:
           del object
         
    def add_commands(self, command_aux):
        self.commands_list.append(command_aux)
    
    def executar(self):
        for object in self.commands_list:
            object.executar()
            

class Assign_Command(Command):
    
    def __init__(self, linha, variable, expr):
        super().__init__(linha)
        self.variable = variable
        self.expr = expr
        
    def executar(self):
        valor = int(self.expr.executar())
        self.variable.set_valor(valor)
        

class Output_Command(Command):
    
    def __init__(self, linha, expr):
        super().__init__(linha)
        self.expr = expr
        
    def executar(self):
        print(self.expr.executar())
    

class If_Command (Command):
    
    def __init__(self, linha, bool_expr, then_command, else_command):
        super().__init__(linha)
        self.bool_expr = bool_expr
        self.then_command = then_command
        self.else_command = else_command
        
    def executar(self):
        if self.bool_expr.executar():
            self.then_command.executar()
        else:
            if self.else_command:
                self.else_command.executar()   
    

class While_Command(Command):
    
    def __init__(self, linha, bool_expr_cond, commands):
        super().__init__(linha)
        self.bool_expr_cond = bool_expr_cond
        self.commands = commands
        
    def executar(self):
        while self.bool_expr_cond.executar():
            self.commands.executar()
		
