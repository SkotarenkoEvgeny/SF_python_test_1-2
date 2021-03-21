"""
A bank has implemented criteria for determining whether the transaction passwords typed by customers of the bank are valid or not.

The following are the criteria for checking the transaction password:

1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [*#+@]
5. Minimum length of transaction password: 4
6. Maximum length of transaction password: 6
7. No space is allowed

Write a program that will accept a sequence of comma-separated transaction passwords and
will check them according to the bank's criteria. Passwords that match the criteria
are to be printed, each separated by a comma.

Example

If the following passwords are given as input to the program:

Abc@1,a B1#,2w3E*,2We#3345

Then, the output of the program should be:

Abc@1,2w3E*

Note: You should assume that input to the program is from console input (raw_input)


"""

import re


test_string = input('Input a string ')

test_list = test_string.split(',')
rez_list = []

for item in range(len(test_list)):
    temp = re.search(r'^[a-zA-z0-9*#+@]+$', test_list[item])
    item_length = len(test_list[item])
    if item_length >= 4 and item_length <= 6 and temp is not None:
        rez_list.append(test_list[item])

print(','.join(rez_list))
