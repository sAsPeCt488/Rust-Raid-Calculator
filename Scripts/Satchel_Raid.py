import time
import runpy

satchel_cost = {
    "gunpowder": 240,
    "metal": 80,
    "cloth": 10
}


satchel_needed_doors = {
    "metal": 4,
    "wood": 2,
    "armored": 12,
    "garage": 9,
}

satchel_needed_walls = {
    "wood": 3,
    "stone": 10,
    "metal": 24,
    "armored": 47
}


def resource_msg_creator(quantity, raid_entity, explosive_needed, gunpowder, metal, cloth, explosive="Satchel"):
    str_explosive = str(explosive) + \
        "s" if explosive_needed > 1 else str(explosive)
    converted_entity = str(raid_entity) + \
        "s" if quantity > 1 else str(raid_entity)
    msg = f"""To destroy {str(quantity)} {converted_entity} You will need {str(explosive_needed)}
{str_explosive} which is/are equal to {str(gunpowder)} Gunpowder ,
{str(metal)} Metal Fragments and {str(cloth)} Cloth """
    return msg


def resources_calculator(explosive_number, gunpowder=satchel_cost["gunpowder"], metal=satchel_cost["metal"], cloth=satchel_cost["cloth"]):
    gunpowder_needed = explosive_number * gunpowder
    metal_needed = explosive_number * metal
    cloth_needed = explosive_number * cloth
    return gunpowder_needed, metal_needed, cloth_needed


def user_confirmation(raid_entity, quantity, explosive="Satchels"):
    converted_entity = str(raid_entity) + \
        "s" if quantity > 1 else str(raid_entity)
    msg = f"Do you want to raid {str(quantity)} {converted_entity} with {explosive}(Yes/No)? "
    return msg


def raid_entity_check(selection):
    if selection == 1:  # Doors
        raid_entity = "Wooden door"
        kind = "door"
        material = "wood"
    elif selection == 2:
        raid_entity = "Sheet metal door"
        kind = "door"
        material = "metal"
    elif selection == 3:
        raid_entity = "Armored door"
        kind = "door"
        material = "armored"
    elif selection == 4:
        raid_entity = "Garage door"
        kind = "door"
        material = "garage"
    elif selection == 5:  # Walls
        raid_entity = "Wooden wall"
        kind = "wall"
        material = "wood"
    elif selection == 6:
        raid_entity = "Stone wall"
        kind = "wall"
        material = "stone"
    elif selection == 7:
        raid_entity = "Sheet metal wall"
        kind = "wall"
        material = "metal"
    elif selection == 8:
        raid_entity = "Armored wall"
        kind = "wall"
        material = "armored"
    return raid_entity, kind, material


while True:
    try:
        print("Satchel Raid!")
        print('''
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
''')
        menu_select = int(input("Enter Number: "))
        if 1 > menu_select or menu_select > 8:
            print("No Valid Answer!")
            print("Restarting in 5 seconds")
            time.sleep(4)
            continue
        entity_quantity = int(input("How many of them? "))
        raid_entity, raid_type, raid_material = raid_entity_check(menu_select)
        user_confirm_msg = user_confirmation(
            raid_entity, entity_quantity)
        user_confirmation_input = input(user_confirm_msg)
        if user_confirmation_input.lower() == "yes":
            if raid_type == "door":
                explosive_needed = entity_quantity * \
                    satchel_needed_doors.get(raid_material)
            elif raid_type == "wall":
                explosive_needed = entity_quantity * \
                    satchel_needed_walls.get(raid_material)
            gunpowder_needed, metal_needed,  cloth_needed = resources_calculator(
                explosive_needed)
            resources_text = resource_msg_creator(quantity=entity_quantity, raid_entity=raid_entity,
                                                  explosive_needed=explosive_needed, gunpowder=gunpowder_needed, metal=metal_needed, cloth=cloth_needed)
            print(resources_text)
            user_end_confirm = input(
                "Do you want to calculate something else(Yes/No)? ")
            if user_end_confirm.lower() == "yes":
                print("Restarting...")
                time.sleep(4)
                continue

            elif user_end_confirm.lower() == "no":
                print("Redirecting to the main page...")
                time.sleep(4)
                runpy.run_module(mod_name="Rust_Raid_Calculator")
            else:
                print("Invalid Answer: Restarting....")
                time.sleep(4)
                continue
        elif user_confirmation_input.lower() == "no":
            print("Restarting in 5 seconds")
            time.sleep(4)
            continue
        else:
            ("Invalid Answer! Restarting....")
            continue
    except ValueError:
        print("No Valid Answer!")
        print("Restarting in 5 seconds")
        time.sleep(4)
        continue
