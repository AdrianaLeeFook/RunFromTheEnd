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

    show Taylor:
        xalign 0.5
        yalign 0.68
        zoom 0.65

    Taylor "I walked out of the house and pulled my mask up. While the town looks like a desolate wasteland, it’s best not to be recognized by these cretins at the protest."

    Taylor "Even if it feels…repetitive, I’ll keep going."

    hide Taylor
    show Julie:
        xalign 0.5
        yalign 0.68
        zoom 0.65

    Julie "No more dictators! Give us our freedom! No more dictators! Give us our freedom!"

    hide Julie
    show Taylor:
        xalign 0.2
        yalign 0.68
        zoom 0.65
    show Julie:
        xalign 0.8
        yalign 0.68
        zoom 0.65

    Taylor "Hey Jules."

    Julie "EEE! Tay, you MADE IT! You’re late!"

    Taylor "You know I take any opportunity to…fight back against the new government. They’re cruel and must be put to rest."

    Taylor "We need a new resolve that doesn’t involve…any of those bastards."

    Julie "And here I thought you’d stay back for once. You go to EVERYTHING! I thought you’d take a break!"

    Taylor "There’s no time for breaks."

    Julie "Girl you NEED to take some rest! It’ll be good for youuuuu."

    Taylor "Yeah yeah, I know. Hayden keeps saying that. But I can’t rest. Not until those assholes are dead."

    hide Julie
    show Kyle:
        xalign 0.8
        yalign 0.68
        zoom 0.65

    Kyle "Woahhh, Tay-Tay, you gotta slow your roll. Protests are peaceful obligations, bro."

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

    Julie "Hey, the donut vendors at these things are AWESOME! I don’t blame Kyle at all."

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

    Julie "So…how are ya holding up, Tay?"

    Taylor "Oh, you mean after I lost my parents a few weeks ago? Still awful. Hayden and I have had to hide more just because of it."

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