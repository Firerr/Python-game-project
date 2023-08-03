import time, textwrap, re, random

# Replacements for colorama
YELLOW = "\x1b[33m"
GREEN = "\x1b[32m"
BLUE = "\x1b[34m"
CYAN = "\x1b[36m"
RED = "\x1b[31m"
RESET = "\x1b[39m"
RESET2 = "\033[40m"

sea_image = ' \x1b[47m     \x1b[44m\x1b[37m▓                                            \x1b[47m                 \x1b[44m▓▓           \x1b[49m\n \x1b[47m      \x1b[44m                      ▓▓▓▓▓▓            ▓▓▓\x1b[47m                \x1b[44m▓      \x1b[32m▓▓   ▓▓ \x1b[49m\n \x1b[47m      \x1b[44m\x1b[37m▓                  ▓▓▓▓\x1b[47m     \x1b[44m▓▓    ▓▓▓\x1b[47m                    \x1b[44m▓       \x1b[32m▓▓\x1b[42m  \x1b[44m \x1b[42m \x1b[34m▓\x1b[44m  \x1b[49m\n \x1b[47m       \x1b[44m\x1b[37m▓    \x1b[47m▓ \x1b[44m       ▓▓\x1b[47m        \x1b[44m   ▓\x1b[47m                    \x1b[44m▓▓▓▓           \x1b[36m▓ \x1b[42m\x1b[34m▓ \x1b[31m▓  \x1b[36m▓ \x1b[44m \x1b[49m\n \x1b[44m \x1b[37m▓\x1b[47m      \x1b[44m▓  \x1b[47m \x1b[44m▓ \x1b[47m \x1b[44m     ▓\x1b[41m \x1b[47m       \x1b[44m            ▓▓▓▓▓▓▓▓▓▓▓▓                   \x1b[42m \x1b[44m  \x1b[41m \x1b[44m \x1b[42m \x1b[44m  \x1b[49m\n \x1b[44m   ▓\x1b[47m▓    \x1b[44m     \x1b[47m \x1b[44m▓    \x1b[43m\x1b[31m▓\x1b[41m \x1b[47m     \x1b[44m   \x1b[37m▓▓   \x1b[41m \x1b[44m                                    \x1b[36m▓   \x1b[41m \x1b[44m   \x1b[49m\n \x1b[44m      \x1b[37m▓\x1b[47m▓  \x1b[44m▓ ▓\x1b[47m  \x1b[44m▓   \x1b[41m \x1b[43m\x1b[31m▓\x1b[41m \x1b[47m     \x1b[44m     \x1b[37m▓\x1b[47m \x1b[44m  \x1b[41m \x1b[44m                                       \x1b[41m \x1b[44m   \x1b[49m\n \x1b[44m        ▓\x1b[47m▓▓▓ \x1b[44m▓▓  \x1b[41m   \x1b[43m\x1b[31m▓\x1b[41m \x1b[44m   \x1b[37m▓\x1b[47m   \x1b[44m   \x1b[47m  \x1b[44m  \x1b[41m \x1b[44m                                      \x1b[31m▓\x1b[41m \x1b[44m   \x1b[49m\n \x1b[44m                 \x1b[41m   \x1b[43m▓\x1b[41m \x1b[44m     \x1b[37m▓▓\x1b[47m  \x1b[41m      \x1b[44m                                     \x1b[31m▓\x1b[41m \x1b[44m    \x1b[49m\n \x1b[44m               \x1b[41m     \x1b[43m \x1b[41m \x1b[44m    \x1b[41m     \x1b[44m      \x1b[41m \x1b[44m                                \x1b[33m▓\x1b[43m \x1b[31m▓       \x1b[49m\n \x1b[44m               \x1b[41m     \x1b[43m \x1b[41m     \x1b[44m           \x1b[41m \x1b[44m                           \x1b[33m▓\x1b[43m              \x1b[49m\n \x1b[44m\x1b[36m▓▓▓▓▓▓▓▓▓▓▓▓▓▓\x1b[41m      \x1b[43m \x1b[41m \x1b[44m▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\x1b[33m▓\x1b[43m                \x1b[31m▓ \x1b[49m\n \x1b[46m              \x1b[41m      \x1b[43m \x1b[41m \x1b[46m      \x1b[37m▓▓▓                                 \x1b[33m▓▓▓▓\x1b[31m▓▓▓\x1b[43m\x1b[33m▓        \x1b[49m\n \x1b[47m \x1b[37m▓▓\x1b[46m▓▓▓       \x1b[47m \x1b[41m      \x1b[43m \x1b[41m \x1b[47m \x1b[46m                                          \x1b[33m▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\x1b[49m\n \x1b[46m              \x1b[44m        \x1b[46m                    \x1b[37m▓ \x1b[47m    ▓▓▓\x1b[46m▓▓                 \x1b[33m▓▓▓▓▓▓▓▓▓▓\x1b[49m\n \x1b[46m              \x1b[34m▓▓▓▓▓▓▓▓ ▓▓                                        \x1b[47m   \x1b[46m       \x1b[31m▓    \x1b[49m\n \x1b[46m         \x1b[47m    \x1b[37m▓ \x1b[46m▓\x1b[34m▓▓\x1b[37m▓\x1b[34m▓▓▓                                                     \x1b[31m▓    \x1b[49m\n \x1b[46m                                                                            ▓   \x1b[49m '
pirate_image = ' \x1b[44m      \x1b[41m        \x1b[43m\x1b[31m▓▓▓▓▓▓▓▓▓▓▓▓▓\x1b[41m      \x1b[44m                    \x1b[36m▓\x1b[43m  \x1b[47m\x1b[33m▓▓▓▓▓▓▓▓▓▓▓▓\x1b[49m\n \x1b[44m        \x1b[43m\x1b[31m▓▓▓▓▓▓▓\x1b[44m▓▓▓▓▓          \x1b[41m   \x1b[44m                    \x1b[36m▓\x1b[43m  \x1b[47m\x1b[33m▓▓▓▓▓▓▓▓▓▓▓▓\x1b[49m\n \x1b[44m     \x1b[36m▓▓▓\x1b[31m▓▓▓▓▓▓▓     \x1b[43m▓▓▓▓▓▓▓▓▓▓▓▓\x1b[41m \x1b[44m                    \x1b[36m▓\x1b[43m  \x1b[47m\x1b[33m▓▓▓▓▓▓▓▓▓▓▓▓\x1b[49m\n \x1b[44m     \x1b[36m▓\x1b[34m▓▓            \x1b[43m\x1b[31m▓▓▓▓▓▓▓▓▓▓▓▓▓\x1b[41m  \x1b[44m                  \x1b[36m▓\x1b[43m  \x1b[47m\x1b[33m▓▓▓▓▓▓▓▓▓▓▓▓\x1b[49m\n \x1b[44m     \x1b[36m▓\x1b[34m▓▓            \x1b[43m\x1b[31m▓\x1b[44m▓▓\x1b[43m▓▓▓▓▓▓▓▓▓▓\x1b[41m   \x1b[44m                 \x1b[36m▓\x1b[43m  \x1b[47m\x1b[33m▓▓▓▓▓▓▓▓▓▓▓▓\x1b[49m\n \x1b[44m      \x1b[43m\x1b[31m▓\x1b[44m▓            \x1b[43m▓▓▓▓\x1b[44m▓▓▓▓▓▓\x1b[43m▓▓▓\x1b[41m     \x1b[44m                \x1b[43m  \x1b[47m\x1b[33m▓▓▓▓▓▓▓▓▓▓▓▓\x1b[49m\n \x1b[44m   \x1b[43m\x1b[31m▓▓\x1b[44m \x1b[43m▓\x1b[44m▓          ▓\x1b[43m▓▓▓▓▓▓\x1b[44m▓▓\x1b[43m▓▓▓▓▓▓\x1b[41m  \x1b[43m▓▓▓\x1b[41m \x1b[44m               \x1b[43m  \x1b[47m\x1b[33m▓▓▓▓▓▓▓▓▓▓▓▓\x1b[49m\n \x1b[44m   \x1b[43m\x1b[31m▓▓\x1b[44m \x1b[43m▓▓\x1b[44m▓         \x1b[43m▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\x1b[41m  \x1b[43m▓▓▓\x1b[41m   \x1b[44m             \x1b[43m  \x1b[42m\x1b[33m▓▓▓▓▓▓▓▓▓▓▓▓\x1b[49m\n \x1b[44m   \x1b[43m\x1b[31m▓▓\x1b[44m \x1b[43m▓▓▓\x1b[44m▓▓      \x1b[43m▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\x1b[41m  \x1b[43m▓▓▓\x1b[41m   \x1b[44m             \x1b[43m  \x1b[42m\x1b[33m▓▓▓▓▓▓▓▓▓▓▓▓\x1b[49m\n \x1b[44m     \x1b[31m▓\x1b[43m▓▓▓▓▓\x1b[44m    \x1b[43m▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\x1b[41m  \x1b[43m▓▓▓\x1b[41m    \x1b[44m            \x1b[43m  \x1b[42m\x1b[33m▓▓▓▓▓▓▓▓▓▓▓▓\x1b[49m\n \x1b[44m     \x1b[31m▓\x1b[43m▓▓▓▓▓▓▓▓▓\x1b[44m▓▓\x1b[43m▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\x1b[41m  ▓▓▓    \x1b[44m            \x1b[36m▓▓\x1b[43m \x1b[42m\x1b[33m▓▓▓▓▓▓▓▓\x1b[47m▓▓▓\x1b[49m\n \x1b[44m     \x1b[31m▓\x1b[43m▓▓▓▓▓▓▓▓▓▓▓\x1b[44m▓▓▓▓\x1b[43m▓▓▓▓▓▓▓▓▓▓▓▓\x1b[41m         \x1b[44m            \x1b[36m▓▓\x1b[43m \x1b[42m\x1b[33m▓▓▓▓▓▓▓▓▓▓▓\x1b[49m\n \x1b[44m     \x1b[41m \x1b[43m\x1b[31m▓▓▓\x1b[41m▓▓\x1b[43m▓▓▓▓▓▓\x1b[41m    \x1b[43m▓▓▓▓▓\x1b[41m▓\x1b[43m▓▓▓▓▓▓\x1b[41m           \x1b[44m            \x1b[36m▓\x1b[43m  \x1b[42m\x1b[33m▓▓▓▓▓▓▓▓▓\x1b[49m\n \x1b[44m   \x1b[31m▓▓\x1b[41m \x1b[43m▓▓\x1b[41m▓\x1b[43m▓▓▓▓▓▓\x1b[41m        \x1b[43m▓▓▓▓\x1b[41m▓▓\x1b[43m▓▓▓▓\x1b[41m           \x1b[44m            \x1b[36m▓\x1b[43m  \x1b[42m\x1b[33m▓▓▓▓▓▓▓▓▓\x1b[49m\n \x1b[44m   \x1b[41m   \x1b[43m\x1b[31m▓▓▓▓▓\x1b[41m      \x1b[43m▓▓▓\x1b[41m      \x1b[43m▓▓▓▓▓▓▓\x1b[41m           \x1b[44m            \x1b[36m▓\x1b[43m  \x1b[42m\x1b[33m▓▓▓▓▓▓▓▓▓\x1b[49m\n \x1b[44m   \x1b[41m     \x1b[43m\x1b[31m▓▓▓\x1b[41m   \x1b[43m▓\x1b[44m▓▓▓▓▓▓\x1b[41m      \x1b[43m▓▓▓▓▓\x1b[41m▓           \x1b[44m            \x1b[36m▓\x1b[43m  \x1b[42m\x1b[33m▓▓▓▓▓▓▓▓▓\x1b[49m\n \x1b[44m  \x1b[31m▓\x1b[41m         \x1b[43m▓▓\x1b[44m▓\x1b[43m▓▓▓▓▓▓▓▓▓\x1b[41m      ▓▓▓           \x1b[44m          \x1b[36m▓▓\x1b[43m \x1b[42m\x1b[33m▓▓▓▓▓▓▓▓▓▓\x1b[47m▓\x1b[49m\n \x1b[44m  \x1b[41m          \x1b[43m\x1b[31m▓▓▓▓▓\x1b[41m    \x1b[43m▓▓▓▓▓\x1b[41m   ▓▓▓▓           \x1b[44m         \x1b[36m▓\x1b[43m  \x1b[42m\x1b[33m▓▓▓▓▓▓▓▓▓▓▓▓\x1b[49m\n \x1b[44m\x1b[31m▓▓\x1b[41m                     \x1b[43m▓\x1b[41m     ▓▓▓\x1b[44m▓\x1b[41m           \x1b[44m       \x1b[36m▓▓\x1b[43m \x1b[42m\x1b[33m▓▓▓▓▓▓▓▓▓▓▓▓▓▓\x1b[49m\x1b[0m '
chest_image = ' \x1b[43m\x1b[31m▓                                 \x1b[47m \x1b[43m\x1b[36m▓▓▓▓\x1b[46m           \x1b[49m\n \x1b[43m                                   \x1b[47m  \x1b[43m▓▓\x1b[46m           \x1b[49m\n \x1b[43m       \x1b[41m                    \x1b[43m         \x1b[47m \x1b[43m▓▓\x1b[46m           \x1b[49m\n \x1b[43m      \x1b[41m    \x1b[33m▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ \x1b[43m         \x1b[47m \x1b[43m\x1b[36m▓▓\x1b[46m          \x1b[49m\n \x1b[43m     \x1b[41m    \x1b[43m \x1b[41m  \x1b[33m▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ \x1b[43m        \x1b[47m \x1b[36m▓\x1b[43m▓▓▓▓▓\x1b[46m      \x1b[49m\n \x1b[43m    \x1b[41m \x1b[43m \x1b[41m       \x1b[33m▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ \x1b[43m        \x1b[47m   \x1b[43m\x1b[36m▓▓▓\x1b[46m      \x1b[49m\n \x1b[43m    \x1b[41m        \x1b[43m \x1b[41m ▓▓\x1b[33m▓▓▓▓▓▓▓▓▓▓▓▓▓ \x1b[43m          \x1b[36m▓▓▓▓\x1b[46m      \x1b[49m\n \x1b[43m    \x1b[41m \x1b[43m \x1b[41m        \x1b[33m▓▓▓▓▓▓▓\x1b[43m▓▓\x1b[41m▓▓▓▓▓▓ \x1b[43m          \x1b[36m▓▓▓▓\x1b[46m      \x1b[49m\n \x1b[43m    \x1b[41m          \x1b[33m▓▓▓▓▓▓\x1b[43m▓\x1b[41m\x1b[36m▓▓\x1b[43m\x1b[33m▓\x1b[41m▓▓▓▓▓ \x1b[43m         \x1b[47m \x1b[43m\x1b[36m▓▓▓▓▓\x1b[46m     \x1b[49m\n \x1b[43m    \x1b[41m \x1b[43m \x1b[41m      \x1b[43m \x1b[41m       \x1b[43m\x1b[33m▓\x1b[41m\x1b[36m▓▓\x1b[43m\x1b[33m▓\x1b[41m      \x1b[43m         \x1b[47m \x1b[36m▓\x1b[43m▓▓▓▓▓\x1b[46m▓   \x1b[49m\n \x1b[43m  \x1b[41m            \x1b[33m▓▓▓▓▓▓\x1b[43m▓\x1b[41m\x1b[36m▓\x1b[43m\x1b[33m▓\x1b[41m▓▓▓▓▓▓   \x1b[43m        \x1b[47m \x1b[36m▓ \x1b[43m▓▓▓▓▓\x1b[46m▓▓\x1b[49m\n \x1b[43m \x1b[41m \x1b[43m\x1b[31m▓\x1b[36m▓\x1b[41m          \x1b[33m▓▓▓▓▓▓▓\x1b[43m▓\x1b[41m▓▓▓▓▓▓▓ \x1b[43m \x1b[31m▓\x1b[41m \x1b[43m         \x1b[47m  \x1b[43m\x1b[36m▓▓▓▓▓\x1b[46m▓\x1b[49m\n \x1b[43m \x1b[31m▓  \x1b[36m▓▓\x1b[41m      \x1b[43m \x1b[41m \x1b[33m▓▓▓▓▓▓▓▓▓▓▓▓▓▓\x1b[36m▓ \x1b[43m  \x1b[31m▓\x1b[41m \x1b[43m    ▓    \x1b[47m   \x1b[43m\x1b[36m▓▓▓▓\x1b[49m\n \x1b[43m      ▓▓\x1b[41m      \x1b[33m▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ \x1b[43m   \x1b[41m \x1b[43m   \x1b[31m▓▓▓     \x1b[47m \x1b[43m\x1b[36m▓▓▓▓\x1b[49m\n \x1b[43m   \x1b[31m▓    \x1b[36m▓▓\x1b[41m                    \x1b[43m               \x1b[47m ▓\x1b[43m▓▓▓\x1b[49m\n \x1b[43m  \x1b[31m▓▓                                          \x1b[47m  \x1b[43m\x1b[36m▓▓\x1b[49m '

