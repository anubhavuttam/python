#default arguments:
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")

name("Anubhav", "", "Uttam")


#Keyword arguments:
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")\


#Required arguments:
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

#name("Peter", "Quill") #error

name("Peter", "Ego", "Quill")


#Variable Length arguments:

#Arbitrary Arguments:
def name(*name):
    print(type(name))
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")


#Keyword Arbitrary Arguments:
def name(**name):
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")

#return Statement
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))