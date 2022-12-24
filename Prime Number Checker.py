n = int(input('Write a number: \n'))


def prime_checker(number=n):
    count = 0
    for i in range(1, number):
        if number % i == 0:
            count += 1
    if count > 2:
        print('Not prime')
    else:
        print('Prime')


prime_checker()
