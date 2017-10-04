def run():
    number = int(input('Input a number: '))
    result = is_prime(number)
    if result is True:
        print('Your number is prime')
    else:
        print('Your number not is prime')

def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3,number):
            if number % i == 0:
                return False

    return True

if __name__ == '__main__':
    run()
