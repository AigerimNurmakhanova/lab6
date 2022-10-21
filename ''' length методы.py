''' length методы
list = [1, 2, 3, 4, 5]
print(len(list))

dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
print(len(dict))

tup = (1, 2, 3, 4, 5)
print(len(tup))

set = {1, 2, 3, 4, 5}
length = len(set)
print(length)

#clear методы
list = [1,2,3,4,5]
element = list.clear()
print(element)

dict = {"one":1,"two":2,"three":3,"four":4,"five":5}
element = dict.clear()
print(element)

set = {1,2,3,4,5}
set.clear()
print(set)

tup = (1,2,3,4,5)
del tup

#элементті өшіру
list = [1,2,3,4,5]
print(list.remove(3))

set = {1, 2, 3, 4, 5, 6}
print(set.remove(3))

dict = {"one":1,"two":2,"three":3,"four":4,"five":5}
dict.pop("two")
...