# Characters
define Taylor = Character("Taylor", color="#c8a2ff")
define Hayden = Character("Hayden", color="#6ec1ff")
define Bella = Character("Bella", color="#ffb6c1")
define Logan = Character("Logan", color="#ff9e6b")
define Alex = Character("Alex", color="#9effa1")
define Guard2 = Character("Guard 2", color="#ff4d4d")

# Images for this scene
image bg scene11 = "scene11bg.png"
image bg scene11guards = "scene11guards.png"

image Taylor = "taylor.png"
image Hayden = "hayden.png"
image Bella = "bella.png"
image Logan = "logan.png"
image Alex = "alex.png"

label scene11:

    scene bg scene11:
        zoom 1.5

    show Bella:
        xalign 0.2
        yalign 0.68

    show Alex:
        xalign 0.8
        yalign 0.68

    Bella "Yeah, sorry Alex! Logan’s good at what he does."

    hide Bella
    show Logan:
        xalign 0.2
        yalign 0.68

    Logan "See?"

    hide Alex
    hide Logan
    show Hayden:
        xalign 0.2
        yalign 0.68
        zoom 0.75

    show Taylor:
        xalign 0.8
        yalign 0.68
        zoom 0.65

    Hayden "(whispered) Taylor? Does any of this feel off to you?"

    Taylor "(whispered) Yes. It feels extremely off to me."

    hide Hayden
    hide Taylor

    show Taylor:
        xalign 0.5
        yalign 0.68
        zoom 0.65

    Taylor "Once Logan had the door open, we walked inside. We held our weapons at our side in the scenario we had to immediately begin a counterattack."

    hide Taylor
    show Hayden:
        xalign 0.2
        yalign 0.68
        zoom 0.75

    Hayden "Woah…it’s…enormous here…"

    show Taylor:
        xalign 0.8
        yalign 0.68
        zoom 0.65

    Taylor "Feels more like a regal ballroom than a government establishment. Then again…"

    hide Hayden
    hide Taylor
    show Bella:
        xalign 0.2
        yalign 0.68

    Bella "It’s as if a PRINCESS would live here!"

    hide Bella
    show Logan:
        xalign 0.2
        yalign 0.68

    Logan "Holy shit. If we live through this, I’m doing some renovations on the old place."

    hide Logan
    hide Alex
    hide Bella
    hide Hayden
    hide Taylor

    scene bg scene11guards:
        zoom 1.5

    Guard2 "INTRUDERS! GET THEM!"

    show Taylor:
        xalign 0.5
        yalign 0.68
        zoom 0.65

    Taylor "SHIT!"

    scene bg scene11:
        zoom 1.5

    show Bella:
        xalign 0.5
        yalign 0.68

    Bella "So as I was saying it’s as if this place was run by a- oh sorry! Didn’t see you there!"

    "SHOOT"

    hide Bella
    show Alex:
        xalign 0.2
        yalign 0.68
    show Bella:
        xalign 0.8
        yalign 0.68

    Alex "I- Bella, remind me to never get on your bad side."

    Bella "Hah! That’s not my bad side. I’m just crossbow and archery trained! Why do you think my daddy’s in a labor camp?"

    hide Alex
    show Taylor:
        xalign 0.2
        yalign 0.68
        zoom 0.65
    show Bella:
        xalign 0.8
        yalign 0.68

    Taylor "…OVER TEACHING HIS DAUGHTER TO DEFEND HERSELF?!"

    Bella "Yep! It broke some fine print rule andddd honestly I’ve been WAITING to use my skills."

    hide Taylor
    show Logan:
        xalign 0.2
        yalign 0.68
    show Bella:
        xalign 0.8
        yalign 0.68

    Logan "Damn. That’s impressive, even for you, Bell."

    Bella "What can I say? I have talents!"

    hide Logan
    hide Bella
    show Hayden:
        xalign 0.2
        yalign 0.68
        zoom 0.75

    Hayden "Don’t get too excited yet, there’s still more coming!"

    label test_menu3:

    $ tries = 5
    $ wins = 0

    $ import random

    # Start battle loop
    label battle_loop3:

    if tries <= 0:
        jump check_result3

    menu:
        "Choose your move:"

        "Strike":
            # 80% chance to succeed
            $ result = 1 if random.random() < 0.8 else 0

        "Defend":
            # 50% chance to succeed
            $ result = 1 if random.random() < 0.5 else 0

        "Counter":
            # 30% chance to succeed
            $ result = 1 if random.random() < 0.8 else 0

    if result == 1:
        $ wins += 1
        "You gained the advantage!"
    else:
        "The guards gained the advantage!"

    $ tries -= 1

    "Wins: [wins] / 5   Tries left: [tries]"

    jump battle_loop3  # repeat the loop

# Check result after all tries
label check_result3:

    if wins >= 4:
        jump taylor_win
    else:
        jump taylor_defeat

# BAD END
label taylor_defeat:

    show Taylor at center

    Taylor "URGH…dammit…"

    scene black with fade

    "GAME END"

    jump scene11

# GOOD END (YOU WIN)

label taylor_win:

    show Taylor at center

    Taylor "That was easier than I thought…"

    hide Taylor
    hide Hayden
    show Bella:
        xalign 0.2
        yalign 0.68
    show Logan:
        xalign 0.8
        yalign 0.68

    Bella "That was AWESOME!"

    Logan "Didn’t think shooting those bastards would feel this relieving!"

    hide Bella
    hide Logan
    show Taylor:
        xalign 0.2
        yalign 0.68
        zoom 0.65
    show Hayden:
        xalign 0.8
        yalign 0.68
        zoom 0.75

    Taylor "Gotta say…that was actually kinda fun."

    Hayden "I got to use a dagger. That was just so COOL!"

    hide Taylor
    hide Hayden
    show Alex:
        xalign 0.2
        yalign 0.68

    Alex "Hey, gotta love times when you can just deal some well deserved justice."

    show Taylor:
        xalign 0.8
        yalign 0.68
        zoom 0.65

    Taylor "I guess. There’s still something that just isn’t sitting right with me in this situation."

    hide Alex
    show Bella:
        xalign 0.2
        yalign 0.68
    show Taylor:
        xalign 0.8
        yalign 0.68
        zoom 0.65

    Bella "What’s wrong, Taylor?"

    Taylor "I just feel like there’s something underlying here…it’s as if someone is watching us…"

    hide Bella
    show Hayden:
        xalign 0.2
        yalign 0.68
        zoom 0.75
    show Taylor:
        xalign 0.8
        yalign 0.68
        zoom 0.65

    Hayden "Yeah…usually I can say Taylor’s being crazy but…I feel it too…"

    return