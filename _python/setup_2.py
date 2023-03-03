terrain_types = ['oasis','desert_hills','flood_plain','plains','mountain','hills','desert','marsh','jungle','farmland','forest']
foods = [3,2,5,4,2,3,2,2.5,3,5,2.5]
food_per_yeld = 0.25
filename = "common\\scripted_effects\\pafo_setup_effects.txt"
data = "pafo_setup_effect = {\n    switch = {\n        trigger = terrain"
for i in range(len(terrain_types)):
    data += "\n        "+ terrain_types[i] +" = {\n"
    data += "            set_variable = { name = fields value = "+ str(int(foods[i]/food_per_yeld)) +" }\n"
    data += """			set_variable = {
				name = curr_farmers
				value = this.total_population
			}
			change_variable = {
				name =curr_farmers
				subtract = this.num_of_nobles
			}
			set_variable = {
				name = fields_balance
				value = var:fields
			}
			change_variable = {
				name = fields_balance
				subtract = var:curr_farmers
			}
			if ={
				limit = { var:fields_balance > 0 }
				set_variable = {
					name = fields_balance
					value = 0
				}
			}
			set_variable = {
				name = curr_levies
				value = this.num_of_citizen
			}
			change_variable = {
				name = curr_levies
				add = var:fields_balance
			}
			if ={
				limit = { var:curr_levies < 0 }
				set_variable = {
					name = curr_levies
					value = 0
				}
			}
		}"""
data += "\n    }\n}"
file=open(filename,'w',encoding='utf-8')
file.write(data)