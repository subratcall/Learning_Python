def recall_password(cipher_grille, ciphered_password):
    # define a function to express the password from the current grill
    def decrypt(cipher_grille, ciphered_password):
        sn = ''
        coor1 = ''.join((map(lambda x: str(x) * cipher_grille[x].count('X'), list(range(4)))))
        coor2 = ''
        for i in cipher_grille:
            for n in range(4):
                if i[n] == 'X':
                    coor2 += str(n)
        for c in range(0, 4):
            sn += ciphered_password[int(coor1[c])][int(coor2[c])]
        return sn

    # define a function to rotate the cipher_grille 90 degree clockwise
    def rotate(cipher_grille):
        def new(n):
            new_line = ''
            for i in range(4):
                new_line += cipher_grille[i][n]
            return new_line[::-1]

        new_grille = list(map(new, list(range(4))))
        return new_grille

    # add 4 runs of decrypt() together as the final password
    password = ''
    for i in range(4):
        r = decrypt(cipher_grille, ciphered_password)
        cipher_grille = rotate(cipher_grille)
        password += r

    return password


cipher_grille = ('X...',
                 '..X.',
                 'X..X',
                 '....')

password = 'icantforgetiddqd'


def write_password(cipher_grille, password):
    # define a function to express the password from the current grill
    ciphered_password = [[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]]
    password = password
    def encrypt(cipher_grille, password):
        coor1 = ''.join((map(lambda x: str(x) * cipher_grille[x].count('X'), list(range(4)))))
        coor2 = ''
        for i in cipher_grille:
            for n in range(4):
                if i[n] == 'X':
                    coor2 += str(n)
        for c in range(0, 4):
            ciphered_password[int(coor1[c])][int(coor2[c])] = password[c]
        return ciphered_password

    # define a function to rotate the cipher_grille 90 degree clockwise
    def rotate(cipher_grille):
        def new(n):
            new_line = ''
            for i in range(4):
                new_line += cipher_grille[i][n]
            return new_line[::-1]

        new_grille = list(map(new, list(range(4))))
        return new_grille

    # write in the password with rotating grille 4 times
    for i in range(4):
        ciphered_password = encrypt(cipher_grille, password)
        password = password[4:]
        cipher_grille = rotate(cipher_grille)

    # convert the list in ciphered_password into tuple with strings
    for i in range(4):
        str_element = ''.join(ciphered_password[i])
        ciphered_password[i] = str_element
    ciphered_password = tuple(ciphered_password)
    return ciphered_password

print(write_password(cipher_grille, password))
