terrain_types = ['plains','mountain','hills','desert','marsh','jungle','farmland','forest']
foods = [4,2,3,2,2.5,3,5,2.5]
food_per_yeld = 0.25
filename = "_python\\fire_raw.txt"
data = "every_owned_province = {\n    switch = {\n        trigger = terrain"
for i in range(len(terrain_types)):
    data += "\n        "+ terrain_types[i] +" = {\n"
    data += "            set_variable = { name = fields value = "+ str(int(foods[i]/food_per_yeld)) +" }\n"
    data += """			set_variable = {
				name = curr_farmer
				value = calcu_curr_farmer
			}
			set_variable = {
				name = curr_levies
				value = calcu_curr_levies
			}
		}"""
data += "\n    }\n}"
file=open(filename,'w',encoding='utf8')
file.write(data)