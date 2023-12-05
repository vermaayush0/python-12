marks = {'Physics':4,
         'English':6,
         'Maths':7,
         'WebTech':5,
         'Python': None}

s = 1
for i in marks:
    total = marks[i]
    if type(total)== int :
        s = s*total
print("Total Marks",s)