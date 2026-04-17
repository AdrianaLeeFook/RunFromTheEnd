# Characters
define Taylor = Character("Taylor", color="#c8a2ff")
define Hayden = Character("Hayden", color="#6ec1ff")
define Bella = Character("Bella", color="#ffb6c1")
define Logan = Character("Logan", color="#ff9e6b")
define Alex = Character("Alex", color="#9effa1")
define Cara = Character("Miss Cara", color="#ffd700")

# Images
image bg scene6 = "scene6bg.png"

image Taylor = "taylor.png"
image Hayden = "hayden.png"
image Bella = "bella.png"
image Logan = "logan.png"
image Alex = "alex.png"
image Cara = "cara.png"

label scene6:

    scene bg scene6:
        zoom 1.5

    show Taylor:
        xalign 0.5
        yalign 0.68
        zoom 0.65

    Taylor "As we walked over to the dining area, the other three were already at the table. Not surprising, considering this is home to them."

    hide Taylor
    show Bella:
        xalign 0.2
        yalign 0.68 
    show Hayden:
        xalign 0.8
        yalign 0.68
        zoom 0.75

    Bella "Hey guys! Oh em gee I can’t WAIT to see your rooms later!"

    hide Hayden
    show Logan:
        xalign 0.8
        yalign 0.68

    Logan "If it’s anything like her usual room setups, I won’t be shocked."

    hide Bella
    show Taylor:
        xalign 0.2
        yalign 0.68
        zoom 0.65
    show Logan:
        xalign 0.8
        yalign 0.68

    Taylor "What do you mean by that?"

    hide Logan
    show Alex:
        xalign 0.8
        yalign 0.68

    Alex "Miss Cara has this sixth sense when it comes to the people that stay here. It’s kinda creepy, but you get used to it."

    hide Taylor
    show Hayden:
        xalign 0.2
        yalign 0.68
        zoom 0.75
    show Alex:
        xalign 0.8
        yalign 0.68
        zoom 0.65

    Hayden "Creepy?"

    hide Alex
    show Logan:
        xalign 0.8
        yalign 0.68
        zoom 0.65

    Logan "Yeah, the hag can be extremely creepy. I’ve seen worse though."

    hide Hayden
    show Taylor:
        xalign 0.2
        yalign 0.68
        zoom 0.65
    show Logan:
        xalign 0.8
        yalign 0.68

    Taylor "Must relate to where you’re from."

    Logan "Ironhill District. They enjoy severe violence over there. Gunfights at least once a week."

    hide Taylor
    show Hayden:
        xalign 0.2
        yalign 0.68
        zoom 0.75
    show Logan:
        xalign 0.8
        yalign 0.68

    Hayden "What about you Alex?"

    hide Logan
    show Alex:
        xalign 0.8
        yalign 0.68

    Alex "I don’t really remember. My parents dropped me off here when I was a baby."

    hide Hayden
    hide Alex
    show Cara:
        xalign 0.5
        yalign 0.68

    Cara "It’s true. Alex is like the child I never knew I needed."

    hide Cara
    show Alex:
        xalign 0.2
        yalign 0.68
    show Hayden:
        xalign 0.8
        yalign 0.68
        zoom 0.75

    Alex "Thank you Miss Cara. And thank you for the food!"

    Hayden "Woah! This looks yummy!"

    hide Hayden
    show Bella:
        xalign 0.8
        yalign 0.68

    Bella "I love love LOVE spaghetti days! Thank you Miss Cara!"

    hide Alex
    show Logan:
        xalign 0.2
        yalign 0.68
    show Bella:
        xalign 0.8
        yalign 0.68

    Logan "Thanks."

    hide Logan
    show Hayden:
        xalign 0.2
        yalign 0.68
        zoom 0.75
    show Bella:
        xalign 0.8
        yalign 0.68

    Hayden "Thank you!"

    hide Bella
    show Taylor:
        xalign 0.8
        yalign 0.68
        zoom 0.65

    Taylor "…Thanks."

    hide Hayden
    hide Taylor
    show Cara:
        xalign 0.5
        yalign 0.68

    Cara "You kids enjoy now, ok?"

    hide Cara
    show Taylor:
        xalign 0.5
        yalign 0.68
        zoom 0.65

    Taylor "As we all began eating, something felt off about all of this. How convenient was it that we were able to find a place to stay just like the other three? I don’t trust any of this."

    Taylor "As I began to eat, I felt something weird about the meal."

    Taylor "Guys…does anything feel…weird about this to-"

    hide Taylor
    show Bella:
        xalign 0.5
        yalign 0.68

    Bella "(quiet) SHUT UP! She hears everything but our whispers."

    hide Bella
    show Logan:
        xalign 0.2
        yalign 0.68
    show Taylor:
        xalign 0.8
        yalign 0.68
        zoom 0.65

    Logan "(whispered) She’s creepy for real. We eat the food. Call it a day. That’s why we’ve been trying to escape."

    hide Taylor
    show Hayden:
        xalign 0.8
        yalign 0.68
        zoom 0.75

    Hayden "(whispered) What’s so bad about being here?"

    Logan "(whispered) Just trust us."

    hide Logan
    show Bella:
        xalign 0.2
        yalign 0.68
    show Hayden:
        xalign 0.8
        yalign 0.68
        zoom 0.75

    Bella "(whispered) We want to escape tonight. Well, try again at least."

    hide Hayden
    show Alex:
        xalign 0.8
        yalign 0.68

    Alex "(whispered) We have you guys now…you can help us get to the castle."

    hide Bella
    show Taylor:
        xalign 0.2
        yalign 0.68
        zoom 0.65
    show Alex:
        xalign 0.8
        yalign 0.68

    Taylor "(whispered) But to get into the castle…you’d need to know the ways in."

    Alex "(whispered) It’s not that hard."

    hide Taylor
    show Bella:
        xalign 0.2
        yalign 0.68
    show Alex:
        xalign 0.8
        yalign 0.68

    Bella "(whispered) Yeah! Alex said they’ve snuck in there before! They’re super cool!"

    hide Alex
    show Hayden:
        xalign 0.8
        yalign 0.68
        zoom 0.75

    Hayden "(whispered) But what’s in this food then…"

    Bella "(whispered) It’s just regular spaghetti, it’s fine."

    hide Bella
    hide Hayden
    show Taylor:
        xalign 0.5
        yalign 0.68
        zoom 0.65

    Taylor "We all continued eating. But now I pondered about those locked rooms…if these three have been trying to escape…were there others that tried?"

    Taylor "(whispered) What about the locked rooms?"

    "…"

    hide Taylor
    show Hayden:
        xalign 0.5
        yalign 0.68
        zoom 0.75

    Hayden "(whispered) Why did you three get quiet?"

    return