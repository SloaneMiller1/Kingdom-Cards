# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Heart", color = "#990033")

define de = Character("Dee", color = "#ff0000")

define du = Character("Dum", color = "#ff0000")

define dendu = Character("Dee and Dum", color = "#ff0000")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
    "You don’t know where you are but it hurts your eyes a lot and not just your eyes actually all your senses hurt. A lot!"
    "It feels like you had a sensory overload and its so bad you cant even get your eyes back open."

    dendu "HALT"

    de "Halt in the name-"
    du "-Of the Heart Queen’s bodyguards!"


    # This ends the game.

    return
