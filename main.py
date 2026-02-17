import inspect
import os

import src.Diagramas


def main():
    os.makedirs("out", exist_ok=True)
    with open("out/index.md", "w") as f:
        f.write("# **Índice de Diagramas**\n\n\n\n")

    for name, obj in inspect.getmembers(src.Diagramas):
        if inspect.isfunction(obj) and obj.__module__ == src.Diagramas.__name__:
            if name not in ["N", "T"]:
                print(f"Ejecutando: {name}")
                with open(f"out/svg/{name}.svg", "w") as f:
                    obj().writeStandalone(f.write)
                with open(f"out/index.md", "a") as f:
                    f.write(f"## *{name}*\n![{name}](svg/{name}.svg)\n\n")


if __name__ == "__main__":
    main()
