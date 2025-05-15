parent(john, alice).
parent(john, bob).
parent(alice, claire).
male(john).
female(alice).
female(claire).

grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
