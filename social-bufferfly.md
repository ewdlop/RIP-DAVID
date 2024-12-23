from psychopy import visual, event, core, gui

# Create a window
win = visual.Window(size=(800, 600), color=(1, 1, 1), fullscr=False)

# Introduction text
intro_text = visual.TextStim(win, text="Welcome to the Social Interaction Study!\n\n"
                                       "Please answer the following questions.\n\n"
                                       "Press any key to continue.", color=(-1, -1, -1))
intro_text.draw()
win.flip()
event.waitKeys()

# Self-report survey
questions = [
    "I enjoy being the center of attention.",
    "I find it easy to start conversations.",
    "I am comfortable in social situations.",
    "I often feel energetic and enthusiastic."
]
responses = []

# Loop through questions
for question in questions:
    dlg = gui.DlgFromDict({question: ""}, title="Self-Report Survey")
    if dlg.OK:
        responses.append(dlg.data[0])
    else:
        core.quit()

# Display thank you message
thankyou_text = visual.TextStim(win, text="Thank you for your participation!\n\n"
                                          "Press any key to exit.", color=(-1, -1, -1))
thankyou_text.draw()
win.flip()
event.waitKeys()

# Close the window
win.close()
core.quit()
