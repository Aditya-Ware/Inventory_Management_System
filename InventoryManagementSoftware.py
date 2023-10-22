import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

#data structures

class Stack:
    def __init__(self, size):
        self.size = size
        self.elements = [None] * self.size
        self.top = -1

    def isfull(self):
        if self.top == self.size - 1:
            return True
        return False

    def push(self, data, category):
        if self.isfull():
            print("Currently Supplier List is Full")
        else:
            self.top += 1
            self.elements[self.top] = {'data': data, 'category': category}

    def isempty(self):
        if self.top == -1:
            return True
        return False

    def pop(self):
        if self.isempty():
            print("Currently Supplier List is Empty")
        else:
            data = self.elements[self.top]
            self.top -= 1
            return data

    def display(self):
        if self.isempty():
            print("Currently Supplier List is Empty")
        else:
            for i in range(0, self.top + 1):
                print(self.elements[i])

#####################################################################

class Queue:
    def __init__(self, size):
        self.size = size
        self.elements = [None] * self.size
        self.front = -1
        self.rear = -1

    def isfull(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, data,type):
        if self.isfull():
            print("Customers Order Queue is Completed")
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.elements[self.rear] = {'data': data, 'type':type}

    def isempty(self):
        return self.front == -1

    def dequeue(self):
        if self.isempty():
            print("Customers Current all orders are empty")
        else:
            data = self.elements[self.front]
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
            return data

    def display(self):
        if self.isempty():
            print("Customers Current all orders are empty")
        elif self.rear >= self.front:
            print("Current Customer Order List", end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.elements[i], end=" ")
            print()
        else:
            print("Current Customer Order List", end=" ")
            for i in range(self.front, self.size):
                print(self.elements[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.elements[i], end=" ")
            print()

        if (self.rear + 1) % self.size == self.front:
            print("Customers Current all orders are empty")
#######################################################################

class Node_ll:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.next = None
        self.prev = None

# Linked List
class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, name, price):
        new_node = Node_ll(name, price)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete(self, old_name):
        current = self.head
        while current:
            if current.name == old_name:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                return
            current = current.next

    def update(self, old_name, new_name):
        current = self.head
        while current:
            if current.name == old_name:
                current.name = new_name
                return
            current = current.next


######################################################################################

class ProductNode:
    def __init__(self, sku, product_data):
        self.sku = sku  # Stock Keeping Unit
        self.product_data = product_data
        self.left = None
        self.right = None

    def insert(self, sku, product_data):
        if self.sku:
            if sku < self.sku:
                if self.left is None:
                    self.left = ProductNode(sku, product_data)
                else:
                    self.left.insert(sku, product_data)
            elif sku > self.sku:
                if self.right is None:
                    self.right = ProductNode(sku, product_data)
                else:
                    self.right.insert(sku, product_data)
        else:
            self.sku = sku
            self.product_data = product_data

    def search(self, sku):
        if self.sku is None:
            return None  # SKU not found
        if sku == self.sku:
            return self.product_data  # Found the product
        elif sku < self.sku:
            if self.left:
                return self.left.search(sku)  # Search in the left subtree
        else:
            if self.right:
                return self.right.search(sku)  # Search in the right subtree

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(f"SKU: {self.sku}, Product Data: {self.product_data}")
        if self.right:
            self.right.inorder()


###################################################################
            
class CustomerGraph:
    def __init__(self):
        self.graph = {}

    def add_customer(self, customer):
        if customer not in self.graph:
            self.graph[customer] = []

    def add_relationship(self, customer1, customer2):
        self.add_customer(customer1)
        self.add_customer(customer2)
        self.graph[customer1].append(customer2)

    def find_influential_customers(self):
        in_degrees = {}
        for customer in self.graph:
            in_degrees[customer] = 0

        for customer1 in self.graph:
            for customer2 in self.graph[customer1]:
                in_degrees[customer2] += 1

        influential_customers = [customer for customer, in_degree in in_degrees.items() if in_degree > 1]
        return influential_customers


#######################################################################
#database connection
db = client['Inventory_Management']
suppliers_collection = db['Supplier']
order_collection = db['Order']
Product_Management_collection = db['Product_management']
Inventory_Tracking_collection = db['Inventory_tracking']
Customer_Data_collection = db['Customer_data']

########################################################################
Add_Supplier = Stack(20)
New_order = Queue(20)
product = linked_list()
def can_process_order(order_type):
    
    matching_suppliers = suppliers_collection.count_documents({'category': order_type})    
    return matching_suppliers > 0

