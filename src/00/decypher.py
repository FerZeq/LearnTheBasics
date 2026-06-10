import sys

def decypher(text: str) -> str:
    is_start_of_word = True
    return_line = ""
    for char in text:
        if is_start_of_word:
            return_line += char
            is_start_of_word = False
        if char == ' ':
            is_start_of_word = True
    return return_line


def main() -> None:
    line = sys.argv[1]
    print(decypher(line))

if __name__ == "__main__":
    main()