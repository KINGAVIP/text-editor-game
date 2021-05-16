class Item():
    def __init__(self,item_name):
        self.name=item_name
        self.description=None
    def set_name(self,item):
        self.name=item
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def set_description(self,desc):
        self.description=desc
    def describer(self):
        print("The [" + self.name + "] is here - " + self.description)