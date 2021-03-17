
student = {'name': 'john', 'age': 25, 'courses': ['math', 'compsci']}

student['phone'] = '555-5555'       # add an entry
student['name'] = 'jane'            # change an entry

print()
print(student)

# print nice error if not found
print(student.get('name', 'Not found'))
print()

student.update({'name': 'james', 'gender': 'm'})
del student['courses']

print(student)
print()

print(student.keys())
print(student.values())
print(student.items())
print()

for key, value in student.items():
    print(key, value)

print()
