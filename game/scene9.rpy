# Declaring characters used by this scene.
define Pierce = Character("Pierce")
define Taylor = Character("Taylor")
define Bella = Character("Bella")
define Logan = Character("Logan")
define Alex = Character("Alex")
define Hayden = Character("Hayden")

# Scene 9 starts here
label scene9:
    
    # Show the background.
    scene bg room

    # Declare the character sprites to images.
    image Pierce = "PiercePlaceholder.png"
    image Taylor = "TaylorPlaceholder.png"
    image Bella = "BellaPlaceholder.png"
    image Logan = "LoganPlaceholder.png"
    image Alex = "AlexPlaceholder.png"
    image Hayden = "HaydenPlaceholder.png"

    # The dialogue for this scene. And to show the character sprites.
    show Pierce at right:
        zoom 0.75
    show Taylor at left:
        zoom 0.65

    Pierce "Alrighty, so that's two daggers for the kid."

    Taylor "He doesn't need two."

    Pierce "Please. I overheard you two talking. He'll need two."

    hide Taylor
    show Bella at left

    Bella "LOGAN LOGAN! LOOK AT THIS CROSSBOW! OH HELL YEAH! THIS SHIT BOUTTA BE BITCHIN!"

    show Logan at center

    Logan "You got guns?"

    Pierce "You know I do man! Also, I got those knives you like. Do you want both?"

    Logan "Hell yeah."

    hide Logan
    hide Bella
    show Alex at left
    show Taylor at center:
        zoom 0.65

    Alex "I think this katana will serve me well."

    Taylor "And this sword will work just fine for me. You said this was on the house?"

    Pierce "Yeah. You guys are about to go take down one of the FIERCEST forces that I've ever seen. If anything, I'd give yall a grenade just as backup."
    
    hide Taylor 
    show Bella at center

    Bella "BOMBS?!"

    hide Bella 
    show Taylor at center:
        zoom 0.65

    Pierce "I got a few grenades. No landmines or anything. Everything would just explode in an instant. Grenades though…those are way easier to deal with."
    
    Taylor " …give them to me."
   
    Alex "What makes you think you're the one to be trusted with them?"
    
    Taylor "Quite frankly, I still don't trust any of you. I know what protestors are like, and I know how storming the castle can end up."
    
    Taylor "So I think it's in everyone's best interest for me to hold onto these."
    
    hide Pierce 
    hide Taylor 
    show Hayden at right:
        zoom 0.75
    show Bella at center

    Hayden "Taylor's good at making sure things don't mess up! You gotta trust her on this one Alex."

    Bella " I trust her too! I mean…granted, logically, it's silly. But…Taylor hasn't threatened to kill an entire district before, even jokingly."
    
    Alex "You remember that?"

    Bella "Mhm! I'm not that dumb!"

    hide Bella 
    hide Hayden
    hide Alex
    show Taylor at right:
        zoom 0.65
    show Logan at center
    show Pierce at left:
        zoom 0.75
    
    Logan "Look at that. Her brain isn't entirely made of rocks after all."

    Taylor "…I'll ask about that later. Anyways…thank you Pierce."

    Pierce "No problem! And hey, if you somehow manage to free the ones in the execution lineup, try and save my mom. She got caught the other day and her execution is coming up."
    
    hide Logan
    hide Pierce
    show Hayden at left:
        zoom 0.75

    Hayden "You got it! We're gonna save everyone! R-right?"

    Taylor "Yes.Yes we are."

    Taylor "We marched through the districts…while the Maintown district wasn't far…it was still a bit of a walk. Everything did feel a little too…good."

# end of scene 9.
return