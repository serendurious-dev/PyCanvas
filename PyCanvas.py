"""
turtle_painter.py
-----------------
Interactive drawing application using Python's built-in turtle module.

── MOVEMENT ───────────────────────────────────────────────
  Arrow Up / Down     Move forward / backward
  Arrow Left / Right  Turn left / right (15°)
  , / .               Micro-turn left / right (3°)  ← precise aim
  [ / ]               Step size  smaller / larger

── CURVES (move + turn in one press) ──────────────────────
  z / x               Gentle curve left / right  (10°)  ← circles, ovals
  a / s               Tight  curve left / right  (20°)  ← hearts, loops
  w / e               Micro  curve left / right  ( 5°)  ← soft arcs, trees

── PEN ────────────────────────────────────────────────────
  Space               Toggle pen up / down
  c                   Cycle pen colour
  m / n               Pen size up / down
  f                   Toggle fill (press f before & after a closed shape)

── UTILITY ────────────────────────────────────────────────
  u                   Undo last action
  r                   Reset / clear canvas
  d                   Draw the built-in artwork demo
  h                   Toggle help overlay
  q                   Quit

── SHAPE TIPS ─────────────────────────────────────────────
  Circle  : z ×36  (or x ×36 for opposite direction)
  Oval    : z ×18, then w ×18  (mix curve sizes)
  Heart   : face up → a×9 right, a×9 left, straight lines down
  Leaf    : z ×18, micro-turn 150° with . key, z ×18 back
  Tree    : straight lines (trunk), lift pen, branch with w/e curves
  Wave    : alternate z×6 and x×6 repeatedly
"""

import turtle

# ── Palette ──────────────────────────────────────────────────────────────────
PALETTE = [
    "#FFFFFF",  # white
    "#E63946",  # red
    "#F4A261",  # orange
    "#E9C46A",  # yellow
    "#57CC99",  # green
    "#2A9D8F",  # teal
    "#00BBF9",  # sky blue
    "#457B9D",  # steel blue
    "#9B5DE5",  # violet
    "#F15BB5",  # pink
]

STEP_SIZES = [3, 5, 8, 10, 15, 20, 30, 40]

# ── Mutable state (single dict so lambdas can mutate it) ─────────────────────
S = {
    "color_idx": 0,
    "pen_size":  2,
    "pen_down":  True,
    "step":      15,
    "step_idx":  4,   # index into STEP_SIZES (15px default)
    "filling":   False,
    "show_help": False,
}

# ── Screen ───────────────────────────────────────────────────────────────────
screen = turtle.Screen()
screen.title("Turtle Painter  |  h = help")
screen.bgcolor("black")
screen.setup(width=960, height=720)
screen.tracer(0)

# ── Drawing turtle ───────────────────────────────────────────────────────────
t = turtle.Turtle()
t.speed(0)
t.width(S["pen_size"])
t.color(PALETTE[S["color_idx"]])
t.pendown()
t.shape("classic")

# ── HUD turtle ───────────────────────────────────────────────────────────────
hud = turtle.Turtle()
hud.hideturtle()
hud.penup()
hud.color("#888888")
hud.goto(-470, 345)

# ── Help overlay turtle ──────────────────────────────────────────────────────
helper = turtle.Turtle()
helper.hideturtle()
helper.penup()
helper.color("#CCCCCC")


# ── HUD refresh ──────────────────────────────────────────────────────────────
def draw_hud():
    hud.clear()
    pen_str  = "DOWN ✏" if S["pen_down"] else "UP ✋"
    fill_str = " | FILL ON" if S["filling"] else ""
    hud.write(
        f"Color: {PALETTE[S['color_idx']]}  │  Size: {S['pen_size']}  │  "
        f"Step: {S['step']}px  │  Pen: {pen_str}{fill_str}  │  "
        f"({int(t.xcor())},{int(t.ycor())})  Angle:{int(t.heading())}°  │  h=help",
        font=("Courier", 9, "normal"),
    )
    screen.update()


draw_hud()