# Alternative allowed responses for Yes No questions.
no_responses = ["n", "no", "nay", "nah", "nope", "no thanks"]
yes_responses = ["y", "yes", "ok", "sure", "aye", "why not"]

# Debug settings
fast_text = False

# Make sure all the variables exist from the start
event_count = 0
player_name = "Player"
event_list = money = health = ship_name = fruit_name = None

# Set everything to the initial values in case of restart.
def initialise():
    global event_count, event_list, event_list, money, health, still_alive
    event_count = 0
    still_alive = True

    # Finds all event functions in the program, and puts them in a list using list comprehension
    # We do this rather than making a list manually so we can be sure every valid function is listed.
    
    event_list = [
        globals()[x] for x in globals().keys() 
        # Uses regex to find functions with a name that starts with "eventXX" where XX is a number.
        if re.match("event\d+.*", x) 
    ]

    money = 5.00
    health = 10

# Basically time.sleep, but it only runs if {fast_text} isn't enabled.
def sleep(seconds:float):
    if not fast_text:
        time.sleep(seconds)

# Types out text one character at a time.
# Speed argument dictates how many characters are printed per second.
# If Vertical is True, prints an entire line at a time instead.
def typewrite(text, speed=None, vertical=False):
    if speed == None: speed = 1/100
    else: speed = 1/speed

    if not vertical: # Prints one character at a time
        # Wraps the text onto multiple lines, to make text more readable.
        
        # Added some code to fix the problems caused by textwrap removing newlines.
        # Works by splitting each string into its component lines,
        # wrapping each line, and then joining them together again.
        text = '\n'.join(
            ['\n'.join(textwrap.wrap(line, 100, break_long_words=True, replace_whitespace=True)) for line in text.splitlines() if line.strip() != '']
        )
        
        for i,character in enumerate(text):
            print(character, end='', flush=True) # Makes flush with previous line

            # Pauses a little longer at full stops, and the like.
            # Checks to make sure it is actually a full stop and not
            # an ellipsis or a decimal point by seeing if the next character
            # is a space or a new line.
            if i+1 < len(text):
                if text[i] in [".", "?", "!", ":"] and text[i+1] in [" ", "\n"]:
                    sleep(speed*100)
                else:
                    sleep(speed)
            else:
                sleep(1) # Waits a second after each line for pacing.
    else: # Prints one line at a time
        for line in text.split("\n"):
            print(line)
            sleep(speed)
    print() # Makes sure the next print statement isn't on the same line.

