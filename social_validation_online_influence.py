from psychopy import visual, core, event, gui, data

# Set up the experiment
exp_info = {"Participant ID": ""}
dlg = gui.DlgFromDict(dictionary=exp_info, title="Social Media Experiment")
if not dlg.OK:
    core.quit()

# Create a window
win = visual.Window(size=(1280, 720), fullscr=False, color=(1, 1, 1))

# Stimuli setup (simulated social media posts)
posts = [
    {"image": "high_likes.png", "caption": "Look at this amazing sunset! ☀️", "likes": "15.6K Likes"},
    {"image": "low_likes.png", "caption": "Check out this new phone! 📱", "likes": "5 Likes"},
    {"image": "no_likes.png", "caption": "Just another random post...", "likes": ""}
]

# Shuffle for randomization
import random
random.shuffle(posts)

# Response collection
results = []

for post in posts:
    # Display image
    image = visual.ImageStim(win, image=post["image"], size=(1.5, 1.0))
    caption = visual.TextStim(win, text=post["caption"], pos=(0, -0.5), color=(-1, -1, -1))
    likes = visual.TextStim(win, text=post["likes"], pos=(0, -0.7), color=(-1, -1, -1))

    # Draw elements
    image.draw()
    caption.draw()
    likes.draw()
    win.flip()

    # Get rating response
    rating_scale = visual.RatingScale(win, low=1, high=5, markerStart=3, textColor=(-1, -1, -1),
                                      scale="How much would you engage with this post?")
    while rating_scale.noResponse:
        rating_scale.draw()
        win.flip()
    response = rating_scale.getRating()

    results.append({"Post": post["caption"], "Likes": post["likes"], "Response": response})

# Save results
import pandas as pd
df = pd.DataFrame(results)
df.to_csv("social_experiment_results.csv", index=False)

# End Experiment
win.close()
core.quit()
