
n = int(input())

maius = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

minu = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i in range(n):
    caso = input()
    if caso[1] in maius:
        if int(caso[0]) == int(caso[2]):
            print(int(caso[0]) * int(caso[2]))
        else:
            print(int(caso[2]) - int(caso[0]))
    elif caso[1] in minu:
        if int(caso[0]) == int(caso[2]):
            print(int(caso[0]) * int(caso[2]))
        else:
            print(int(caso[0]) + int(caso[2]))

