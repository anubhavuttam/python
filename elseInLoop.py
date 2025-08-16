# Python - else in Loop
# As you have learned before, the else clause is used along with the if statement.

# Python allows the else keyword to be used with the for and while loops too. The else block appears after the body of the loop. 
# The statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.

# Syntax

# for counter in sequence:
#     #Statements inside for loop block
# else:
#     #Statements inside else block

for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")


for y in range(5):
    print(y)
    if y == 4:
        break
else:
    print("ye print nahi hoga because of break in loop")