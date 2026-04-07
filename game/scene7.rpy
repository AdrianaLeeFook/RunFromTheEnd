# Characters
define Taylor = Character("Taylor", color="#c8a2ff")
define Hayden = Character("Hayden", color="#6ec1ff")
define Bella = Character("Bella", color="#ffb6c1")
define Logan = Character("Logan", color="#ff9e6b")
define Alex = Character("Alex", color="#9effa1")
define Cara = Character("Miss Cara", color="#ffd700")

# Images for this scene
image bg scene7inside = "scene7inside.png"
image bg scene7outside = "scene7outside.png"

image Taylor = "taylor.png"
image Hayden = "hayden.png"
image Bella = "bella.png"
image Logan = "logan.png"
image Alex = "alex.png"

label scene7:

    scene bg scene7inside:
        zoom 1.5

    show Bella:
        xalign 0.2
        yalign 0.68

    show Taylor:
        xalign 0.8
        yalign 0.68
        zoom 0.65

    Bella "(whispered) It’s something we’ll tell you if we manage to escape successfully."

    Taylor "(whispered) So it’s bad."

    hide Bella
    show Logan:
        xalign 0.2
        yalign 0.68

    Logan "(whispered) Yeah. It’s…worse than bad. Awful. Abhorrent. Sickening."

    Taylor "(whispered) So basically we need to leave here tonight."

    hide Logan
    show Bella:
        xalign 0.2
        yalign 0.68

    Bella "(whispered) Mhm. Which sucks, Miss Cara is sweet, but it isn’t super safe here!"

    hide Bella
    show Hayden:
        xalign 0.2
        yalign 0.68
        zoom 0.75

    Hayden "(whispered) We didn’t unpack our stuff, right Tay?"

    Taylor "(whispered) No we did not."

    hide Hayden
    show Alex:
        xalign 0.2
        yalign 0.68

    Alex "(whispered) We’ll be packed and ready to go by the time Miss Cara goes to sleep."

    hide Alex
    hide Taylor

    show Taylor:
        xalign 0.5
        yalign 0.68
        zoom 0.65

    Taylor "So we all finished eating. We washed our dishes. We went to our rooms, and waited. And waited. Time crept ever so slowly."

    Taylor "We needed to leave on time to make our escape not only from the safehouse, but from this hellhole in general."

    "Tick…tock…tick…tock…"

    # Optional puzzle placeholder
    # TODO: Jigsaw Puzzle or Wordsearch

    Taylor "It felt as if time was moving slower than usual. The clock in the room sounded like a Grandfather Clock, with every second weighing heavy on my conscience."

    "Knock knock knock"

    hide Taylor
    show Hayden:
        xalign 0.2
        yalign 0.68
        zoom 0.75

    Hayden "Taylor? Tayyy? Can you hear me?"

    show Taylor:
        xalign 0.8
        yalign 0.68
        zoom 0.65

    Taylor "What is it?"

    hide Hayden
    show Bella:
        xalign 0.2
        yalign 0.68

    Bella "It’s timeeee!"

    Taylor "Oh shit. Alright. I hear ya loud and clear."

    hide Bella
    hide Taylor

    show Taylor:
        xalign 0.5
        yalign 0.68
        zoom 0.65

    Taylor "I carefully grabbed my things. I’ve learned not to make a lot of noise, but to get out of here, I felt I needed to be even quieter than usual."

    Taylor "As I opened the door, the four were there waiting."

    hide Taylor
    show Alex:
        xalign 0.5
        yalign 0.68

    Alex "Before we went outside though, I went to work on the security system."

    # Timed puzzle placeholder
    # TODO: Security system puzzle
    # If fail:
    # Cara "Children? Where are you going?"
    # return

    Alex "(whispered) Luckily for us…Miss Cara doesn’t bother looking at her security system half the time."

    hide Alex
    show Logan:
        xalign 0.2
        yalign 0.68
    show Taylor:
        xalign 0.8
        yalign 0.68
        zoom 0.65

    Logan "(whispered, but annoyed) Ok, Hacker…person…thing…I don’t know what to say but ok you hacker."

    hide Logan
    hide Taylor

    scene bg scene7outside:
        zoom 1.5

    show Taylor:
        xalign 0.5
        yalign 0.68
        zoom 0.65

    Taylor "We walked outside and the air felt…different. It felt more like a setup."

    hide Taylor
    show Bella:
        xalign 0.2
        yalign 0.68

    Bella "Woah! The outside looks so different now!"

    hide Bella
    show Logan:
        xalign 0.2
        yalign 0.68

    Logan "Holy shit…this place went even further to hell."

    hide Logan
    show Hayden:
        xalign 0.2
        yalign 0.68
        zoom 0.75
    show Taylor:
        xalign 0.8
        yalign 0.68
        zoom 0.65

    Hayden "Have you guys just…not gone outside?"

    hide Hayden
    hide Taylor
    show Bella:
        xalign 0.2
        yalign 0.68
    show Alex:
        xalign 0.8
        yalign 0.68

    Bella "Alex has! The rest of us just…didn’t bother."

    hide Bella
    show Taylor:
        xalign 0.2
        yalign 0.68
        zoom 0.65

    Taylor "The rest?"

    hide Taylor
    hide Alex
    show Logan:
        xalign 0.2
        yalign 0.68

    Logan "The locked rooms."

    hide Logan
    show Hayden:
        xalign 0.2
        yalign 0.68
        zoom 0.75

    Hayden "What about them? You guys said you’d tell us once we were out."

    hide Hayden
    show Alex:
        xalign 0.2
        yalign 0.68

    Alex "We gotta walk a little farther first."

    hide Alex

    return