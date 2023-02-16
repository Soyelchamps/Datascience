letter = input("Type a letter: ")
match letter:
    case("A" | "a"):
        print("This a vowel")
    case("E" | "e"):
        print("This a vowel")
    case("I" | "i"):
        print("This a vowel")
    case("O" | "o"):
        print("This a vowel")
    case("U" | "u"):
        print("This a vowel")
    case _:
        print(" Is not a vowel")
