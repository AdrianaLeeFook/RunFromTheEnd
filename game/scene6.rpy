define taylor_thought = Character("Taylor" , what_italic = True)
define taylor = Character("Taylor")
define hayden = Character("Hayden")
define cara = Character("Miss Cara")
define logan = Character("Logan")
define bella = Character("Bella")
define alex = Character("Alex")

label scene6:

    image taylor = "TaylorPlaceholder.png"
    image hayden = "HaydenPlaceholder.png"
    image logan = "LoganPlaceholder.png"
    image bella = "BellaPlaceholder.png"
    image alex = "AlexPlaceholder.png"
    image cara = "CaraPlaceholder.png"

    scene dining_room with fade

#there isn't any audio that I have but I think it will sound good with some here 
    #play music audio fadein 2.0

    show taylor at center:
        zoom 0.65

    # taylors arrival 

    taylor_thought "As we walked over to the dining area, the other three were already at the table."

    taylor_thought "Not surprising… this is home to them."

    hide taylor
    show bella at right
    show logan at left

    bella "Hey guys! Oh my gosh, I can’t WAIT to see your rooms later!"

    logan "If it’s anything like her usual setups, I won’t be shocked."

    hide logan
    show taylor at left:
        zoom 0.65 
    taylor "What do you mean by that?"

    hide bella
    show alex at right
    alex "Miss Cara has this… sixth sense when it comes to the people who stay here."

    alex "It’s kinda creepy, but you get used to it."

    hide taylor
    show hayden at left:
        zoom 0.75
    hayden "Creepy?"

    hide alex
    show logan at right
    logan "Yeah. The hag can be extremely creepy."

    logan "I’ve seen worse though."

    hide hayden
    show taylor at left:
        zoom 0.65
    taylor "Must relate to where you’re from."

    logan "Ironhill District."

    logan "They enjoy severe violence over there. Gunfights at least once a week."

    hide logan 
    show hayden at right:
        zoom 0.75
    hayden "What about you, Alex?"

    hide taylor
    show alex at left
    alex "I don’t really remember."

    alex "My parents dropped me off here when I was a baby."

    # Miss Cara Enters

    show cara at center with moveinright

    cara "It’s true. Alex is like the child I never knew I needed."

    alex "Thank you, Miss Cara. And thank you for the food!"

    hayden "Woah! This looks amazing!"

    hide cara
    hide hayden
    show bella at right
    bella "I LOVE spaghetti days! Thank you, Miss Cara!"

    hide alex
    show logan at left
    logan "Thanks."

    hide bella
    show hayden at right:
        zoom 0.75
    hayden "Thank you!"

    hide logan
    show taylor at left:
        zoom 0.65
    taylor "…Thanks."

    hide hayden
    show cara at right
    cara "You kids enjoy now, okay?"

    hide cara with moveoutright

    # taylor thoughts

    taylor_thought "As we began eating… something felt off."

    taylor_thought "How convenient was it that we found a place to stay… just like the others?"

    taylor_thought "I don’t trust any of this."

    taylor_thought "Even the food feels… strange."

    # a low conversation begins. Hopefully what I did here works

    taylor "Guys… does anything feel… weird about this—"

    show bella at right
    bella "{size=-5} SHUT UP! She hears everything but our whispers.{/size}"

    hide taylor
    show logan at left
    logan "{size=-5} She’s creepy for real. We eat the food. Call it a day.{/size}"

    logan "{size=-5} That’s why we’ve been trying to escape.{/size}"

    hide bella
    show hayden at right:
        zoom 0.75
    hayden "{size=-5} Escape? What’s so bad about being here?{/size}"

    logan "{size=-5} Just trust us.{/size}"

    hide hayden
    show bella at right
    bella "{size=-5} We want to escape tonight. Well… try again.{/size}"

    hide logan
    show alex at left
    alex "{size=-5} Now that you’re here… you can help us get to the castle.{/size}"

    hide bella
    show taylor at right:
        zoom 0.65
    taylor "{size=-5} To get into the castle… you’d need to know the way in.{/size}"

    alex "{size=-5} It’s not that hard.{/size}"

    hide alex
    show bella at left
    bella "{size=-5} Yeah! Alex has snuck in before!{/size}"

    bella "{size=-5} They’re super cool!{/size}"

    hide taylor
    show hayden at right:
        zoom 0.75
    hayden "{size=-5} But… what’s in this food then…?{/size}"

    bella "{size=-5} It’s just spaghetti. It’s fine.{/size}"

    # tension starts to creep up 

    show taylor at center:
        zoom 0.65

    taylor_thought "We kept eating…"

    taylor_thought "But now I couldn’t stop thinking about those locked rooms."

    taylor_thought "If they’ve been trying to escape…"

    taylor_thought "Were there others before them?"

    #suspense in the final lines

    hide bella
    show taylor at left:
        zoom 0.65
    taylor "{size=-5} What about the locked rooms?{/size}"

    pause 1.0

    hayden "{size=-5} Why did you all get quiet…?{/size}"

    #end of scene 6 

    stop music fadeout 2.0
    scene black with fade

    return