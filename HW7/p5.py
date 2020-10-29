from z3 import *
import ast

encoded_list = []

variable_num_list = []
variable_list = []
Condition_list = []

if (len(sys.argv) != 2):
    print("Wrong number of arguments")
    exit(-1)

with open(sys.argv[1], 'r') as f:
    encoded_list = ast.literal_eval(f.read())


# Get all variables needed from objective function
for i in encoded_list[0]:
    for j in i[1]:
        if ((j[1] in variable_num_list) == False):
            variable_num_list.append(j[1])
            variable_number = str(j[1])
            variable_name = "x" + variable_number
            negate_variable_name = "_x" + variable_number
            variable_list.append(Int(variable_name))
            variable_list.append(Int(negate_variable_name))
            Condition_list.append(Int(variable_name) >= 0)
            Condition_list.append(Int(variable_name) <= 1)
            Condition_list.append(Int(negate_variable_name) + Int(variable_name) == 1)

for i in encoded_list:
    if (encoded_list.index(i) == 0):
        continue
    j_line_sum_cond = []
    for j in i:
        if (len(j[1]) > 1): # case of *
            j_1_product = []
            for z in j[1]:
                if (z[0] == 0):
                    variable_name = "x" + str(z[1])
                    j_1_product.append(Int(variable_name))
                elif (z[0] == 1):
                    variable_name = "_x" + str(z[1])
                    j_1_product.append(Int(variable_name))
            j_1_product.append(j[0])
            j_line_sum_cond.append(Product(j_1_product))
        elif (len(j[1]) == 1):
            if (j[1][0][0] == 0):
                variable_name = "x" + str(j[1][0][1])
                j_line_sum_cond.append(j[0] * Int(variable_name))
            elif(j[1][0][0] == 1):
                variable_name = "_x" + str(j[1][0][1])
                j_line_sum_cond.append(j[0] * Int(variable_name))
        elif (len(j[1]) == 0):
            j_line_sum_cond.append(j[0])
    Condition_list.append(Sum(j_line_sum_cond) <= 0)
    j_line_sum_cond = []

s = Solver()
s.add(Condition_list)

result = str(s.check())

if result == "unsat":
    print("False")
    exit()
else:
    print("True")

models = []

while s.check() == sat:
    m = s.model()
    models.append(m)
    tmp_list = []
    for i in variable_list:
        tmp_list.append(i != m.eval(i, model_completion=True))
    s.add(Or(tmp_list))

model_objective_values = []

for i in models:
    sum = 0
    for j in encoded_list[0]:
        if (len(j[1]) >= 1):
            product_result = 1
            for z in j[1]:
                variable_name = ""
                if (z[0] == 0):
                    variable_name = "x" + str(z[1])
                elif(z[0] == 1):
                    variable_name = "_x" + str(z[1])
                variable_value = int(str(i.eval(Int(variable_name))))
                product_result = product_result * variable_value
            product_result = product_result * j[0]
            sum += product_result
        elif (len(j[1]) == 1):
            variable_name = ""
            if (j[1][0][0] == 0):
                variable_name = "x" + str(j[1][0][1])
            elif (j[1][0][0] == 1):
                variable_name = "_x" + str(j[1][0][1])
            variable_value = int(str(i.eval(Int(variable_name))))
            sum += j[0] * variable_value
        elif (len(j[1]) == 0):
            sum += j[0]
    model_objective_values.append(sum)

print(models[model_objective_values.index(min(model_objective_values))])