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
#c4 costs
c4_gunpowder = 1000
c4_lowgrade = 60
c4_sulfur = 200
c4_metal = 200
#c4 needed
c4_metal_door = 1
c4_wooden_door = 1
c4_armored_door = 2
c4_garage_door = 2
c4_wooden_wall = 1
c4_stone_wall = 2
c4_metal_wall = 4
c4_armored_wall = 8

#if statements - c4 needed
if raid_entity == 1:
    c4_entity = "Wooden doors"
    c4_needed = entity_quantity * c4_wooden_door
elif raid_entity == 2:
    c4_entity = "Sheet metal doors"
    c4_needed = entity_quantity * c4_metal_door
elif raid_entity == 3:
    c4_entity = "Armored Doors"
    c4_needed = entity_quantity * c4_armored_door
elif raid_entity == 4:
    c4_entity = "Garage Doors"
    c4_needed = entity_quantity * c4_garage_door
elif raid_entity == 5:
    c4_entity = "Wooden Walls"
    c4_needed = entity_quantity * c4_wooden_wall
elif raid_entity == 6:
    c4_entity = "Stone Walls"
    c4_needed = entity_quantity * c4_stone_wall
elif raid_entity == 7:
    c4_entity = "Sheet Metal Walls"
    c4_needed = entity_quantity * c4_metal_wall
elif raid_entity == 8:
    c4_entity = "Armored Walls"
    c4_needed = entity_quantity * c4_armored_wall
#Resources needed
c4_sulfur_needed = c4_needed * c4_sulfur
c4_metal_needed = c4_needed * c4_metal
c4_lowgrade_needed = c4_needed * c4_lowgrade
c4_gunpowder_needed = c4_needed * c4_gunpowder

resources_needed =f'To destroy {str(entity_quantity_input)} {c4_entity} You will need {str(c4_needed)} C4 which equal to {str(c4_gunpowder_needed)} Gunpowder ,{str(c4_sulfur_needed)} Sulfur , {str(c4_metal_needed)} Metal Fragments , {str(c4_lowgrade_needed)} Lowgrade Fuel'

print(resources_needed)
time.sleep(120)
