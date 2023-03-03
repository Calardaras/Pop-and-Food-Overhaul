terrain_types = ['plains','mountain','hills','desert','marsh','jungle','farmland','forest']
foods = [4,2,3,2,2.5,3,5,2.5]
food_per_yeld = 0.25
duration = 365
filename = "common\\modifiers\\pafo_province_foods.txt"
data = ""
for i in range(int(6.5/food_per_yeld+1)):
    data += "foods_output_"+str(i)+" = { local_monthly_food = "+str(i*food_per_yeld)+" }\n"
    data += "levies_raised_"+str(i)+" = { local_monthly_food = -"+str(i*food_per_yeld)+" }\n"
file=open(filename,'w',encoding='utf8bom')
file.write(data)