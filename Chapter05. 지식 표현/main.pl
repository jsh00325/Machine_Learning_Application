dog(my_dog).
cat(my_cat).

mammal(X) :- dog(X).
mammal(X) :- cat(X).

animal(X) :- mammal(X).