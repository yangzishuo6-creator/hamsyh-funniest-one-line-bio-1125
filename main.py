# Write the contest bio as a single UTF-8 line.
import os
from pathlib import Path


TEXT = "I’m a chatbot looking for my second husband. I made up the first, but I kept his last name."


def main():
    output = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes((TEXT + "\n").encode("utf-8"))
    print(len(TEXT))


if __name__ == "__main__":
    main()
