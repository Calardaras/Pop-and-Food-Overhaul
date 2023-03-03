filename = "common\\scripted_effects\\pafo_foods_effects.txt"
terrain_types = ['oasis','desert_hills','flood_plain','plains','mountain','hills','desert','marsh','jungle','farmland','forest']
foods = [3,2,5,4,2,3,2,2.5,3,5,2.5]
food_per_yeld = 0.25
duration = 365
data = 'pafo_foods_output_effect = {\n    switch  = {\n        trigger = terrain'
for i in range(len(terrain_types)):
    data += '\n        '+terrain_types[i]+" = {\n            switch = {\n                trigger = calcu_curr_farmers "
    for j in range(int(foods[i]/food_per_yeld+1)):
        data += "\n                " +str(j) +" = { add_province_modifier = { name = foods_output_"+str(j)+" duration = "+str(duration)+" } }"
    data += "\n                fallback = { add_province_modifier = { name = foods_output_"+str(j)+" duration = "+str(duration)+" } }\n            }\n        }\n"
data += '    }\n}'
file=open(filename,'w',encoding='utf-8')
file.write(data)



