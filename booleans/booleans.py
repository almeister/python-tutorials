### Booleans

## What is a boolean type?
# bool is a type that represents one of two values; True or False
# Boolean values (True / False) are analagous to (on / off) or (1 / 0)
print("Type of value True is: " + str(type(True)))
print("Type of value False is: " + str(type(False)))


## Where are booleans used directly?
# In conditional statements, ie: if

# Using a boolean value
if (True):
    print("Execute on condition True")

# Using a boolean variable, x
x = True 
if (x):
    print("Execute on condition x")

# In while loops
while (True):
    print("Execute until the while loop is broken")
    break

y = True
while (y):
    print("Execute until x is False")
    y = False

# In function return statements
speed = 5
def is_moving() -> bool:
    # Type hinting the return type with '-> bool' is optional
    if (speed != 0):
        return True
        
    return False

print("is_moving() returns: " + str(is_moving()))


## How are booleans used?
# In evaluation of comparisons, eg: comparing numbers
# Zelda analogy
gems = 100
arrows_price = 30

if (gems > arrows_price):
    print("Execute if gems is greater than arrows_price")
    
if (gems >= arrows_price):
    print("Execute if gems is greater than or equal to arrows_price")

if (gems == 100):
    print("Execute if gems is equal to 100")
    # eg: Lucky number, player gets a special wallet
    
if (gems != 0):
    print("Execute if gems is not equal to 0")
    # eg: Show player where the store is


# In boolean operations, using boolean algebra
# Worms analogy
is_sheep_detonated = True
is_sheep_timer_complete = True
is_turn_over = False

if (not is_turn_over):
    # 'not' is equavilent to (is_turn_over == False)
    print("Execute if not is_turn_over")
    # eg: Player may continue to move their worm

if (is_sheep_timer_complete and not is_turn_over):
    print("Execute if is_sheep_timer_complete and not is_turn_over")
    # eg: Hide the timer and explode the sheep
    
if (is_sheep_detonated or is_sheep_timer_complete):
    print("Execute if either is_sheep_timer_complete or is_sheep_timer_complete")
    # eg: Hide the timer and explode the sheep
