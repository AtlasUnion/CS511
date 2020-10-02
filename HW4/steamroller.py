from z3 import *

s = Solver()

Obj, (Wolf, Fox, Bird, Caterpillar, Snail, Grain) = EnumSort('Obj', ['Wolf', 'Fox', 'Bird', 'Caterpillar', 'Snail', 'Grain'])
Animal = Function('Animal', Obj, BoolSort())
Plant = Function('Plant', Obj, BoolSort())
Eats = Function('Eats', Obj, Obj, BoolSort())
Smaller = Function('Smaller', Obj, Obj, BoolSort())


x = Const('x', Obj)
y = Const('y', Obj)
z = Const('z', Obj)
u = Const('u', Obj)

s.add(ForAll(x, Implies(x == Wolf, Animal(x))))
s.add(ForAll(x, Implies(x == Fox, Animal(x))))
s.add(ForAll(x, Implies(x == Bird, Animal(x))))
s.add(ForAll(x, Implies(x == Caterpillar, Animal(x))))
s.add(ForAll(x, Implies(x == Snail, Animal(x))))
s.add(ForAll(x, Implies(x == Grain, Plant(x))))

s.add(Exists(x, x == Wolf))
s.add(Exists(x, x == Fox))
s.add(Exists(x, x == Bird))
s.add(Exists(x, x == Caterpillar))
s.add(Exists(x, x == Snail))
s.add(Exists(x, x == Grain))

s.add(ForAll(x, Implies(Animal(x), Or(
                                      ForAll(y, Implies(Plant(y), Eats(x,y))),
                                      ForAll(z, Implies(And(Animal(z), Smaller(z,x), Exists(u, And(Plant(u), Eats(z,u)))),Eats(x,z)))))))

s.add(ForAll(x, ForAll(y, Implies(And(x == Caterpillar, y == Bird), Smaller(x,y)))))
s.add(ForAll(x, ForAll(y, Implies(And(x == Snail, y == Bird), Smaller(x,y)))))
s.add(ForAll(x, ForAll(y, Implies(And(x == Bird, y == Fox), Smaller(x,y)))))
s.add(ForAll(x, ForAll(y, Implies(And(x == Fox, y == Wolf), Smaller(x,y)))))
s.add(ForAll(x, ForAll(y, Implies(And(x == Bird, y == Caterpillar), Eats(x,y)))))

s.add(ForAll(x, Implies(x == Caterpillar, Exists(y, And(Plant(y), Eats(x,y))))))
s.add(ForAll(x, Implies(x == Snail, Exists(y, And(Plant(y), Eats(x,y))))))

s.add(ForAll(x, ForAll(y, Implies(And(x == Wolf, y == Fox), Not(Eats(x,y))))))
s.add(ForAll(x, ForAll(y, Implies(And(x == Wolf, y == Grain), Not(Eats(x,y))))))
s.add(ForAll(x, ForAll(y, Implies(And(x == Bird, y == Snail), Not(Eats(x,y))))))

s.add(Exists(x, Exists(y, And(Animal(x), Animal(y), Eats(x,y), ForAll(z, Implies(z == Grain, Eats(y,z))) ))))

print s.check()