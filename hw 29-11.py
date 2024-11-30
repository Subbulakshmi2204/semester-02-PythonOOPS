class Library:
    def __init__(self,lib_name,lib_address):
        self.lib_name=lib_name
        self.lib_address=lib_address
    def displayLibraryInfo(self):
        print(f"Name of Library:{self.lib_name}\nLibrary Address:{self.lib_address}")
class Member:
    def __init__(self,mem_name,mem_contact):
        self.mem_name=mem_name
        self.mem_contact=mem_contact
    def displayMemberInfo(self):
        print(f"Name of Members:{self.mem_name}\nMember Contact:{self.mem_contact}")
class Librarymanagement(Library,Member):
    def __init__(self,lib_name,lib_address,mem_name,mem_contact):
        super().__init__(lib_name,lib_address)
        Member.__init__(self,mem_name,mem_contact)
    def display(self):
        self.displayLibraryInfo()
        self.displayMemberInfo()
lib=Librarymanagement("Ambedkar","Perumal Kovil Street","Subbu",9382835213)
lib.display()


class Restaurant:
    def __init__(self,Restaurant_name,Items):
        self.Restaurant_name=Restaurant_name
        self.Items=Items
    def displayRestaurantInfo(self):
        print(f"Name of the Restaurant:{self.Restaurant_name}\nItems Available:{self.Items}")
class Delivery:
    def __init__(self,deliveryboy_name,contact):
        self.deliveryboy_name=deliveryboy_name
        self.contact=contact
    def displayDeliveryInfo(self):
        print(f"Name of the delivery boy:{self.deliveryboy_name}\nBoy's Contact:{self.contact}")
class Order(Restaurant,Delivery):
    def __init__(self,Restaurant_name,Items,deliveryboy_name,contact):
        super().__init__(Restaurant_name,Items)
        Delivery.__init__(self,deliveryboy_name,contact)
    def display(self):
        self.displayRestaurantInfo()
        self.displayDeliveryInfo()
Del=Order("Northern Chappathis","Noodles,Chappathi,Naan,Paneer 65","Mukesh",7418406444)
Del.display()
