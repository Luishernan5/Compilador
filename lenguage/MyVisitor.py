for GrammarVisitor import GrammarVisitor
for GrammarParser import GrammarParser

class MyVisitor(GrammarVisitor):
    def __init__(self):
        self.memory = {}

    # Definimos la asignación
    def visitAssign(self,ctx):
        name=ctx.ID().getText()
        value=self.visit(ctx.expr())
        self.memory[name]=value

    #Definimos la asignación
    def visitPrint(self,ctx):
        value=self.visit(ctx.expr())
        print(value)