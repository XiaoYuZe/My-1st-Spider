a=['apple','rush','muscle','may','moon']

#第一种尝试

# empty = []
# for i in a:
# 	empty.append(i)
# print empty

#第二种尝试

# empty = ''
# for i in a:
# 	empty = empty +str(i)+' '
# print empty

#第三种尝试 
print ' '.join(a)