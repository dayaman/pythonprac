def fizzbuzz(num):
    # return num
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)

def main():

    fbs = []
    
    for num in range(1, 101):
        fbs.append(fizzbuzz(num))
        print(fizzbuzz(num))

    print('Fizz:', fbs.count('Fizz'))
    
    print('Buzz:', fbs.count('Buzz'))
    
    print('FizzBuzz', fbs.count('FizzBuzz'))

    
if __name__ == '__main__':
    main()



