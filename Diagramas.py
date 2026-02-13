from railroad import Diagram, Sequence, Choice, Terminal, NonTerminal, ZeroOrMore

"""
Esto solo fue un testeo de la librería railroad no lo vean como avances del taller en sí IMPORTANTE LEER
Este código lo que hace es hacer un diagrama del texto grammarTest.txt, denle a compilar y se creará un archivo .svg
Posteriormente pueden hacer doble click en el explorador de archivos para visualizarlo

Recuerden poner .\.venv\Scripts\Activate para activar el entorno jeje
"""
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


