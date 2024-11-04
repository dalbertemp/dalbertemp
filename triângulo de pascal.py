from math import factorial


# returns the row described in the argument
def pascal_triangle(line):
    line += 1
    row = []
    for x in range(line):
        row.append(factorial(line-1)//(factorial(x)*factorial(line-1-x)))
    return row

rows = int(input("How many rows do you want?"))

file = open('pascal_triangle.txt', 'w')

for a in range(rows):

    spaces = (len(str(pascal_triangle(rows-1))) - len(str(pascal_triangle(a))))//2

    print(' ' * spaces + str(pascal_triangle(a)))
    file.write(' '*spaces+str(pascal_triangle(a))+'\n')

file.close()


