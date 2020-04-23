
import time
import runpy


print('''
Tips / Tricks when raiding

1. Team Communication and Uniform: Communication is a primary key in Rust. Having a team with microphones is an ideal
team where you are all in a A good way to tell if someone is on your team or now is when you all wear a specific
uniform to different your self from the other players. (It's important for teammates to tell if they died with
uniform so they will know if someone stole the uniform to blend in.) A upside to having uniforms is not having to ask
for a jump check. (If no one took your uniform). A question to ask for a jump check and waiting for a response in a
jump is enough time for you to be killed by the enemy.


2. Binds:
Auto sprint bind:
Put this into console: bind f2 forward;sprint
This allows you to hit F2 and auto run, So if you're running to a raid and it's along run you can hit F2 and auto sprint.
[ To stop auto run you hit [ 'W' and your 'Sprint Key' ] [ Not your bind key ] ]
Auto mine bind:
Put this into console: bind z attack;duck
This allows you to hit Z and auto pickaxe. This is handy when breaking walls. Instead of holding mouse 1 you can hit Z
to do it for you.
[ To stop auto mine you click [ 'Mouse One' and hit your 'Crouch Key' ] ]
Auto toggle crouch bind:
Put this into console: bind c duck
This allows you to toggle crouching instead of having to hold down the crouch key to keep crouched.
[ To stop toggle couch you simply hit your [ 'Crouch Key' ] [ Not the toggle bind ] ]



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
