 # lambda expression 
'''
Syntax;
fun_name = lambda argv: return_expression

'''

ls = ['Ayush','Zoya','Aryan','Govind']
print('before sorting',ls)
ls.sort(key=lambda st : st[-1])
print('After sorting',ls)