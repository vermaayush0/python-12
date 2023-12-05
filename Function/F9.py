def strict_difference(ls1):
   ls_d = []
   for i in range(len(ls1)-1):
      ls_d.append(abs(ls1[i]-ls1[i+1]))
   return sorted(ls_d)==ls_d

# main code
ls = [1, 4, 0, -5]
out = strict_difference(ls)
print(out)