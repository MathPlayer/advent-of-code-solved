#!/usr/bin/env python3


def print_round(recipes, first, second):
    for i in range(len(recipes)):
        if i == first:
            print("({})".format(recipes[i]), end="")
        elif i == second:
            print("[{}]".format(recipes[i]), end="")
        else:
            print(" {} ".format(recipes[i]), end="")
    print()


def recipe_score(n):
    recipes = [3, 7]
    first = 0
    second = 1

    while len(recipes) < n + 11:
        recipes.extend(map(int, list(str(recipes[first] + recipes[second]))))
        first = (first + 1 + recipes[first]) % len(recipes)
        second = (second + 1 + recipes[second]) % len(recipes)

    # print_round(recipes, first, second)
    return "".join(map(str, recipes[n:n+10]))


def recipe_score_2(pattern):
    recipes = [3, 7]
    first = 0
    second = 1

    counter = 0
    while True:
        recipes.extend(map(int, list(str(recipes[first] + recipes[second]))))
        first = (first + 1 + recipes[first]) % len(recipes)
        second = (second + 1 + recipes[second]) % len(recipes)
        counter += 1
        if pattern in "".join(map(str, recipes[-10:])):
            return "".join(map(str, recipes)).rindex(pattern)
        if counter % 10000 == 0 and counter:
            print("Debug: {}".format(counter))


print(recipe_score(5))
print(recipe_score(9))
print(recipe_score(18))
print(recipe_score(2018))
print(recipe_score(47801))
print("=============")
print(recipe_score_2("51589"))
print(recipe_score_2("01245"))
print(recipe_score_2("92510"))
print(recipe_score_2("59414"))
print(recipe_score_2("047801"))