# Handles player input prompts.
# Requires a prompt, a message to output if given an invalid input, and lists of valid inputs.
# Unless fail_gracefully is True, the prompt will loop until a valid input is given or
# the number of attempts runs out (if set to anything but None).
# When loop ends, returns the corresponding index of a valid input, and -1 otherwise.
def ask_question(prompt, invalid_response_string, choices, fail_gracefully=False, attempts=None):  
    def question():
        typewrite(prompt)
        print()
        return input(f"   >  {CYAN}").lower().strip()

    valid_answer = False

    # Keep looping until user inputs a valid answer
    # (unless {fail_gracefully} is True, in which case output -1)
    while valid_answer == False:
        response = question()
        print(RESET)
        valid_answer = True # Assume the answer is valid until told otherwise

        # Check if input is listed in any of the lists of valid answers.
        for i,choice in enumerate(choices):
            if response in choice:
                # Return the index of the valid answer.
                return i
        else:
            # If the attempts argument is set, the loop can
            # end if too many invalid inputs are given.
            if attempts is not None: 
                attempts -= 1
                if attempts <= 0:
                    return -1;
            typewrite(invalid_response_string) # Print the message
            valid_answer = False
            if fail_gracefully:
                return -1

# Gives the player a prompt to restart or quit the game,
# when they finish the story or reach a failure state.

