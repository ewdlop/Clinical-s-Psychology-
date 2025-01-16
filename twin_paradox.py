from psychopy import visual, core, event
import numpy as np

# Create a window
win = visual.Window([800, 600], color="black")

# Create stimuli
stationary_twin = visual.TextStim(win, text="Stationary Twin Age: 0", pos=(-0.5, 0.5), color="white")
traveling_twin = visual.TextStim(win, text="Traveling Twin Age: 0", pos=(0.5, 0.5), color="white")
travel_animation = visual.Rect(win, width=0.1, height=0.1, pos=(-0.5, -0.2), color="blue")

# Time variables
stationary_age = 0
traveling_age = 0
speed = 0.8  # As a fraction of the speed of light (v/c)
gamma = 1 / np.sqrt(1 - speed**2)  # Lorentz factor
simulation_time = 10  # seconds
frame_rate = 60  # frames per second
total_frames = int(simulation_time * frame_rate)

# Main loop
for frame in range(total_frames):
    stationary_age += 1 / frame_rate  # Increment age per second
    traveling_age += (1 / frame_rate) / gamma  # Increment age with time dilation

    # Update text
    stationary_twin.text = f"Stationary Twin Age: {stationary_age:.2f}"
    traveling_twin.text = f"Traveling Twin Age: {traveling_age:.2f}"

    # Animate traveling twin
    travel_animation.pos += (0.01, 0)  # Move to the right
    if travel_animation.pos[0] > 0.5:
        travel_animation.pos = (-0.5, -0.2)  # Reset position

    # Draw stimuli
    stationary_twin.draw()
    traveling_twin.draw()
    travel_animation.draw()

    # Flip the window
    win.flip()

    # Exit if a key is pressed
    if event.getKeys():
        break

# Clean up
win.close()
core.quit()
