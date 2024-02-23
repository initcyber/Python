# This program takes an integer and converts it to decimal
# Author: Justin

# This function converts binary to decimal
def bin2dec(num):
    num = str(num)
    num = int(num, 2)
    return num

# This function converts decimal to binary
def dec2bin(num):
    num = str(num)
    num = bin(int(num))
    num = num[2:]
    return num

# Main  - Asks user if converting from binary to decimal or vice versa
def main():
    while True:
        print("1. Binary to Decimal")
        print("2. Decimal to Binary")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            num = input("Enter a binary number: ")
            num = bin2dec(num)
            print(num)
        elif choice == "2":
            num = input("Enter a decimal number: ")
            num = dec2bin(num)
            print(num)
        elif choice == "3":
            break
        else:
            print("Invalid choice")

# Main Function
if __name__ == "__main__":
    main()