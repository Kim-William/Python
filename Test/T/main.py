# import another_module

# print(another_module.another_variable)

# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)

# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(300)
# timmy.right(180)
# timmy.forward(600)
# timmy.right(180)
# timmy.forward(300)

# my_screen = Screen()
# print(my_screen.canvheight)

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])
# table.add_row(table._format_row())
print(table)