"""
Email validation in python using String Function
"""
user_input = input("Enter Your Email : ")

if user_input.strip() != "" and len(user_input) >= 6:
    if user_input[0].isalpha():
        if ("@" in user_input) and (user_input.count('@') == 1):
            if user_input[-4] == '.' ^ user_input[-3] == '.':
                pass
            else:
                print('Enter a valid email 4')
        else:
            print('Enter a valid email 3')
    else:
        print('Enter a valid email 2')
    print(user_input)
else:
    print('Enter a valid email 1')
