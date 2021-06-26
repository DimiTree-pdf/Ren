from browser import document, prompt, html, alert
cont = document["container"]
def clearchildren(obj):
    obj.clear()
button1 = html.BUTTON("Clear me! (hopefully)")
cont <= button1
cont[button1].bind("click", clearchildren(cont))
