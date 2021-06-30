from browser import document, prompt, html, alert
cont = document["container"]
newdiv = html.DIV(id = "newdiv")
def clearchildren():
    del cont[newdiv]
    x = 1
button1 = html.BUTTON("Clear me! (hopefully)")
button1.bind("click", clearchildren())
newdiv <= button1
cont <= newdiv
