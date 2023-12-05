lst = [4, 6, 7, 8]
print('Before mapping',lst)
out = list(filter(lambda x : x<=5, lst))
print('After Mapping',out)