def gameOver(good_ending=True):
    if good_ending:
        print(" " + CYAN + " ")
        typewrite(f"THE END", 3)
        print(" " + RESET + " ")
    else:
        typewrite(f"  {RED}Game Over{RESET}   ", 5)
        print()
        

    result = ask_question(
        prompt=f"Do you want to {CYAN}Q{RESET}uit or {CYAN}R{RESET}estart?",
        invalid_response_string="Sorry, but that's not an option.",
        choices=[
            ["q", "n", "quit", "exit"],
            ["r", "y", "restart", "replay"],
        ],
    )

    if result == 0: quit()

# New events can be added as functions if they use the
# naming format "eventXX", where XX is a 2 digit number.
# These functions will automatically be sorted into a list
# and run in order.

def event01_intro():
    global player_name, fast_text, ship_name, fruit_name
    player_name = input("Enter your name: ").capitalize()
    if player_name == "": 
        player_name = "Player"  # Use a default name if the player doesn't enter one.
    
    if player_name == "Debug": 
        fast_text = True  # Secret code for quicker replays.
        ship_name = f"{YELLOW}The Wanderer{RESET}"
        fruit_name = f"{YELLOW}Sapphire Berry{RESET}"
    else:
        fast_text = False
        ship_name = f"{YELLOW}{input('What is the name of your ship?: ')}{RESET}"
        fruit_name = f"{YELLOW}{input('What mythical fruit are you transporting?: ')}{RESET}"

    print()

    typewrite(f"\nYou are the captain of a merchant vessel, {ship_name}, transporting the super rare {fruit_name} fruit from the Bahamas. The sea is a beautiful blue, and the sun is shining.")
    typewrite("Everything is going well, but being the silly sausage that you are, you crash your ship.")

    typewrite(f"\"Ah dang,\" you think aloud. You stand on the deck of the {ship_name} surveying the sea, wondering what the heck to do now.\n")
    print()
    typewrite("That's when you notice two potentially life-saving objects, tied to the side guardrails:")
    typewrite(f" • Your {YELLOW}life jacket{RESET} (It has never failed you).")
    typewrite(f" • Your trusty {YELLOW}life raft{RESET} Sandra.\n")

    result = ask_question(
        prompt=f"Do you pick {GREEN}A{RESET}, the {CYAN}life jacket{RESET}, or {GREEN}B{RESET} the {CYAN}life raft{RESET}?",
        invalid_response_string=f"{RED}This is no time to mess around! You've got a sinking feeling about this and it's very literal.{RESET}",
        choices=[
            ["a", "life jacket", "jacket"],
            ["b", "life raft", "raft", "sandra"],
        ]
    )

    if result == 0:
        global health
        typewrite(f"You decide to trust your good old faithful life jacket.")
        typewrite("Clipping in the last of the jacket’s straps, you prepare to vault the guardrail.")
        typewrite("Before you even touch the water, a shark jumps and eats you in one clean bite. You failed to look for lifejacket eating sharks before leaping.")
        change_health(-10)
    elif result == 1:
        typewrite(f"You run over to Sandra and yank on the rip cord.")
        typewrite("The raft inflates within mere seconds. You chuck Sandra overboard and jump off the side of your sinking vessel, landing with a bump on the raft.")    

