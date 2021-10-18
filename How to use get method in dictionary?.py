# The get() method on dictionaries
# and its "default" argument

user_name = {
    1: "Elshad",
    2: "Renad",
    3: "Edy",
}

def greet(userid):
    print(f"Hi {user_name.get(userid, 'there')}!")

greet(1)
# "Hi Elshad!"
greet(4)
# "Hi there!"







