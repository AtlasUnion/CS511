from z3 import *
import imp

data = []

with open(sys.argv[1], 'r') as f:
    data = imp.load_source('data', sys.argv[1])

s = Solver()

for i in range(1,len(data.w)+1):
    variable_name = "x" + str(i)
    neg_variable_name = "_x" + str(i)
    s.add(Or(Int(variable_name) == 0, Int(variable_name) == 1))
    s.add(Or(Int(neg_variable_name) == 0, Int(neg_variable_name) == 1))
    s.add(Int(neg_variable_name) + Int(variable_name) == 1)

objective_list = []

for i in range(len(data.c)):
    for j in range(len(data.c)):
        objective_list.append(data.c[i][j] * ( Int("x"+str(i+1))*Int("_x"+str(j+1)) + Int("_x"+str(i+1))*Int("x"+str(j+1)) ))

objective = Int("objective")
s.add(objective == Sum(objective_list))

# print(type(data.c[0][0]))

if s.check == unsat:
    print("Unsat")
    quit()

model = ""

while s.check() == sat:
    model = s.model()
    s.add(objective > model[objective])
print(model)