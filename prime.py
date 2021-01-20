import sys
import time

user_time = 0                                                                   #must be here so it can be called and used everywhere if needed

def start_counting_timed():
    """counting all the primes with a timer"""

    global user_time                                                            #allow thing outside "start_counting" to be called and edited

    start = 2                                                                   #resets all the "scores" to make sure it starts well
    division = 1
    is_divided = 0
    prime_num = []

    number = int(sys.maxsize)                                                   #insert the biggest number it can so it doesnt stop bcs he reached it

    timer_start = time.time()                                                   #starts the timer
    timer_stop = timer_start + user_time                                        #gives the limit given by user

    while start < number:                                                       #starts making the list
        if start % 2 == 0 and start > 2:                                        #if the number is even it is skipped to the next one
            #print("{} is even, then we skip.".format(start))
            start += 1

        while is_divided < 3 and division <= start ** (1/2):                    #each number is checked as prime here
            if start % division == 0:
                #print("{} % {} == 0".format(start, division))
                is_divided += 1
                division += 2
            else:
                #print("{} % {} != 0".format(start, division))
                division += 2

        print("finished {}.".format(start))                                     #shows what number ended

        if is_divided < 2:                                                      #if it is prime then it keeps the number
            #print("{} is prime.".format(start))
            prime_num.append(start)
            start += 1
            division = 1
            is_divided = 0
        else:                                                                   #it continues
            start += 1
            division = 1
            is_divided = 0

        timer_lap = time.time()

        if timer_lap > timer_stop:                                              #stops the counting when time limit is reached
            print("Time limit reached.")
            break

    timer_end = time.time()                                                     #ends the timer

    print("List of primes: ")                                                   #shows the list
    print(" ".join(map(str, prime_num)))
    print(119 * "-")

    print("There are {} primes that are smaller than {}.".format(len(prime_num), start))
    print("Last prime number: ", prime_num[-1])

    print("Elapsed time: {}".format(timer_end - timer_start))                   #shows the time it took
    print(119 * "-")


def start_counting():
    """counting all the primes"""

    start = 2
    division = 1
    is_divided = 0
    prime_num = []

    number = int(input("Till what number you wish to see the primes? "))

    timer_start = time.time()                                                   #starts the timer

    while start < number:                                                       #making the list
        if start % 2 == 0 and start > 2:                                        #if the number is even it is skipped to the next one
            print("{} is even, then we skip.".format(start))
            start += 1

        while is_divided < 3 and division <= start ** (1/2):                    #each number is checked if prime here
            if start % division == 0:
                print("{} % {} == 0".format(start, division))
                is_divided += 1
                division += 2
            else:
                print("{} % {} != 0".format(start, division))
                division += 2

        print("finished {}.".format(start))                                     #shows the number it finished checking

        if is_divided < 2:                                                      #is prime
            print("{} is prime.".format(start))
            prime_num.append(start)
            start += 1
            division = 1
            is_divided = 0
        else:                                                                   #isnt prime
            start += 1
            division = 1
            is_divided = 0
    
    timer_end = time.time()                                                     #ends the timer

    print("List of primes: ")                                                   #shows the list
    print(" ".join(map(str, prime_num)))
    print(119 * "-")

    print("There are {} primes that are smaller than {}.".format(len(prime_num), number))

    print("Elapsed time: {}".format(timer_end - timer_start))                   #shows us the time it took
    print(119 * "-")

def play_game():
    """main menu for the player"""

    global user_time                                                            #allow thing outside "play_game" to be called and edited

    n = input("Program mode(time|number/num): ")
    _input = n.upper()                                                          #the "_" at the beggining is used to make sure it wont collide with input or any other function

    if _input == "TIME":                                                        #counts untill it reaches the time limit
        user_time = int(input("Time in seconds: "))
        start_counting_timed()
        play_game()
    elif _input == "NUMBER" or _input == "NUM":                                 #counts the list - doesnt care about timer
        print("Biggest number you can give is: {}".format(sys.maxsize))         #shows the limit from the system
        start_counting()
        play_game()
    else:                                                                       #ends the program
        print("Game over.")
        input()

print("Keep in mind that the program is showing all the calculations, which means it is slower than without them.")
print("You can turn them off by adding '#' in front of some prints. Just make sure you keep the ona that shows you the list.")
print(119 * "-")
print("informations: ")
print("The program has 2 modes")
print("1) For a given time by the user.(time)")
print("2) Untill it reaches the number the user gave.(number/num)")
print("The 'time' mod has a bit less prints to make it faster. Better for performance tests I guess.")
print("To end the program just write anything else than time or number/num.")
print(119 * "-")
play_game()
