import time
import runpy

c4_cost = {
    "gunpowder": 1000,
    "metal": 200,
    "low_grade": 60,
    "sulfur": 200
}


c4_needed_doors = {
    "metal": 1,
    "wood": 1,
    "armored": 2,
    "garage": 2,
}

c4_needed_walls = {
    "wood": 1,
    "stone": 2,
    "metal": 4,
    "armored": 8
}


def resource_msg_creator(quantity, raid_entity, explosive_needed, gunpowder, metal, lowgrade, sulfur, explosive="C4"):
    str_explosive = str(explosive) + \
        "s" if explosive_needed > 1 else str(explosive)
    converted_entity = str(raid_entity) + \
        "s" if quantity > 1 else str(raid_entity)
    msg = f"""To destroy {str(quantity)} {converted_entity} You will need {str(explosive_needed)}
{str_explosive} which is/are equal to {str(gunpowder)} Gunpowder ,
{str(metal)} Metal Fragments, {str(lowgrade)} Low-grade Fuel and {str(sulfur)} Sulfur """
    return msg


def resources_calculator(explosive_number, gunpowder=c4_cost["gunpowder"], metal=c4_cost["metal"], sulfur=c4_cost["sulfur"], low_grade=c4_cost["low_grade"]):
    gunpowder_needed = explosive_number * gunpowder
    metal_needed = explosive_number * metal
    lowgrade_needed = explosive_number * low_grade
    sulfur_needed = explosive_number * sulfur
    return gunpowder_needed, metal_needed, lowgrade_needed, sulfur_needed


def user_confirmation(raid_entity, quantity, explosive="C4s"):
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
        print("C4 Raid!")
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
                    c4_needed_doors.get(raid_material)
            elif raid_type == "wall":
                explosive_needed = entity_quantity * \
                    c4_needed_walls.get(raid_material)
            gunpowder_needed, metal_needed, lowgrade_needed, sulfur_needed = resources_calculator(
                explosive_needed)
            resources_text = resource_msg_creator(quantity=entity_quantity, raid_entity=raid_entity,
                                                  explosive_needed=explosive_needed, gunpowder=gunpowder_needed, metal=metal_needed, lowgrade=lowgrade_needed, sulfur=sulfur_needed)
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


# Resources needed
