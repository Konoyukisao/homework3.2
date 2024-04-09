def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)


print_params()
print_params(2)
print_params(b = 25)
print_params(c = [False, 2, 3])


values_list = [120, "120", 1.20]
values_dict = {'a': 20, 'b': '245', 'c' : False}
values_list_2 = [98, True]

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
