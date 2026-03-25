define Taylor = Character("Taylor")
define Hayden = Character("Hayden")
define Cara = Character("Miss Cara")
define Logan = Character("Logan")
define Bella = Character("Bella")
define Alex = Character("Alex")

# The game starts here.

label scene4:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    image Taylor = "Cara0-2.png"
    image Hayden = "Cara9-1.png"
    image Cara = "Cara15-9.png"
    image Bella = "Cara96-6.png"
    image Logan = "Fuyuhiko_Kuzuryuu_Halfbody_Sprite_29.png"
    image Alex = "Quiz_detail_image_38.png"

    show Taylor at center
    Taylor "We kept walking through the town, hiding at certain points in guard-heavy areas."

    Taylor "We tried our best to not get caught. Somehow, we didn’t."

    Taylor "The safehouse was bigger than we thought."

    show Hayden at right
    show Taylor at left

    Hayden "Woah. This is…big."

    Taylor "Yeah, bigger than I expected when mom and dad told us about it."

    Hayden "At least it gives you a protest break."

    Taylor "There’s no breaks in fighting for the better of the world, Hayden. Never."

    Taylor "I knocked on the door and an older woman opened it. She seemed very kind and wanted to help. I think."

    hide Hayden
    hide Taylor
    show Cara at center

    Cara "Oh yes yes yes! We have been expecting you two for weeks!"

    Cara "Taylor and Hayden, children of the Jenkins! We know you two very well. Come in come in!"

    show Taylor at left
    show Cara at right

    Taylor "Um. Who are you?"

    Cara "Oh right yes! I’m Miss Cara."

    Cara "I run this safehouse and protect the children of those whose parents or other family members are on the run from the government. Or have…suffered the pain of a loss."

    show Hayden at left
    hide Taylor

    Hayden "We lost our parents a few weeks back…but now…"

    hide Cara
    show Taylor at right

    Taylor "They’re after me due to my stance in constant protests."

    hide Hayden
    show Cara at left

    Cara "Oh my…first of all, I’m sorry for your loss. Second of all, let me get you over to the others because most of them are on the run too. Not for the same reasons as you though, young lady."

    Taylor "Yeah yeah."

    hide Taylor
    show Bella at right

    Bella "Miss Cara! I’ve been looking for you EVERYWHERE!"

    Cara "I’m so sorry, dear. We have some new arrivals that need to be settled in."

    Bella "Oh em gee WELCOME! My name’s Bella. I’m from the Huntsworth District."

    Bella "My momma is in jail, and my daddy is in one of the labor camps. So I’m here hiding!"

    Cara "Bella dear, would you show Taylor and Hayden around while I get their rooms set up?"

    Bella "Of course, Miss Cara! Follow me! I’ll introduce you to…the others. It's just the three of us!"

    hide Cara
    show Hayden at left

    Hayden "A shelter this big and there’s only three others here?"

    Bella "Well, the others were able to leave after a while, but some of us are stuck here! Like me! If I get caught, I’ll be joining my momma in a cell!"

    hide Hayden
    show Taylor at left

    Taylor "So basically, we can’t leave."

    Bella "Uhhh, I mean, you can leave, but you ALWAYS have to come back. Otherwise, Miss Cara gets maaaaaaad."

    Taylor "Mad?"

    Bella "Yeah, she’s not big on people leaving."

    hide Taylor
    show Hayden at left

    Hayden "Ok, so, who else is here?"

    Bella "Oh allow me to introduce you! The brooding one that looks like he listens to emo music is Logan."

    hide Hayden
    show Logan at left

    Logan "You cannot keep introducing people to me like that, Bell."

    Bella "Awwww, it’s ok Logan, we all know you’re a super softie."

    Logan "Back off."

    Bella "And the one with the hoodie is Alex!"

    hide Logan
    show Alex at left

    Alex "Sup."

    Bella "Ahem-"

    hide Bella
    hide Alex
    show Taylor at center
    
    Taylor "I’m Taylor Jenkins, and this is my brother Hayden."

    show Taylor at left
    show Logan at right

    Logan "Oh shit, the rumors about the Jenkins siblings are true. You two aren’t dead. Ain’t this a shock."

    hide Taylor
    show Hayden at left

    Hayden "What do you mean?"

    hide Logan
    show Bella at right

    Bella "A lot of people in other districts assumed you two were dead. I didn’t realize you were THOSE Jenkins kids. Oh my god."

    hide Hayden
    show Alex at left

    Alex "Wow. What an honor to be in front of such legends."

    hide Bella
    show Hayden at right

    Hayden "I wouldn’t say we’re LEGENDS. I’d say my sister needs to take a break, though."

    hide Alex
    show Taylor at left

    Taylor "Breaks don’t exist for those fighting against corruption, I keep telling you this."
    Hayden "And I keep-"

    show Bella at center

    Bella "Woah woah woah! No need to fight. In fact, we’re alllll running a scheme under Miss Cara’s nose!"

    hide Bella
    hide Taylor
    show Logan at left

    Logan "Do you really wanna let these two in on it?"

    hide Hayden
    show Alex at right

    Alex "It wouldn’t hurt. Escaping is already going to be hard enough. Backup would be good."

    hide Logan
    show Taylor at left

    Taylor "A plan for what?"

    hide Alex
    show Bella at right

    Bella "Escape!"

    hide Taylor
    show Hayden at left

    Hayden "WHAT?!"

    hide Bella
    show Logan at right

    Logan "Keep your voice down, squirt. Ugh."

    return