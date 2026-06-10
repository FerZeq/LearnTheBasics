import sys

def is_three_by_five(lines) -> bool:
    final = True
    if len(lines) != 3:
        final = False
    else:
        for line in lines:
            if len(line) != 6:
                final = False

    return final

def is_m(lines) -> bool:
    final = False
    m_base = lines[0][0]
    i = 0
    j = 0
    for line in lines:
        for char in line:
            if char != m_base:
                j += 1
        if j == 9:
            if (line[0] == m_base or line[len(line) - 2] == m_base
                or line[i] == m_base or line[len(line) - i - 2] == m_base):
                final = True
            i += 1

    return final

def main() -> None:
    lines = sys.stdin.readlines()
    if not is_three_by_five(lines):
        print('Error')
    else:
        print(is_m(lines))

if __name__ == "__main__":
    main()