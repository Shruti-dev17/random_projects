class phonebook:
    phone_directory =[]

    def __init__(self,name,phone_no):
        self.name=name
        self.phone_no=phone_no
        
        phonebook.phone_directory.append(self)

    def show_contact(self):
        print(f"Name = {self.name}-------> Phone number: {self.phone_no}")

    @classmethod
    def show_all(cls):
        if len(cls.phone_directory) == 0:
            return("no contacts found")
        else:
            for i in cls.phone_directory:
                i.show_contact()
            
    @classmethod
    def search(cls,search):
        for i in cls.phone_directory:
            if i.name.lower() == search.lower():
                return i.phone_no
       

    @staticmethod
    def validate(n):
        if len(n)==10 and n.isdigit():
            return True
        else:
            print("invalid Phone number")

no_contacts= int(input("how many contacts do you want to add: "))
for i in range(no_contacts):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        if phonebook.validate(phone):
            phonebook(name,phone)
        else:
            print("Invalid Input!! Try again.")
choose = input("what do you wish to do: ")

if choose.lower() == "show all":
        phonebook.show_all()
        
elif choose.lower() == "search":
        print(phonebook.search(input("who are you searching for?: ")))
        
else: 
        print("Invalid choice")