"""
Write a program that takes 4 inputs, where each input consists of 2 numbers in the format x,y.
You are required to print a two-dimensional array having x rows and y columns for each input.
The elements of the arrays should be whole numbers starting from 1 and incrementing by 1.

Example

Suppose the following 4 inputs are given to the program:

2,2
2,3
3,3
3,4

Then, the output of the program should be:

[[1, 2], [3, 4]]
[[1, 2, 3], [4, 5, 6]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

Note: You should assume that input to the program is from console input (raw_input)
"""

step = 4


def matrix_generator(rows, columns):
    """
    matrix_generator(rows, columns)
    to generate matrix with size rows and columns
    """
    count = 1
    temp_value = columns
    rez_list = []
    raw_list = []

    while count < rows * columns:
        while count <= temp_value:
            raw_list.append(count)
            count += 1
        rez_list.append(raw_list)
        raw_list = []
        temp_value += columns

    return rez_list


print("Input a 4 size of matrix like 2,2 (rows,columns)")

while step != 0:
    raw_matrix_size = list(input())
    if len(raw_matrix_size) != 3:
        print('Not correct length of matrix size. Input a size 10,10 for example')
        continue
    if not raw_matrix_size[0].isdigit() and raw_matrix_size[-1].isdigit():
        print('insert a digit value for rows or columns')
        continue

    print(matrix_generator(int(raw_matrix_size[0]), int(raw_matrix_size[-1])))
    step -= 1