# ── Help overlay ─────────────────────────────────────────────────────────────
HELP_LINES = [
    "─── MOVEMENT ──────────────────────────────────────",
    " ↑ / ↓        Move forward / backward",
    " ← / →        Turn 15° left / right",
    " , / .        Micro-turn 3° left / right",
    " [ / ]        Step size smaller / larger",
    "",
    "─── CURVES (move + turn together) ────────────────",
    " z / x        Gentle curve 10°  → circles, ovals",
    " a / s        Tight  curve 20°  → hearts, tight loops",
    " w / e        Micro  curve  5°  → soft arcs, trees",
    "",
    "─── PEN ───────────────────────────────────────────",
    " Space        Pen up / down",
    " c            Cycle colour",
    " m / n        Pen size up / down",
    " f            Toggle fill  (press before & after shape)",
    "",
    "─── UTILITY ───────────────────────────────────────",
    " u            Undo last stroke",
    " r            Clear canvas",
    " d            Draw demo artwork",
    " h            Toggle this help",
    " q            Quit",
    "",
    "─── QUICK RECIPES ─────────────────────────────────",
    " Circle : z ×36  (or x ×36)",
    " Heart  : face up → a×9 right, a×9 left, lines down",
    " Leaf   : z ×18, turn 150° with . key, z ×18",
    " Wave   : alternate z×6 and x×6",
    " Tree   : straight lines (trunk), lift pen, branch w/e",
]


def toggle_help():
    S["show_help"] = not S["show_help"]
    helper.clear()
    if S["show_help"]:
        for i, line in enumerate(HELP_LINES):
            helper.goto(-465, 318 - i * 16)
            helper.write(line, font=("Courier", 9, "normal"))
    screen.update()


# ── Movement handlers ────────────────────────────────────────────────────────
def move_forward():
    t.forward(S["step"])
    draw_hud()

def move_backward():
    t.backward(S["step"])
    draw_hud()

def turn_left():
    t.left(15)
    draw_hud()

def turn_right():
    t.right(15)
    draw_hud()

def micro_left():
    t.left(3)
    draw_hud()

def micro_right():
    t.right(3)
    draw_hud()

def step_smaller():
    S["step_idx"] = max(0, S["step_idx"] - 1)
    S["step"] = STEP_SIZES[S["step_idx"]]
    draw_hud()

def step_larger():
    S["step_idx"] = min(len(STEP_SIZES) - 1, S["step_idx"] + 1)
    S["step"] = STEP_SIZES[S["step_idx"]]
    draw_hud()


# ── Curve handlers ───────────────────────────────────────────────────────────
def _curve(deg):
    t.forward(S["step"])
    t.left(deg)
    draw_hud()

def gentle_left():   _curve( 10)   # z
def gentle_right():  _curve(-10)   # x
def tight_left():    _curve( 20)   # a
def tight_right():   _curve(-20)   # s
def micro_curve_l(): _curve(  5)   # w
def micro_curve_r(): _curve( -5)   # e


# ── Pen handlers ─────────────────────────────────────────────────────────────
def toggle_pen():
    S["pen_down"] = not S["pen_down"]
    t.pendown() if S["pen_down"] else t.penup()
    draw_hud()

def cycle_color():
    S["color_idx"] = (S["color_idx"] + 1) % len(PALETTE)
    t.color(PALETTE[S["color_idx"]])
    if S["filling"]:
        t.fillcolor(PALETTE[S["color_idx"]])
    draw_hud()

def increase_size():
    S["pen_size"] = min(S["pen_size"] + 1, 30)
    t.width(S["pen_size"])
    draw_hud()

def decrease_size():
    S["pen_size"] = max(S["pen_size"] - 1, 1)
    t.width(S["pen_size"])
    draw_hud()

def toggle_fill():
    S["filling"] = not S["filling"]
    if S["filling"]:
        t.fillcolor(PALETTE[S["color_idx"]])
        t.begin_fill()
    else:
        t.end_fill()
    draw_hud()


# ── Utility handlers ─────────────────────────────────────────────────────────
def undo():
    t.undo()
    draw_hud()

def reset_canvas():
    if S["filling"]:
        t.end_fill()
        S["filling"] = False
    t.clear()
    t.penup()
    t.goto(0, 0)
    t.setheading(90)
    t.color(PALETTE[S["color_idx"]])
    t.width(S["pen_size"])
    if S["pen_down"]:
        t.pendown()
    helper.clear()
    S["show_help"] = False
    draw_hud()

def quit_app():
    screen.bye()


