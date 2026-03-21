# x = "Hello " "world" "go"

# print(x)

# if (
#     2 + 2
#     and 2 + 2
#     and 2 + 2
#     and 2 + 2
#     and 2 + 2
#     and 2 + 2
#     and 2 + 2
#     and 2 + 2
#     and 2 + 2
#     and 2 + 2
#     and 2 + 2
# ):
#     print("Yes")

# x = """erjfierjfer
# ergergerger
# regregerg
# regerger egerg ergerg
# rferg"""

# print(x)


# x = r"C:\\Users\name\Desktop"

# print(x)
# ////////////////////////////////////////////////////////////////////
# name = "Alex"
# id = 637748
# # message = "Helllo {}, your id is: {}".format(name, id)
# message = f"Helllo {name}, your id is: {id}"

# message = f"""gfb
# {name}
# gf"""

# print(message)

# ///////////////////////////////////////////////////////////////////////////


name = "Alex"
rating = 4.9523489

message = f"{name} your rating is: {rating:.1f}"

print(message)
# /////////////////////////////////////////////////////////////////////////

name = "Alex"
rating = 4.9523489

message = "{name} your rating is: {rating:.1f}"

message = message.format(name=name, rating=rating)

print(message)
