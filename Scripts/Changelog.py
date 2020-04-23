import time
import runpy


print('''
  /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/Rust - Raid Calculator /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/                                                                       
                                                     Changelog
Version 2.0:

Rebuild all the Programm!
Now user has to confirm his/her selection!

For Devs:
Made code more readable and reusable!
Included Value exceptions!



''')
time.sleep(120)
while True:
    continue_confirm = input(' Do you want to continue reading?(Yes/No)? ')
    if continue_confirm.lower() != "yes":
        print("Redirecting to the main page!")
        time.sleep(4)
        runpy.run_module(mod_name="Rust_Raid_Calculator")
        break
    else:
        print("Okay, waiting 30 seconds before asking again!")
        time.sleep(30)
        continue
