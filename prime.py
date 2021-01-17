import sys
import time

print("Biggest number you can give is: {}".format(sys.maxsize))

start = 2
division = 1
is_divided = 0
prime_num = [1]

number = int(input("Till what number you wish to see the primes? "))

begin = time.time()

while start < number:
    if start % 2 == 0 and start > 2:                                        #optimize a bit
        print("number {} is even, then we skip.".format(start))
        start +=1
    while is_divided < 3 and division <= start:
        if start % division == 0:
            print("{} % {} == 0".format(start, division))
            is_divided += 1
            division += 2
        else:
            print("{} % {} != 0".format(start, division))
            division += 2

    print("finished {}.".format(start))

    if is_divided < 3:                                                      #number is prime after divisions and hop to the next number
        print("{} is prime.".format(start))
        prime_num.append(start)
        start += 1
        division = 1
        is_divided = 0
    elif is_divided >= 3 and start < number:                                #number isnt prime and can continue
        print("{} isnt prime.".format(start))
        start += 1
        division = 1
        is_divided = 0

print(" ".join(map(str, prime_num)))

end = time.time()
print(end - begin)