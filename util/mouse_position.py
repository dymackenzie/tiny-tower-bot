from pynput import mouse, keyboard

saved_positions = []
running = True

def on_click(x, y, button, pressed):
    if pressed:
        saved_positions.append((x, y))
        print(f"Saved position: ({x}, {y})")

def on_press(key):
    global running
    try:
        if key.char == 'q':
            running = False
            return False
    except AttributeError:
        pass

with mouse.Listener(on_click=on_click) as mouse_listener, \
     keyboard.Listener(on_press=on_press) as keyboard_listener:

    while running:
        pass

print("\nSaved positions:")
for i, pos in enumerate(saved_positions, start=1):
    print(f"{i}: {pos}")
