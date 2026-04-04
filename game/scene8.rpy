define Taylor = Character("Taylor")
define Hayden = Character("Hayden")
define Pierce = Character("Pierce")
define Logan = Character("Logan")
define Bella = Character("Bella")
define Alex = Character("Alex")

label scene8:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    image Taylor = "TaylorPlaceholder.png"
    image Hayden = "HaydenPlaceholder.png"
    image Logan = "LoganPlaceholder.png"
    image Bella = "BellaPlaceholder.png"
    image Alex = "AlexPlaceholder.png"
    image Pierce = "PiercePlaceholder.png"

    show Taylor at center:
        zoom 0.65

    Taylor "So we did. We walked towards the outskirts of Frontworst District. I had no idea what time it was anymore."

    Taylor "After a while, the sky was unrecognizable. It did feel livelier, though."

    hide Taylor
    show Alex at left

    Alex "Ok. So those locked rooms? Those are where past children would’ve stayed. You and Hayden were on track to be her next victims."

    show Hayden at right:
        zoom 0.75

    Hayden "What do you mean?"

    hide Alex
    show Logan at left

    Logan "She’s an executioner that acts as a safe house warden. She waits and then. Gone." 

    hide Hayden
    show Bella at right

    Bella "She never had instructions to kill us off though. You two would’ve been in severe danger if you had stayed any longer. "

    hide Logan
    show Alex at left

    Alex "The food was normal. We just wanted to scare you a bit."

    hide Bella
    show Hayden at right:
        zoom 0.75

    Hayden "WHAT?! That’s mean!"

    hide Alex
    show Logan at left

    Logan "Oh yeah, it’s a classic joke we use on the newbies. It’s a miracle we got you both out in time. That safehouse USED to be a safehouse when the three of us were there. But then…money."

    hide Hayden
    show Taylor at right:
        zoom 0.65

    Taylor "That’s usually the case. But…those…those cretins…I’ll never forgive them."

    hide Logan
    show Hayden at left:
        zoom 0.75

    Hayden "So…where do we go now?"

    hide Taylor
    show Alex at right

    Alex "As much as the gates would be my first choice…the skies don’t look like they did when I first saw the gates unguarded."

    hide Hayden
    show Bella at left

    Bella "No it doesn’t…but…why?"

    hide Alex
    show Taylor at right:
        zoom 0.65

    Taylor "…What day of the month is it?"

    hide Bella
    show Logan at left

    Logan "How the hell are we supposed to know?!"

    hide Logan
    show Hayden at left:
        zoom 0.75

    Hayden "Taylor, we’ve only been gone a day. It’s Saturday."

    Taylor "Which Saturday though?!"

    Hayden "Um…third Saturday? Of the month? Why?"

    Taylor "…Premium protest day. Everything will be extra guarded."

    hide Hayden
    show Bella at left

    Bella "Extra guarded?"

    Taylor "Every third Saturday is dedicated by the people as a citywide protest day."

    Taylor "I mean…I finally get a break but it would be a great opportunity to get those bastards out of office."

    hide Bella
    show Logan at left

    Logan "Are you suggesting we STORM THE CASTLE?! ARE YOU MAD WOMAN?!"

    Taylor "Sometimes."

    hide Logan
    show Hayden at left:
        zoom 0.75

    Hayden "I’m so sorry for her! Taylor, that’s a bad idea!"

    hide Taylor
    show Bella at right

    Bella "Plus…we could ALL get killed!"

    hide Hayden
    show Alex at left
    
    Alex "I don’t know…it’d be a day the castle isn’t armed."

    hide Bella
    show Taylor at right:
        zoom 0.65

    Taylor "That’s the point. The guards will all be off at protest sites. But we need weapons. At least a sword."

    hide Alex
    show Logan at left

    Logan "…I know a place within this district. Old buddy of mine."

    Taylor "So did he move districts?"

    Logan "Yeah. After middle school. He told me if I ever needed anything. He’d have a weapons spot in town."

    Taylor "We walked a while behind Logan, which I don't think was the best option, but hey protection is protection."

    Logan "Ah yep. Here’s the place."

    "KNOCK KNOCK"

    Logan "PIERCE! OPEN THE DAMN DOOR!"

    hide Taylor
    show Pierce at right:
        zoom 0.75

    Pierce "Well shit, I never expected ya to come around this neck of the woods, Logan."

    hide Logan
    show Alex at left

    Alex "Seriously, Logan? This is the place you trust?"

    hide Pierce
    show Logan at right

    Logan "Hey, I don’t trust a lot of people. But I gotta at least trust this loser."

    hide Alex
    show Pierce at left:
        zoom 0.75

    Pierce "How cruel. Especially in front of ladies. How can I help?"
    
    hide Logan
    show Taylor at right:
        zoom 0.65

    Taylor "We need weapons. Anything will do."

    Pierce "Came to the right dealer. Considering your buddies with Logan, it’s on the house."

    hide Pierce
    show Bella at left

    Bella "Thank you! I really appreciate it! DIBS ON CROSSBOWS!"

    hide Bella
    show Hayden at left:
        zoom 0.75

    Hayden "Can I at least get a dagger, sis?"

    Taylor "Huh? Yeah. I’m not letting you go into this unarmed. Even if I’ve dedicated the rest of my life to protecting you, it wouldn’t hurt for you to learn a little bit of self defense on your own."

    Taylor "Especially if it’s to take down a cruel and unruly government."

    return