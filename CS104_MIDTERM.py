# 1

print(2 * -5 + 4 * 3 + 8 * -5)
print(24 % 5 + 32.0 / 4 % 3 - 15 % (16 % 9))
print(str(int("1") + 2 + 3) + "4" + str(5 * 6) + "7")
print(3.0 * 4 / int(len("al")) + 5 % 4 + int(4.5 * -2.0))


# 2

def mystery(my_text):
    y = 0
    new_text = ""
    for o in range(my_text):
        if o == 1:
            y += 1
        if o >= 8:
            break
        else:
            new_text = new_text + str(o)
    y += 1
    print(y)
    return new_text


text = input("hello, hi, CS 104 is fun, or bye: ")
if len(text) > 4:
    output = mystery(len(text))
    print(output)
elif text == "hello":
    print("hi")
elif text == "hey":
    print("Hey you!")

# 3


nr = int(input("Enter the number of quizzes: "))


def calculate_grades(num_of_quizzes):
    grades = 0
    minimum = 100
    print("Enter the grades:")
    for f in range(num_of_quizzes):
        grade = int(input())
        grades += grade
        if grade < minimum:
            minimum = grade
    print("Minimum grade:", minimum)
    return grades / num_of_quizzes


print("Average:", calculate_grades(nr))

# 4

today = int(input('Enter index of today [0,6]: '))
N = int(input('Enter N: '))
N_Days_Later = (today + N) % 7

if N_Days_Later == 0:
    print(f'{N} days later is Monday')
elif N_Days_Later == 1:
    print(f'{N} days later is Tuesday')
elif N_Days_Later == 2:
    print(f'{N} days later is Wednesday')
elif N_Days_Later == 3:
    print(f'{N} days later is Thursday')
elif N_Days_Later == 4:
    print(f'{N} days later is Friday')
elif N_Days_Later == 5:
    print(f'{N} days later is Saturday')
elif N_Days_Later == 6:
    print(f'{N} days later is Sunday')


# 5


m = int(input('Enter M: '))
output = ''
for i in range(0, m):
    output = ''
    if i == int(m / 2):
        for j in range(0, m):
            output += '*'
        print(output)
    else:
        output = '*'
        for j in range(0, m - 2):
            output += '-'
        output += '*'
        print(output)
