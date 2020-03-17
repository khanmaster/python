'''# tuples

essentials = ("bread", "eggs", "milk")
print(essentials)
print(essentials.count("bread"))
# essentials [0] = "beans" will not allow as its immutable
'''
# Dictionaries
# Dictonary is a collection which is unordered, changeable and indexed
# we use curly brackets and Dictonaries have keys  values pairs
student_1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lession": 4,
    " completed_lession_names": ["variables", "date_type", "set up"]
}
print(student_1["stream"])
#print(student_1["completed_lession"]) = 3
print(student_1[" completed_lession_names"][1])

# how to change the value
#student_1(["completed_lession]") = 3

# print(student_1[" completed_lession"])
# print(student_1[" completed_lession_names"].renove("data_type"))

# sets - set is a collection which is unordered and unindexed.
# sets area written with curly brackets
car_parts = {"wheels", "doors", "exhausts"}
print(car_parts)
# adding
car_parts.add("windows")
print(car_parts)
# deleting
car_parts.discard("doors")
print(car_parts)

# Frozen Sets - Immutable version of sets similar tuple

x = frozenset([1, 2, 3, 4])
print(type(x))
# used to store data that will not need to change ever
# for example date of birth
