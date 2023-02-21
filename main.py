def main():
    ##################################################
    # Comlete your code here
    ##################################################

    var1 = int(input('Enter your first number'))
    var2 = int(input('Enter your second number '))
    var3 = int(input('Enter your third number '))

    total = var1 + var2 + var3
    print(f'The summation is {total:>20}')

    avg = total / 3
    print(f'The summation is {avg:.2f}')


if __name__ == '__main__':
    main()
