at(monkey, door).
at(banana, ceiling).
has(monkey, nothing).

can_reach(monkey, banana) :- at(monkey, chair), at(chair, banana).
