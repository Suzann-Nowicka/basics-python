# course = "Python for Beginners"
# print(len(course))
# course.upper

# print(course.replace('P','J'))
# print('Python' in course) #in operator produces value True or False


# x = 10
# x = x + 3
# x += 3 # we are incrementing the number (+= augumented asigment or enchanced assingn operator
# print(x)


# #Math functions
# x = 10 + 3 *2 # =60 it's an operator precedence
# x = (10 + 3) *10 -3 # 

# # 
# #parenthesis
# X = 2** 3 # 4 /exponentation 
# X = 2** 3 # addition or subtraction

# x = 2.9
# print(round(x)) #it will bring always positive values
# print(abs(x)) #it will bring always positive values

# # to make an advance mathematical calculation we need to imprort math module
# import math

# print(math.ceil(2.9))
# print(math.floor(2.9))
# #we will have access to a module's methods using . 
# #we can read about all available methods for certain module by readind python documentation

#IF STATEMENTS IN PYTHON
# is_hot = False
# is_cold = False

# if is_hot:
# 	print("It's a hot day")
# 	print("Drink plenty of water")
# elif is_cold:
# 	print("It's a cold day")
# 	print("Wear warm clothes")
# else:
# 	print("It's a lovely day")
# print("Enjoy your day")


# house_price = 1000_000
# Buyer_has_a_good_credit = False

# if Buyer_has_a_good_credit:
# 	down_payment = 0.1 * house_price
# else:
# 	down_payment = 0.2 * house_price
# print(f"down_payment: ${down_payment}")

# #LOGICAL OPERATORS IN PYTHON/ if statements
# # 
# # has_high_incom = False
# has_good_credit = False
# has_criminal_record = True

# # if has_high_incom and has_good_credit:
# # 	print("Eligible for loan")
# # else:
# # 	print("Not eliglible for loan")
# # print("be niece for client")


# # if has_high_incom or has_good_credit:
# # 	print("Eligible for loan")
# # else:
# # 	print("Not eliglible for loan")

# if has_good_credit and not has_criminal_record:
# 	print("Eligible for loan")
# else:
# 	print("Not eligible for loan")

#COMPARISON OPERATORS / for compareoperator with a value
 
temperature = 30.01


if temperature > 30:
 	print("It's a hot day")
elif temperature == 30:
	print("It will be a hot day")
else:
 	print("It's not a hot day")