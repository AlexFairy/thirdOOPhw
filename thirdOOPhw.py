class BudgetCategory():
    def __init__(self, category_name, initial_budget=0):
        self.__initial_budget = initial_budget #private attr
        self.category_name = category_name #public attr

    #Getter
    def get_allocated_budget(self):
        return self.__initial_budget
    
    #Setter
    def set_allocated_budget(self, new_budget):
        self.__initial_budget = new_budget
    
    #Getter
    def get_category_name(self):
        return self.category_name
    
    #Setter
    def set_category_name(self, new_category):
        self.category_name = new_category

    def add_expense(self, amount):
        if amount > 0:
            self.set_allocated_budget(self.get_allocated_budget() + amount)
            print(f"Expenses added: {amount}")
        else:
            print("Amount cannot be in the negatives!") 

    def display_category_summary(self, amount):
        if 0 < amount <= self.get_allocated_budget():
            self.set_category_name(self.get_allocated_budget() - amount)
            print(f"Display amount: {amount}")
        else:
            print("Insufficient budget")
        
food_category = BudgetCategory("Food", 500)
print(f"Bill Category: {food_category.get_category_name()} ")
print(f"Initial budget {food_category.get_allocated_budget()}")

food_category.add_expense(100)
print(f"Updated bill: {food_category.get_allocated_budget()}")
food_category.display_category_summary(200)