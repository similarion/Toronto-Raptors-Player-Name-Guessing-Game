def main():
    total = 0

    num1 = int(input("enter a number"))
    total = total + num1
    num2 = int(input("enter a number"))
    total = total + num2
    num3 = int(input("enter a number"))
    total = total + num3

    if total > 100:
        print("That's a big number!")
    else:
        print("That's a small number.")
    print(total)

while True:
    answer = input("Run again? (y/n): ")
    if answer not in ('y', 'n'):
        print("Invalid input.")
        break
    if answer == 'y':
        main()
    else:
        print("Goodbye")
        break