class Info():
    auth="anonymous"
    def __init__(self,title):
        self.title=title
    def welcome(self):
        print("Welcome to the game")

    @staticmethod
    def creation():
        print("This game is created using OOP's method")
    @classmethod
    def credits(cls):
        print("Thank you for playing the game")
        print("This game was created by "  + cls.auth)
