blocked=["admin","root","moderator"]
username=input("enter username: ")
if username not in blocked:
    print("username is avaliable!")
else:
    print("username is blocked")