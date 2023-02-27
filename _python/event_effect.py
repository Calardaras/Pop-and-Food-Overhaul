filename = "common\\scripted_effects\\pafo_effects.txt"
terrain_types = ['plains','mountain','hills','desert','marsh','jungle','farmland','forest']
foods = [4,2,3,2,2.5,3,5,2.5]
food_per_yeld = 0.25
duration = 365
data = 'pafo_foods_output_effect = {\n'
for i in range(len(terrain_types)):
    data += "    If = {\n        limit = { terrain = "+ terrain_types[i]+" }\n        switch = {\n            trigger = var:curr_fields"
    for j in range(int(foods[i]/food_per_yeld+1)):
        data += "\n            " +str(j) +" = {add_province_modifier = { name = foods_output_"+str(j)+" duration = "+str(duration)+"}}"
    data += "\n            fallback = {add_province_modifier = { name = foods_output_"+str(j)+" duration = "+str(duration)+"}}\n        }\n    }\n"
data += '}'
file=open(filename,'w',encoding='utf8')
file.write(data)

filename = "_python//fire_raw.txt"
data = "every_owned_province = {\n    switch = {\n        trigger = terrain"
for i in range(len(terrain_types)):
    data += "\n        "+ terrain_types[i] +" = {\n"
    data += "            set_variable = { name = fields value = "+ str(int(foods[i]/food_per_yeld)) +" }\n"
    data += "            set_variable = { name = curr_fields value = 0 }\n        }"
data += "\n    }\n}"
file=open(filename,'w',encoding='utf8')
file.write(data)

filename = "common\\modifiers\\pafo_province_foods.txt"
data = "levies_raised = { local_monthly_food_modifier = -0.6 }\n"
for i in range(int(6.5/food_per_yeld+1)):
    data += "foods_output_"+str(i)+" = { local_monthly_food = "+str(i*food_per_yeld)+" }\n"
file=open(filename,'w',encoding='utf8')
file.write(data)

