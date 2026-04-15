# Characters
define Taylor = Character("Taylor", color="#c8a2ff")
define Julie = Character("Julie", color="#ff8fd8")
define Kyle = Character("Kyle", color="#7fd4ff")
define Guard1 = Character("Guard 1", color="#ff4d4d")

# Images
image bg scene2 = "scene2bg.png"
image bg scene2guard = "scene2_guard_confrontation.png"

image Taylor = "taylor.png"
image Julie = "julie.png"
image Kyle = "kyle.png"

label scene2:

    scene bg scene2:
        zoom 1.5

    image taylor = "taylor.jpg"
    image julie = "JuliePlaceholder.png"
    image kyle = "KylePlaceholder.png"

    #Taylor inside thoughts as he's leaving and walking to the protest

    taylor_thought "I step outside and pull my mask up."
    pause 0.5

    taylor_thought "The town looks like a desolate wasteland..."
    pause 0.5

    taylor_thought "Best not to be recognize by these cretins at the protest"
    pause 0.5

    taylor_thought "Even if it feels repetitive... I have to keep going."
    pause 1.0

    #add some sound to show that the protest is getting louder and taylor is getting closer

    #Julie in the middle of protesting and then sees Taylor and gets excited
    #show both characters

    show taylor at right:
        zoom 0.65
    show julie at left
    play sound "Julie_Line_1.mp3"
    julie "No more dictators! Give us our freedom! No more dictators! Give us our freedom!"
    stop sound

    taylor "Hey, Jules."

    play sound "Julie_Line_2.mp3"
    julie "EEE! Tay, you MADE IT! You’re late!"
    stop sound

    taylor "Yeah yeah, but I'm here."

    taylor "You know I'd take any opportunity to fight back against the new government, they're cruel and must be put to rest!"

    taylor "We need a resolution that doesn't involve any of those bastards."

    play sound "Julie_Line_3.mp3"
    julie "And here I thought you’d stay back for once. You go to EVERYTHING! I thought you’d take a break!"
    stop sound

    taylor "There’s no time for breaks."

    play sound "Julie_Line_4.mp3"
    julie "Girl you NEED to take some rest! It’ll be good for youuuuu."
    stop sound

    taylor "Yeah yeah, I know. Hayden keeps saying the same thing. But I can’t rest. Not until those assholes are dead!"

    #Kyle comes into the conversation

    label protest_scene:

