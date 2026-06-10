# PyCanvas Documentation

> A deeper technical write-up of the project, how it is structured, and why the
> implementation choices matter.

This document explains the internal design of **PyCanvas**, a keyboard-driven
drawing application built with Python's turtle graphics module. The project looks
simple on the surface, but under that surface it is really about input handling,
state management, rendering control, and turning a basic graphics library into a
more complete user-facing application.

Built by **Prodipta Acharjee**.

---

## 1. Project overview

PyCanvas is an interactive drawing environment where the user creates shapes and
artwork through keyboard input instead of mouse input.

The user can move a drawing cursor forward and backward, rotate it, make small
angle corrections, create curves of different intensities, change colours,
increase or decrease pen thickness, adjust the movement step size, toggle fill
mode, undo actions, clear the canvas, open a help screen, and trigger a built-in
demo artwork routine.

The goal of the project was not just to make something that draws. The goal was
to make something that feels like a miniature application, with visible state,
structured controls, and a better user experience than a default turtle demo.

---

## 2. Core design idea

The central idea behind the project is very simple:

- drawing is movement,
- movement becomes shape,
- shape becomes expression,
- and state is what makes that whole system usable.

A plain turtle program can already move and draw, but it usually feels limited
because the user does not have enough feedback and does not have enough control
variety. PyCanvas improves that by adding layers around the basic turtle:

- a state system,
- a HUD,
- a help overlay,
- multiple curve controls,
- utility commands,
- and a structured set of keyboard bindings.

That is what turns the project from a script into a small tool.

---

## 3. Main components

The application is built around four main pieces.

### 3.1 Screen

The `turtle.Screen()` object creates the main application window, sets the window
title, background colour, and dimensions, and listens for keyboard input.

It is also responsible for the refresh cycle. Because the program uses manual
screen updates, the screen does not redraw automatically after every tiny change.
That gives better control over responsiveness and avoids unnecessary visual
flicker.

### 3.2 Drawing turtle

The main turtle is the actual drawing agent.

This object is responsible for:

- moving forward and backward,
- rotating left and right,
- drawing curves,
- changing pen width,
- changing colour,
- handling fill operations,
- undoing work,
- drawing the built-in artwork,
- and resetting position and orientation.

This turtle is the visible actor of the whole program.

### 3.3 HUD turtle

A second hidden turtle is used only for interface text.

Its job is to display live information such as:

- current colour,
- current pen size,
- current movement step,
- pen up/down state,
- coordinates,
- current angle,
- and the help shortcut hint.

This layer matters because the user is constantly changing state while drawing.
Without it, the program would still function, but it would feel much more blind
and much less usable.

### 3.4 Help turtle

A third hidden turtle is used for the help overlay.

When the user presses the help key, it writes a multi-line instruction panel onto
the screen. That lets the controls stay discoverable without forcing the user to
switch to the terminal or memorise everything.

---

## 4. State management

One of the better implementation choices in this project is the shared state
dictionary.

Instead of storing everything in separate loose variables, the application keeps
its active runtime values together in one structure. That state includes:

- active colour index,
- current pen size,
- whether the pen is down,
- current step size,
- step-size index,
- whether fill mode is active,
- whether the help overlay is visible.

This is a small design decision, but it improves the project a lot. It keeps the
handlers consistent, makes updates easier to track, and reduces the mess that
interactive scripts often fall into.

A typical state model looks like this:

```python
S = {
    "color_idx": 0,
    "pen_size": 2,
    "pen_down": True,
    "step": 15,
    "step_idx": 4,
    "filling": False,
    "show_help": False,
}
```

---

## 5. Event-driven structure

The whole application runs as an event-driven system.

That means the program mostly waits for user input. Each key is linked to one
specific function. When that key is pressed, the function runs, changes either the
drawing or the state, and then refreshes the interface.

This matters because it keeps the logic clean:

- movement keys call movement functions,
- curve keys call curve functions,
- pen keys call pen functions,
- utility keys call utility functions.

It is a simple architecture, but it scales well for this kind of project.

---

## 6. Movement and curve system

The movement system is the foundation of the program.

### Standard movement

The arrow keys let the user:

- move forward,
- move backward,
- rotate left,
- rotate right.

These commands are enough for basic line drawing.

### Fine control

The micro-turn keys allow small-angle adjustments. This is important because large
rotations are useful for strong direction changes, but small rotations are what
make drawing feel more precise.

### Step-size control

The step-size controls let the user decide how far each movement goes. A larger
step gives faster, broader drawing. A smaller step allows more careful detail.

### Curves

