from browser import document, prompt, html, alert
cont = document["container"]
newdiv = html.DIV(id = "newdiv")
def clearchildren(_):
    del cont[newdiv]
    testdiv = html.DIV(id = "testdiv")
    button2 = html.BUTTON("It worked!")
    button2 <= testdiv
    testdiv <= cont
button1 = html.BUTTON("Clear me! (hopefully)")
button1.bind("click", clearchildren)
newdiv <= button1
cont <= newdiv
