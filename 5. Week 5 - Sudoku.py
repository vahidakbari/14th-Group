import turtle
import random
turtle.speed(0)
turtle.pensize(1)
# turtle.hideturtle()                            # turn it back on later
# Change Initial Position
turtle.penup()
turtle.goto(-150, 150)
turtle.pendown()
# Small Squares - pensize 1
for row in range(9):
    for col in range(9):
        for cube in range(4):
            turtle.forward(50)
            turtle.right(90)
        turtle.forward(50)
    turtle.backward(450)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
turtle.goto(-150, 150)
turtle.pensize(3)
# Inner Squares - pensize 3
for row in range(3):
    for col in range(3):
        for cube in range(4):
            turtle.forward(150)
            turtle.right(90)
        turtle.forward(150)
    turtle.backward(450)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
turtle.pensize(5)
# Outer Square - pensize 5
for i in range(4):
    turtle.forward(450)
    turtle.left(90)
# Filling the table
temp_col = list()
row_dic = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
teil_dict = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
row_num = 0
column_num = 1
teil_num = 1
# for x in range(-125, 300, 50):
#     for y in range(-290, 150, 50):
#         turtle.penup()
#         turtle.setpos(x, y)
#         turtle.pendown()
#         row_num += 1
#         while True:
#             temp_num = random.randint(1, 9)
#             if temp_num not in teil_dict[teil_num]:
#                 if temp_num not in temp_col:
#                     if temp_num not in row_dic[row_num]:
#                         turtle.write(temp_num, move=False, align='center', font=('Arial', 20, 'normal'))
#                         temp_col.append(temp_num)
#                         row_dic[row_num].append(temp_num)
#                         teil_dict[teil_num].append(temp_num)
#                         break
#                     else:
#                         continue
#                 else:
#                     continue
#             else:
#                 continue
#         if row_num in [3, 6]:
#             teil_num += 1
#         else:
#             continue
#         # print(f'Row # {row_num}, Column # {column_num}, Teil # {teil_num}')
#     if 2 < column_num < 6:
#         teil_num = 4
#     elif column_num >= 6:
#         teil_num = 7
#     else:
#         teil_num = 1
#     # print('Current Teil: ', teil_num)
#     # print('temp col is: ', temp_col)
#     # print('Row dic is:', row_dic)
#     # print('Teil dic is: ', teil_dict)
#     # print('='*100)
#     temp_col.clear()
#     row_num = 0
#     column_num += 1
turtle.done()
