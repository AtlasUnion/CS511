from z3 import *

in_a = 0
m = 0
in_b = 0
n = 0

Lines = []
variable_list = []
And_list = []

with open('./test', 'r') as fp:
    Lines = fp.readlines()
    if len(Lines) != 4:
        print("Wrong number of lines")
        exit()

for line in Lines:
    splited_line = line.split(' ')
    if len(splited_line) != 2:
        print("Wrong number of line input")
        exit()
    if (splited_line[0] == "in_a"):
        in_a = int(splited_line[1])
        variable_list.append(Int('in_a'))
    elif (splited_line[0] == "m"):
        m = int(splited_line[1])
    elif (splited_line[0] == "in_b"):
        in_b = int(splited_line[1])
        variable_list.append(Int('in_b'))
    elif (splited_line[0] == "n"):
        n = int(splited_line[1])
    else:
        print("Unrecongized input name")
        exit()


ina_value = (variable_list[0] == in_a)
inb_value = (variable_list[1] == in_b)
And_list.append(ina_value)
And_list.append(inb_value)

for i in range(m+1):
    number = str(i)
    name = "outa_" + number
    variable_list.append(Int(name))
for i in range(n+1):
    number = str(i)
    name = "outb_" + number
    variable_list.append(Int(name))

for i in range(m+1):
    if i == 0:
        And_list.append((variable_list[1+i+1] == variable_list[0]))
    else:
        And_list.append((variable_list[1+i+1] == (variable_list[1+i] * variable_list[0])))

for i in range(n+1):
    if i == 0:
        And_list.append((variable_list[1+m+2+i] == variable_list[1]))
    else:
        And_list.append((variable_list[1+m+2+i] == (variable_list[1+m+1+i] * variable_list[1+m+1+i])))

s = Solver()
implies_a = And(And_list)
implies_b = (variable_list[1+m+1] == variable_list[1+m+1+n+1])
final_imply = ForAll(variable_list, Implies(implies_a, implies_b))
s.add(Not(final_imply))
result = str(s.check())

if result == "unsat":
    print(True)
else:
    print(False)