# ── Built-in artwork ─────────────────────────────────────────────────────────
def draw_artwork():
    import math

    if S["filling"]:
        t.end_fill()
        S["filling"] = False

    screen.tracer(0)
    t.penup()
    t.clear()

    def star5(cx, cy, size, color):
        t.penup(); t.goto(cx, cy - size); t.setheading(0)
        t.fillcolor(color); t.begin_fill()
        t.pendown(); t.color(color); t.width(1)
        for _ in range(5):
            t.forward(size); t.right(144)
        t.end_fill(); t.penup()

    def flower(cx, cy, petals, radius, pc, cc):
        t.penup(); t.width(1)
        for i in range(petals):
            t.goto(cx, cy); t.setheading(i * (360 / petals))
            t.forward(radius * 0.3)
            t.fillcolor(pc); t.begin_fill()
            t.pendown(); t.circle(radius * 0.4)
            t.end_fill(); t.penup()
        t.goto(cx, cy - radius * 0.18)
        t.fillcolor(cc); t.begin_fill()
        t.pendown(); t.circle(radius * 0.18)
        t.end_fill(); t.penup()

    def poly_ring(cx, cy, n, r, color):
        t.penup(); t.goto(cx, cy - r); t.setheading(0)
        t.pendown(); t.color(color); t.width(2)
        side = 2 * r * math.sin(math.pi / n)
        for _ in range(n):
            t.forward(side); t.left(360 / n)
        t.penup()

    # background rings
    for i, rc in enumerate(["#16213E", "#0F3460", "#533483"]):
        r = 280 - i * 60
        t.goto(0, -r); t.fillcolor(rc); t.begin_fill()
        t.pendown(); t.color(rc); t.width(1); t.circle(r)
        t.end_fill(); t.penup()

    # outer stars
    sc = ["#E63946","#F4A261","#E9C46A","#2A9D8F",
          "#457B9D","#9B5DE5","#F15BB5","#00BBF9"]
    for i in range(8):
        a = math.radians(i * 45)
        star5(200 * math.cos(a), 200 * math.sin(a), 22, sc[i])

    # flowers
    fp = [("#F15BB5","#E9C46A"),("#00BBF9","#FFFFFF"),("#9B5DE5","#F4A261"),
          ("#E63946","#FFFFFF"),("#2A9D8F","#E9C46A"),("#457B9D","#F15BB5")]
    for i in range(6):
        a = math.radians(i * 60)
        flower(120 * math.cos(a), 120 * math.sin(a), 8, 28, fp[i][0], fp[i][1])

    # geometric rings
    for n, r, col in [(6,55,"#2A9D8F"),(8,78,"#9B5DE5"),(6,100,"#F4A261")]:
        poly_ring(0, 0, n, r, col)

    # central 8-pointed star
    t.goto(0, -40); t.setheading(0)
    t.fillcolor("#E9C46A"); t.begin_fill()
    t.pendown(); t.color("#E9C46A"); t.width(2)
    for _ in range(8):
        t.forward(40); t.right(135)
    t.end_fill(); t.penup()

    # centre dot
    t.goto(0, -12); t.fillcolor("#FFFFFF"); t.begin_fill()
    t.pendown(); t.color("#FFFFFF"); t.circle(12)
    t.end_fill(); t.penup()

    # accent dots
    dc = ["#E63946","#F4A261","#E9C46A","#2A9D8F",
          "#457B9D","#9B5DE5","#F15BB5","#00BBF9",
          "#E63946","#F4A261","#E9C46A","#2A9D8F"]
    for i in range(12):
        a = math.radians(i * 30)
        t.goto(148 * math.cos(a), 148 * math.sin(a))
        t.dot(10, dc[i])

    # restore user state
    t.goto(0, 0); t.setheading(90)
    t.color(PALETTE[S["color_idx"]]); t.width(S["pen_size"])
    if S["pen_down"]: t.pendown()
    screen.tracer(1)
    draw_hud()


# ── Key bindings ─────────────────────────────────────────────────────────────
screen.listen()

screen.onkey(move_forward,   "Up")
screen.onkey(move_backward,  "Down")
screen.onkey(turn_left,      "Left")
screen.onkey(turn_right,     "Right")
screen.onkey(micro_left,     "comma")
screen.onkey(micro_right,    "period")
screen.onkey(step_smaller,   "bracketleft")
screen.onkey(step_larger,    "bracketright")

screen.onkey(gentle_left,    "z")
screen.onkey(gentle_right,   "x")
screen.onkey(tight_left,     "a")
screen.onkey(tight_right,    "s")
screen.onkey(micro_curve_l,  "w")
screen.onkey(micro_curve_r,  "e")

screen.onkey(toggle_pen,     "space")
screen.onkey(cycle_color,    "c")
screen.onkey(increase_size,  "m")
screen.onkey(decrease_size,  "n")
screen.onkey(toggle_fill,    "f")

screen.onkey(undo,           "u")
screen.onkey(reset_canvas,   "r")
screen.onkey(draw_artwork,   "d")
screen.onkey(toggle_help,    "h")
screen.onkey(quit_app,       "q")

# ── Launch ───────────────────────────────────────────────────────────────────
print("Turtle Painter ready  |  press h in the window for help")
draw_artwork()
screen.tracer(1)
turtle.mainloop()
