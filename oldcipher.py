program = True
while program == True:
    menuinput = input("""
  Would you like to encrypt or decrypt?

Input: """)
    menuinput2 = menuinput.lower()
    if menuinput2 == "encrypt":
        cleartext = input("CLEARTEXT: ")
        cleartext = cleartext.lower()
        ciphertext = cleartext.replace("g", "11 ")
        ciphertext = ciphertext.replace("a", "BYQ ")
        ciphertext = ciphertext.replace("b", "BYG ")
        ciphertext = ciphertext.replace("c", "YW ")
        ciphertext = ciphertext.replace("d", "ZA ")
        ciphertext = ciphertext.replace("e", "1 ")
        ciphertext = ciphertext.replace("f", "10 ")
        ciphertext = ciphertext.replace("h", "100 ")
        ciphertext = ciphertext.replace("i", "AAAAA ")
        ciphertext = ciphertext.replace("j", "AAAAB ")
        ciphertext = ciphertext.replace("k", "AAABA ")
        ciphertext = ciphertext.replace("l", "AAABB ")
        ciphertext = ciphertext.replace("o", "ZOOLOGY ")
        ciphertext = ciphertext.replace("m", "MOMMY ")
        ciphertext = ciphertext.replace("n", "NANNA ")
        ciphertext = ciphertext.replace("p", "POPPING ")
        ciphertext = ciphertext.replace("q", "QUIZZES ")
        ciphertext = ciphertext.replace("r", "ROZZERS ")
        ciphertext = ciphertext.replace("s", "SIZZLE ")
        ciphertext = ciphertext.replace("t", "TIZZY ")
        ciphertext = ciphertext.replace("u", "DQ ")
        ciphertext = ciphertext.replace("v", "DG ")
        ciphertext = ciphertext.replace("w", "DW ")
        ciphertext = ciphertext.replace("x", "EA ")
        ciphertext = ciphertext.replace("y", "EQ ")
        ciphertext = ciphertext.replace("z", "EG ")
        lowercipher = cleartext.lower()
        print("""Encrypted Text: """ + ciphertext)
        print()
        print("""Original text: """ + cleartext)
    else:
        cleartext = input("ENCRYPTED STRING: ")
        ciphertext = cleartext.replace("BYQ ", "a")
        ciphertext = ciphertext.replace("BYG ", "b")
        ciphertext = ciphertext.replace("YW ", "c")
        ciphertext = ciphertext.replace("ZA ", "d")
        ciphertext = ciphertext.replace("100 ", "h")
        ciphertext = ciphertext.replace("11 ", "g")
        ciphertext = ciphertext.replace("10 ", "f")
        ciphertext = ciphertext.replace("1 ", "e")
        ciphertext = ciphertext.replace("AAAAA ", "i")
        ciphertext = ciphertext.replace("AAAAB ", "j")
        ciphertext = ciphertext.replace("AAABA ", "k")
        ciphertext = ciphertext.replace("AAABB ", "l")
        ciphertext = ciphertext.replace("ZOOLOGY ", "o")
        ciphertext = ciphertext.replace("MOMMY ", "m")
        ciphertext = ciphertext.replace("NANNA ", "n")
        ciphertext = ciphertext.replace("POPPING ", "p")
        ciphertext = ciphertext.replace("QUIZZES ", "q")
        ciphertext = ciphertext.replace("ROZZERS ", "r")
        ciphertext = ciphertext.replace("SIZZLE ", "s")
        ciphertext = ciphertext.replace("TIZZY ", "t")
        ciphertext = ciphertext.replace("DQ ", "u")
        ciphertext = ciphertext.replace("DG ", "v")
        ciphertext = ciphertext.replace("DW ", "w")
        ciphertext = ciphertext.replace("EA ", "x")
        ciphertext = ciphertext.replace("EQ ", "y")
        ciphertext = ciphertext.replace("EG ", "z")
        print("ORIGINAL TEXT: " + cleartext)
        print("UNENCRYPTED STRING: " + ciphertext)