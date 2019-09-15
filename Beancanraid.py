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
#beancn costs
beancn_gunpowder = 60
beancn_metal = 20
#beancn needed
beancn_metal_door = 18
beancn_wooden_door = 6
beancn_armored_door = 56
beancn_garage_door = 42
beancn_wooden_wall = 14
beancn_stone_wall = 46
beancn_metal_wall = 122
beancn_armored_wall = 223

#if statements - beancn needed
if raid_entity == 1:
    beancn_entity = "Wooden doors"
    beancn_needed = entity_quantity * beancn_wooden_door
elif raid_entity == 2:
    beancn_entity = "Sheet metal doors"
    beancn_needed = entity_quantity * beancn_metal_door
elif raid_entity == 3:
    beancn_entity = "Armored Doors"
    beancn_needed = entity_quantity * beancn_armored_door
elif raid_entity == 4:
    beancn_entity = "Garage Doors"
    beancn_needed = entity_quantity * beancn_garage_door
elif raid_entity == 5:
    beancn_entity = "Wooden Walls"
    beancn_needed = entity_quantity * beancn_wooden_wall
elif raid_entity == 6:
    beancn_entity = "Stone Walls"
    beancn_needed = entity_quantity * beancn_stone_wall
elif raid_entity == 7:
    beancn_entity = "Sheet Metal Walls"
    beancn_needed = entity_quantity * beancn_metal_wall
elif raid_entity == 8:
    beancn_entity = "Armored Walls"
    beancn_needed = entity_quantity * beancn_armored_wall
#Resources needed
beancn_metal_needed = beancn_needed * beancn_metal
beancn_gunpowder_needed = beancn_needed * beancn_gunpowder

resources_needed =f'To destroy {str(entity_quantity_input)} {beancn_entity} You will need {str(beancn_needed)} Beancan Grenades which equal to {str(beancn_gunpowder_needed)} Gunpowder ,  {str(beancn_metal_needed)} Metal Fragments '

print(resources_needed)
time.sleep(120)
