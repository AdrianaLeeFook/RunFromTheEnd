# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define taylor = Character("Taylor")
define hayden = Character("Hayden")


# The game starts here.

label scene1:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "empty town.png" or "empty town.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    image taylor = "taylor.jpg"
    image hayden = "hayden.jpg"

    # These display lines of dialogue.
    show taylor at center
    
    taylor "This town…empty of its former glory…the town I grew up in. Shattered by a dictatorship that punishes those they deem unfit."

    taylor "It’s hell. Utter and complete hell. They didn’t hesitate with taking over. I want to leave, but we’ve all been stuck here for five years."

    taylor "Anyone who tries? Well…they never see the light of day again."
    
    show hayden at left
    show taylor at right

    hayden "Tay, where are you going?"

    taylor "...Protest."

    hayden "Again? Taylor, you know what happens at those!"

    taylor "Please. They can try and silence us…but I don’t get caught."

    hayden "But Taylor.."

    taylor "Hayden, it doesn't matter right now. I..."
 
    hayden "Taylor, you don't have to go to every protest."

    taylor "I know. But I feel like I have to. The only way change is going to happen is if they hear us."

    hayden "Taylor, I'm worried about you"
 
    taylor "...Don't be. Please. For your sake and mine..."

    hayden "Why do you even go every time? I know you want to speak out but..."

    taylor "If anything, it's to make sure you don't get caught up in my mess."

    hayden "I'm not some little kid anymore! You don't have to protect me!"
  
    taylor "Too bad."

    hayden "I don’t want you getting hurt, is that so bad to be concerned about, Tay?"

    taylor "No, but you don't need to worry about me. I'm fine."
   
    hayden "But Taylor...I don't want you to come back with..."
  
    taylor "...I'll be fine. As long as you're safe that's what matters to me. ...I can't afford to lose anyone else."



    # This ends the game
    


    return
