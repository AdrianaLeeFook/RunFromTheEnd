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

    play sound "Bella_Line-34.mp3"
    Bella "(whispered) It's something we'll tell you if we manage to escape successfully."
    stop sound

    play sound "Taylor_RFTE_LINE98.mp3"
    Taylor "(whispered) So it's bad."
    stop sound

    hide Bella
    show Logan:
        xalign 0.2
        yalign 0.68

    play sound "Logan_Run_From_the_End_Line-021.mp3"
    Logan "(whispered) Yeah. It's…worse than bad. Awful. Abhorrent. Sickening."
    stop sound

    play sound "Taylor_RFTE_LINE99.mp3"
    Taylor "(whispered) So basically we need to leave here tonight."
    stop sound

    hide Logan
    show Bella:
        xalign 0.2
        yalign 0.68
    
    play sound "Bella_Line-35.mp3"
    Bella "(whispered) Mhm. Which sucks, Miss Cara is sweet, but it isn't super safe here!"
    stop sound

    hide Bella
    show Hayden:
        xalign 0.2
        yalign 0.68
        zoom 0.75

    play sound "Hayden50.mp3"
    Hayden "(whispered) We didn't unpack our stuff, right Tay?"
    stop sound

    play sound "Taylor_RFTE_LINE100.mp3"
    Taylor "(whispered) No we did not."
    stop sound

    hide Hayden
    show Alex:
        xalign 0.2
        yalign 0.68

    play sound "Alex_Line_18.mp3"
    Alex "(whispered) We'll be packed and ready to go by the time Miss Cara goes to sleep."
    stop sound 

    hide Alex
    hide Taylor

    show Taylor:
        xalign 0.5
        yalign 0.68
        zoom 0.65

    play sound "Taylor_RFTE_LINE101.mp3"
    Taylor "So we all finished eating. We washed our dishes. We went to our rooms, and waited. And waited. Time crept ever so slowly."
    stop sound

    play sound "Taylor_RFTE_LINE102.mp3"
    Taylor "We needed to leave on time to make our escape not only from the safehouse, but from this hellhole in general."
    stop sound 

    "Tick…tock…tick…tock…"

    call scene7_puzzle1_clock

    play sound "Taylor_RFTE_LINE103.mp3"
    Taylor "It felt as if time was moving slower than usual. The clock in the room sounded like a Grandfather Clock, with every second weighing heavy on my conscience."
    stop sound

    "Knock knock knock"

    hide Taylor
    show Hayden:
        xalign 0.2
        yalign 0.68
        zoom 0.75

    play sound "Hayden51.mp3"
    Hayden "Taylor? Tayyy? Can you hear me?"
    stop sound

    show Taylor:
        xalign 0.8
        yalign 0.68
        zoom 0.65

    play sound "Taylor_RFTE_LINE104.mp3"
    Taylor "What is it?"
    stop sound

    hide Hayden
    show Bella:
        xalign 0.2
        yalign 0.68

    play sound "Bella_Line-36.mp3"
    Bella "It's timeeee!"
    stop sound
    
    play sound "Taylor_RFTE_LINE105.mp3"
    Taylor "Oh shit. Alright. I hear ya loud and clear."
    stop sound

    hide Bella
    hide Taylor

    show Taylor:
        xalign 0.5
        yalign 0.68
        zoom 0.65

    play sound "Taylor_RFTE_LINE106.mp3"
    Taylor "I carefully grabbed my things. I've learned not to make a lot of noise, but to get out of here, I felt I needed to be even quieter than usual."
    Taylor "As I opened the door, the four were there waiting."
    stop sound 

    hide Taylor
    show Alex:
        xalign 0.5
        yalign 0.68
    
    play sound "Alex_Line_18.mp3"
    Alex "Before we went outside though, I went to work on the security system."
    stop sound 

    call scene7_puzzle2_security

    if _return == "fail":
        jump scene7_puzzle2_fail
    else:
        jump scene7_puzzle2_success


label scene7_puzzle2_fail:

    hide Alex

    show Cara:
        xalign 0.5
        yalign 0.68
    
    play sound "Miss_Cara_line17.mp3"
    Cara "Children? Where are you going?"
    stop sound

    "Game End"

    jump scene7


label scene7_puzzle2_success:

    hide Alex

    show Alex:
        xalign 0.5
        yalign 0.68

    play sound "Alex_Line_19.mp3"
    Alex "(whispered) Luckily for us…Miss Cara doesn't bother looking at her security system half the time."
    stop sound

    hide Alex
    show Logan:
        xalign 0.2
        yalign 0.68
    show Taylor:
        xalign 0.8
        yalign 0.68
        zoom 0.65

    play sound "Logan_Run_From_the_End_Line-022.mp3"
    Logan "(whispered, but annoyed) Ok, Hacker…person…thing…I don't know what to say but ok you hacker."
    stop sound

    hide Logan
    hide Taylor

    scene bg scene7outside:
        zoom 1.5

    show Taylor:
        xalign 0.5
        yalign 0.68
        zoom 0.65

    play sound "Taylor_RFTE_LINE107.mp3"
    Taylor "We walked outside and the air felt…different. It felt more like a setup."
    stop sound 

    hide Taylor
    show Bella:
        xalign 0.2
        yalign 0.68

    play sound "Bella_Line-37.mp3"
    Bella "Woah! The outside looks so different now!"
    stop sound

    hide Bella
    show Logan:
        xalign 0.2
        yalign 0.68

    play sound "Logan_Run_From_the_End_Line-023.mp3"
    Logan "Holy shit…this place went even further to hell."
    stop sound 

    hide Logan
    show Hayden:
        xalign 0.2
        yalign 0.68
        zoom 0.75
    show Taylor:
        xalign 0.8
        yalign 0.68
        zoom 0.65

    play sound "Hayden52.mp3"
    Hayden "Have you guys just…not gone outside?"
    stop sound

    hide Hayden
    hide Taylor
    show Bella:
        xalign 0.2
        yalign 0.68
    show Alex:
        xalign 0.8
        yalign 0.68

    play sound "Bella_Line-38.mp3"
    Bella "Alex has! The rest of us just…didn't bother."
    stop sound

    hide Bella
    show Taylor:
        xalign 0.2
        yalign 0.68
        zoom 0.65

    play sound "Taylor_RFTE_LINE108.mp3"
    Taylor "The rest?"
    stop sound

    hide Taylor
    hide Alex
    show Logan:
        xalign 0.2
        yalign 0.68

    play sound "Logan_Run_From_the_End_Line-024.mp3"
    Logan "The locked rooms."
    stop sound

    hide Logan
    show Hayden:
        xalign 0.2
        yalign 0.68
        zoom 0.75

    play sound "Hayden53.mp3"
    Hayden "What about them? You guys said you'd tell us once we were out."
    stop sound

    hide Hayden
    show Alex:
        xalign 0.2
        yalign 0.68

    play sound "Alex_Line_20.mp3"
    Alex "We gotta walk a little farther first."
    stop sound

    hide Alex

    return