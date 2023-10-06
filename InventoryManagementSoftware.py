#data structures

class stack:
    def __init__(self,size):
        self.size = size
        self.elements= [None]*self.size
        self.top = -1

    def isfull(self):
        if(self.top ==self.size - 1):
            return true
        return false
    def push(self,data):
       if(self.isfull()):
            print("Currently Supplier List is Full")
        else:
            self.top+=1
            self.elements[self.top] = data
    def isempty(self):
        if(self.top == -1):
            return true
        return false
    def pop(self):
        if(self.isempty()):
            print("Currently Supplier List is Empty")
        else:
           data = self.elements[self.top]
           self.top -= 1
    
    def display(self):
        if(self.isempty()):
			print("Currently Supplier List is Empty")
		else:
			for i in range(0,self.top):
				print(self.elements[i])

#####################################################################

class queue:
    def __init__(self,size):
        self.size = size        
        self.elements = [None]*self.size
        self.front = -1
        self.rear = -1

    def isfull(self):
        if((self.rear +1)%self.size == self.size - 1):
            return true:
        return false    
    def enqueue(self,data):
        if(self.isfull()):
            print("Customers Order Queue is Completed")
        elif(self.front = -1):
            self.front = 0 
            self.rear = 0
            sel.elements[self.rear] = data
        else:
            self.rear = (self.rear+1)%self.size
            self.elements[self.rear] = data
    
    def isempty(self):
        if(self.front == -1):
            return true
        return false
    def dequeue(self):
        if(isempty()):
            print("Customers Current all orders are empty")
        elif(self.front == self.rear):
            data = self.elements[self.front]
            self.front = -1
            self.rear = -1
            return data
        else:
            data = self.elements[self.front]
            self.front = (self.front+1)%self.size
            return data

    def display(self):
        if(isempty()):
             print("Customers Current all orders are empty")
        elif (self.rear >= self.front):
            print("Current Customer Order List",  end = " ")
                                              
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end = " ")
            print ()
 
        else:
            print ("Current Customer Order List",  end = " ")
            for i in range(self.front, self.size):
                print(self.queue[i], end = " ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end = " ")
            print ()
 
        if ((self.rear + 1) % self.size == self.front):
            print("Customers Current all orders are empty")

#######################################################################

class Node_ll:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        self.next = None
        self.prev = None

class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    def add(self,name,price):
        new_node = Node_ll(name,price)
        if(self.head == None):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete(self,position):
        index = int(position)
        node = self.get_node(index)
        if node is None:
            print("No such index found")
            return None
        elif node.prev is None:
            self.head = node.next
            self.head.prev = None
        elif node.next is None:
            node.prev = None
            self.tail=node.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.next 

    def update(self,old_name,new_name):
        current = self.head
        while current:
            if(current == old_name):
                current = new_name
                return 
            else:
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
        influential_customers = []
        for customer in self.graph:
            in_degree = 0
            for other_customer in self.graph:
                if customer != other_customer and customer in self.graph[other_customer]:
                    in_degree += 1
            if in_degree > 1:
                influential_customers.append(customer)
        return influential_customers

    def find_customer_clusters(self):
        visited = set()
        clusters = []

        def dfs(customer, cluster):
            visited.add(customer)
            cluster.append(customer)
            for related_customer in self.graph[customer]:
                if related_customer not in visited:
                    dfs(related_customer, cluster)

        for customer in self.graph:
            if customer not in visited:
                cluster = []
                dfs(customer, cluster)
                clusters.append(cluster)

        return clusters


########################################################################

#inventory management Code

#############################################################
#Supplier Management System

Add_Supplier = stack(20)
option_stack = input(parseInt("Enter Your Input Serial Number"))
#i/o logic most probably if statement condition 1 (add new)
Supplier_Name = input("Enter Your supplier Name")
Add_Supplier.push(Supplier_Name)
print("New Supplier Added successfully")
#i/o logic most probably elif statement condition 2(update existing)
Supplier_Name_new = input("Enter update of supplier name")
Supplier_Name_old = input("Enter supplier old name")
Add_Supplier.update(Supplier_Name_new, Supplier_Name_old)
print("Supplier data has been updated Successfully")
#i/o logic for removing recent supplier condition 3 (remove)
Add_Supplier.pop()
print("Latest SUpplier has been removed")
#i/o logic for displaying all supplier name condition 4 (display)
Add_Supplier.display()
#exception handling
print("PLease enter valid input")
#######################################################################

#order processing system

New_order = queue(20)
option_queue = input(parseInt("Enter Your Input Serial Number"))
#putting up a order i/o logic
order_data = input("Enter Your order")
New_order.enqueue(order_data)
print("Your order is succcessfully placed")
#to dequeue order i/o logic
New_order.dequeue()
print("Your first order is processed and and out for delivery")
# to display all order i/o logic
New_order.display()
#exception handling
print("PLease enter valid input")

######################################################################

#Product management

product = linked_list()
option_dll = input(parseInt("Enter Your Input Serial Number"))
#add new product i/o logic
name = input("Enter name of product")
price = input("Enter price of product")
product.add(name,price)
print("Product details are successfully  added")
# update the product name
old_name = input("Enter name of old product")
new_name = input("Enter name of new product")
product.update(old_name,new_name)
print("Product details are successfully updated")
#delete product detail
position = input("Enter serial number of product")
product.delete(position)

######################################################################

#inventory tracking
#logic to trigger bst
sku = input("Enter SKU number")
product_data = input("Enter Product Name")
#first time node creation logic
Sku_inventory =  ProductNode(sku,product_data)
print("Process Successfully Added")
#after that this logic for insertion
Sku_inventory.insert(sku,product_data)

#find product using sku
sku_search = input("Enter SKU number")
Sku_inventory.search(sku_search)

#inorder display
Sku_inventory.inorder()

###################################################################

















#driver code