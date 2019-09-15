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
#expa costs
expa_gunpowder = 20
expa_sulfur = 10
expa_metal = 10
#expa needed
expa_metal_door = 63
expa_wooden_door = 20
expa_armored_door = 200
expa_garage_door = 150
expa_wooden_wall = 56
expa_stone_wall = 200
expa_metal_wall = 400
expa_armored_wall = 800

#if statements - expa needed
if raid_entity == 1:
    expa_entity = "Wooden doors"
    expa_needed = entity_quantity * expa_wooden_door
elif raid_entity == 2:
    expa_entity = "Sheet metal doors"
    expa_needed = entity_quantity * expa_metal_door
elif raid_entity == 3:
    expa_entity = "Armored Doors"
    expa_needed = entity_quantity * expa_armored_door
elif raid_entity == 4:
    expa_entity = "Garage Doors"
    expa_needed = entity_quantity * expa_garage_door
elif raid_entity == 5:
    expa_entity = "Wooden Walls"
    expa_needed = entity_quantity * expa_wooden_wall
elif raid_entity == 6:
    expa_entity = "Stone Walls"
    expa_needed = entity_quantity * expa_stone_wall
elif raid_entity == 7:
    expa_entity = "Sheet Metal Walls"
    expa_needed = entity_quantity * expa_metal_wall
elif raid_entity == 8:
    expa_entity = "Armored Walls"
    expa_needed = entity_quantity * expa_armored_wall
#Resources needed
expa_sulfur_needed = expa_needed * expa_sulfur
expa_metal_needed = expa_needed * expa_metal
expa_gunpowder_needed = expa_needed * expa_gunpowder

resources_needed =f'To destroy {str(entity_quantity_input)} {expa_entity} You will need {str(expa_needed)} Explosive Ammo which equal to {str(expa_gunpowder_needed)} Gunpowder ,{str(expa_sulfur_needed)} Sulfur , {str(expa_metal_needed)} Metal Fragments '

print(resources_needed)
time.sleep(120)