def event02():
    try:
        typewrite(sea_image + RESET + RESET2, 20, vertical=True)    
        sleep(2) # Slight delay before the moving on.
    except UnicodeEncodeError:
        pass

    typewrite("Using the oars contained within your swiss army knife, you paddle away from the ship-turned-submarine. Not long after that, you spy two islands in the distance.")
    typewrite("Unfolding your Tesco© branded pocket size map, you quickly ascertain the islands' names:\n")

    result = ask_question(
        prompt=f"Do you row toward A) {CYAN}Normal Sane Island{RESET}, or B) {CYAN}Idiot Island{RESET}?",
        invalid_response_string=f"{RED}Your raft is starting to deflate. Better make a choice pronto.{RESET}",
        choices=[
            ["a", "1", "normal", "normal island", "normal sane island"],
            ["b", "2", "idiot", "idiot island"],
        ]
    )

    if result == 0:
        global money
        typewrite(f"Good news, {player_name}. Normal Sane Island is part of the Idiot Island Premium Expansion DLC. Purchase now for the low price of £4.99.")
        change_money(-4.99)
        sleep(2)
        print()
        typewrite("Payment has been accepted. Download will now begin.")
        print()
        typewrite(" . . .", 100)
        typewrite("Download 0.1% Complete")
        sleep(2)
        print()
        typewrite("This is taking too long. For now, you decide to just sail to Idiot Island")
    else:
        typewrite("You sail over to Idiot Island, an evil black storm localised entirely over the island spits lightning, thunder rips through the sky, a menacing organ plays, dun dun duuun!")

