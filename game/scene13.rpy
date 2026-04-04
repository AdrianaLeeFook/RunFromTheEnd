# Declaring characters used by this scene.
define Bella = Character("Bella")
define TheRuler = Character("The Ruler")
define Taylor = Character("Taylor")
define Alex = Character("Alex")
define Logan = Character("Logan")

# Scene 13 starts here
label scene13:
    
    # Show the background.
    scene bg room

    # Declare the character sprites to images.
    image Bella = "BellaPlaceholder.png"
    image The Ruler = "RulerPlaceholderr.png"
    image Taylor = "TaylorPlaceholder.png"
    image Alex = "AlexPlaceholder.png"
    image Logan = "LoganPlaceholder.png"

    # The dialogue for this scene. And to show the character sprites.
    
    show Bella at left
    show TheRuler at right
    show Taylor at center

    Bella "YES! Way to go Taylor!"

    TheRuler "What's with all that detestable noise?!"

    Taylor "…Is…is that a-"

    TheRuler "No. I'm not a child. I just look young. Now what are you all doing in MY CASTLE?!"

    Bella "Well duh. We're here to TAKE YOU DOWN!"

    TheRuler "…BAHAHAHAHAHAHA! Oh my GOD! You four have the courage to face me? In my own HOME?! How bold!"

    hide Bella
    hide Taylor
    show Alex at left

    Alex " (coughs) Psh. They're even bolder for bringing one of your fugitives, my liege."

    TheRuler "Really? Who?"

    Alex "Taylor Jenkins."

    hide Alex
    show Taylor at left 
    
    TheRuler "Oh! THAT fugitive! What a joyous day! I'll be able to do her execution…personally."
   
    Taylor "I don't think so. You've already torn apart countless families and ended the lives of so many. Your reign ends here."
   
    TheRuler "Oh really? …Oh my oh my. Four people from three families. Little Miss Bella Andrews. The daughter of a well known mercenary."
   
    TheRuler "A mercenary who is now working off his crimes in one of my labor camps. The wife got the…lighter punishment of jail time."
    
    TheRuler " I had no say over that however."
   
    hide Taylor
    show Bella at left
   
    Bella "EEP! How-"

    TheRuler "My father was the one who imprisoned your mother. The labor camp for your father? That was my idea."
   
    Bella "(gasps) Wh-what…?"
    
    TheRuler "And Logan Davies. The self proclaimed rebel. Friends with weapon dealers. Parents…unknown location. Weapons dealers though…"
    
    TheRuler "Quite the intrigue here. Your parents ran into hiding as soon as their arrest warrants were released. My my my…"
   
    hide Bella
    show Logan at left
    
    Logan "You can rightfully shut up about my parents."
   
    TheRuler "And of course…the Jenkins siblings. You know…weren't your parents executed just two weeks ago? For attending illegal protests? Against MY regime?!"
   
    show Bella at center

    Bella " Wait…that was only two weeks ago but…but the stories…"
   
    Logan "The stories Miss Cara told us were bullshit."
    
    hide Loagan
    hide Bella
    show Alex at left 
    
    TheRuler " Oh yes, the housekeeper. Alex, did she know of your plans?"
   
    Alex "Eh. No. She's probably freaking out."
    
    hide Alex 
    show Taylor at left

    Taylor "It doesn't matter what kind of plans you guys have. This reign of terror ends now."
   
    TheRuler "Hah…oh really? You and what army?"
# end of scene 13.
return