from z3 import *

graph_list = [[1,2, [2,3,4,5]],
              [2,4,[1,4]],
              [3,4,[1,5]],
              [4,7,[1,2,5]],
              [5,7,[1,3,4]]]
variable_list = []
weight_list = []
first_or_list = []
second_or_list = []


for i in graph_list:
    variable_list.append(Bool(str(i[0])))
    weight_list.append(i[1])

for i in graph_list:
    variable = i[0]
    for j in range(len(variable_list)):      
        num = int(variable_list[j].decl().name())
        if num in i[2]:
            first_or_list.append(And(variable_list[i[0] - 1], variable_list[j]))
        else:
            if num != i[0]:
                exp_one = Or(Not(variable_list[i[0] - 1]), Not(variable_list[j]) )
                second_or_list.append( exp_one )

cond_one = Or(first_or_list)
cond_two = And(second_or_list)
s = Solver()
s.add(And(cond_one, cond_two))
results = []

while s.check() == sat:
    m = s.model()
    results.append(m)
    tmp_list = []
    for i in variable_list:
        tmp_list.append(i != m.eval(i, model_completion=True))
    s.add(Or(tmp_list))
    # print m

max_weight = 0
max_model = None

for i in results:
    current_weight = 0
    for j in i.decls():
        current_weight += weight_list[int(j.name()) - 1]
    if (current_weight > max_weight):
        max_weight = current_weight
        max_model = i
print "Max weighted clique: %s with weight %s" % (i, max_weight)