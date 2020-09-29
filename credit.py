from random import randint

### main functions
def main():
    option = ""

    # loop options until 'quit'
    while option != 4:
        # get option from user
        option = get_option()

        # run option
        run(option)

def run(option):
    run_options = {
    '1' : check_card, '2' : import_cards, '3' : generate_random_CCs, '4' : quit
    }
    print()
    run_options[option]()

def check_card():
    # get CC from user
    card = get_card()

    # check if CC is valid
    if luhn_algorithm(card):
        print("Valid CC\n")
    else:
        print("Invalid CC\n")

def import_cards():
    # get file name from user and open file
    file = get_file()

    # line by line, check if card is valid
    for card in file:
        valid = check_card_format(card)
        valid = luhn_algorithm(card) if valid else valid

        # print if card is valid
        print("Credit Card: {}".format(card))
        print("CC Validation: {}\n".format(valid))

def generate_random_CCs():
    # get number of CC user wants to generate
    num_of_CC = get_num_of_CCs()

    # generate CCs
    CCs = []
    while len(CCs) < int(num_of_CC):
        new_CC = generate_CC()
        if new_CC not in CCs:
            CCs.append(new_CC)

    # print genereated CCs
    for i in range(len(CCs)):
        print("Card {}: {}".format(i + 1, CCs[i]))

    # write CCs to file
    with open("CCs.txt", 'w') as file:
        file.write('\n'.join(CCs))
    print()

### get functions
def get_option():
    while True:
        # get option from user
        option = input("1. Check my card\n2. Import numbers to check\
        \n3. Generate a valid CC number\n4. Quit\nOption: ")

        # check if option is valid
        if check_num(option, 1, 4):
            break
        else:
            print("Type in option between 1 and 4\n")

    # return option to main function
    return option

def get_card():
    card = ""

    # get CC number from user - ensure card is of right format
    while not check_card_format(card):
        card = input("Credit Card Number: ")

    return card

def get_file():
    while True:
        try:
            # get file name from user
            fname = input("Filename: ")

            # try open file
            with open(fname + '.txt') as file:
                file = file.read().split('\n')
            break

        except:
            print("Enter Valid Filename\n")

    return file

def get_num_of_CCs():
    while True:
        # get number of CCs to generate from user
        num_of_CC = input("Number of CC: ")

        # check if value entered is valid
        if check_num(num_of_CC, 1, 100):
            break
        else:
            print("Invalid: Type in Number between 1 and 100\n")

    return num_of_CC


### calculate functions
def mult_and_add(n):
    n *= 2
    return n // 10 + n % 10

def calc_sum(card):
    sum1 = sum(card[::-2])
    sum2 = sum(map(mult_and_add, card[::2]))
    return sum1 + sum2

def luhn_algorithm(card):
    # convert all elements in card to integer
    card = [int(n) for n in card]

    # calculate sum using luhns algorithm
    sum = calc_sum(card)

    # return true if card is valid else false
    return sum % 10 == 0

def generate_CC():
    # generate 15 digits randomly of new CC
    card = [randint(1,9) if x != 15 else 0 for x in range(16)]

    # check if the CC is valid
    sum = calc_sum(card)
    if sum % 10 != 0:
        # if CC is not valid
        card[-1] = 10 - sum % 10

    # return CC as string
    return "".join(str(x) for x in card)

def load_CC_file(CCs):
    # open and write to file new CCs
    with open("CCs.txt", "w") as file:
        file.write('\n'.join(CCs))

### check functions
def check_num(n, lb, ub):
    # check if all chars are digits
    if not n.isdigit():
        return False

    # check lower bound <= number <= upper bound
    return lb <= int(n) <= ub

def check_card_format(card):
    # check if CC is of length 16
    if len(card) != 16:
        return False

    # check if all values are digits
    if not [x for x in card if x.isdigit()]:
        return False

    return True

if __name__ == "__main__":
    main()
