import time
raid_entity_input = input('''
Doors :
1. Wooden Door
2. Sheet metal door
3. Armored Door
4. Garage Door
Walls :
5. Wooden
6. Stone
7. Metal 
8. Armored

Enter Here:
''')
entity_quantity_input = input("How many of them? ")
raid_entity = int(raid_entity_input)
entity_quantity = int(entity_quantity_input)
#rocket costs
rocket_gunpowder = 500
rocket_lowgrade = 30
rocket_sulfur = 100
rocket_metal = 100
rocket_metal_pipes = 2
#rocket needed
rocket_metal_door = 2
rocket_wooden_door = 1
rocket_armored_door = 4
rocket_garage_door = 3
rocket_wooden_wall = 2
rocket_stone_wall = 4
rocket_metal_wall = 8
rocket_armored_wall = 15

#if statements - rocket needed
if raid_entity == 1:
    rocket_entity = "Wooden doors"
    rocket_needed = entity_quantity * rocket_wooden_door
elif raid_entity == 2:
    rocket_entity = "Sheet metal doors"
    rocket_needed = entity_quantity * rocket_metal_door
elif raid_entity == 3:
    rocket_entity = "Armored Doors"
    rocket_needed = entity_quantity * rocket_armored_door
elif raid_entity == 4:
    rocket_entity = "Garage Doors"
    rocket_needed = entity_quantity * rocket_garage_door
elif raid_entity == 5:
    rocket_entity = "Wooden Walls"
    rocket_needed = entity_quantity * rocket_wooden_wall
elif raid_entity == 6:
    rocket_entity = "Stone Walls"
    rocket_needed = entity_quantity * rocket_stone_wall
elif raid_entity == 7:
    rocket_entity = "Sheet Metal Walls"
    rocket_needed = entity_quantity * rocket_metal_wall
elif raid_entity == 8:
    rocket_entity = "Armored Walls"
    rocket_needed = entity_quantity * rocket_armored_wall
#Resources needed
rocket_sulfur_needed = rocket_needed * rocket_sulfur
rocket_metal_needed = rocket_needed * rocket_metal
rocket_lowgrade_needed = rocket_needed * rocket_lowgrade
rocket_gunpowder_needed = rocket_needed * rocket_gunpowder
rocket_metal_pipes_needed = rocket_needed * rocket_metal_pipes

resources_needed =f'To destroy {str(entity_quantity_input)} {rocket_entity} You will need {str(rocket_needed)} Rockets which equal to {str(rocket_gunpowder_needed)} Gunpowder ,{str(rocket_sulfur_needed)} Sulfur , {str(rocket_metal_needed)} Metal Fragments , {str(rocket_lowgrade_needed)} Lowgrade Fuel and {str(rocket_metal_pipes_needed)} Metal Pipes'

print(resources_needed)
time.sleep(120)
