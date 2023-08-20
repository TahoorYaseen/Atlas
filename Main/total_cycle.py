import ast

with open('dummy3.txt','r') as f:
    k=f.read()
my_dict=ast.literal_eval(k)
# print(len(my_dict))


total_vehicles=0
total_cycle_length=0
n=2
L=20
for i in range(1,n+1):
    total_green=sum(my_dict[str(i)][1])
    cycle_length=total_green + L
    total_cycle_length+=cycle_length+4
    # print(my_dict[str(i)][1])
    total_vehicles+=sum(my_dict[str(i)][0][0]+my_dict[str(i)][0][1]+my_dict[str(i)][0][2]+my_dict[str(i)][0][3])
    # print(cycle_length)
print(total_vehicles)
print(total_cycle_length)
   