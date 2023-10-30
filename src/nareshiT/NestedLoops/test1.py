# WAP to generate the tables from 250 to 253

# for i in range(999, 990, -1):
#     for j in range(10, 0, -1):
#         product = i * j
#         # print(f'{i} * {j} = {product}')


# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i, end= ' ')
#     print()

# for i in range(5, 0, -1):
#     for j in range(1, 6):
#         print(i, end= ' ')
#     print()

# for i in range(1, 6):
#     for j in range(5, 0, -1):
#         print(j, end= ' ')
#     print()

'''
1
2 2
3 3 3
4 4 4 4 
5 5 5 5 5
'''

# for row in range(1, 6):
#     for coloumn in range(1, row+1):
#         print(row, end= ' ')
#     print()

for row in range(5, 0, -1):
    for coloumn in range(5-row+1, 0, -1):
        print(row, end=' ')
    print()
