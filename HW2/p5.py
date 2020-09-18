from z3 import *

p1,p2,p3,p4 = Bools('p1 p2 p3 p4')

cnf_clause1 = Or(p1,Or(Not(p2),Or(p3,p4)))
cnf_clause2 = Or(Not(p1),Or(p2,Or(p3,p4)))
cnf_clause3 = Or(p1,Or(p2,Or(p3,Not(p4))))
cnf_clause4 = Or(Not(p1),Or(Not(p2),Or(p3,Not(p4))))
cnf_clause5 = Or(p1,Or(Not(p2),Or(Not(p3),Not(p4))))
cnf_clause6 = Or(Not(p1),Or(p2,Or(Not(p3),Not(p4))))
cnf_clause7 = Or(p1,Or(p2,Or(Not(p3),p4)))
cnf_clause8 = Or(Not(p1),Or(Not(p2),Or(Not(p3),p4)))

cnf = And(cnf_clause1,And(cnf_clause2,And(cnf_clause3,And(cnf_clause4,And(cnf_clause5,And(cnf_clause6,And(cnf_clause7,cnf_clause8)))))))

dnf_clause1 = And(Not(p1),And(Not(p2),And(Not(p3),Not(p4))))
dnf_clause2 = And(p1,And(p2,And(Not(p3),Not(p4))))
dnf_clause3 = And(Not(p1),And(p2,And(Not(p3),p4)))
dnf_clause4 = And(p1,And(Not(p2),And(Not(p3),p4)))
dnf_clause5 = And(Not(p1),And(Not(p2),And(p3,p4)))
dnf_clause6 = And(p1,And(p2,And(p3,p4)))
dnf_clause7 = And(Not(p1),And(p2,And(p3,Not(p4))))
dnf_clause8 = And(p1,And(Not(p2),And(p3,Not(p4))))

dnf = Or(dnf_clause1,Or(dnf_clause2,Or(dnf_clause3,Or(dnf_clause4,Or(dnf_clause5,Or(dnf_clause6,Or(dnf_clause7,dnf_clause8)))))))

bidirectional = ((((Not(p1) == Not(p2)) == Not(p3))) == Not(p4))

s1 = Solver()
s1.add(Not(cnf == dnf))
print s1.check()

s2 = Solver()
s2.add(Not(cnf == bidirectional))
print s2.check()

s3 = Solver()
s3.add(Not(dnf == bidirectional))
print s3.check()
