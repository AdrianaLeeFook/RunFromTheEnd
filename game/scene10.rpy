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
    taylor "It felt too good to be true but…we had a plan. We had defense. I have a team."

    taylor "We arrived at the gates of the castle a few hours later, after a quick snack break as we all wanted to eat something. But we made it." 

    taylor "Considering the area was unguarded, it felt like an easy entrance. That’s what we thought at first."

    # Everyone gets to the castle
    
    show hayden at left:
        zoom 0.75
    show bella at right

    hayden "Woah. The castle is a lot bigger than I ever imagined."

    bella "Woah! It’s MASSIVE!"

    hide hayden
    show taylor at left:
        zoom 0.65
    
    taylor "And unarmed. Which is suspicious enough."

    hide bella
    show logan at right

    logan "An unmanned castle on a heavy protest day is confusing and suspicious."

    
    hide taylor
    show alex at left

    alex "Hey maybe we can just kick the gate."

    hide logan
    show bella at right
    bella "ARE YOU CRAZY?! We can’t just KICK the gate!"

    alex "You wanna test that?"

    hide bella
    show taylor at right:
        zoom 0.65

    taylor "…Your funeral. Good luck."

    alex "Bet."

    # the gate breaks 

    #again you can add audio to dramtics/ or not
   

    with hpunch

    pause 0.5

    taylor " I didn’t think they’d actually kick open the gate. But they did. That was shocking enough. You’d think the area would have a higher security measure."

    hide taylor
    show logan at right

    logan "…Didn’t think that’d ACTUALLY work. But… wow."

    alex "Let’s get moving!"


    # ENTERING THE GROUNDS

    #again you can add audio to dramtics/ or not

    hide alex
    show hayden at left:
        zoom 0.75
    hayden "That’s insane…I’m scared…"

    hide logan
    show bella at right
    bella "Eh. It’s Alex."

    bella "Eh. It’s Alex, I wouldn’t be that scared that they can easily kick down a gate to a government establishment."

    # The tone starts to shift 

    show taylor at center:
        zoom 0.65

    taylor "As we walked, everything still felt…too good to be true. How Alex just…easily kicked down the gate. How normalized some of these reactions are. "
   
    taylor "I have never been on these grounds but…it felt like a mass graveyard. A land of memories. Families and friends torn apart on these very grounds."
   
    taylor "We kept walking until we reached the doors."
    
    #getting to castle doors 

    scene castle_doors with fade

    show alex at center
    show logan at left
    show taylor at right:
        zoom 0.65

    alex "ALockpicking anyone?"

    logan "Gimme that. Lockpicking is the one thing you suck at."

    # End of scene

    stop music fadeout 2.0
    scene black with fade

    return