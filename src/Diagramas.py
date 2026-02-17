from railroad import (
    Choice,
    Diagram,
    NonTerminal,
    Sequence,
    Terminal,
    ZeroOrMore,
)


def T(x):
    return Terminal(x)


def N(x):
    return NonTerminal(x)


# lval
def lvalue():
    return Diagram(Choice(0, T("ID"), Sequence(T("ID"), N("index"))))


# stmt Bien
def stmt():
    return Diagram(Choice(0, N("open_stmt"), N("closed_stmt")))


# openStmt Bien
def openStmt():
    return Diagram(
        Choice(0, N("if_stmt_open"), N("for_stmt_open"), N("while_stmt_open"))
    )


# closedStmt Bien
def closedStmt():
    return Diagram(
        Choice(
            0,
            N("if_stmt_closed"),
            N("for_stmt_closed"),
            N("while_stmt_closed"),
            N("simple_stmt"),
        )
    )


# if Bien
def if_cond():
    return Diagram(Sequence(T("IF"), T("("), N("opt_expr"), T(")")))


def ifStmtClosed():
    return Diagram(
        Sequence(
            N(
                "if_cond"
            ),  # Recordar que if_cond ya tenía una definición previa en la gramática, justo arriba
            N("closed_stmt"),
            T("ELSE"),
            N("closed_stmt"),
        )
    )


def ifStmtOpen():
    return Diagram(
        Choice(
            0,
            Sequence(N("if_cond"), N("stmt")),
            Sequence(N("if_cond"), N("closed_stmt"), T("ELSE"), N("if_stmt_open")),
        )
    )


# for Bien
def forHeader():
    return Diagram(
        Sequence(
            T("FOR"),
            T("("),
            N("opt_expr"),
            T(";"),
            N("opt_expr"),
            T(";"),
            N("opt_expr"),
            T(")"),
        )
    )


def forStmtOpen():
    return Diagram(Sequence(N("for_header"), N("open_stmt")))


def forStmtClosed():
    return Diagram(Sequence(N("for_header"), N("closed_stmt")))


# while Bien
def whileStmtOpen():
    return Diagram(Sequence(T("WHILE"), T("("), N("expr"), T(")"), N("open_stmt")))


def whileStmtClosed():
    return Diagram(Sequence(T("WHILE"), T("("), N("expr"), T(")"), N("closed_stmt")))


# simpleStmt Bien
def simpleStmt():
    return Diagram(
        Choice(
            0,
            N("print_stmt"),
            N("return_stmt"),
            N("block_stmt"),
            N("decl"),
            Sequence(N("expr"), T(";")),
        )
    )


# Expr
def expr():
    return Diagram(N("expr1"))


def expr1():
    return Diagram(Choice(0, Sequence(N("lval"), T("="), N("expr1")), N("expr2")))


def lval():
    return Diagram(Choice(0, T("ID"), Sequence(T("ID"), N("index"))))


def expr2():
    return Diagram(Sequence(N("expr3"), ZeroOrMore(Sequence(T("LOR"), N("expr3")))))


def expr3():
    return Diagram(Sequence(N("expr4"), ZeroOrMore(Sequence(T("LAND"), N("expr4")))))


def expr4():
    return Diagram(
        Sequence(
            N("expr5"),
            ZeroOrMore(
                Sequence(
                    Choice(0, T("EQ"), T("NE"), T("LT"), T("LE"), T("GT"), T("GE")),
                    N("expr5"),
                )
            ),
        )
    )


def expr5():
    return Diagram(
        Sequence(
            N("expr6"), ZeroOrMore(Sequence(Choice(0, T("+"), T("-")), N("expr6")))
        )
    )


def expr6():
    return Diagram(
        Sequence(
            N("expr7"),
            ZeroOrMore(Sequence(Choice(0, T("*"), T("/"), T("%")), N("expr7"))),
        )
    )


def expr7():
    return Diagram(Sequence(N("expr8"), ZeroOrMore(Sequence(T("^"), N("expr8")))))


def expr8():
    return Diagram(Sequence(ZeroOrMore(Choice(0, T("-"), T("NOT"))), N("expr9")))


def group():
    return Diagram(
        Choice(
            0,
            Sequence(T("("), N("expr"), T(")")),
            Sequence(T("ID"), T("("), N("opt_expr_list"), T(")")),
            Sequence(T("ID"), N("index")),
            N("factor"),
        )
    )


def expr9():
    return Diagram(Sequence(N("group"), ZeroOrMore(Choice(0, T("INC"), T("DEC")))))


def assignOp():
    return Diagram(Choice(0, T("+="), T("-="), T("*="), T("/=")))


def assignExpr():
    return Diagram(Sequence(N("lval"), N("assignOp"), N("expr")))


def incdecOp():
    return Diagram(Choice(0, T("++"), T("--")))


def incdecExpr():
    return Diagram(
        Choice(
            0,
            # Prefix
            Sequence(N("incdec_op"), N("lval")),
            # Postfix
            Sequence(N("lval"), N("incdec_op")),
        )
    )


# Clases
def typeClass():
    return Diagram(Sequence(T("CLASS"), T("("), N("parent_class"), T(")")))


with open("out/svg/typeClass.svg", "w", encoding="utf-8") as f:
    typeClass().writeStandalone(f.write)


# type_array
def typeArray():
    return Diagram(
        Choice(
            0,
            Sequence(T("ARRAY"), T("["), T("]"), N("type_simple")),
            Sequence(T("ARRAY"), T("["), T("]"), N("type_array")),
            Sequence(T("ARRAY"), T("["), T("]"), N("type_class")),
        )
    )


def typeArraySized():
    return Diagram(
        Choice(
            0,
            Sequence(T("ARRAY"), N("index"), N("type_simple")),
            Sequence(T("ARRAY"), N("index"), N("type_array_sized")),
            Sequence(T("ARRAY"), N("index"), N("type_class")),
        )
    )


# type_func
def typeFunc():
    return Diagram(
        Choice(
            0,
            Sequence(
                T("FUNCTION"), N("type_simple"), T("("), N("opt_param_list"), T(")")
            ),
            Sequence(
                T("FUNCTION"),
                N("type_array_sized"),
                T("("),
                N("opt_param_list"),
                T(")"),
            ),
            Sequence(
                T("FUNCTION"), N("type_class"), T("("), N("opt_param_list"), T(")")
            ),
        )
    )
