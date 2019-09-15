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
#satchel costs
satchel_gunpowder = 240
satchel_cloth = 10
satchel_metal = 80
#satchel needed
satchel_metal_door = 4
satchel_wooden_door = 2
satchel_armored_door = 12
satchel_garage_door = 9
satchel_wooden_wall = 3
satchel_stone_wall = 10
satchel_metal_wall = 24
satchel_armored_wall = 47

#if statements - satchel needed
if raid_entity == 1:
    satchel_entity = "Wooden doors"
    satchel_needed = entity_quantity * satchel_wooden_door
elif raid_entity == 2:
    satchel_entity = "Sheet metal doors"
    satchel_needed = entity_quantity * satchel_metal_door
elif raid_entity == 3:
    satchel_entity = "Armored Doors"
    satchel_needed = entity_quantity * satchel_armored_door
elif raid_entity == 4:
    satchel_entity = "Garage Doors"
    satchel_needed = entity_quantity * satchel_garage_door
elif raid_entity == 5:
    satchel_entity = "Wooden Walls"
    satchel_needed = entity_quantity * satchel_wooden_wall
elif raid_entity == 6:
    satchel_entity = "Stone Walls"
    satchel_needed = entity_quantity * satchel_stone_wall
elif raid_entity == 7:
    satchel_entity = "Sheet Metal Walls"
    satchel_needed = entity_quantity * satchel_metal_wall
elif raid_entity == 8:
    satchel_entity = "Armored Walls"
    satchel_needed = entity_quantity * satchel_armored_wall
#Resources needed
satchel_cloth_needed = satchel_needed * satchel_cloth
satchel_metal_needed = satchel_needed * satchel_metal
satchel_gunpowder_needed = satchel_needed * satchel_gunpowder

resources_needed =f'To destroy {str(entity_quantity_input)} {satchel_entity} You will need {str(satchel_needed)} Satchel Charges which equal to {str(satchel_gunpowder_needed)} Gunpowder ,{str(satchel_cloth_needed)} Cloth , {str(satchel_metal_needed)} Metal Fragments '

print(resources_needed)
time.sleep(120)


