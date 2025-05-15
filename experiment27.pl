edge(a, b, 1).
edge(a, c, 3).
edge(b, d, 1).
edge(c, d, 1).

heuristic(b, 2).
heuristic(c, 1).
heuristic(d, 0).

best_first(Node, Goal, Path) :-
    bfs([[Node]], Goal, RevPath),
    reverse(RevPath, Path).

bfs([[Goal|Rest]|_], Goal, [Goal|Rest]).
bfs([[Node|Rest]|Others], Goal, Path) :-
    findall([X,Node|Rest],
            (edge(Node, X, _), \+ member(X, [Node|Rest])),
            NewPaths),
    append(Others, NewPaths, AllPaths),
    sort(AllPaths, Sorted),
    bfs(Sorted, Goal, Path).
