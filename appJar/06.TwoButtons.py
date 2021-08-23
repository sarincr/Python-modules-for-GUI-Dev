 
from appJar import gui
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("User:", usr, "Pass:", pwd)
app = gui()
app.addLabel("title", "Hello")
app.addButtons(["Submit", "Cancel"], press)
app.go()
