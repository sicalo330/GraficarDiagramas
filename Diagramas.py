from railroad import Diagram, Sequence, Choice, Terminal, NonTerminal, ZeroOrMore

def T(x): return Terminal(x)
def N(x): return NonTerminal(x)


def test():
    return Diagram(
        Choice(1,
            Sequence(T("print"),N("expr")),N("expr")
        )
    )


# Exportar a SVG
with open("test.svg", "w", encoding="utf-8") as f:
    test().writeStandalone(f.write)


