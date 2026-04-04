define taylor_thought = Character("Taylor" , what_italic = True)

label scene6:

    image taylor = "TaylorPlaceholder.png"
    image hayden = "HaydenPlaceholder.png"
    image logan = "LoganPlaceholder.png"
    image bella = "BellaPlaceholder.png"
    image alex = "AlexPlaceholder.png"

    scene dining_room with fade

#there isn't any audio that I have but I think it will sound good with some here 
    #play music audio fadein 2.0

    show taylor at center

    # taylors arrival 

    taylor_thought "As we walked over to the dining area, the other three were already at the table."

    taylor_thought "Not surprising… this is home to them."

    show bella happy at right
    show logan neutral at left

    bella "Hey guys! Oh my gosh, I can’t WAIT to see your rooms later!"

    logan "If it’s anything like her usual setups, I won’t be shocked."

    show taylor confused
    taylor "What do you mean by that?"

    show alex calm at right
    alex "Miss Cara has this… sixth sense when it comes to the people who stay here."

    alex "It’s kinda creepy, but you get used to it."

    show hayden confused
    hayden "Creepy?"

    logan "Yeah. The hag can be extremely creepy."

    logan "I’ve seen worse though."

    show taylor neutral
    taylor "Must relate to where you’re from."

    logan "Ironhill District."

    logan "They enjoy severe violence over there. Gunfights at least once a week."

    show hayden neutral
    hayden "What about you, Alex?"

    alex "I don’t really remember."

    alex "My parents dropped me off here when I was a baby."

    # Miss Cara Enters

    show cara smile at center with moveinright

    cara "It’s true. Alex is like the child I never knew I needed."

    alex "Thank you, Miss Cara. And thank you for the food!"

    show hayden happy
    hayden "Woah! This looks amazing!"

    bella "I LOVE spaghetti days! Thank you, Miss Cara!"

    logan "Thanks."

    hayden "Thank you!"

    show taylor neutral
    taylor "…Thanks."

    cara "You kids enjoy now, okay?"

    hide cara with moveoutright

    # taylor thoughts

    taylor_thought "As we began eating… something felt off."

    taylor_thought "How convenient was it that we found a place to stay… just like the others?"

    taylor_thought "I don’t trust any of this."

    taylor_thought "Even the food feels… strange."

    # a low conversation begins. Hopefully what I did here works

    taylor "Guys… does anything feel… weird about this—"

    show bella serious
    bella "{size=-5}(quiet) SHUT UP! She hears everything but our whispers.{/size}"

    show logan serious
    logan "{size=-5}(whispering) She’s creepy for real. We eat the food. Call it a day.{/size}"

    logan "{size=-5}(whispering) That’s why we’ve been trying to escape.{/size}"

    show hayden shocked
    hayden "{size=-5}(whispering) Escape? What’s so bad about being here?{/size}"

    logan "{size=-5}(whispering) Just trust us.{/size}"

    bella "{size=-5}(whispering) We want to escape tonight. Well… try again.{/size}"

    alex "{size=-5}(whispering) Now that you’re here… you can help us get to the castle.{/size}"

    show taylor serious
    taylor "{size=-5}(whispering) To get into the castle… you’d need to know the way in.{/size}"

    alex "{size=-5}(whispering) It’s not that hard.{/size}"

    bella "{size=-5}(whispering) Yeah! Alex has snuck in before!{/size}"

    bella "{size=-5}(whispering) They’re super cool!{/size}"

    show hayden uneasy
    hayden "{size=-5}(whispering) But… what’s in this food then…?{/size}"

    bella "{size=-5}(whispering) It’s just spaghetti. It’s fine.{/size}"

    # tension starts to creep up 

    taylor_thought "We kept eating…"

    taylor_thought "But now I couldn’t stop thinking about those locked rooms."

    taylor_thought "If they’ve been trying to escape…"

    taylor_thought "Were there others before them?"

    #suspense in the final lines


    show taylor serious

    taylor "{size=-5}(whispering) What about the locked rooms?{/size}"

    pause 1.0

    show hayden uneasy
    hayden "{size=-5}(whispering) Why did you all get quiet…?{/size}"

    #end of scene 6 

    stop music fadeout 2.0
    scene black with fade

    return