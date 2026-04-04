label scene14:

    scene throne_room with fade

    show ruler angry at center
    show taylor serious at left
    show hayden nervous at right

    # OPENING

    hayden "Th-there’s only one of you…"

    ruler "No? I have— …why are my guards passed out on the floor?"

    taylor "Because we took them down."

    taylor "Maybe killed one or two."

    ruler "You would dare kill the KING’S ROYAL GUARD?!"

    ruler "I’LL HAVE YOU ALL ARRESTED AND EXECUTED!"

    show taylor angry
    taylor "Not if we make sure your reign ENDS HERE!"


    # PUZZLE SYSTEM

    label test_menu:

    $ tries = 5
    $ wins = 0

    # Start battle loop
    label battle_loop:

        if tries <= 0:
            jump check_result

        menu:
            "Choose your move:"

            "Attack":
                $ result = renpy.random.randint(0, 1)

            "Defend":
                $ result = renpy.random.randint(0, 1)

            "Counter":
                $ result = renpy.random.randint(0, 1)

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

    show ruler grin at center

    ruler "Oh how I cannot WAIT for execution day…"

    scene black with fade

    "GAME END"

    return


# GOOD END (YOU WIN)

label ruler_defeat:

    show ruler shocked at center

    ruler "D…D…DAMN YOU, TAYLOR JENKINS!"

    ruler "I WILL SEE TO IT THAT YOU AND YOUR BROTHER ARE KILLED!"

    show taylor calm
    taylor "I don’t think so."

# you can add audio for dramatic effect


    with hpunch

    "STAB."

    show alex shocked at right

    alex "…You…you killed him…"

    show taylor serious
    taylor "…Yeah. I did."

    # SELF DESTRUCT



    "Castle PA" "ALERT! Intruders detected."

    "Castle PA" "The King has been found dead."

    "Castle PA" "Self destruct sequence initiated."

    show bella shocked
    bella "SELF DESTRUCT?!"

    show logan scared
    logan "SHIT—we gotta RUN!"

    show taylor urgent
    taylor "…Alex. Come on."

    alex "Wait… you’re saving me too?"

    show hayden urgent
    hayden "YES NOW MOVE BEFORE WE ALL DIE!"

    # escaping the castle

    # you can add audio for dramatic effect

    scene castle_escape with fade

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

    "Civilian" "{size=-5}(whispering) What happened to the castle?{/size}"
    "Civilian" "{size=-5}(whispering) Did they actually survive that?{/size}"

    show julie shocked
    julie "{size=-5}(whispering) Kyle—look! It’s Tay!{/size}"

    show kyle shocked
    kyle "{size=-5}(whispering) What the hell…{/size}"

    show cara serious
    cara "The children… they’re all here…"

    show pierce proud
    pierce "I knew they could do it…"

    "Guard" "Does this mean we’re free?"

    stop music fadeout 2.0
    scene black with fade

    "END OF SCENE 14"

    return