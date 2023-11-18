from datetime import datetime

class Student:
    def __init__(self,name,dob,branch):
        self.name=name
        self.dob=dob
        self.branch=branch
        self.credits=0
    
    def get_age(self):
        return (datetime.now()-self.dob).days // 365
    
    def set_credits(self,value):
        self.credits+=value
    
    def get_credits(self):
        return self.credits
    



# if __name__=="__main__":
#     s=Student('Nitesh',datetime(2000,1,1),'Admin')
#     print(s.get_age())
