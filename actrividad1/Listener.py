from SimpleListener import SimpleListener
from SimpleParser import SimpleParser

class ClaseMetodoAsignacionListener(SimpleListener):

    def enterClassDef(self, ctx: SimpleParser.ClassDefContext):
        class_name = ctx.ID().getText()
        print(f"🧩 Clase: {class_name}")

    def enterMember(self, ctx: SimpleParser.MemberContext):
        if ctx.getChildCount() > 2 and ctx.getChild(2).getText() == '(':
            method_name = ctx.ID(0).getText()
            print(f"🔧 Método: {method_name}")

    def enterStat(self, ctx: SimpleParser.StatContext):
        if ctx.getChildCount() >= 3 and ctx.getChild(1).getText() == '=':
            var_name = ctx.getChild(0).getText()
            print(f"📌 Asignación: {var_name} = ...")