One of the most interesting parts of the project is that curves are not treated as
special predefined shapes. Instead, they are created by combining forward motion
with a slight rotation on each key press.

That means a curve function is conceptually just this:

```python
def curve(deg):
    t.forward(step)
    t.left(deg)
```

Different degrees create different effects:

- gentle curves for circles and ovals,
- tighter curves for hearts and loops,
- micro-curves for soft bends and branches.

This is a strong design choice because it gives expressive control without making
the code overly complicated.

---

## 7. Pen system

The pen system gives the user control over how marks are made.

### Colour

The colour system cycles through a predefined palette. That makes colour changes
fast and consistent. Instead of entering values manually, the user can keep
drawing and switch colours instantly.

### Pen size

The pen width can be increased or decreased. This changes visual weight and lets
the user move between detail work and bold strokes.

### Pen up / pen down

The pen toggle changes whether the turtle moves while drawing or moves silently.
This is essential for repositioning and composing more complicated figures.

### Fill mode

Fill mode allows the user to create closed shapes with colour inside them.

The idea is simple:

1. turn fill mode on,
2. draw a closed shape,
3. turn fill mode off.

This uses turtle's fill system under the hood, but from the user's perspective it
feels like a more complete drawing tool.

---

## 8. HUD and feedback layer

The HUD is one of the most important usability features in the project.

Each time something changes, the HUD is redrawn to show the new live values. That
means the user always knows the current state without guessing.

A typical HUD line includes:

```text
Color: #E63946 | Size: 2 | Step: 15px | Pen: DOWN | (x, y) | Angle: 90°
```

That feedback loop is what makes the controls manageable even after the feature
set grows. Once a project has multiple states, visible feedback stops being extra
polish and starts being necessary structure.

---

## 9. Help overlay

The help overlay is a second interface layer built directly into the canvas.

Pressing the help key toggles a text panel that lists:

- movement controls,
- curve controls,
- pen controls,
- utility controls,
- and quick shape recipes.

I included this because I wanted the project to feel self-contained. The user
should be able to learn and use the app from inside the app itself.

That is a small feature, but it changes the experience a lot.

---

## 10. Built-in artwork routine

The project includes a built-in artwork generator that draws a decorative
composition automatically.

This routine exists for two reasons:

- to show that the program can produce more than user-controlled lines,
- and to demonstrate how the same drawing engine can be reused for procedural art.

The artwork combines several geometric ideas:

- background rings,
- stars,
- flowers,
- polygons,
- a central star,
- and accent dots.

This feature also works as a visual test. If the artwork renders correctly, it is
a good sign that movement, filling, colour handling, and rendering order are all
working together properly.

---

## 11. Rendering decisions

A normal turtle program updates constantly by default. That can become messy once
you add HUD text and multiple interface layers.

To solve that, the project uses manual refresh logic. The screen tracer is
controlled so the program can update deliberately after each meaningful action.

That approach improves:

- smoothness,
- readability,
- consistency of the HUD,
- and overall control of the drawing cycle.

This is one of those technical decisions that the user may not notice directly,
but they definitely feel the effect of it.

---

## 12. Controls reference

### Movement

| Key | Action |
|---|---|
| `Up` | Move forward |
| `Down` | Move backward |
| `Left` | Turn left |
| `Right` | Turn right |
| `,` | Micro-turn left |
| `.` | Micro-turn right |
| `[` | Step size smaller |
| `]` | Step size larger |

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

## 13. Running the project

Run the program with:

```bash
python pycanvas.py
```

There are no required third-party dependencies for the core drawing system.

If the turtle window does not respond to keys, click the window first so it has
focus.

---

## 14. Limitations

Like any small project, this one has some limits.

- It is keyboard-only, which is the design choice, but also a constraint.
- The drawing is based on turtle graphics, so it is not meant to compete with a
  full modern painting app.
- Fill mode depends on the user closing shapes properly.
- Undo is useful, but not a full history system like professional software.

I do not see these as flaws as much as boundaries. The point of the project was
to turn a simple graphics module into a more thoughtful interactive program, and
it does that well.

---

## 15. What makes this project more than a basic turtle demo

A lot of turtle projects stop at showing movement. This one goes further because
it treats drawing as an application design problem.

It includes:

- structured controls,
- visible live state,
- layered interface elements,
- curve-based expressive drawing,
- utility features,
- procedural art generation,
- and a more polished interaction model.

That is the difference. It is still lightweight, but it feels intentional.

---

## 16. Final note

What I like most about this project is that it sits in a nice middle space between
graphics, interaction, and programming logic.

It is simple enough to understand clearly, but rich enough that the design
choices actually matter. For me, that is what made it satisfying to build.
