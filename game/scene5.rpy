# Declaring characters used by this scene.
define Bella = Character("Bella")
define Logan = Character("Logan")
define MissCara = Character("Miss Cara")
define Alex = Character("Alex")
define Taylor = Character("Taylor")
define Hayden = Character("Hayden")

# Scene 5 starts here
label scene5:
    
    # Show the background.
    scene bg room 

    # Declare the character sprites to images.
    image Bella = "BellaPlaceholder.png"
    image Logan = "LoganPlaceholder.png"
    image MissCara = "CaraPlaceholder.png"
    image Alex = "AlexPlaceholder.png"
    image Taylor = "TaylorPlaceholder.png"
    image Hayden = "HaydenPlaceholder.png"

    # The dialogue for this scene. And to show the character sprites.
    show Bella at left
    show MissCara at center 
    show Logan at right
    
    Bella "Nothing at all, Miss Cara! We are telling Taylor and Hayden how much we love it here! So safeee, so secureee!"
   
    Logan "Yeah. Pretty much."
   
    MissCara "Oh well that is lovely to hear! I just thought I'd let you all know that we are having spaghetti tonight."
    
    hide MissCara
    hide Bella
    show Alex at left

    Alex "Oh snap, she makes some good spaghetti!"

    hide Alex
    show Taylor at left

    Taylor "I haven't had anyone else's cooking in weeks."

    Hayden "You barely even eat, Tay. You save most of the food for me."

    Taylor "Because I'm usually eating donuts from the protests."

    show MissCara at center

    MissCara "Just like your parents."

    Taylor "They fought as long as they could. It's my turn now."

    Hayden "Miss Cara, are our rooms ready?"

    MissCara "Yes indeed! Come along, children."

    Taylor "Not a child. but ok."

    hide MissCara
    hide Hayden 
    show Taylor at center

    Taylor "Miss Cara showed us to our rooms. Though, there were a lot of bedrooms that were locked. It had me suspecting if she was hiding something or someone in them."
    
    Taylor "You never know. Trust is a very rare thing nowadays. She opened the doors to our rooms and I could already tell…she knew a little too much about us."
   
    Taylor "Hayden was astonished by his room, but these rooms felt too good to be true."

    show MissCara at right 
    show Hayden at left

    MissCara "Well children, do you like it?"

    Hayden "It looks just like home! Are you a genie?!"

    MissCara "(soft chuckle) Well aren’t you a sweetie! Taylor, dear, what do you think?"

    Taylor "…You know too much for your own good."

    MissCara " Is that your way of showing appreciation?"

    Taylor "Skepticism laced with appreciation for giving us a place to stay."

    MissCara " That’s alright. Dinner will be ready in a few minutes."

    hide Taylor 
    hide Hayden
    show Bella at left 
    
    Bella "I HEARD DINNER!"

    MissCara " Miss Bella, we talked about this! No yelling about food."

    Bella "Sorry, Miss Cara."

    hide Bella
    hide MissCara
    show Taylor at right
    show Hayden at left

    Hayden "I wonder what districts the others come from."

    Taylor "Well…Bella’s from the Huntsworth District, which does explain her excitement over the smaller things. If I remember correctly, Huntsworth is one of the less fortunate districts."
    
    Hayden "Meanwhile, we’re from Fort Graves. The prime spot for protests."
   
    Taylor "There’s protests everywhere, Hayden. Fort Graves is just the place most people get caught. The graves in the name isn’t just for show."
   
    Hayden "Maybe we can ask them while we’re at dinner!"
   
    Taylor " Yeah. Gives us a chance to learn more about them."

# end of scene 5.
return