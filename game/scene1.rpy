# Declaring characters used by this scene.
define Taylor = Character("Taylor")
define Hayden = Character("Hayden")

# Scene 1 starts here
label scene1:

    # Show the background.
    scene bg room

    # Declare the character sprites to images.
    image Taylor = "TaylorPlaceholder.png"
    image Hayden = "HaydenPlaceholder.png"

    # The dialogue for this scene. And to show the character sprites.
    show Taylor at center:
        zoom 0.65
    
    play sound "Taylor_RFTE_LINE1.mp3"
    Taylor "This town…empty of its former glory…the town I grew up in. Shattered by a dictatorship that punishes those they deem unfit."
    stop sound

    play sound "Taylor_RFTE_LINE2.mp3"
    Taylor "It's hell. Utter and complete hell. They didn't hesitate with taking over. I want to leave, but we've all been stuck here for five years."
    stop sound

    play sound "Taylor_RFTE_LINE3.mp3"
    Taylor "Anyone who tries? Well…they never see the light of day again."
    stop sound
    
    show Hayden at left:
        zoom 0.75
    show Taylor at right:
        zoom 0.65

    play sound "Hayden1.mp3"
    Hayden "Tay, where are you going?"
    stop sound

    play sound "Taylor_RFTE_LINE4.mp3"
    Taylor "...Protest."
    stop sound

    play sound "Hayden2.mp3"
    Hayden "Again? Taylor, you know what happens at those!"
    stop sound

    play sound "Taylor_RFTE_LINE5.mp3"
    Taylor "Please. They can try and silence us…but I don't get caught."
    stop sound

    play sound "Hayden3.mp3"
    Hayden "But Taylor.."
    stop sound

    play sound "Taylor_RFTE_LINE6.mp3"
    Taylor "Hayden, it doesn't matter right now. I..."
    stop sound
 
    play sound "Hayden4.mp3"
    Hayden "Taylor, you don't have to go to every protest."
    stop sound

    play sound "Taylor_RFTE_LINE7.mp3"
    Taylor "I know. But I feel like I have to. The only way change is going to happen is if they hear us."
    stop sound

    play sound "Hayden5.mp3"
    Hayden "Taylor, I'm worried about you."
    stop sound
 
    play sound "Taylor_RFTE_LINE8.mp3"
    Taylor "...Don't be. Please. For your sake and mine..."
    stop sound

    play sound "Hayden6.mp3"
    Hayden "Why do you even go every time? I know you want to speak out but..."
    stop sound

    play sound "Taylor_RFTE_LINE9.mp3"
    Taylor "If anything, it's to make sure you don't get caught up in my mess."
    stop sound

    play sound "Hayden7.mp3"
    Hayden "I'm not some little kid anymore! You don't have to protect me!"
    stop sound
  
    play sound "Taylor_RFTE_LINE10.mp3"
    Taylor "Too bad."
    stop sound

    play sound "Hayden8.mp3"
    Hayden "I don't want you getting hurt, is that so bad to be concerned about, Tay?"
    stop sound

    play sound "Taylor_RFTE_LINE11.mp3"
    Taylor "No, but you don't need to worry about me. I'm fine."
    stop sound
   
    play sound "Hayden9.mp3"
    Hayden "But Taylor...I don't want you to come back with..."
    stop sound
  
    play sound "Taylor_RFTE_LINE12.mp3"
    Taylor "...I'll be fine. As long as you're safe that's what matters to me. ...I can't afford to lose anyone else."
    stop sound



    # This ends the game
    


    return