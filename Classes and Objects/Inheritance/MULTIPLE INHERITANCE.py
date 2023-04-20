class Father():
    def __init__(self):
        self.fname = input("Enter Your Father Name : ")
        self.desgn = input("Enter your Father's occupation : ")
        self.fpropval = ["200 CR Bank balance", "150 Acres Land in Shamshabad", "2 Villas in Jubilee Hills"]

    def getfprop(self):
        print("Father Name : ", self.fname)
        print("Father Occupation : ", self.desgn)
        print("Your Father Property Includes : ", self.fpropval)

class Mother():
    def __init__(self):
        self.mname = input("Your Mother Name : ")
        self.desgn = input("Enter your Mother's occupation : ")
        self.mpropval = ["100 CR Bank balance", "150 Acres Land in Begumpet", "1 Villa in Anna Nagar"]

    def getmprop(self):
        print("Mother Name : ", self.mname)
        print("Mother Occupation : ", self.desgn)
        print("Your Mother Property Includes : ", self.mpropval)

class Yourself(Father, Mother):

    def __init__(self):
        self.name = input("Enter Your Name : ")

    def calprop(self):
        f1 = Father()
        m1 = Mother()
        yprop = []
        yprop.append(f1.fpropval)
        yprop.append(m1.mpropval)
        print("Your Property Includes : ", yprop)

Y = Yourself()
Y.calprop()
