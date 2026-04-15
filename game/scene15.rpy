# Characters
define Taylor = Character("Taylor", color="#c8a2ff")
define Hayden = Character("Hayden", color="#6ec1ff")
define Bella = Character("Bella", color="#ffb6c1")
define Logan = Character("Logan", color="#ff9e6b")
define Alex = Character("Alex", color="#9effa1")
define Julie = Character("Julie", color="#ff8fd8")
define Kyle = Character("Kyle", color="#7fd4ff")
define Cara = Character("Miss Cara", color="#ffd700")
define Pierce = Character("Pierce", color="#9bff7f")

# Images
image bg scene15 = "scene15bg.png"

image Taylor = "taylor.png"
image Hayden = "hayden.png"
image Bella = "bella.png"
image Logan = "logan.png"
image Alex = "alex.png"
image Julie = "julie.png"
image Kyle = "kyle.png"
image Cara = "cara.png"
image Pierce = "pierce.png"

label scene15:

    scene bg scene15:
        zoom 1.5

    # Opening speech
    show Taylor:
        xalign 0.5
        yalign 0.68
        zoom 0.65

    Taylor "(projecting) Ahem! People of the Yonder District and anyone else who hears my words! This awful nightmare is over."

    Taylor "(projecting) The Ruler has been slain, and we can finally live our lives as we want to."

    Taylor "We can leave. Be on our own. He is no more."

    "Crowd Cheers"

    # Logan + Alex
    hide Taylor
    show Logan:
        xalign 0.2
        yalign 0.68
    show Alex:
        xalign 0.8
        yalign 0.68

    Logan "Well shit. I can finally get out of here. Maybe find my parents."

    Alex "Oh dude, they’re dead."

    Logan "WHAT THE HELL?! How do- oh yeah. You worked for the bastards."

    # Hayden + Taylor
    hide Logan
    hide Alex
    show Hayden:
        xalign 0.2
        yalign 0.68
        zoom 0.75
    show Taylor:
        xalign 0.8
        yalign 0.68
        zoom 0.65

    Hayden "Taylor? Are we gonna be alright after all of this?"

    Taylor "Yeah. But we’re leaving. There’s nothing left here for us."

    # Bella + Alex
    hide Hayden
    hide Taylor
    show Bella:
        xalign 0.2
        yalign 0.68
    show Alex:
        xalign 0.8
        yalign 0.68

    Bella "Hey! You aren’t leaving without me! I mean, we still have more adventures!"

    Alex "…I’m probably gonna head off on my own. I need to have some time for self recovery after this."

    # Logan argues
    hide Bella
    show Logan:
        xalign 0.2
        yalign 0.68
    show Alex:
        xalign 0.8
        yalign 0.68

    Logan "HAH! After all this shit, we aren’t letting you leave. You’re sticking with us."

    # Bella joins
    hide Logan
    show Bella:
        xalign 0.2
        yalign 0.68
    show Alex:
        xalign 0.8
        yalign 0.68

    Bella "After allll you did…alllll the trickery…you’re on a SHORT LEASH!"

    Alex "WHAT?! I didn’t even DO that much!"

    # Logan continues
    hide Bella
    show Logan:
        xalign 0.2
        yalign 0.68

    Logan "…YOU BROKE US INTO THE CASTLE KNOWING WHAT WOULD HAPPEN! At least Taylor just knew it wouldn’t be super guarded!"

    Logan "You aren’t going ANYWHERE."

    # Bella final word
    hide Logan
    show Bella:
        xalign 0.2
        yalign 0.68

    Bella "YEAH! Wherever we go next, you go too! You can’t be trusted alone!"

    show Alex:
        xalign 0.8
        yalign 0.68

    Alex "…Ugh fine."

    hide Bella
    hide Alex

    # Julie enters
    show Julie:
        xalign 0.5
        yalign 0.68
    play sound "Julie_Line_12.mp3"
    Julie "TAY TAYYYY! WHAT HAPPENED?! WHAT DID YOU DO GIRL?!"
    stop sound

    hide Julie
    show Taylor:
        xalign 0.5
        yalign 0.68
        zoom 0.65

    Taylor "…I killed the Ruler and a guard. Maybe two."

    hide Taylor

    # Kyle + Hayden
    show Kyle:
        xalign 0.2
        yalign 0.68
    show Hayden:
        xalign 0.8
        yalign 0.68
        zoom 0.75
    play sound "Kyle_Line_6.mp3"
    Kyle "Yoooo dude, that’s so sick! And the little man’s here!"
    stop sound

    Hayden "ACK! KYLE! STOPPP!"

    hide Kyle
    hide Hayden

    # Cara moment
    show Cara:
        xalign 0.5
        yalign 0.68

    Cara "BELLA! LOGAN! ALEX! You three are alright! I got worried. I wasn’t prepared to hear about THIS!"

    hide Cara
    show Bella:
        xalign 0.5
        yalign 0.68

    Bella "Miss Cara…I…is it true you killed those kids on purpose?"

    hide Bella
    show Cara:
        xalign 0.5
        yalign 0.68

    Cara "…I let Alex do what they needed. I just housed them…the money…"

    hide Cara
    show Bella:
        xalign 0.5
        yalign 0.68

    Bella "It was wrong…Miss Cara. I…I don’t know…if we can trust you right now…"

    hide Bella
    show Cara:
        xalign 0.5
        yalign 0.68

    Cara "(tearing up) I understand…and I’m sorry…"

    hide Cara
    show Bella:
        xalign 0.5
        yalign 0.68

    Bella "…I don’t think I can forgive you right now…but…maybe one day I will…"

    hide Bella

    # Pierce + ending
    show Pierce:
        xalign 0.2
        yalign 0.68
        zoom 0.65
    show Logan:
        xalign 0.8
        yalign 0.68

    Logan "Yo, Pierce!"

    Pierce "I knew yall could do it! Like holy shit! Yall managed to take down a monarch! So who got the final blow and were the grenades used?"

    show Taylor:
        xalign 0.5
        yalign 0.68
        zoom 0.65

    Logan "Taylor got the final blow, but the castle had a self destruct sequence."

    return