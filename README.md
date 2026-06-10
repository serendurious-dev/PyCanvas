# PyCanvas

> A keyboard-first drawing app built in Python, where movement, curves, colour,
> and form all come from code and control instead of a mouse.

This is my project built around Python's turtle graphics system, but I do
not think "Turtle Painter" is the right identity for it anymore. The project is
really a small drawing environment: a live canvas, a movement system, a visual
HUD, a help layer, shape-building controls, fill mode, and a little built-in art
engine all working together. So I am calling it **PyCanvas**.

Built by **Prodipta Acharjee**.

---

## Why I built it

Most beginner drawing tools are mouse-first, and most turtle projects stop at
very simple movement demos. I wanted something in between: a project that still
uses the simplicity of turtle graphics, but feels more like a real interactive
application than a classroom exercise.

What interested me most was control. I liked the idea that drawing could come
from direction, turning, rhythm, and repeated key input rather than direct
clicking. That turns the whole experience into something halfway between sketching
and programming. You are not just placing lines, you are steering them.

I also wanted the project to feel alive while you are using it. That is why I
added the status display, the help overlay, pen controls, curve controls, fill
mode, reset and undo actions, and a built-in demo artwork. I cared about both
sides equally: the part that feels creative, and the part that feels properly
engineered.

---

## What it does

At the core, PyCanvas is a keyboard-controlled drawing application.

You open the window and control the drawing cursor entirely from the keyboard:

- Move forward and backward.
- Turn left and right.
- Make precise micro-turns for better control.
- Draw gentle, tight, and micro-curves for circles, leaves, loops, waves, and
  more complex shapes.
- Change pen colour.
- Increase or decrease pen size.
- Change movement step size.
- Toggle the pen up or down.
- Toggle fill mode for closed shapes.
- Undo actions.
- Reset the canvas.
- Open a help overlay.
- Launch a built-in demo artwork.
- Quit from the keyboard.

On top of that, there is a live **HUD** that keeps showing the current colour,
pen size, step size, pen state, current position, and angle. That one detail
matters a lot because it makes the program feel readable while you are drawing,
not blind. You always know what state you are in.

The project also includes a built-in artwork routine that draws a decorative,
mandala-like composition made from circles, stars, flowers, polygons, and accent
dots. I added that partly as a showcase and partly because I wanted the app to
prove it could create something polished on its own, not just wait for user
input.

---

## How it works

The application is built with Python's standard `turtle` module and follows a
simple event-driven structure.

A `Screen` object creates the window and listens for input. One turtle handles
the actual drawing. A second turtle handles the HUD text. A third turtle handles
the help overlay. Instead of scattering variables everywhere, the active values
are grouped into a single shared state dictionary, which keeps track of colour,
pen size, step size, fill state, pen state, and whether the help overlay is
visible.

Every key is mapped to a function. When a key is pressed, the linked function
runs, updates the drawing state, and refreshes the HUD. That means the program is
constantly responding in real time, but still stays easy to reason about because
each input has a very clear handler behind it.

I also used manual screen updates so the program redraws smoothly and keeps the
status layer consistent. That gives better control than relying on default turtle
animation alone.

---

## Features

- **Keyboard-first drawing.** No mouse required.
- **Movement system.** Standard movement, rotation, and fine-angle adjustments.
- **Curve system.** Multiple curve intensities for more natural shapes.
- **Live HUD.** Real-time display of current state.
- **Help overlay.** On-screen control reference.
- **Colour cycling.** Fast switching through a curated palette.
- **Adjustable pen thickness.**
- **Adjustable step size.**
- **Fill mode.** Draw enclosed coloured shapes.
- **Undo support.**
- **Canvas reset.**
- **Built-in demo artwork.**
- **Clean single-file structure.**

---

## Controls

### Movement

| Key | Action |
|---|---|
| `Up` | Move forward |
| `Down` | Move backward |
| `Left` | Turn left |
| `Right` | Turn right |
| `,` | Micro-turn left |
| `.` | Micro-turn right |
| `[` | Smaller step size |
| `]` | Larger step size |

### Curves

| Key | Action |
|---|---|
| `z` | Gentle curve left |
| `x` | Gentle curve right |
| `a` | Tight curve left |
| `s` | Tight curve right |
| `w` | Micro-curve left |
| `e` | Micro-curve right |

### Pen and utility

| Key | Action |
|---|---|
| `Space` | Toggle pen up/down |
| `c` | Cycle colour |
| `m` | Increase pen size |
| `n` | Decrease pen size |
| `f` | Toggle fill mode |
| `u` | Undo |
| `r` | Reset canvas |
| `d` | Draw demo artwork |
| `h` | Toggle help overlay |
| `q` | Quit |

---

## System idea

Even though this is visually a drawing app, the part I find interesting is that
it is really a state-driven input system.

| Part | Role | What it does |
|---|---|---|
| `screen` | Window + input layer | Creates the canvas and listens for keyboard input |
| Drawing turtle | Render layer | Moves, turns, draws, fills, resets, and renders artwork |
| HUD turtle | Status layer | Shows colour, size, step, pen state, coordinates, and angle |
| Help turtle | Instruction layer | Draws the on-screen controls overlay |
| State dictionary | Runtime memory | Stores active values the handlers depend on |
| Key bindings | Control system | Connects key presses to specific drawing actions |

That structure is what makes the project feel coherent. It is still lightweight,
but it behaves like a real little application rather than a loose script.

---

## Getting started

You need Python 3 installed. No external drawing library is required because
`turtle` is part of the standard library.

Run the project with:

```bash
python pycanvas.py
```

If your file is still named differently right now, run that filename first and
rename it later.

When the window opens, the demo artwork appears first. Press `r` to clear the
canvas and start drawing from scratch.

---

## Usage notes

A few things matter while using the program:

- The turtle window needs to stay focused for key input to register.
- Fill mode should be turned on before drawing a closed shape and turned off
  after the shape is completed.
- The curve keys are what make the program feel much more flexible than a normal
  forward-left-right turtle demo.
- The HUD is not just decoration, it is what makes the app usable when step size,
  angle, and pen state keep changing.

A simple example:

- Press `r` to clear the canvas.
- Press `c` a few times to choose a colour.
- Press `f` to start fill mode.
- Use `z` repeatedly to form a curved loop.
- Press `f` again to fill the shape.
- Press `u` if you want to undo part of it.

---

## Project structure

```text
pycanvas.py         main application
README.md           project overview
DOCUMENTATION.md    deeper technical write-up
LICENSE             MIT license
```

---

## What I learned

This project taught me that even a small graphics program becomes much better the
moment it has state, feedback, and a clear control system.

It also reminded me that polish is usually not one giant feature. It is the small
things stacking together: the HUD, the help overlay, the curve shortcuts, the
reset logic, the demo artwork, the feeling that the app is guiding you instead of
making you guess.

For me, that is what pushed this beyond just another turtle assignment.

---

## License

MIT. See [LICENSE](LICENSE).

---

## Author

Prodipta Acharjee. Built as a Python graphics project focused on interactive
drawing, keyboard control, and application design.
