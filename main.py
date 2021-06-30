from browser import document, prompt, html, alert
cont = document["container"]
newdiv = html.DIV(id = "newdiv")
def clearchildren(div):
    del cont[div]
button1 = html.BUTTON("Clear me! (hopefully)")
button1.bind("click", clearchildren(newdiv))
newdiv <= button1
cont <= newdiv
