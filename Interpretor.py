from RunTimeResult import *
from Values import *
from Constants import *

class Interpretor:
    def visit(self, node, context):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node, context)

    def no_visit_method(self, node, context):
        raise Exception(f'No visit_{type(node).__name__} method found')

    def visit_NumberNode(self, node, context):
        return RTResult().success(Number(node.tok.value).setContext(context).setPos(node.pos_start, node.pos_end))

    def visit_VarAccessNode(self, node, context):
        res = RTResult()
        var_name = node.var_name_tok.value
        value = context.symbol_table.get(var_name)

        if not value:
            return res.failure(RunTimeError(
                node.pos_start, node.pos_end,
                f"'{var_name}' is not defined",
                context
            ))

        value = value.copy().setPos(node.pos_start, node.pos_end)
        return res.success(value)

    def visit_VarAssignNode(self, node, context):
        res = RTResult()
        var_name = node.var_name_tok.value
        value = res.register(self.visit(node.value_node, context))
        if res.err:
            return res

        context.symbol_table.set(var_name, value)
        return res.success(value)

    def visit_BinOpNode(self, node, context):
        res = RTResult()
        left = res.register(self.visit(node.left_node, context))
        if res.err:
            return res
        right = res.register(self.visit(node.right_node, context))
        if res.err:
            return res
        error = None
        if (node.op_tok.type == TT_PLUS):
            result, error = left.addedTo(right)
        if (node.op_tok.type == TT_MINUS):
            result, error = left.subbedBy(right)
        if (node.op_tok.type == TT_MUL):
            result, error = left.multiTo(right)
        if (node.op_tok.type == TT_DIV):
            result, error = left.divideBy(right)
        if (node.op_tok.type == TT_POW):
            result, error = left.poweredTo(right)
        if error:
            return res.failure(error)
        return res.success(result.setPos(node.pos_start, node.pos_end))

    def visit_UnaryOpNode(self, node, context):
        res = RTResult()
        number = res.register(self.visit(node.node, context))
        if res.err:
            return res

        error = None

        if node.op_tok.type == TT_MINUS:
            number, error = number.multiTo(Number(-1))

        if error:
            return res.failure(error)
        return res.success(number.setPos(node.pos_start, node.pos_end))