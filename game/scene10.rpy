define taylor_thought = Character("Taylor" , what_italic = True)
define taylor = Character("Taylor")
define hayden = Character("Hayden")
define logan = Character("Logan")
define bella = Character("Bella")
define alex = Character("Alex")

label scene10:

    scene castle_gate_night with fade

    image taylor = "TaylorPlaceholder.png"
    image hayden = "HaydenPlaceholder.png"
    image logan = "LoganPlaceholder.png"
    image bella = "BellaPlaceholder.png"
    image alex = "AlexPlaceholder.png"

    play music "audio/ominous.ogg" fadein 2.0

    show taylor at center:
        zoom 0.65

    # ARRIVAL
    taylor_thought "It felt too good to be true… but we had a plan."

    taylor_thought "We had defense."

    taylor_thought "I had a team."

    taylor_thought "A few hours later, after a quick snack break… we made it."

    taylor_thought "The castle gates stood right in front of us."

    # Everyone gets to the castle
    
    show hayden at left:
        zoom 0.75
    show bella at right

    hayden "Woah… the castle is a lot bigger than I imagined."

    bella "WOAH! It’s MASSIVE!"

    hide hayden
    show taylor at left:
        zoom 0.65
    taylor "And unguarded… which makes it even more suspicious."

    hide bella
    show logan at right
    logan "An unmanned castle on a protest day?"

    logan "Yeah… that’s not normal."
    
    hide taylor
    show alex at left

    alex "Hey… maybe we can just kick the gate."

    hide logan
    show bella at right
    bella "ARE YOU CRAZY?! We can’t just KICK the gate!"

    alex "You wanna test that?"

    hide bella
    show taylor at right:
        zoom 0.65
    taylor "…Your funeral. Go ahead."

    alex "Bet."

    # the gate breaks 

    #again you can add audio to dramtics/ or not
   

    with hpunch

    pause 0.5

    taylor_thought "I didn’t think they’d actually do it…"

    taylor_thought "But they did."

    taylor_thought "The gate just… gave in."

    hide taylor
    show logan at right
    logan "…Didn’t think that’d ACTUALLY work. But… wow."

    alex "Let’s get moving."

    # ENTERING THE GROUNDS

    #again you can add audio to dramtics/ or not

    hide alex
    show hayden at left:
        zoom 0.75
    hayden "That’s insane… I’m kinda scared…"

    hide logan
    show bella at right
    bella "Eh. It’s Alex."

    bella "I’m more concerned that a government gate just… broke like that."

    # The tone starts to shift 

    show taylor at center:
        zoom 0.65

    taylor_thought "As we walked further in… something still felt wrong."

    taylor_thought "Too easy."

    taylor_thought "Way too easy."

    taylor_thought "I’ve never been here before…"

    taylor_thought "But it felt like a graveyard."

    taylor_thought "Like this place carried memories."

    taylor_thought "Families… friends… torn apart on these very grounds."

    
    #getting to castle doors 

    scene castle_doors with fade

    show alex at center
    show logan at left
    show taylor at right:
        zoom 0.65

    alex "Alright… who’s got lockpicking skills?"

    logan "Gimme that."

    logan "Lockpicking is the one thing you suck at."

    # End of scene

    taylor_thought "Still no guards."

    taylor_thought "No resistance."

    taylor_thought "…Why?"

    stop music fadeout 2.0
    scene black with fade

    return