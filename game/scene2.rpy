# Defining the characters

define taylor = (Character("Taylor"))
define taylor_thought = Character("Taylor" , what_italic = True)
define julie = (Character("Julie"))
define kyle = Character("Kyle")



# The game starts here

label scene2:

    # Show the background image for the scene
    scene bg room

    image taylor = "taylor.jpg"
    image julie = "JuliePlaceholder.png"
    image kyle = "KylePlaceholder.png"

    #Taylor inside thoughts as he's leaving and walking to the protest

    taylor_thought "I step outside and pull my mask up."
    pause 0.5

    taylor_thought "The town looks like a desolate wasteland..."
    pause 0.5

    taylor_thought "Best not to be recognize by these cretins at the protest"
    pause 0.5

    taylor_thought "Even if it feels repetitive... I have to keep going."
    pause 1.0

    #add some sound to show that the protest is getting louder and taylor is getting closer

    #Julie in the middle of protesting and then sees Taylor and gets excited
    #show both characters

    show taylor at right:
        zoom 0.65
    show julie at left

    julie "NO MORE DICTATORS! GIVE US OUR FREEDOM!"

    taylor "Hey, Jules."

    julie "EEEEE! Taylor, you made it! But you're late!"

    taylor "Yeah yeah, but I'm here."

    taylor "You know I'd take any opportunity to fight back against the new government, they're cruel and must be put to rest!"

    taylor "We need a resolution that doesn't involve any of those bastards."

    julie "And here I thought you’d stay back for once."

    julie "You go to EVERYTHING! I thought you’d be taking a break!"

    taylor "There’s no time for breaks."

    julie "Girlll you NEED to take some time to rest! It’ll be good for youuuuu."

    taylor "Yeah yeah, I know. Hayden keeps saying the same thing. But I can’t rest. Not until those assholes are dead!"

    #Kyle comes into the conversation

    label protest_scene:

#scene of outside protest added her

    # Initial characters
    show taylor at left:
        zoom 0.65
    show julie at right

    
    show kyle at center with moveinbottom

    # Kyle speaking  focus him
    show kyle at center
    show taylor at left:
        zoom 0.65
    show julie at right

    kyle "Woahhh, Tay-Tay, you gotta slow your roll. Protests are peaceful obligations, bro."

    # Taylor responds → focus Taylor
    show taylor at left:
        zoom 0.65
    show kyle at center
    show julie at right

    taylor "Oh please, you come to protests for the free food, Kyle."

    # Kyle again → focus Kyle
    show kyle at center
    show taylor at left:
        zoom 0.65
    show julie at right

    kyle "And to support a valiant cause. Our freedom. And the donuts, man. The donuts."

    # Taylor → focus Taylor
    show taylor at center:
        zoom 0.65
    show kyle at left
    show julie at right

    taylor "So human freedom and donuts are on your agenda as usual...got it..."

    # JULIE joins back in
   
    show julie at center
    show taylor at left:
        zoom 0.65
    show kyle at right

    julie "Hey, the donut vendors at these things are AWESOME! I don't blame Kyle at all."

    # TAYLOR 

    show taylor at center:
        zoom 0.65
    show julie at right
    show kyle at left

    taylor "Whatever. As long as we're fighting for what we want, I don't see a problem."

    # KYLE EXITS

    show kyle at center
    show taylor at left:
        zoom 0.65
    show julie at right

    kyle "I'm gonna get more donuts, dudes. LATERS!"

    hide kyle with moveoutright

    # CROWD CHANT add some chanting audio

    kyle "WE WANT FREEDOM, NOT DEPENDENCE! WE WANT FREEDOM, NOT DEPENDENCE!"

    # use vpunch to show Kyle protesting as he leaves the scence
    with vpunch

    # TONE SHIFT (SERIOUS)

    show julie at right
    show taylor at left:
        zoom 0.65

    julie "So...how are ya holding up, Tay?"

    show taylor at left:
        zoom 0.65
    show julie at right

    taylor "Oh, you mean after I lost my parents a few weeks ago? Still awful. Hayden and I have had to hide more just because of it."

    show julie at right
    show taylor at left:
        zoom 0.65

    julie "That's awful..."

    # TAYLOR OPENS UP

    show taylor at left:
        zoom 0.65
    show julie at right

    taylor "I miss them like hell, but...it's made me stronger. I want to make a change even more than before."

    # Julie responds
    show julie at right
    show taylor at left:
        zoom 0.65

    julie "That's the spirit! But seriously, please take a break. You're an easy target. Even with your mask"

    # Taylor pushes back
    show taylor at left:
        zoom 0.65
    show julie at right

    taylor "I switch it up a lot, I'm not scared."

    # GUARD INTERRUPTION (HIGH TENSION)

    # Screen shake + louder atmosphere
    with vpunch

# maybesound " need to add audio"

    "Guard 1" "OK! EVERYONE MOVE IT! IF YOU DON'T LEAVE NOW, YOU WILL BE EXECUTED!"

    # Julie reacts (lighter tone but nervous)

    show julie at right
    show taylor at left:
        zoom 0.65

    julie "Aw man, what the heck!"

    # Taylor reaction (calm/dismissive)

    show taylor at left:
        zoom 0.65
    show julie at right

    taylor "Psh."

    # JULIE EXITS

    show julie at right
    show taylor at left:
        zoom 0.65

    julie "Well, I'll see ya around, Tay. don't get yourself killed out there."

    taylor "Yeah, I know. Be safe, bye."

    hide julie with moveoutright

    # Taylor left alone (optional final beat)

    show taylor at center:
        zoom 0.65

    #taylor making her way out
    
    show taylor at left:
        zoom 0.65

    taylor "Yeah, I know."

    # Kyle pops back in briefly (optional visual or just voice)
    show kyle at right with moveinright

    show kyle at right
    show taylor at left:
        zoom 0.65

    kyle "BYE TAY-TAY! Here, take some donuts for the little man."

    # Kyle exits again
    hide kyle with moveoutright

    # Taylor responds
    show taylor at center:
        zoom 0.65

    taylor "Thanks."
    pause 0.5


    # Optional: fade out crowd noise/music here
    # stop sound fadeout 1.0
    # stop music fadeout 2.0

    show taylor at center:
        zoom 0.65

    taylor_thought "Some folks decided to stay, but when your parents were the ones leading the protests at their peak you have to hide. That's my life."

    taylor_thought "Our town used to be so vibrant and beautiful now it's desolate. A total wasteland. You get caught breaking a single rule, it's either labor work or death."

    taylor_thought "Jailtime is considered mercy. Fines are basically non-existent outside of specified cases. Usually for the rich people, not for others..."

    # End of scence 2

    # Optional fade out
    scene black with fade

    

    return