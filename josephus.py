#   PRINT inTRO
#   soldiers variable stands for the x amount of soldiers


def start():
    global lists
    global soldiers
    soldiers = input("Enter the number of soldiers:")

    try:
        # backdoor to check all the possible outcomes
        if soldiers == "list":
            lists = input("Enter the number of soldiers, which will loop to:")
            # loop trough the numbers till a certain point
            lists = int(lists)
            if lists > 1500:
                print("Sorry, please don't use the backdoor for numbers above 1500!")
                start()
            number = 1
            listing(lists, number)
        soldiers = int(soldiers)
        if soldiers == 0:
            print("There must be at least 1 soldier in group for josephus to be calculated")
            start()
    except ValueError:
        print("Please use whole numeric values!")
        #   return to start to instead of exit()
        start()
    refine()


def refine():
    if (soldiers & (soldiers - 1)) == 0 or soldiers % 2 == 0:
        print("the soldier who dies at last is soldier: #1")
        #   all scenarios with powers of 2 will end with #1 as the winner, this is a basic rule of the game
        start()
    count = 1
    #   highest power of 2
    while (2 ** count) < soldiers:
        count += 1
    else:
        count -= 1
        power = 2 ** count
        remainder = soldiers - power
        #   print("count: " + str(count) + " soldiers: " + str(soldiers) + " biggest power of two: " + str(power))
        if remainder <= power:
            josephus = 2 * remainder + 1
            print("the soldier who dies at last is soldier: #" + str(josephus))
            start()
        else:
            print("error: number not found, please try again")
            start()


def listing(lists, number):
    # print(str(lists) + " - " + str(number))
    while lists > number:
        if (number & (number - 1)) == 0 or number % 2 == 0:
            print("total soldiers: #" + str(number) + " | last man: 1")
            #   all scenarios with powers of 2 will end with #1 as the winner, this is a basic rule of the game
            number += 1
            listing(lists, number)
        count = 1
        #  highest power of 2
        while (2 ** count) < number:
            count += 1
        else:
            count -= 1
            power = 2 ** count
            remainder = number - power
            #   print("count: " + str(count) + " number: " + str(number) + " biggest power of two: " + str(power))
            if remainder <= power:
                josephus = 2 * remainder + 1
                print("total soldiers: #" + str(number) + " | last man: " + str(josephus))
                number += 1
            else:
                print("error: number not found")
                number += 1
                listing(lists, number)

    start()


start()
refine()
