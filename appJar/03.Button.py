from appJar import gui
def press(btn):
    print(btn)
app=gui()
app.addButton("Hello World", press)
app.go()
