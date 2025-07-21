# import cal
# import lambda_calculator


# # print(cal.name(3,4))
# # print(cal.substract(3,4))
# # print(cal.multiply(3,4))
# # print(cal.divide(3,4))


# # print(lambda_calculator.addlambda(3,4))
# # print(lambda_calculator.substractlambda(3,4))
# # print(lambda_calculator.multiplylambda(3,4))
# # print(lambda_calculator.dividelambda(3,4))
# import string_operations as s

# sample_string = "hello World"

# print("Original:", sample_string)
# print("Reversed:", s.reverse_string(sample_string))
# print("Capitalized:", s.capitalize_string(sample_string))
# print("Lowercase:", s.lowercase_string(sample_string))
# print("Uppercase:", s.uppercase_string(sample_string))



# from utilities.cal import name as name_def, substract as subtract_def, multiply as multiply_def, divide as divide_def
# from utilities.string_operations import reverse_string, capitalize_string, lowercase_string, uppercase_string

# # Sample inputs and printing results using calculator.py
# print("Using calculator.py:")
# print("Addition:", name_def(10, 5))
# print("Subtraction:", subtract_def(10, 5))
# print("Multiplication:", multiply_def(10, 5))
# print("Division:", divide_def(10, 5))

# # Sample strings and printing results using string_operations.py
# sample_string = "hello World"
# print("\nUsing string_operations.py:")
# print("Original:", sample_string)
# print("Reversed:", reverse_string(sample_string))
# print("Capitalized:", capitalize_string(sample_string))
# print("Lowercase:", lowercase_string(sample_string))
# print("Uppercase:", uppercase_string(sample_string))




grades = [55, 70, 65, 40, 90, 85, 50, 77]
passed_with_bonus = list(map(lambda grade: grade * 1.05, 
                             filter(lambda grade: grade >= 60, grades)))
print(passed_with_bonus)





# children = [ {"name": "Alice", "age": 2, "height": 95}, 
#             {"name": "Bob", "age": 4, "height": 105}, 
#             {"name": "Charlie", "age": 3, "height": 110}, 
#             {"name": "David", "age": 5, "height": 102}, 
#             {"name": "Eve", "age": 6, "height": 99} ]


# eligible_children = list(filter(lambda c: c['age'] > 3 and c['height'] > 100, children))
# print("Eligible children for the fun park:", eligible_children)



children = [ {"name": "Alice", "age": 2, "height": 95}, 
             {"name": "Bob", "age": 4, "height": 105}, 
             {"name": "Charlie", "age": 3, "height": 110}, 
             {"name": "David", "age": 5, "height": 102}, 
             {"name": "Eve", "age": 6, "height": 99}]

critiria = lambda child: True if child["age"] > 3 and child["height"] > 100 else False
Filtered_child = list(filter(critiria,children))
print(Filtered_child)