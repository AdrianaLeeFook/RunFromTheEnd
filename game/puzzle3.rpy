default found_cash = False
default found_key = False
default found_clothes = False
default found_water = False
default found_backpack = False
default score = 0
default tooltip = ""

define Taylor = Character("Taylor")

screen hidden():

    add "hiddenobject.png"
    modal True

    text "Found: [score]/5" xpos 20 ypos 20 size 30 color "#fff"
    text tooltip xpos 20 ypos 60 size 25 color "#ff0"

    # CASH
    if not found_cash:
        imagebutton:
            idle "cash_idle.png"

            hovered SetVariable("tooltip", "Cash")
            unhovered SetVariable("tooltip", "")

            action [
                SetVariable("found_cash", True),
                SetVariable("score", score + 1)
            ]

    # KEY
    if not found_key:
        imagebutton:
            idle "key_idle.png"

            hovered SetVariable("tooltip", "Key")
            unhovered SetVariable("tooltip", "")

            action [
                SetVariable("found_key", True),
                SetVariable("score", score + 1)
            ]

    # CLOTHES
    if not found_clothes:
        imagebutton:
            idle "cloth_idle.png"

            hovered SetVariable("tooltip", "Clothes")
            unhovered SetVariable("tooltip", "")

            action [
                SetVariable("found_cloth", True),
                SetVariable("score", score + 1)
            ]
    # WATER
    if not found_water:
        imagebutton:
            idle "water_idle.png"

            hovered SetVariable("tooltip", "Water")
            unhovered SetVariable("tooltip", "")

            action [
                SetVariable("found_water", True),
                SetVariable("score", score + 1)
            ]

    # BACKPACK
    if not found_backpack:
        imagebutton:
            idle "backpack_idle.png"

            hovered SetVariable("tooltip", "Backpack")
            unhovered SetVariable("tooltip", "")

            action [
                SetVariable("found_backpack", True),
                SetVariable("score", score + 1)
            ]

    # WIN BUTTON
    if score == 5:
        textbutton "Next Level":
            xpos 850 ypos 600
            action Return()


label puzzle:

    image Taylor = "taylor.jpg"

    scene black
    "Find all the hidden objects!"

    call screen hidden

    "You found everything!"
 
    show Taylor at center
  
    Taylor "Taylor: Ok that's everything. NOW LETS GET OUT OF HERE! "

    return