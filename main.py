from browser import document, prompt, html, alert
cont = document["container"]
newdiv = html.DIV(id = "newdiv")
def clearchildren():
    del cont[newdiv]
button1 = html.BUTTON("Clear me! (hopefully)")
newdiv <= button1
newdiv[button1].bind("click", clearchildren())
cont <= newdiv
