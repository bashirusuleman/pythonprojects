

def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')
    print("Please enter your name ")


def remind_name():
    print('Please, remind me your name.')    
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    print("Enter remainder when divided by 3")
    rem3 = int(input("> "))
    print("Enter remainder when divided by 5")
    rem5 = int(input("> "))
    print("Enter remainder when divided by 7")
    rem7 = int(input("> "))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print("How do you declare a function in python?")
    print("1. def.")
    print("2. var.")
    print("3. class.")
    print("4. return.")
    options = ['1','2','3','4']
    answer = " "
    while answer  != options[0]:
        answer = input()
        if answer == options[0]:
            print('Completed, have a nice day!')
            break
        else:
            print('Please, try again.')
            
               
    print('Completed, have a nice day!')


def end():
    print(f'Congratulations {name}, have a nice day!')


greet('Aid', '2020')  
name = input("> ")
remind_name()
guess_age()
count()
test()
end()