#scene of outside protest added her

    # Initial characters
    show taylor at left:
        zoom 0.65
    show julie at right

    
    show kyle at center with moveinbottom

    # Kyle speaking  focus him
    show kyle at center
    show taylor at left:
        zoom 0.65
    show julie at right
    play sound "Kyle_Line_1.mp3"
    kyle "Woahhh, Tay-Tay, you gotta slow your roll. Protests are peaceful obligations, bro."
    stop sound

    # Taylor responds → focus Taylor
    show taylor at left:
        zoom 0.65
    show kyle at center
    show julie at right

    taylor "Oh please, you come to protests for the free food, Kyle."

    # Kyle again → focus Kyle
    show kyle at center
    show taylor at left:
        zoom 0.65
    show julie at right
    play sound "Kyle_Line_2.mp3"
    kyle "And to support a valiant cause. Our freedom. And the donuts, man. The donuts."
    stop sound

    # Taylor → focus Taylor
    show taylor at center:
        zoom 0.65
    show kyle at left
    show julie at right

    taylor "So human freedom and donuts are on your agenda as usual...got it..."

    # JULIE joins back in
   
    show julie at center
    show taylor at left:
        zoom 0.65
    show kyle at right

    play sound "Julie_Line_5.mp3"
    julie "Hey, the donut vendors at these things are AWESOME! I don’t blame Kyle at all."
    stop sound

    # TAYLOR 

    show taylor at center:
        zoom 0.65
    show julie at right
    show kyle at left

    taylor "Whatever. As long as we're fighting for what we want, I don't see a problem."

    # KYLE EXITS

    show kyle at center
    show taylor at left:
        zoom 0.65
    show julie at right
    play sound "Kyle_Line_3.mp3"
    kyle "I'm gonna get more donuts, dudes. LATERS!"

    hide kyle with moveoutright

    # CROWD CHANT add some chanting audio

    kyle "WE WANT FREEDOM, NOT DEPENDENCE! WE WANT FREEDOM, NOT DEPENDENCE!"
    stop sound
    # use vpunch to show Kyle protesting as he leaves the scence
    with vpunch

    # TONE SHIFT (SERIOUS)

    show julie at right
    show taylor at left:
        zoom 0.65
    play sound "Julie_Line_6.mp3"
    julie "So...how are ya holding up, Tay?"
    stop sound

    Taylor "Even if it feels…repetitive, I’ll keep going."

    hide Taylor
    show Julie:
        xalign 0.5
        yalign 0.68
        zoom 0.65
    play sound "Julie_Line_7.mp3"
    julie "That's awful..."
    stop sound

    hide Julie
    show Taylor:
        xalign 0.2
        yalign 0.68
        zoom 0.65
    show Julie:
        xalign 0.8
        yalign 0.68
        zoom 0.65
    play sound "Julie_Line_8.mp3"
    julie "That’s the spirit! But seriously, please take a break. You’re an easy target. Even with your mask."
    stop sound

    Julie "EEE! Tay, you MADE IT! You’re late!"

    Taylor "You know I take any opportunity to…fight back against the new government. They’re cruel and must be put to rest."

    Taylor "We need a new resolve that doesn’t involve…any of those bastards."

    Julie "And here I thought you’d stay back for once. You go to EVERYTHING! I thought you’d take a break!"

    Taylor "There’s no time for breaks."

    play sound "guard1_timkvo.mp3"
    "Guard 1" "OK! EVERYONE MOVE IT! IF YOU DON'T LEAVE NOW, YOU WILL BE EXECUTED!"
    stop sound

    Taylor "Yeah yeah, I know. Hayden keeps saying that. But I can’t rest. Not until those assholes are dead."

    hide Julie
    show Kyle:
        xalign 0.8
        yalign 0.68
        zoom 0.65
    play sound "Julie_Line_9.mp3"
    julie "Aw man, the fuzz."
    stop sound

    Taylor "Oh please, you come to protests for the free food, Kyle."

    Kyle "And to support a valiant cause. Our freedom. And the donuts, man. The donuts."

    Taylor "So human freedom and donuts are on your agenda as usual…got it…"

    hide Taylor
    show Julie:
        xalign 0.2
        yalign 0.68
        zoom 0.65
    show Kyle:
        xalign 0.8
        yalign 0.68
        zoom 0.65

    play sound "Julie_Line_10.mp3"
    julie "Well, I’ll see ya around, Tay. Don’t get yourself killed out there."
    stop sound

    hide Kyle
    show Taylor:
        xalign 0.8
        yalign 0.68
        zoom 0.65

    Taylor "Whatever. As long as we’re fighting for what we want, I don’t see a problem."

    hide Julie
    show Kyle:
        xalign 0.2
        yalign 0.68
        zoom 0.65

    Kyle "I’m gonna get more donuts, dudes. LATERS! (trailing off) WE WANT FREEDOM, NOT DEPENDENCE! WE WANT FREEDOM, NOT DEPENDENCE!"

    hide Kyle
    hide Taylor
    show Julie:
        xalign 0.2
        yalign 0.68
        zoom 0.65
    show Taylor:
        xalign 0.8
        yalign 0.68
        zoom 0.65
    play sound "Kyle_Line_4.mp3"
    kyle "BYE TAY-TAY! Here, take some donuts for the little man."
    stop sound
    # Kyle exits again
    hide kyle with moveoutright

    Julie "That’s awful…"

    Taylor "I miss them like hell but…it’s made me stronger. I want to make a change even more than before."

    Julie "That’s the spirit! But seriously, please take a break. You’re an easy target. Even with your mask."

    Taylor "I switch it up a lot, I’m not scared."

    hide Julie
    hide Taylor

    scene bg scene2guard:
        zoom 1.5

    Guard1 "OK! EVERYONE MOVE IT! IF YOU DON’T LEAVE NOW, YOU WILL BE EXECUTED!"

    scene bg scene2:
        zoom 1.5

    show Julie:
        xalign 0.2
        yalign 0.68
        zoom 0.65
    show Taylor:
        xalign 0.8
        yalign 0.68
        zoom 0.65

    Julie "Aw man, the fuzz."

    Taylor "Psh."

    Julie "Well, I’ll see ya around, Tay. Don’t get yourself killed out there."

    Taylor "Yeah, I know."

    hide Julie
    show Kyle:
        xalign 0.2
        yalign 0.68
        zoom 0.65
    show Taylor:
        xalign 0.8
        yalign 0.68
        zoom 0.65

    Kyle "BYE TAY-TAY! Here, take some donuts for the little man."

    Taylor "Thanks."

    hide Kyle
    hide Taylor
    show Taylor:
        xalign 0.5
        yalign 0.68
        zoom 0.65

    Taylor "Some folks decided to stay, but when your parents were the ones leading the protests at their peak, you have to hide. That’s my life."

    Taylor "Our town used to be so vibrant and beautiful now it’s desolate. A total wasteland."

    Taylor "You get caught breaking a single rule, it’s either labor work or death."

    Taylor "Jailtime is considered mercy. Fines are basically non-existent outside of specified cases. Usually for the rich people, not for others…"

    return