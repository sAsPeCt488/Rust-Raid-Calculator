import time
import runpy

print('''Welcome, Rust - Raid Calculator
   Version 2.0 - Developed by sAsPeCt(Thanasis Mitragkas)
   ''')
while True:
    try:
        menu_select = int(input('''
    1. C4 Raid Cost
    2. Rocket Raid Cost
    3. Explosive Ammo Raid Cost
    4. Satchel Charge Raid Cost
    5. Beancan Raid Cost
    6. Raiding Tips
    7. Changelog
    
    Enter the number : 
    '''))
        if menu_select < 1 or menu_select > 8:
            print("Invalid Answer")
            print("Restarting ")
            time.sleep(2)
            continue
        break
    except ValueError:
        print("Restarting in 5....")
        time.sleep(4)
        continue

if menu_select == 1:
    runpy.run_module(mod_name="C4_Raid")
elif menu_select == 2:
    runpy.run_module(mod_name="Rocket_Raid")
elif menu_select == 3:
    runpy.run_module(mod_name="Explosive_Ammo_Raid")
elif menu_select == 4:
    runpy.run_module(mod_name="Satchel_Raid")
elif menu_select == 5:
    runpy.run_module(mod_name="Beancan_Raid")
elif menu_select == 6:
    runpy.run_module(mod_name="Raiding_Tips")
elif menu_select == 7:
    runpy.run_module(mod_name="Changelog")
