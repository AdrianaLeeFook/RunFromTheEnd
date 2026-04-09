define taylor_thought = Character("Taylor" , what_italic = True)
define taylor = Character("Taylor")
define hayden = Character("Hayden")
define logan = Character("Logan")
define bella = Character("Bella")
define alex = Character("Alex")
define ruler = Character("The Ruler")
define julie = (Character("Julie"))
define kyle = Character("Kyle")
define cara = Character("Miss Cara")
define pierce = Character("Pierce")

label scene14:

    image taylor = "TaylorPlaceholder.png"
    image hayden = "HaydenPlaceholder.png"
    image logan = "LoganPlaceholder.png"
    image bella = "BellaPlaceholder.png"
    image alex = "AlexPlaceholder.png"
    image ruler = "RulerPlaceholderr.png"
    image julie = "JuliePlaceholder.png"
    image kyle = "KylePlaceholder.png"
    image pierce = "PiercePlaceholder.png"
    image cara = "CaraPlaceholder.png"

    scene throne_room with fade

    show ruler at center
    show taylor at left:
        zoom 0.65
    show hayden at right:
        zoom 0.75

    # OPENING

    hayden "Th-there’s only one of you…"

    ruler "No? I have— …why are my guards passed out on the floor?"

    taylor "Because we took them down."

    taylor "Maybe killed one or two."

    ruler "You would dare kill the KING’S ROYAL GUARD?!"

    ruler "I’LL HAVE YOU ALL ARRESTED AND EXECUTED!"

    taylor "Not if we make sure your reign ENDS HERE!"


    # PUZZLE SYSTEM

    label test_menu:

    $ tries = 5
    $ wins = 0

    # Optional: import random if not already
    $ import random

    # Start battle loop
    label battle_loop:

        if tries <= 0:
            jump check_result

        menu:
            "Choose your move:"

            "Attack":
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
            "The Ruler overpowered you!"

        $ tries -= 1

        "Wins: [wins] / 5   Tries left: [tries]"

        jump battle_loop  # repeat the loop

    # Check result after all tries
    label check_result:

        if wins >= 4:
            jump ruler_defeat
        else:
            jump ruler_win

# BAD END
label ruler_win:

    show ruler at center

    ruler "Oh how I cannot WAIT for execution day…"

    scene black with fade

    "GAME END"

    jump scene14

# GOOD END (YOU WIN)

label ruler_defeat:

    show ruler at center

    ruler "D…D…DAMN YOU, TAYLOR JENKINS!"

    ruler "I WILL SEE TO IT THAT YOU AND YOUR BROTHER ARE KILLED!"

    show taylor at left:
        zoom 0.65
    taylor "I don’t think so."

# you can add audio for dramatic effect


    with hpunch

    "STAB."

    hide hayden
    hide ruler
    show alex at right

    alex "…You…you killed him…"

    taylor "…Yeah. I did."

    # SELF DESTRUCT
    play sound "pasystem.mp3"
    "Castle PA" "ALERT! Intruders have breached the castle. The King has been found dead. Self destruct sequence will now begin."
    stop sound

    hide taylor
    show bella at left
    bella "SELF DESTRUCT?!"

    hide alex
    show logan at right
    logan "SHIT—we gotta RUN!"

    hide bella
    show taylor at left:
        zoom 0.65
    taylor "…Alex. Come on."

    show alex at center
    alex "Wait… you’re saving me too?"

    hide logan
    show hayden at right:
        zoom 0.75
    hayden "YES NOW MOVE BEFORE WE ALL DIE!"

    # escaping the castle

    # you can add audio for dramatic effect

    scene castle_escape with fade

    hide alex
    hide hayden
    show taylor at center:
        zoom 0.65

    taylor_thought "We ran."

    taylor_thought "And we made it out."

    taylor_thought "Behind us… the castle collapsed."

    taylor_thought "Stone by stone."

    taylor_thought "Until nothing remained."

    taylor_thought "Just rubble."

    taylor_thought "The remains of a monarchy."

    taylor_thought "Dead."

    # FINAL CROWD SCENE
    
    scene city_crowd with fade
    hide pierce
    "Civilian" "{size=-5} What happened to the castle?{/size}"
    play sound "Civilian2_BunBun.mp3"
    "Civilian" "{size=-5} Did those people sneak into the castle and come out alive? That’s unbelievable!{/size}"
    stop sound

    hide taylor
    show julie at right
    julie "{size=-5}(whispering) Kyle—look! It’s Tay!{/size}"

    show kyle at left
    play sound "Kyle_Line_5.mp3"
    kyle "{size=-5}(whispering) What the shit…{/size}"
    stop sound

    hide julie
    hide kyle
    show cara at center
    cara "The children… they’re all here…"

    hide cara
    show pierce at center:
        zoom 0.75
    pierce "I knew they could do it…"

    "Guard" "Does this mean we’re free?"

    stop music fadeout 2.0
    scene black with fade

    return