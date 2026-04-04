define Taylor = Character("Taylor")
define Hayden = Character("Hayden")
define Cara = Character("Miss Cara")
define Logan = Character("Logan")
define Bella = Character("Bella")
define Alex = Character("Alex")
define hb = Character("Hayden and Bella")

# The game starts here.

label scene4:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    image Taylor = "Cara0-2.png"
    image Hayden = "Cara9-1.png"
    image Cara = "CaraPlaceholder"
    image Bella = "Cara96-6.png"
    image Logan = "Fuyuhiko_Kuzuryuu_Halfbody_Sprite_29.png"
    image Alex = "Quiz_detail_image_38.png"

    show Taylor at center:
        zoom 0.65
    Taylor "We kept walking through the town, hiding at certain points in guard-heavy areas."

    Taylor "We tried our best to not get caught. Somehow, we didn’t."

    Taylor "The safehouse was bigger than we thought."

    show Hayden at right:
        zoom 0.75
    show Taylor at left:
        zoom 0.65

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

    show Taylor at left:
        zoom 0.65
    show Cara at right

    Taylor "Um. Who are you?"

    Cara "Oh right yes! I’m Miss Cara."

    Cara "I run this safehouse and protect the children of those whose parents or other family members are on the run from the government. Or have…suffered the pain of a loss."

    show Hayden at left:
        zoom 0.75
    hide Taylor

    Hayden "We lost our parents a few weeks back…but now…"

    hide Cara
    show Taylor at right:
        zoom 0.65

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
    show Hayden at left:
        zoom 0.75

    Hayden "A shelter this big and there’s only three others here?"

    Bella "Well, the others were able to leave after a while, but some of us are stuck here! Like me! If I get caught, I’ll be joining my momma in a cell!"

    hide Hayden
    show Taylor at left:
        zoom 0.65

    Taylor "So basically, we can’t leave."

    Bella "Uhhh, I mean, you can leave, but you ALWAYS have to come back. Otherwise, Miss Cara gets maaaaaaad."

    Taylor "Mad?"

    Bella "Yeah, she’s not big on people leaving."

    hide Taylor
    show Hayden at left:
        zoom 0.75

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
    show Taylor at center:
        zoom 0.65
    
    Taylor "I’m Taylor Jenkins, and this is my brother Hayden."

    show Taylor at left:
        zoom 0.65
    show Logan at right

    Logan "Oh shit, the rumors about the Jenkins siblings are true. You two aren’t dead. Ain’t this a shock."

    hide Taylor
    show Hayden at left:
        zoom 0.75

    Hayden "What do you mean?"

    hide Logan
    show Bella at right

    Bella "A lot of people in other districts assumed you two were dead. I didn’t realize you were THOSE Jenkins kids. Oh my god."

    hide Hayden
    show Alex at left

    Alex "Wow. What an honor to be in front of such legends."

    hide Bella
    show Hayden at right:
        zoom 0.75

    Hayden "I wouldn’t say we’re LEGENDS. I’d say my sister needs to take a break, though."

    hide Alex
    show Taylor at left:
        zoom 0.65

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
    show Taylor at left:
        zoom 0.65

    Taylor "A plan for what?"

    hide Alex
    show Bella at right

    Bella "Escape!"

    hide Taylor
    show Hayden at left:
        zoom 0.75

    Hayden "WHAT?!"

    hide Bella
    show Logan at right

    Logan "Keep your voice down, squirt. Ugh."

    hide Hayden
    show Taylor at left:
        zoom 0.65

    Taylor "An escape plan…you aren’t scared that it could fail?"

    hide Logan
    show Alex at right

    Alex "We’re somewhat worried but…Logan’s an actual threat so no need to fear!"

    hide Taylor
    show Bella at left

    Bella "He owns a gun!"

    hide Alex
    show Hayden at right:
        zoom 0.75

    Hayden "What?! Really?! Can I see?!"

    hide Bella
    show Logan at left

    Logan "Absolutely not, I don’t show my gun to anyone freely."

    hide Hayden
    show Taylor at right:
        zoom 0.65

    Taylor "Ok edgelord, whatever you say."

    hide Logan
    show Bella at left

    Bella "Oh yeah! Burner phones! Here you guys go!"

    Taylor "No thank you. We do not need them tracking us."

    hide Bella
    show Hayden at left:
        zoom 0.75

    Hayden "We left our phones back at home."

    hide Taylor
    show Alex at right

    Alex "Wait, they’re actively after you guys? That’s terrifying."

    hide Hayden
    show Logan at left

    Logan "So the hag brought us an escaped fugitive. Lovely."

    hide Alex
    show Taylor at right:
        zoom 0.65

    Taylor "I’m not an escaped fugitive. I was protecting my brother. I would’ve stayed but he comes first."

    Logan "…Sorry."

    hide Logan
    show Bella at left

    Bella "Logan might seem harsh but he does mean well!"

    Taylor "Right…. Regardless, if you think you can escape or try and take them down, think again? Psh. It can’t happen."

    hide Bella
    show Hayden at left:
        zoom 0.75

    Hayden "I mean…it could!"

    Taylor "No Hayden, it can’t."

    hide Taylor
    show Bella at right

    Bella "But it could! There’s parts of THIS VERY DISTRICT that aren’t blocked by guards 24/7. And Alex knows EXACTLY which ones!"

    Hayden "Oh really? Which ones?"

    Bella " …Ok, maybe not this EXACT district, but one close by."

    hide Hayden
    show Alex at left

    Alex "There’s a gate by the Frontworst District, which isn’t far from here. Guards are gone between 7 and 11 at night."

    hide Bella
    show Logan at right

    Logan "We’ve also found one down by Ironhill. Those gates are unguarded at like 2 to 4 in the morning. It’s crazy."

    hide Alex
    show Taylor at left:
        zoom 0.65

    Taylor "So some gates go unguarded…"

    hide Logan
    show Hayden at right:
        zoom 0.75

    Hayden "But what about the cameras?"

    hide Taylor
    show Alex at left

    Alex "The gates don’t have cameras!"

    hide Hayden
    show Taylor at right:
        zoom 0.65

    Taylor "Uh. Yes. Yes they do. If those cameras are active, your plan immediately goes down the drain."

    hide Alex
    show Bella at left

    Bella "…How did we forget about the cameras?!"

    hide Taylor
    show Alex at right

    Alex "Guess I wasn’t really thinking about it."

    hide Bella
    show Logan at left

    Logan "There’s cameras everywhere now…ugh…"

    hide Alex
    show Taylor at right:
        zoom 0.65

    Taylor "Unless you plan to disable the cameras, which you can’t do without getting into their server room, you aren’t gonna have a chance to use the gates."

    hide Logan
    show Bella at left

    Bella "Then why don’t we just…break into the castle itself!"

    hide Taylor
    show Logan at right

    Logan "Bella, are you INSANE?!"

    Bella "Yes I am!"

    show Alex at center

    Alex "Oh my word…"

    hide Alex
    hide Bella
    hide Logan
    show Taylor at center:
        zoom 0.65

    Taylor "If you really wanna try anything, you should watch what people do when they try to escape the gates AT the unguarded times. Send someone who doesn’t know any better."

    show Logan at left

    Logan "So Bella or Hayden."

    hide Logan
    hide Taylor
    show Hayden at left:
        zoom 0.75
    show Bella at right

    hb "Hey! We aren’t that useless!"

    hide Bella
    show Taylor at right:
        zoom 0.65

    Taylor "And you are NOT sending my brother into the arms of those…THOSE…THOSE PIECES OF SHIT!"

    hide Hayden
    show Logan at left

    Logan "Ok ok, holy hell, fine fine. Sorry."

    hide Taylor
    show Alex at right

    Alex "If you really want to send someone, try some random person on the street who would fall for it."

    hide Logan
    show Bella at left

    Bella "Why would we sacrifice the innocent?"

    Alex "I mean hey, if you guys don’t wanna do the dirty work, I will."

    hide Alex
    show Taylor at right:
        zoom 0.65

    Taylor "There’s no way I’m sending someone to their death."

    show Cara at center

    Cara "What are you all talking about?"

    return