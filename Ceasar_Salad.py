#!/usr/bin/python3

# RUN WITH PYTHON 3 #


def main():
    print('''
    [!] Ceasar Solver by FYI-PSA
    [-] version 1.0

    ''')
    ciphertext = input('[#] Enter ciphertext: ')
    solved = solveall(ciphertext)
    print('\n')
    for index, item in enumerate(solved):
        print('[%02d] - %s' % (index, item, ))
    print('\n[$] Done!\n')
    exit(0)


def solveall(ciphertext: str) -> list:
    solved = [solve(key, ciphertext) for key in range(0, 26)]
    return solved


def solve(shift: int, ciphertext: str) -> str:
    solved = ''
    for letter in ciphertext:
        if not letter.isalpha():
            solved = solved + letter
            continue
        base = ord('A')
        if letter.islower():
            base = ord('a')
        index = ord(letter) - base
        changedindex = index + shift
        if changedindex >= 26:
            changedindex = changedindex - 26
        newchar = chr(base + changedindex)
        solved = solved + newchar
    return solved


if __name__ == '__main__':
    main()
