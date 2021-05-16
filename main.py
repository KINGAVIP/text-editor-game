from room import Room
from info import Info
from character import Friend,Enemy,Character
from item import Item
game=Info("AVI's game")
game.welcome()
Info.creation()
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")
dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")
ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
#dining_hall.get_details()
kane=Enemy("Kane","The demon")
kane.set_weakness("water")
#kane.anger()
kane.set_conversation("Ha ha ha ha ha ha")
#kane.describe()
dining_hall.set_character(kane)
cheese=Item("cheese")
cheese.set_description("Cheese is Used to treat friends")
water=Item("water")
water.set_description("Water can be used to kill firey foes")
kitchen.set_item(water)
ballroom.set_item(cheese)

kane=Room("kitchen")
#print(kane)

avi=Friend("AVI","A kind but broken person")
avi.set_conversation("Hello my friend")
ballroom.set_character(avi)



current_room = dining_hall
dead=False
backpack=[]

while dead==False:
    print("\n")
    current_room.get_details()

    inhabitant=current_room.get_character()
    if inhabitant is not None:
        #print(inhabitant," is here")
        inhabitant.describe()
    items=current_room.get_item()
    if items is not None:
        items.describer()
    command = input(">")
    if command in ["north","south","west","east"]:
        current_room = current_room.move(command)
    elif command=="fight":
        if inhabitant is not  None :
            if isinstance(inhabitant,Enemy):
                item=input("Select your combat item:")
                if item in backpack:
                    if item==inhabitant.weakness:
                        print("you won")
                        current_room.set_character(None)
                        Enemy.enemy_to_defeat-=1
                        if Enemy.enemy_to_defeat==0:
                            print("you defeated all")
                            dead=True
                    else:
                        print("you lose,game over!")
                        dead=True
                else:
                    print("No such item in backpack go collect it")
            else:
                print(inhabitant.get_name() +" is not an prey")
        else:
            print("There is no one to fight")
    elif command =="hug":
        if inhabitant is not None:
            if isinstance(inhabitant,Enemy):
                print("you would'nt like that")

            else:
                inhabitant.hug()

        else:
            print("No one to hug")
    elif command == "take":
        if items is not None:
            print("You put "+ items.get_name() +"in your  backpack")
            backpack.append(items.get_name())
            current_room.set_item(None)
    elif command=="show":
        print("backpack contains the items:")

        for i in backpack:
            print(i)
Info.auth="AVI"
Info.credits()