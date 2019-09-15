

print('''Welcome, Rust - Raid Calculator
   Version 1.2 - Developed by sAsPeCt
   ''')

menu_select = input('''
1. C4 Raid Cost
2. Rocket Raid Cost
3. Explosive Ammo Raid Cost
4. Satchel Charge Raid Cost
5. Beancan Raid Cost
6. Raiding Tips
7. Changelog

Enter the number : 
''')

selected_number = int(menu_select)

if selected_number == 1 :
    import C4raid
elif selected_number == 2 :
    import rocketraid
elif selected_number == 3 :
    import explosiveammo
elif selected_number == 4 :
   import Satchelcharge
elif selected_number == 5 :
   import Beancanraid
elif selected_number == 6 :
   import raidingtips
elif selected_number == 7 :
   import changelog