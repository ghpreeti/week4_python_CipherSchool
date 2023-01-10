class mobile:
    def __init__(self,name):
        self.name=name

class mobilestore:
    def mobile_store(self):
        self.mobile=[]    

    def add_mobile(self,new_mobile):
        if isinstance(new_mobile,mobile):
            self.mobile.append(new_mobile)
        else:
                 raise TypeError("new mobile should be object of mobile class")


oneplus=mobile('oneplus 6')
samsung = 'samsung galaxy s8'
mobostore = mobilestore()
mobostore.add_mobile(oneplus)
# print(mobostore.mobile)
