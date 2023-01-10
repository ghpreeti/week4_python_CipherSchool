#raise error

class animal:
    def __init__(self,name):
        self.name =name

    
    def sound(self):
       raise NotImplementedError("you have to define this method in subclasses")


class dog(animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed

class cat(animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed      

    def sound(self):
        return "meow meow" 

     
doggy=dog('boony','pug')
print(doggy)