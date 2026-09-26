from cs50 import get_int

def main():
    height = get_height()
    for i in range(1, height+1):
        for j in range(1, height - i + 1):
            print(" ", end="")
        for z in range(1, i + 1):
            print("#", end="")
        print()


def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0 and n < 9:
                break
        except ValueError:
            print("Give an integer")
    return n

main()
