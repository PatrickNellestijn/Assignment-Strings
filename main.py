# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#Printing text and variables;
#Casting types to other types;
#Using and manipulating strings.
# UEFA Euro 1988 final part 1
scorer_name_1 = 'Ruud Gullit'
scorer_name_2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = (scorer_name_1) + ' ' + str(goal_0) + ', ' + (scorer_name_2) + ' ' + str(goal_1)
print(scorers)
report = f'{scorer_name_1} scored in the {goal_0}nd minute' + '\n' f'{scorer_name_2} scored in the {goal_1}th minute'
print(report)

# UEFA Euro 1988 final part 2
player = 'Marco van Basten'
index = player.find(' ')
print(player[index])
first_name = player[0:index]
print(first_name)
last_name = player[index+1:]
last_name_len = len(last_name)
name_short = ((first_name[0]) + '.' + ' ' + (last_name))
print(name_short)
chant = (f"{first_name}! " * len(first_name))[:-1]
print(chant)
good_chant = first_name [-1] != " "
print(good_chant)
