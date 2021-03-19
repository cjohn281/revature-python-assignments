# 1
def get_max(num1, num2):
  return max(num1, num2)



# 2
def fizz_buzz(num):
  if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
  elif num % 3 == 0:
    print("Fizz")
  elif num % 5 == 0:
    print("Buzz")
  else:
    print(num)



# 3
def speed_check(speed):
  if speed <= 70:
    print("Ok")
  elif speed > 70:
    over = speed - 70
    points = over // 5
    print("Points %d" % points)

  if points > 12:
    print("License suspended")



# 4
def showNumbers(limit):
  for x in range(limit + 1):
    if x % 2 == 0:
      print("%d EVEN" % x)
    else:
      print("%d ODD" % x)



# 5
def sum_multiples_of_3_and_5(limit):
  sum = 0
  for x in range(limit + 1):
    if x % 3 == 0 or x % 5 == 0:
      sum = sum + x

  return sum



# 6
def show_stars(rows):
  for x in range(1, rows + 1):
    print(x * "*")



# 7
def primes(limit):
  for x in range(limit + 1):
    if is_prime(x):
      print(x)



# Bonus
def is_prime(num):
  if num <= 1:
    return False

  if num <= 3:
    return True
  
  if num % 2 == 0 or num % 3 == 0:
    return False

  i = 5
  while(i * i <= num):
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i = i + 6

  return True
