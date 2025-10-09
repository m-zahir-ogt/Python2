#it is a callBack example. customer in restaurant put order and waiter deliver food
def checkFoodExistence(food_name:str)->bool:
    arr_foods=["Pizza", "Pasta", "Döner"]
    if food_name in arr_foods:
        return True
    else:
        return False
 
def orderFood(food_name:str, checkFoodExistence):
    is_food_exists = checkFoodExistence(food_name)
    if is_food_exists == True:
        print(f"your {food_name} deliver soon!")
    else:
        print(f"sorry, we have no such food called {food_name}")
    checkFoodExistence(food_name)
 
#-- actual program use upper defined methods --#
order_string = input("what is your order?")
orderFood(order_string,checkFoodExistence)