from z3 import *

def MPE(CPTs, Os):
    s = Solver()
    random_variable_probability_list = []
    for CPT in CPTs:
        s.add(Or(Int(CPT[0]) == 0, Int(CPT[0]) == 1))
        T = CPT[0]
        variable_name = "P_" + CPT[0]
        random_variable_probability_list.append(Real(variable_name))
        for CP in T:
            if len(CP[0]) == 0: # No condition
                s.add(Implies(Int(CPT[0]) == int(CP[1][1]) ,  Real(variable_name) == float(CP[2])))
            else: # has conditions
                conditions_list = []
                for C in CP[0]:
                    conditions_list.append(Int(C[0]) == int(C[1]))
                conditions_list.append(Int(CPT[0]) == int(CP[1][1]))
                s.add(Implies(And(conditions_list), Real(variable_name) == float(CP[2])))
    for O in Os:
        s.add(Int(O[0]) == int(O[1]))
    objective = Real("objective")
    s.add(objective == Product(random_variable_probability_list))
    if s.check == unsat:
        print("Unsat")
        quit()
    mode = ""
    while s.check() == sat:
        model = s.model()
        s.add(objective > model[objective])
    print(model)

