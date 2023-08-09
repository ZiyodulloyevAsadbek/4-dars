from collections import namedtuple

Person = namedtuple('Person', 'first_name, last_name,age')

p_1 = Person ('Sarvarbek','Azimov', 33)

print(p_1)
print(p_1.first_name)
print(p_1[1])
f_name,l_name, age = p_1
print(f_name,l_name,age)
