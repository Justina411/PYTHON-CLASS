name = input("Enter Your Name: ")
if name == "":
    quit()

direction = input("where are you going to ABAKPA or  Emene:  ").upper()


if direction == "ABAKPA":
    print("head west from aptech to p and t junction \n then navigate to the right and countinue to move right then turn left while reachinfg ogui junction then move straight and turn to your left and head straight then move to your first left turn ")
    print(f" {name}  You have Reached your Destination")
elif direction == "EMENE":
    print("siHead east from aptech to old park busstop then move straight to port-harcourt express way then move and you will see a gn written eke-obinagu then move and see a Bold sign written EMENE ")
    print(f"{name}You have Reached your Destination")
else:
    print("invalid input ")

