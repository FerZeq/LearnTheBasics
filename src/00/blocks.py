import sys

def check_string(blck_string):
    return_string = None
    if len(blck_string) == 33:
        i = 0
        while i < 5:
            if blck_string[i] == '0':
                i += 1
            else:
                return_string = None
                break
        if blck_string[5] == '0':
            return_string = None
        if i == 5:
            return_string = blck_string
    else:
        return_string = None
    return return_string


def main() -> None:
    args_num = int(sys.argv[1])
    if args_num < 1 or args_num > 10:
        print("Argument Error")
    else:
        lines = sys.stdin.readlines()
        i = 0
        while i < args_num:
            if check_string(lines[i]) is not None:
                print(check_string(lines[i]), end="")
            i += 1


if __name__ == '__main__':
    main()