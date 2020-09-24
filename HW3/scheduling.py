from z3 import *

A = Int('A')
At = Int('At')
B = Int('B')
Bt = Int('Bt')
C = Int('C')
Ct = Int('Ct')
D = Int('D')
Dt = Int('Dt')
E = Int('E')
Et = Int('Et')
F = Int('F')
Ft = Int('Ft')
End = Int('End')

s = SolverFor("LIA")
s.add(A >= 0, B >= 0, C >= 0, D >= 0, E >= 0, F >= 0)
s.add(At == 2, Bt == 1, Ct == 2, Dt == 2, Et == 7, Ft == 5)
s.add(End == 14)

s.add(Or(A + At <= C, C + Ct <= A))
s.add(Or(B + Bt <= D, D + Dt <= B))
s.add(Or(B + Bt <= E, E + Et <= B))
s.add(Or(D + Dt <= E, E + Et <= D))
s.add(And(D + Dt <= F, E + Et <= F))
s.add(A + At <= B)
s.add(A + At <= End)
s.add(B + Bt <= End)
s.add(C + Ct <= End)
s.add(D + Dt <= End)
s.add(E + Et <= End)
s.add(F + Ft <= End)

print s.check()

m = s.model()

Variable_list = ['A', 'B', 'C', 'D', 'E', 'F']

for name in Variable_list:
    for d in m.decls():
        if (d.name() == name):
            print "%s = %s" % (d.name(), m[d])