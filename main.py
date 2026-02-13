from pathlib import Path


def main():
    dir = Path("out/svg").glob("*.svg")
    with open("out/index.md", "w") as f:
        for file in dir:
            f.write(f"![{file.name}](svg/{file.name})\n")


if __name__ == "__main__":
    main()
