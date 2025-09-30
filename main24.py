code = {'colour': 'black', 'age': 15, 'grade': 15}
print("The orginal dictionary:" + str(code))
k = 15
res = 0
for key in code:
    if code[key]== k:
        res = res +1
        
print("The frequancy of k is" +str(res))

