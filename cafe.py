# Cafe Manmagement System

class cafeManagementSystem:
    def __init__(self):
        # Menu
        self.menu = {
            # Drinks
            "Hot Coffee": 40,
            "Cold Coffee": 150,
            "Black Coffee": 60,
            "Cappuccino":90,
            "Espresso":80,
            "Latte": 110,
            "Iced Latte": 160,
            "Black Tea": 20,
            "Milk Tea": 20,
            "Lemon Tea": 35,
            "Masala Tea": 50,
            "Lemon Iced Tea": 120,
            # Sandwiches
            "Veg Sandwich": 20,
            "Cheese Sandwich": 30,
            "Egg Sandwich": 35,
            "Chicken Sandwich": 40,
            # Burgers
            "Chicken Burger": 250,
            "Veg Burger": 150,
            # Pizza
            "Margherita Pizza": 100,
            "Farmhouse Pizza": 260,
            "Chicken Sausage Pizza": 200,
            "Paneer Pizza": 100,
            # Cookies
            "Chocolate Cookie": 15,
            "Cashewnut Cookie": 30,
            "Coconut Cookie": 20,
            # Pastry
            "Red Velvet Pastry": 45,
            "Choco Lava Pastry": 90,
            "Choco Chips Pastry": 25,
            "BlackForest Pastry": 45,
            "Butterscotch Pastry": 25,
            "Strawberry Pastry": 35,
            "Mango Pastry": 35
        }
        self.orderList = []
        self.orderQuantity = []
        self.gstAndRestaurantCharges = 20.65
        self.platformFee = 10

    def displayMenu(self):
        print("!-----------Welcome To Cafe Desi----------!")
        print(">-------Our Menu------<")
        print("------Beverages------\n Hot Coffee: 40\n Cold Coffee: 150\n Black Coffee: 60\n Cappuccino:90\n Espresso:80\n Latte: 110\n Iced Latte: 160\n Black Tea: 20\n Milk Tea: 20\n Lemon Tea: 35\n Masala Tea: 50\n Lemon Iced Tea: 120\n ------Sandwiches------\n Veg Sandwich: 20\n Cheese Sandwich: 30\n Egg Sandwich: 35\n Chicken Sandwich: 40\n ------Burgers------\n Chicken Burger: 250\n Veg Burger: 150\n ------Pizza------\n Margherita Pizza: 100\n Farmhouse Pizza: 260\n Chicken Sausage Pizza: 200\n Paneer Pizza: 100\n ------Cookies------\n Chocolate Cookie: 15\n Cashewnut Cookie: 30\n Coconut Cookie: 20\n ------Pastry------\n Red Velvet Pastry: 45\n Choco Lava Pastry: 90\n Choco Chips Pastry: 25\n BlackForest Pastry: 45\n Butterscotch Pastry: 25\n Strawberry Pastry: 35\n Mango Pastry: 35")

    def takeOrder(self):
        while True:
           userInput = input("What would you like to order and how many, Sir: ") 
           if userInput.lower() == "no":
            break
           try:
            item, quantity = userInput.split(':')
            item = item.strip()
            quantity = int(quantity.strip())
            if item not in self.menu:
                print(f"Sorry, {item} is not on the menu.")
                continue
            else:
                self.orderList.append((item))
                self.orderQuantity.append((quantity))
           except ValueError:
            print("Invalid format! Please use 'Item Name:Quantity'.")
            continue

    def generateBill(self):
        totalBill = 0
        print("\n-----------------------Bill--------------------")
        print("Item----------------Quantity--------------Price")
        for item, quantity in zip(self.orderList, self.orderQuantity):
            price = self.menu[item] * quantity
            print(f"{item}:   {quantity} =   {price}")
            totalBill += price
        print(f"GST and restaurant charges: {self.gstAndRestaurantCharges}")
        print(f"Platform Fees: {self.platformFee}")
        totalBill += self.gstAndRestaurantCharges + self.platformFee
        print("-------------------------------------------")
        print(f"Total Bill:    {totalBill}")

    def run(self):
        self.displayMenu()
        self.takeOrder()
        self.generateBill()
    
if __name__ == "__main__":
    obj = cafeManagementSystem()
    obj.run()