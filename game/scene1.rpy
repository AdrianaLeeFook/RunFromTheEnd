# Declaring characters used by this scene.
define Taylor = Character("Taylor")
define Hayden = Character("Hayden")

# Scene 1 starts here
label scene1:

    # Show the background.
    scene bg room

    # Declare the character sprites to images.
    image Taylor = "taylor.jpg"
    image Hayden = "hayden.jpg"

    # The dialogue for this scene. And to show the character sprites.
    show Taylor at center
    
    Taylor "This town...empty of its former glory...the town I grew up in. Shattered by a dictatorship that punishes those they deem unfit. It's hell. Utter and complete hell. They didn't hesistate with taking over. I want to leave, but we've all been stuck here for five years. Anyone who tries? Well...they never see the light of day again."
    
    show Hayden at left
    show Taylor at right

    Hayden "Tay,where are you going?"

    Taylor "...Protest."

    Hayden "Again? Taylor,you know what hapens at those!"

    Taylor "They can try and silence us...but I don't get caught."

    Hayden "But Taylor.."

    Taylor "Hayden,it doesn't matter right now. I..."
 
    Hayden "Taylor,you don't have to go to every protest."

    Taylor "I know. But I feel like I have to. The only way change is going to happen is if they hear us."

    Hayden "Taylor,I'm worried about you"
 
    Taylor "...Don't be. Please. For your sake and mine..."

    Hayden "Why do you even go every time? I know you want to speak out but..."

    Taylor "If anything, it's to make sure you don't get caught up in my mess."

    Hayden "I'm not some little kid anymore! You don't have to protect me!"
  
    Taylor "Too bad."

    Hayden "Hmph. I don't want you getting hurt, is that so bad to be concerned about, Tay?"

    Taylor "No, but you don't need to worry about me. I'm fine."
   
    Hayden "But Taylor...I don't want you to come back with..."
  
    Taylor "...I'll be fine. As long as you're safe that's what matters to me. ...I can't afford to lose anyone else."



    # This ends the game
    


    return