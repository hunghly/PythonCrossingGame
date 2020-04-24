# # input_name = input('Enter a name: ')
#
# # output_text = 'Hello ' + input_name
#
# # print(output_text)
#
# print(1 + 1)
#
# name = 'hung'
# number = 1
# number2 = 2.2
# nothing = None
# condition = False
#
# if name: print('yes')
#
# print(type(name))
# print(type(number))
# print(type(number2))
# print(type(nothing))
# print(type(condition))
# condition_is_not = not condition # not operator is used to get the opposite condition
# say_hi = 'Hi ' + name
# print(condition_is_not)
# print(say_hi)
#
# num = 12
# floor_num = num // 10 # using // will floor the resulting number
# square_num = num ** 2 # use ** to square
# print(floor_num)
# print(square_num)
# fivestr = '5'
# fivenum = 5
#
# print(fivestr == fivenum)
# print(fivenum)
#
# #dictionary
#
# width = 10
# height = 20
#
# # redefine it as a tuple to size which has 100 width and 200 height
# size = (100, 200)
# width = size[0]
# height = size[1]
# new_size = size + (300, )
# print(size)
# print(width)
# print(height)
# print(new_size)
# print(len(size))
# print(max(size))
# print(min(size))
# does_contain = 100 in size
# print(does_contain)
#
# movement = [5, -2, -3, -3, 4, -1]
# print('-------------------------------------')
# print(movement)
# print(movement[0])
# movement[0] = 8
# print(movement[0])
# movement.append(-5)
# print(movement)
# movement.remove(-3) # removes only the first element
# print(movement)
#
# starting_position = {
#     'p_0': 50,
#     'p_1': 100,
#     'p_2': 150
# }
# print(starting_position['p_0'])
# print(starting_position.keys())
#
# print('------------Control Flow-------------')
# # if condition:
# #     code to execute if condition is true
# # is_game_over = False
# # p_0_x_pos = 0
# # e_0_x_pos = 3
# # e_1_x_pos = 5
# #
# # p_0_x_pos += 2
# # if p_0_x_pos == e_0_x_pos:
# #     print('you hit the enemy')
# #     is_game_over = True
# # elif p_0_x_pos == e_1_x_pos:
# #     print('you hit enemy2')
# #     is_game_over = True
# # else:
# #     e_0_x_pos += 1
# #     e_1_x_pos += 1
# # print(is_game_over)
#
# # if p_0_x_pos == e_0_x_pos or p_0_x_pos == e_1_x_pos:
# #     print('you hit the enemy')
# #     is_game_over = True
# # else:
# #     e_0_x_pos += 1
# #     e_1_x_pos += 1
#
# print('------------LOOPS------------')
# # while loops
# # for in loops
# index = 0
# # while not is_game_over:
# #     print(index)
# #     index += 1
# #     if index == 10:
# #         is_game_over = True
# #
# is_game_over = False
# p_x_pos = 2
# e_x_pos = 3
# end_x_pos = 10
#
# while not is_game_over:
#     print(p_x_pos)
#     print(e_x_pos)
#     if p_x_pos == e_x_pos:
#         print('you lose!')
#         is_game_over = True
#     elif p_x_pos >= end_x_pos:
#         print('you win!')
#         is_game_over = True
#     else:
#         p_x_pos += 3
#         e_x_pos += 1
#
# x_pos = 5
# movements = [1, -2, 6, -3, -2, 4]
# # similar to for each loop
# for movement in movements:
#     x_pos+= movement
#     print(x_pos)
#
# books = ['stephen king''s it', 'seven effective habits']
#
# for book in books:
#     print(book)
#
# index = 0
# while index < 10:
#     print(index)
#     index += 1

# print('---------------Functions--------------')
# x_pos = 0
# e_x_pos = 4
# print(x_pos)
#
#
# def check_for_collision():
#     global x_pos
#     global e_x_pos
#     if x_pos == e_x_pos:
#         return True
#     else:
#         return False
#
#
# def move():
#     global x_pos
#     x_pos += 1
#
#
# def move_by(amount):
#     global x_pos  # retrieves the global variable
#     x_pos += amount
#
#
# move_by(4)
# did_collide = check_for_collision()
#
# print(did_collide)

# print('--------Objects--------')
#
#


class GameCharacter:
    speed = 5

    def __init__(self, name, width, height, x_pos, y_pos):
        self.name = name
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, by_x_amount, by_y_amount):
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount


#
#
# character_0 = GameCharacter('hung', 50, 100, 100, 100)
# print(character_0.name)
# character_0.name = 'joe'
# print(character_0.name)
#
# character_0.move(50, 100)
# print(character_0.x_pos)
# print(character_0.y_pos)

print('------subclasses, superclasses, inheritance------')


# subclasses inherit from superclass and gets access to fields and methods from superclasses

class PlayerCharacter(GameCharacter):

    speed = 10

    def __init__(self, name, x_pos, y_pos):
        super().__init__(name, 100, 100, x_pos, y_pos)

    def move(self, by_y_amount):
        super().move(0, by_y_amount)


player_character = PlayerCharacter('P_character', 500, 500)

print(player_character.name)
player_character.move(100)
print(player_character.x_pos)
print(player_character.y_pos)