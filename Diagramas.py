import os

from railroad import (
    Choice,
    Diagram,
    NonTerminal,
    Sequence,
    Terminal,
    ZeroOrMore,
)

os.makedirs("out/svg", exist_ok=True)
# Recuerden poner .\.venv\Scripts\Activate para activar el entorno jeje


def T(x):
    return Terminal(x)


def N(x):
    return NonTerminal(x)


# lval
def lvalue():
    return Diagram(Choice(0, T("ID"), Sequence(T("ID"), N("index"))))


with open("out/svg/lvalue.svg", "w", encoding="utf-8") as f:
    lvalue().writeStandalone(f.write)


# stmt Bien
def stmt():
    return Diagram(Choice(0, N("open_stmt"), N("closed_stmt")))


with open("out/svg/stmt.svg", "w", encoding="utf-8") as f:
    stmt().writeStandalone(f.write)


# openStmt Bien
def openStmt():
    return Diagram(
        Choice(0, N("if_stmt_open"), N("for_stmt_open"), N("while_stmt_open"))
    )


with open("out/svg/openStmt.svg", "w", encoding="utf-8") as f:
    openStmt().writeStandalone(f.write)


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


with open("out/svg/closedStmt.svg", "w", encoding="utf-8") as f:
    closedStmt().writeStandalone(f.write)


# if Bien
def if_cond():
    return Diagram(Sequence(T("IF"), T("("), N("opt_expr"), T(")")))


with open("out/svg/if_cond.svg", "w", encoding="utf-8") as f:
    if_cond().writeStandalone(f.write)


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


with open("out/svg/ifStmtClosed.svg", "w", encoding="utf-8") as f:
    ifStmtClosed().writeStandalone(f.write)


def ifStmtOpen():
    return Diagram(
        Choice(
            0,
            Sequence(N("if_cond"), N("stmt")),
            Sequence(N("if_cond"), N("closed_stmt"), T("ELSE"), N("if_stmt_open")),
        )
    )


with open("out/svg/ifStmtOpen.svg", "w", encoding="utf-8") as f:
    ifStmtOpen().writeStandalone(f.write)


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


with open("out/svg/forHeader.svg", "w", encoding="utf-8") as f:
    forHeader().writeStandalone(f.write)


def forStmtOpen():
    return Diagram(Sequence(N("for_header"), N("open_stmt")))


with open("out/svg/forStmtOpen.svg", "w", encoding="utf-8") as f:
    forStmtOpen().writeStandalone(f.write)


def forStmtClosed():
    return Diagram(Sequence(N("for_header"), N("closed_stmt")))


with open("out/svg/forStmtClosed.svg", "w", encoding="utf-8") as f:
    forStmtClosed().writeStandalone(f.write)


# while Bien
def whileStmtOpen():
    return Diagram(Sequence(T("WHILE"), T("("), N("expr"), T(")"), N("open_stmt")))


with open("out/svg/whileStmtOpen.svg", "w", encoding="utf-8") as f:
    whileStmtOpen().writeStandalone(f.write)


def whileStmtClosed():
    return Diagram(Sequence(T("WHILE"), T("("), N("expr"), T(")"), N("closed_stmt")))


with open("out/svg/whileStmtClosed.svg", "w", encoding="utf-8") as f:
    whileStmtClosed().writeStandalone(f.write)


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


with open("out/svg/simpleStmt.svg", "w", encoding="utf-8") as f:
    simpleStmt().writeStandalone(f.write)


# Expr
def expr():
    return Diagram(N("expr1"))


with open("out/svg/expr.svg", "w", encoding="utf-8") as f:
    expr().writeStandalone(f.write)


def expr1():
    return Diagram(Choice(0, Sequence(N("lval"), T("="), N("expr1")), N("expr2")))


with open("out/svg/expr1.svg", "w", encoding="utf-8") as f:
    expr1().writeStandalone(f.write)


def lval():
    return Diagram(Choice(0, T("ID"), Sequence(T("ID"), N("index"))))


with open("out/svg/lval.svg", "w", encoding="utf-8") as f:
    lval().writeStandalone(f.write)


def expr2():
    return Diagram(Sequence(N("expr3"), ZeroOrMore(Sequence(T("LOR"), N("expr3")))))


with open("out/svg/expr2.svg", "w", encoding="utf-8") as f:
    expr2().writeStandalone(f.write)


def expr3():
    return Diagram(Sequence(N("expr4"), ZeroOrMore(Sequence(T("LAND"), N("expr4")))))


with open("out/svg/expr3.svg", "w", encoding="utf-8") as f:
    expr3().writeStandalone(f.write)


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


with open("out/svg/expr4.svg", "w", encoding="utf-8") as f:
    expr4().writeStandalone(f.write)


def expr5():
    return Diagram(
        Sequence(
            N("expr6"), ZeroOrMore(Sequence(Choice(0, T("+"), T("-")), N("expr6")))
        )
    )


with open("out/svg/expr5.svg", "w", encoding="utf-8") as f:
    expr5().writeStandalone(f.write)


def expr6():
    return Diagram(
        Sequence(
            N("expr7"),
            ZeroOrMore(Sequence(Choice(0, T("*"), T("/"), T("%")), N("expr7"))),
        )
    )


with open("out/svg/expr6.svg", "w", encoding="utf-8") as f:
    expr6().writeStandalone(f.write)


def expr7():
    return Diagram(Sequence(N("expr8"), ZeroOrMore(Sequence(T("^"), N("expr8")))))


with open("out/svg/expr7.svg", "w", encoding="utf-8") as f:
    expr7().writeStandalone(f.write)


def expr8():
    return Diagram(Sequence(ZeroOrMore(Choice(0, T("-"), T("NOT"))), N("expr9")))


with open("out/svg/expr8.svg", "w", encoding="utf-8") as f:
    expr8().writeStandalone(f.write)


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


with open("out/svg/group.svg", "w", encoding="utf-8") as f:
    group().writeStandalone(f.write)


def expr9():
    return Diagram(Sequence(N("group"), ZeroOrMore(Choice(0, T("INC"), T("DEC")))))


with open("out/svg/expr9.svg", "w", encoding="utf-8") as f:
    expr9().writeStandalone(f.write)


def assignOp():
    return Diagram(Choice(0, T("+="), T("-="), T("*="), T("/=")))


with open("out/svg/assignOp.svg", "w", encoding="utf-8") as f:
    assignOp().writeStandalone(f.write)


def assignExpr():
    return Diagram(Sequence(N("lval"), N("assignOp"), N("expr")))


with open("out/svg/assignExpr.svg", "w", encoding="utf-8") as f:
    assignExpr().writeStandalone(f.write)


def incdecOp():
    return Diagram(Choice(0, T("++"), T("--")))


with open("out/svg/incdecOp.svg", "w", encoding="utf-8") as f:
    incdecOp().writeStandalone(f.write)


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


with open("out/svg/incdecExpr.svg", "w", encoding="utf-8") as f:
    incdecExpr().writeStandalone(f.write)
