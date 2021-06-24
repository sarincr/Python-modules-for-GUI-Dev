from guizero import App, PushButton
def ClickHere():
    print("Button pressed")

root = App()
button = PushButton(root, command=ClickHere)
root.display()