def event03():
    typewrite("Pulling your precious Sandra up onto the beach, you gaze across the island, in front of you lies a jungle, to the left and right an endless beach disappears into the horizon.")
    typewrite("Not wanting to imagine how much additional effort it would take to explore these branching paths, you decide to just go straight into the jungle. Stomach grumbling, you swear to yourself.")
    typewrite(f"\"{RED}Gosh{RESET}\" you curse to the heavens. \"{RED}Dang{RESET}, {RED}darn{RESET}, {RED}fiddlesticks{RESET} and {RED}silly sausage{RESET}\". You use all the foulest words your potty mouth can possibly muster to express your blistering rage at this situation. You should have packed a Mars bar before you abandoned the ship.")
    typewrite("That's when you come across a coconut tree. You'd prefer something filled with caramel, but either way it's food! What do you do?.")

    result = ask_question(
        prompt=f"{GREEN}A{RESET}) {CYAN}Climb the tree{RESET} and attempt to knock out a coconut.\n{GREEN}B{RESET}) {CYAN}Throw something{RESET} at the coconuts to knock one loose.",
        invalid_response_string=f"{player_name} attempts to throw '{YELLOW}something{RESET}' at the coconuts, unfortunately they don't have '{YELLOW}something{RESET}' in their inventory.",
        choices=[
            ["a", "climb"],
        ]
    )

    if result == 0:
        typewrite(f"{player_name} decides to shimmy their way up the coconut tree, resisting with all their willpower the urge to make monkey noises.")
        typewrite(f"Sadly, they are not part simian and slip from the tree, losing {RED}9 HP{RESET}. The vibration of their butt hitting the ground knocks a {YELLOW}coconut{RESET} loose, which they promptly eat to restore {CYAN}14 HP{RESET}. Nom!")
        change_health(5)

def event04a():
    # Create a list of items you have in your pocket
    # and add a few to start.
    pocket_contents = ["gold", "broom", "bicycle"]

    # Puts new item in pocket
    def pick_up_item(item):
        typewrite(f"Whilst wandering through the jungle, you find a {YELLOW + item + RESET} and you pick it up and put in your pocket.")
        pocket_contents.append(item)

    # If an item is in your pocket, drops it.
    # If it isn't, does nothing.
    def drop_an_item(item):
        nonlocal loop_is_running

        if item in pocket_contents:
            typewrite(f"You throw the {item} away and climb out of the quicksand.")
            pocket_contents.remove(item)
            loop_is_running = False
        else:
            typewrite(f"You don't have any {item}s to drop.")

    pick_up_item("flower")
    loop_is_running = True

    typewrite(f"Suddenly, you realise you've been walking in {YELLOW}quicksand{RESET}! You're sinking fast, but you think you might be light enough to escape if you just drop just one item.")

    while loop_is_running:
        typewrite("In your pocket right now, you have:")
        typewrite(", ".join(pocket_contents))
        typewrite("You need to type the name of the item you want to drop")
        print()
        player_input = input(" > ")
        print()
        drop_an_item(player_input)    
    typewrite("That was a close call!")

