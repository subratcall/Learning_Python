# Input: A map as a list of lists with 1 or 0.
# Output: The sizes of island as a list of integers.

def checkio(land_map):
    return [1]



# if __name__ == '__main__':
#     assert checkio([[0, 0, 0, 0, 0],
#                     [0, 0, 1, 1, 0],
#                     [0, 0, 0, 1, 0],
#                     [0, 1, 0, 0, 0],
#                     [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
#     assert checkio([[0, 0, 0, 0, 0],
#                     [0, 0, 1, 1, 0],
#                     [0, 0, 0, 1, 0],
#                     [0, 1, 1, 0, 0]]) == [5], "2nd example"
#     assert checkio([[0, 0, 0, 0, 0, 0],
#                     [1, 0, 0, 1, 1, 1],
#                     [1, 0, 0, 0, 0, 0],
#                     [0, 0, 1, 1, 1, 0],
#                     [0, 0, 0, 0, 0, 0],
#                     [0, 1, 1, 1, 1, 0],
#                     [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
#     print('done')


land_map = ([[1, 0, 0, 0, 0],
             [0, 0, 1, 0, 1],
             [0, 0, 1, 0, 1],
             [0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0]])

temp_list = []
for i in range(len(land_map)):
    for x in range(len(land_map)):
        if land_map[i][x] == 1:
            collect = int(str(i) + str(x))
            temp_list.append(collect)
print(temp_list)

final = []
temp = []
def neighbor(x):
    candi = [x]
    for i in candi:
        up, down, left, right = i-10, i+10, i-1, i+1
        for neighbor in [up, down, left, right]:
            if neighbor not in temp and neighbor in temp_list:
                temp.append(neighbor)
                candi.append(neighbor)









# print(checkio(land_map))


