import sys
import time

print("Biggest number you can give is: {}".format(sys.maxsize))             #shows the limit from the system

start = 2
division = 1
is_divided = 0
prime_num = []

number = int(input("Till what number you wish to see the primes? "))

begin = time.time()                                                         #starts the timer

while start < number:
    if start % 2 == 0 and start > 2:                                        #optimize a bit
        print("number {} is even, then we skip.".format(start))
        start +=1
    while is_divided < 3 and division <= start ** (1/2):                    #checks if it is % 0 and if it is more than 2 times it goes to the next number
        if start % division == 0:                                           # if exactly 2 times then it append the number to the list
            print("{} % {} == 0".format(start, division))                   #new optimisation - no need to go untill the last number x ** (1/2) is enough
            is_divided += 1                                                 #just had to change how many is_divided are needed to be a prime
            division += 2
        else:
            print("{} % {} != 0".format(start, division))
            division += 2

    print("finished {}.".format(start))

    if is_divided < 2:                                                      #number is prime after divisions and hop to the next number
        print("{} is prime.".format(start))
        prime_num.append(start)
        start += 1
        division = 1
        is_divided = 0
    elif is_divided >= 2 and start < number:                                #number isnt prime and can continue
        start += 1
        division = 1
        is_divided = 0

print(" ".join(map(str, prime_num)))

end = time.time()                                                           #stop the timer
print("Elapsed time: {}".format(end - begin))                               #show the timer result
input()
