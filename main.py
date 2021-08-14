from browser import document, prompt, html, alert
#First page: upload .ren file button and create .ren file page
#first, lets create an upload button
cont = document[container]
fileTable = html.TABLE()
text = "Upload .ren file:"
fileInput = html.INPUT(type="file", name="fileUpload")
