from browser import document, prompt, html, alert
import secrets
from argon2 import PasswordHasher
ph = PasswordHasher()
signupbool = True
signedin = False
cont = document["container"]
newdiv = html.DIV(id = "newdiv")
signin = html.BUTTON("Sign Up Page")
login = html.BUTTON("Log In Page")
def switchlogin(_):
    signupbool = False
def switchsignin(_):
    signupbool = True
def signup(_):
    username = cont["signupdiv"]["signupusername"].value
    password = cont["signupdiv"]["signuppassword"].value
    confirm = cont["signupdiv"]["signupconfirm"].value
    if (not username | not password | not confirm) | (username == "Username" | password == "Password" | confirm == "Confirm Password"):
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
lastsignbool = False
while not signedin:
    if lastsignbool != signupbool:
        #this means that the page loaded has changed. 
        #therefore, we must redraw the page
        if signupbool:
            #we have to redraw the sign-up page
            signupdiv = html.DIV(id = "signupdiv")
            signupusername = html.INPUT(type="text", name="username", value="Username")
            signuppassword = html.INPUT(type="text", name="password", value="Password")
            signupconfirm = html.INPUT(type="text", name="confirm", value="Confirm Password")
            signupdiv <=  signupusername + html.BR()
            signupdiv <=  signuppassword + html.BR()
            signupdiv <=  signupconfirm + html.BR()
            submitsignup = html.BUTTON("Sign Up")
                                  
            
