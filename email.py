email=str(input("enter the email:\n"))
a=0
num=0
alpha=0
stop=0
at=0
if(email.islower()):
    if(email[0].isalpha()):
        if(email.endswith("@gmail.com") or email.endswith("@yahoo.com") or email.endswith("@hotmail.com")or email.endswith("@email.com")):
            pos=email.find(".com")
            for i in range(0,pos):
                if(email[i].isalpha()):
                    alpha=alpha+1
                elif(email[i].isnumeric()):
                    num=num+1
                elif(email[i] in "@"):
                    at=at+1
                elif(email[i] in "_"):
                    a=a+1
                else:
                    stop=stop+1
        else:
            print("email must end with .com sytax invalid email\n")
    else:
        print("email must start with an alphabet\n")
else: 
    print("capital letters are not allowed\ninvalid email")
if( num>=1 and a<=1 and alpha>=7 and stop==0 and at==1):
    print("email is valid")
else:
    print("please look out the composition of letters \nemail is invalid")
