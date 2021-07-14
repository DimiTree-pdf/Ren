from browser import document, prompt, html, alert
#import secrets
#from argon2 import PasswordHasher
#ph = PasswordHasher()
signupbool = True
signedin = False
cont = document["container"]
signinscreendiv = html.DIV(id = "signinscreendiv")    
signupbutton = html.BUTTON("Sign Up Page")
loginbutton = html.BUTTON("Log In Page")
def switchlogin(_):
    signupbool = False
     #_.stopPropagation()
def switchsignup(_):
    signupbool = True
    #_.stopPropagation()
def signup(_):
    username = cont["signupdiv"]["signupusername"].value
    password = cont["signupdiv"]["signuppassword"].value
    confirm = cont["signupdiv"]["signupconfirm"].value
    if (not username | not password | not confirm):
      alert("You must enter a username and a password")
    #TODO: check if username is taken
    if confirm != password:
       alert("Passwords do not match!")
    salt = secrets.token_hex(64)
    hashedpassword = ph.hash(password + salt)
    #this part of the code is where we would store the username, salt, and hashed password in a database
    #we don't have a working database yet so we'll just leave this part blank for now
    #TODO: store account information in db 
    signedin = True
    #_.stopPropagation()
lastsignbool = True
loginbutton.bind("click", switchlogin) 
signupbutton.bind("click", switchsignup)
signinscreendiv <= signupbutton + html.BR()
signinscreendiv <= loginbutton
cont <= signinscreendiv
signupdiv = html.DIV(id = "signupdiv")
usernamemsg = html.DIV("Enter username")
passwordmsg = html.DIV("Enter password")
confirmmsg = html.DIV("Confirm password")
signupusername = html.INPUT(type="text", name="Username", value="")
signuppassword = html.INPUT(type="text", name="Password", value="")
signupconfirm = html.INPUT(type="text", name="Confirm Password", value="")
usernamediv = html.DIV(id = "undiv")
passworddiv = html.DIV(id = "pwdiv")
confirmdiv = html.DIV(id = "cfmdiv")
usernamediv <= usernamemsg + html.BR() + signupusername
passworddiv <= passwordmsg + html.BR() + signuppassword
confirmdiv <= confirmmsg + html.BR() + signupconfirm
#when mouse clicks outside of inputs, the filler text should be replaced
#def fillsignupinputs(_):
    #for child in signupdiv:
        #alert(child.class_name)
#bind click to inputs so that they delete their text when clicked in
#signupdiv.bind("click", fillsignupinputs)
signupdiv <=  usernamediv + html.BR()
signupdiv <=  passworddiv + html.BR()
signupdiv <=  confirmdiv + html.BR()
submitsignup = html.BUTTON("Sign Up")
#submitsignup.bind("click", signup)
signupdiv <= submitsignup
cont <= signupdiv
#while not signedin:
#    if lastsignbool != signupbool:
        #this means that the page loaded has changed. 
        #therefore, we must redraw the page
#        if signupbool:
            #we have to redraw the sign-up page
#           del cont[logindiv]
#           signupdiv = html.DIV(id = "signupdiv")
#           signupusername = html.INPUT(type="text", name="username", value="Username")
#           signuppassword = html.INPUT(type="text", name="password", value="Password")
#           signupconfirm = html.INPUT(type="text", name="confirm", value="Confirm Password")
#           signupdiv <=  signupusername + html.BR()
#           signupdiv <=  signuppassword + html.BR()
#           signupdiv <=  signupconfirm + html.BR()
#           submitsignup = html.BUTTON("Sign Up")
#           submitsignup.bind("click", signup)
#           signupdiv <= submitsignup
#           cont <= signupdiv
            
