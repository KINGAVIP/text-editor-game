class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )
    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation
    def get_conversation(self):
        print(self.conversation)
    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")
    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
class Enemy(Character):
    enemy_to_defeat=0
    def __init__(self,char_name,char_description):
        super().__init__(char_name,char_description)
        self.weakness=None
        Enemy.enemy_to_defeat+=1
    def anger(self):
        print("Woahhhhhhhhhh")
    def set_weakness(self,weakness):
        self.weakness=weakness
    def get_weakness(self):
        return self.weakness
    def attack(self,combat_item):
        if combat_item == self.weakness:
            print("The rival "+self.name+" lost")
        else:
            print(self.name+" wins")
class Friend(Character):
    def __init__(self,char_name,char_descripion):
        super().__init__(char_name,char_descripion)
        self.feeling=None

    def hug(self):
        print(self.name+"wants to hug you back")
    def get_name(self):
        return self.name