from z3 import *

in_a0 = Int('in_a0')
out_a0 = Int('out_a0')
out_a1 = Int('out_a1')
out_a2 = Int('out_a2')

in_b0 = Int('in_b0')
out_b0 = Int('out_b0')

phi_a = And((out_a0 == in_a0), (out_a1 == (out_a0 * in_a0)), (out_a2 == (out_a1 * in_a0)))
phi_b = (out_b0 == ((in_b0 * in_b0) * in_b0))


sub0 = And((in_a0 == in_b0), phi_a, phi_b)
sub1 = (out_a2 == out_b0)

final = ForAll([in_a0, out_a0, out_a1, out_a2, in_b0, out_b0], Not(Implies(sub0, sub1)))

s = Solver()
s.add(final)

print(s.check())