def event04b():
    # Create a list of items you have in your pocket
    # and add a few to start.
    pocket_contents = ["gold", "broom", "bicycle"]

    typewrite(f"You meet a {YELLOW}parrot{RESET}.")
    typewrite(f"\"Alright mate?\" it asks. \"I've had better days.\" you reply.")
    typewrite(f"\"Tell you what mate.\" it says. \"I've got all these {YELLOW}pieces of eight{RESET} rattling around in my feathers. Probably £2.20's worth, given current exchange rates.")
    typewrite(f"If you {CYAN}guess the number{RESET} I'm thinking of, you can have the lot. If you're one off, you can have half of it.\"")
    typewrite(f"You see no reason not to play along.")

    parrot_number = random.randint(1,10)
    print()
    player_number = input("Enter a number between 1 and 10: ")
    print()

    if not player_number.isnumeric():
        typewrite(f"\"OK you're just being silly.\" says the parrot, before stealing whatever change you have on you. You suppose that's how it was making its money.")
        change_money(-10000)
    elif parrot_number == int(player_number):
        typewrite(f"\"Wow, perfect! Have the full £2.20 as a reward\" says the parrot, before flying away.")
        change_money(2.20)
    elif abs(parrot_number - int(player_number))  == 1:
        typewrite(f"\"So close! It was {parrot_number}. Here's £1.10 as promised.\" says the parrot, before flying away.")
        change_money(1.10)
    else:
        typewrite(f"\"Too bad. It was actually {parrot_number}.\" says the parrot, before flying away.")

def event05():
    typewrite("\n It’s beginning to get dark, and with all the random misadventures you’ve been having, you completely forgotten to make shelter. Through the island jungle a brush you distant firelight. Sneaking with the finesse of an elephant you come across the source of the light.")
    print()
    sleep(2) # Slight delay before the image appears.
    try:
        typewrite(pirate_image + RESET + RESET2, 20, vertical=True)   
        sleep(2) # Slight delay before the moving on. 
    except UnicodeEncodeError:
        pass
    
    typewrite(f"An old {YELLOW}pirate{RESET} is sitting by a fire, in his right hand he has a bottle of ‘rum’. He is a broken man. The pirate's face wears an overgrown beard ravaged with filth and knots. The left side of his face is badly scarred, an eyepatch covering a damaged eye.") 
    
    typewrite(f"The pirate spots you and beckons you to approach, this is a man so lonely he would appreciate any company. \"Me name's {YELLOW}Scurvy Jim{RESET}, have some rum\"")     
    typewrite("You take the bottle, and give it sniff, it has a pungent odour, but you don’t know your rum so this could be normal.")
    
    result = ask_question(
        prompt=f"{GREEN}A{RESET}) Drink the {CYAN}rum{RESET}.\n{GREEN}B{RESET}) {CYAN}Refuse{RESET}.",
        invalid_response_string="\"Sorry, matey, ye'll have to speak up a bit. Me hearing's not what it used to be.\" the pirate says. He offers the bottle again.",
        choices=[
            ["a", "drink", "drink rum"] + yes_responses,
            ["b", "refuse"] + no_responses
        ]
    )

    if result == 0:
        typewrite(f"Being courteous, you down a swig of the rum. Oh no... that smell wasn’t normal, that rum that was not rum, it was. . . {YELLOW}wee{RESET}.")
        typewrite(f"You throw up on {YELLOW}Mr Jim{RESET}. He is understandably insulted by this, and reciprocates by jamming his cutlass into your ribcage.")
        typewrite(f"As a result, you lose {RED}1,000,000 HP{RESET}.")
        change_health(-1000000)
    elif result == 1:
        typewrite(f"\"Sorry I’m a recovered alcoholic\" you tell {YELLOW}Jim{RESET}. \"Oh, that’s completely fine\", he replies \"Sorry if I offended you\", he reaches behind him and hands you a bottle of water. \"Here have this ice chilled water, it’s handy having a cooler\".")
        typewrite(f"\"Refreshing! {CYAN}+3 HP{RESET}.")
        change_health(3)

