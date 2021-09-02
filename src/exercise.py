def main():
    #write your code below this line
    last = int(input("Last number?"))
    sum = 0
    for i in range(1, last + 1):
        sum += i
    print("The sum is " + str(sum))

if __name__ == '__main__':
    main()
