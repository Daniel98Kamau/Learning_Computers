class User:
    age = int
    def __init__(self):
        self.time = 'time'
        self.name = 'Name'
        self.occupation = 'Ocupation'
    def enterlibrary(self):
        print('Welcome to the library.')
    def staylibrary(self):
        print('You are in the library.')
    def leavelibrary(self):
        print('You are leaving, Good Bye!')
    def searchmaterial(self):
        search_keyword = input('')
        if 'search_keyword' in 'material_title' or 'contributor_name':
            return location
        else:
            print('Material not in library, input an alternative search_keyword')

class Librarian(User):
    def __init__(self):
        User.__init__(self)
        self.jobID = ''
        self.password = ''
        self.occupation = 'librarian'
    def open_library(self):
        pass
    def updatecatalogue(self):
        pass
    def arrangematerial(self):
        pass
    def lendmaterial(self):
        pass
    def recieveborrowed(self):
        pass
    def registermembers(self):
        pass
    def managechildren(self):
        pass
    def closelibrary(self):
        pass

class Guest(User):
    def __init__(self):
        User.__init__(self)
        self.age = int()
    def isamember(self,x):
        if x is True:
            print('User is a member')
        elif x is False:
            print('User is not a member')

class Member(Guest):
    def __init__(self):
        Guest.__init__(self)
    def borrow_material():
        pass
    def return_material():
        pass
    def renew_membership():
        pass

class Nonmember(Guest):
    def __init__(self):
        Guest.__init__(self)
    def apply_membership(self, age):
        if self.age > 18:
            print('You can apply for membership')
        else:
            print('You cannot apply for membership')
    def child(self,age):
        if self.age<10:
            print("User proceed to Children's area")
    def children_area():
        pass

user1= Librarian()
user1.staylibrary()
user2= Nonmember()
user2.apply_membership(35)
user3= Member()
user3.name = 'David'
print(user3.name)
user4= Nonmember()
user4.child(12)
user5 = Guest()
user5.isamember(False)
user6= Nonmember()
user6.apply_membership(40)        

        

    
