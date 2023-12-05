 # lambda expression 
'''
Syntax;
fun_name = lambda argv: return_expression

'''


ls = ['Ayush','Zoya','Aryan','Govind']
print('before sorting',ls)
ls.sort(key=lambda st: sum([ord(i) for i in st]))
print('After sorting',ls)