#inventory management Code
print("Welcome User enter your serial number to access the required service")
print("1. Supplier Management System")
print("2. Order Processing System")
print("3. Product Management")
print("4. Inventory Tracking")
print("5. Customer Database")
option = int(input(" -> "))
while True:

    if option == 1:
        
        #Supplier Management System

        
        print("User you have entered in Supplier Management System choose below serial number to perform required function")
        print("1. Add new supplier")
        print("2. Update existing data")
        print("3. Remove supplier")
        print("4. List of all Supplier")
        option_stack = int(input("Enter Your Input Serial Number"))
        
        if option_stack == 1:
                #i/o logic most probably if statement condition 1 (add new)
                Supplier_Name = input("Enter Your supplier Name and category: ")
                supplier_data, supplier_category = Supplier_Name.split()
                Add_Supplier.push(supplier_data, supplier_category)

                print("New Supplier Added successfully")
                suppliers_collection.insert_one({'data': supplier_data, 'category': supplier_category})
        elif option_stack==2:

                #i/o logic most probably elif statement condition 2(update existing)
                Supplier_Name_new = input("Enter update of supplier name")
                Supplier_Name_old = input("Enter supplier old name")
                Add_Supplier.update(Supplier_Name_new, Supplier_Name_old)
                print("Supplier data has been updated Successfully")
        elif option_stack==3:

                #i/o logic for removing recent supplier condition 3 (remove)
                Add_Supplier.pop()
                print("Latest SUpplier has been removed")
        elif option_stack==4:

                #i/o logic for displaying all supplier name condition 4 (display)
                Add_Supplier.display()
        else:
                #exception handling
                print("PLease enter valid input")

    elif option==2:
        #order processing system

        
        print("User you have entered in Order Management System choose below serial number to perform required function")
        print("1. To put up a Order")
        print("2. To remove a Order")
        print("3. To view all Orders")
        option_queue = int(input("Enter Your Input Serial Number"))
        
        if option_queue==1:
                #putting up a order i/o logic
                order_data = input("Enter Your order and type: ")
                order_data, order_type = order_data.split()
                if can_process_order(order_type): 
                    New_order.enqueue(order_data, order_type)
                    print("Your order is successfully placed")
                    order_collection.insert_one({'data': order_data, 'type': order_type})
                else:
                    print("Sorry, the order can't be processed")
        elif option_queue==2:

                #to dequeue order i/o logic
                New_order.dequeue()
                print("Your first order is processed and and out for delivery")
        elif option_queue==3:

                    # to display all order i/o logic
                    New_order.display()
        else:

                #exception handling
                print("PLease enter valid input")

    elif option==3:
        #Product management

       
        print("User you have entered in Product Management System choose below serial number to perform required function")
        print("1. To Add new Product")
        print("2. To update product Name")
        print("3 To delete any Product")
        option_dll = int(input("Enter Your Input Serial Number"))
       
        if option_dll==1:

                #add new product i/o logic
                name = input("Enter name of product")
                price = input("Enter price of product")
                product.add(name,price)
                print("Product details are successfully  added")
        elif option_dll==2:

                # update the product name
                old_name = input("Enter name of old product")
                new_name = input("Enter name of new product")
                product.update(old_name,new_name)
                print("Product details are successfully updated")
        elif option_dll==3:

                #delete product detail
                position = input("Enter serial number of product")
                product.delete(position)
        else:
                #exception handling
                print("PLease enter valid input")

    elif option==4:
         #inventory tracking
         print("User you have entered in Inventory Tracking System choose below serial number to perform required function")
         print("1. To Add product SKU & Name")
         print("2. To find find product")
         print("3. To view full inventory")
         option_bst = int(input("Enter your serial number"))
         
         if option_bst==1:

                #logic to trigger bst
                sku = input("Enter SKU number")
                product_data = input("Enter Product Name")
                #first time node creation logic
                Sku_inventory =  ProductNode(sku,product_data)
                print("Process Successfully Added")
                #after that this logic for insertion
                Sku_inventory.insert(sku,product_data)
         elif option_bst==2:
                
                #find product using sku
                sku_search = input("Enter SKU number")
                Sku_inventory.search(sku_search)
         elif option_bst==3:
                
                #inorder display
                Sku_inventory.inorder()
         else:
                        #exception handling
                print("PLease enter valid input")