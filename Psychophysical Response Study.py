from psychopy import visual, event, core, gui
import random

# Create a window
win = visual.Window(size=(800, 600), color=(1, 1, 1), fullscr=False)

# Introduction text
intro_text = visual.TextStim(win, text="Welcome to the Psychophysical Study!\n\n"
                                       "You will be asked a series of questions.\n"
                                       "Please answer honestly.\n\n"
                                       "Press any key to start.", color=(-1, -1, -1))
intro_text.draw()
win.flip()
event.waitKeys()

# List of questions (modify as needed)
questions = [
    "Do you enjoy outdoor activities?",
    "Do you often feel stressed at work?",
    "Are you satisfied with your current life?",
    "Do you feel safe in your environment?",
]

responses = []

# Function to display a question and get a response
def ask_question(question_text):
    question_stim = visual.TextStim(win, text=question_text, color=(-1, -1, -1))
    question_stim.draw()
    win.flip()
    
    response = event.waitKeys(keyList=['y', 'n'])
    return response[0]

# Ask each question and collect responses
for question in questions:
    response = ask_question(question)
    responses.append(response)
    core.wait(1)  # Wait for 1 second between questions

# Display thank you message
thankyou_text = visual.TextStim(win, text="Thank you for your participation!\n\nPress any key to exit.", color=(-1, -1, -1))
thankyou_text.draw()
win.flip()
event.waitKeys()

# Close the window
win.close()
core.quit()
