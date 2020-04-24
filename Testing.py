# input_name = input('Enter a name: ')

# output_text = 'Hello ' + input_name

# print(output_text)

print(1 + 1)

name = 'hung'
number = 1
number2 = 2.2
nothing = None
condition = False

if name: print('yes')

print(type(name))
print(type(number))
print(type(number2))
print(type(nothing))
print(type(condition))
condition_is_not = not condition # not operator is used to get the opposite condition
say_hi = 'Hi ' + name
print(condition_is_not)
print(say_hi)

num = 12
floor_num = num // 10 # using // will floor the resulting number
square_num = num ** 2 # use ** to square
print(floor_num)
print(square_num)
fivestr = '5'
fivenum = 5

print(fivestr == fivenum)
print(fivenum)

#dictionary

width = 10
height = 20

# redefine it as a tuple to size which has 100 width and 200 height
size = (100, 200)
width = size[0]
height = size[1]
new_size = size + (300, )
print(size)
print(width)
print(height)
print(new_size)
print(len(size))
print(max(size))
print(min(size))
does_contain = 100 in size
print(does_contain)

movement = [5, -2, -3, -3, 4, -1]
print('-------------------------------------')
print(movement)
print(movement[0])
movement[0] = 8
print(movement[0])
movement.append(-5)
print(movement)
movement.remove(-3) # removes only the first element
print(movement)

starting_position = {
    'p_0': 50,
    'p_1': 100,
    'p_2': 150
}
print(starting_position['p_0'])
print(starting_position.keys())

print('------------Control Flow-------------')
# if condition:
#     code to execute if condition is true
# is_game_over = False
# p_0_x_pos = 0
# e_0_x_pos = 3
# e_1_x_pos = 5
#
# p_0_x_pos += 2
# if p_0_x_pos == e_0_x_pos:
#     print('you hit the enemy')
#     is_game_over = True
# elif p_0_x_pos == e_1_x_pos:
#     print('you hit enemy2')
#     is_game_over = True
# else:
#     e_0_x_pos += 1
#     e_1_x_pos += 1
# print(is_game_over)

# if p_0_x_pos == e_0_x_pos or p_0_x_pos == e_1_x_pos:
#     print('you hit the enemy')
#     is_game_over = True
# else:
#     e_0_x_pos += 1
#     e_1_x_pos += 1

print('------------LOOPS------------')
# while loops
# for in loops
index = 0
# while not is_game_over:
#     print(index)
#     index += 1
#     if index == 10:
#         is_game_over = True
#
is_game_over = False
p_x_pos = 2
e_x_pos = 3
end_x_pos = 10

while not is_game_over:
    print(p_x_pos)
    print(e_x_pos)
    if p_x_pos == e_x_pos:
        print('you lose!')
        is_game_over = True
    elif p_x_pos >= end_x_pos:
        print('you win!')
        is_game_over = True
    else:
        p_x_pos += 3
        e_x_pos += 1

x_pos = 5
movements = [1, -2, 6, -3, -2, 4]
# similar to for each loop
for movement in movements:
    x_pos+= movement
    print(x_pos)

books = ['stephen king''s it', 'seven effective habits']

for book in books:
    print(book)
