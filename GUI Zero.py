from guizero import App, PushButton, App, Combo, Text, MenuBar, Waffle, Picture

def file_function():
    print("File option")
    
def edit_function():
    print("Edit option")

def start():
    start_button.enable()
    stop_button.enable()

def stop():
    start_button.enable()
    stop_button.disable()
    
def reverse():
    start_button.enable()
    stop_button.disable()

def t_left():
    t_left_button.enable()
    stop_button.disable()

def t_right():
    start_button.enable()
    stop_button.disable()

def update_bg():
    app.bg = bg_combo.value

def update_text():
    app.text_color = text_combo.value
    
colors = ["Black", "White", "Red", "Green", "Blue"]

app = App()
app.title = "JR Droid's"
text = Text(app, text="STRONK TONK ALPHA v.1")
text = Text(app, text="Hit `X` to exit full Screen")

app.set_full_screen("x")

menubar = MenuBar(app,
                  toplevel=["File", "Edit"],
                  options=[
                      [ ["New", file_function], ["Quit", file_function] ],
                      [ ["Copy", edit_function], ["Paste", edit_function] ]
                  ])

app.bg = "black"
app.text_color = "green"

title1 = Text(app, text="Background Color")
bg_combo = Combo(app, options=colors, selected=app.bg, command=update_bg)

title2 = Text(app, text="Text Color")
text_combo = Combo(app, options=colors, selected=app.text_color, command=update_text)

picture = Picture(app, image="F://Yahboom_Tank_Code/python/nvg.gif")
                
start_button = PushButton(app, command=start, text="Forward")
stop_button = PushButton(app, command=stop, text="Stop")
reverse_button = PushButton(app,command=start, text="Reverse")
t_left_button = PushButton(app,command=start, text="Turn Left")
t_right_button = PushButton(app,command=start, text="Turn Right")

app.display()
