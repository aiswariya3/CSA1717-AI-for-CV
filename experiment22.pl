bird(sparrow).
bird(eagle).
bird(penguin).

cannot_fly(penguin).

can_fly(X) :- bird(X), \+ cannot_fly(X).
