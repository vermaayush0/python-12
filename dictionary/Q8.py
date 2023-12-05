marks = {'Physics':4,
         'English':6,
         'Maths':7,
         'WebTech':5,}

val = max(marks.values())
key = []
for i in marks:
    if marks[i]==val:
        key.append(i)
print('Maximum marks in',key, 'is' ,val)