def event05a():
    typewrite(f"With the ice cool water slowly passing its way down your throat, the pirate is warming to you, he seems to want to ask you a question. \"Okay me land lubber, I have me a {YELLOW}question{RESET} for you. Suppose you start with a number. You multiply the number by 3, add 7, divide by ½, subtract 5, and then divide by 12. The result is 5. What number did you start with\"")

    result = ask_question(
        prompt="Oh no... of all the people to get stranded with, you got stranded with a wanna be maths teacher, best get this over with.",
        invalid_response_string="You proudly give what you think is the correct answer... (or so you hope).",
        choices=[
            ["8.5", "8.50", "eight point five"],
        ],
        fail_gracefully=True
    )

    if result == 0:
        typewrite("The answer is 8.5, you declare.. (or at least that's what the guy on Quora said it was.")
        typewrite("The pirate responds, correct, looks like someone passed their GCSE Maths.")
        typewrite("He fishes around in his pocket for a reward. \"Here's a genuine £8.50 note\"")
        change_money(8.50)
    else:
        typewrite("The pirate responds with a flat \"no\".")
        typewrite("He slaps you across the face with the back of his hand.")
        typewrite("Study more!")
        change_health(-1)

def event06():
    typewrite(f"Night falls, {player_name} and {YELLOW}Scurvy Jim{RESET} settle into their hammocks, and the time goes by without incident, besides all the ungodly shrieks and screams that animals make at night-time for some reason.")
    print()
    typewrite(f"Dawn breaks followed slowly by the morning. With the early morning light shining brightly, you realise you're feet away from where you first landed. Your beautiful {YELLOW}rubber vessel{RESET} sits in the sand, glowing fluorescently in the sun's rays.")
    typewrite(f"“Sandraaaaa! I missed you, Sandra” you shout. The pirate looks at you weirdly. You can’t help yourself you just have to do it. You sprint towards your one true rubber covered friend with open arms. Wrapping your arms around the {YELLOW}raft{RESET} in front of you, with tears in your eyes you whisper, “I’ve missed you Sandra”")
    typewrite(f"“You alright mate”, Jim asks.")
    typewrite(f"Are you? It's time to decide.")

    result = ask_question(
        prompt=f"{GREEN}A{RESET}) {CYAN}Leave with Sandra{RESET}.\n{GREEN}B{RESET}) {CYAN}Stay with Jim{RESET}.",
        invalid_response_string="Maybe you can choose something else...",
        choices=[
            ["a", "drink", "drink rum"] + yes_responses,
            ["b", "refuse"] + no_responses
        ],
        fail_gracefully=True
    )

    if result == 0:
        typewrite("Like the few cards missing of a full deck, mad fool you are, you completely forget about your new pirate friend and set sail with Sandra. Onwards to new adventures!")
        typewrite("Jim waits until you've vanished beyond the horizon, sits back, and cracks open a warm one. All alone forever more on")
    elif result == 1:
        typewrite("You snap back into reality, you begin to see sense, “No, no I’m not,” you reply to your real flesh and blood friend. Shame you found the resolve you needed from a nutter who drinks yellow ‘rum’. You yeet Sandra back into the sea from whence she came.")
        typewrite("You have found your place, your true home, here on")
    else:
        typewrite("\"Come with me Jim\" you cry, grasping the old sea-dog's hands. \"Let's leave this silly place forever!\"")
        typewrite(f"\"I'd love nothing more\" he starts crying, and so do you, your salty tears contributing to the rising sea levels. \"Let's do this... together.\" You both gather some of the {fruit_name}s that have washed ashore to keep you fed on the journey, before setting sail and waving goodbye forever to")
    print()
    typewrite(f"{YELLOW}Idiot Island{RESET}", 5)

# Adds or subtracts health points from the player.
# Changes the still_alive flag if health is less than
# or equal to zero.

def change_health(amount):
    global health, still_alive
    health = health + amount

    if health <= 0: still_alive = False

# Adds or subtracts money from the player.
# Checks if the money is below 0 and set it to 0 if it is
# to prevent the situation where they have negative money.

def change_money(amount):
    global money
    money += amount
    if money < 0: money = 0

    return money

# Print player's current health and money (rounded to 2 decimal places)
# and puts a box around the outside.

def show_status(final_result=False):
    if final_result:
        label = "Current Status" # What the label at the top of the box says.
    else: label = "Final Results-" # Change the label if the game is over.
    output = f"| {RED} HP: {RESET} {health} {YELLOW}   Money: {RESET} £{'{0:.2f}'.format(money)}  |"
    print(f"\n--" + label + "-" * (len(output) - 36)) # Makes the box width match the contents               
    print(output)
    print("-" * (len(output) - 20))
    sleep(2)
    print()

keep_playing = True # Needed to start the loop.
while keep_playing:
    # Set all the variables to the starting amounts
    initialise()

    # Runs through the list of events in order.
    # Doing it this way so the status prints between each event,
    # and new events can be added to the list automatically if they
    # match the naming convention {event[eventNumber]}

    while len(event_list) > 0: # Play every event in order
        if not still_alive: break # Break out of the loop if player is out of HP
        
        event = event_list.pop(0)
        event() # Run the event

        # Shows health, money, etc after each turn.
        # Changes status box label from "Current Status" to 
        # "Final Results" if this is the last event.
        show_status(len(event_list) > 0 and still_alive) 
    gameOver(still_alive)