# Assignment : Login system & Prime number finder

true_username = "admin"
true_password = "1234"
attempts = 0
maximum_attempts = 3

logged_in = False
def is_prime(n): 
   if n < 2: 
      return False
   for i in range(2, n): 
      if n%i == 0: 
         return False
   return True

for attempt in range(maximum_attempts):
  username_input = input("Enter username: ")
  password_input = input("Enter password: ")

  if username_input == true_username and password_input == true_password:
    print("Login is correct")
    logged_in = True
    break 
  else:
    left = maximum_attempts - attempt
    if left > 0:
      print("Login is incorrect")
if logged_in == True:
 number = int(input("Enter a number"))
 for i in range(number):
  if is_prime(i): 
    print(i)
else: 
   print("Account Locked")