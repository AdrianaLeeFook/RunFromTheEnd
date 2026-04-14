default s7_p1_progress = 0
default s7_p1_message = ""

screen clock_order_puzzle_screen():

    tag puzzle

    add Transform("clock_bg.png", zoom=1.15)

    text "Rebuild the clock" xalign 0.5 yalign 0.05 size 40
    text "Click the pieces in the correct order." xalign 0.5 yalign 0.10 size 28

    if s7_p1_progress == 4:
        add Transform("clock_full.png", zoom=0.62) xalign 0.5 yalign 0.47

    if s7_p1_message != "":
        text "[s7_p1_message]" xalign 0.5 yalign 0.82 size 28 color "#ffffff"

    if s7_p1_progress < 4:

        imagebutton:
            idle Transform("clock_piece1.png", zoom=0.20)
            hover Transform("clock_piece1.png", zoom=0.22)
            xalign 0.28
            yalign 0.55
            action If(
                s7_p1_progress == 0,
                [SetVariable("s7_p1_progress", 1), SetVariable("s7_p1_message", "")],
                [SetVariable("s7_p1_progress", 0), SetVariable("s7_p1_message", "Incorrect. Start over.")]
            )

        imagebutton:
            idle Transform("clock_piece2.png", zoom=0.20)
            hover Transform("clock_piece2.png", zoom=0.22)
            xalign 0.50
            yalign 0.55
            action If(
                s7_p1_progress == 1,
                [SetVariable("s7_p1_progress", 2), SetVariable("s7_p1_message", "")],
                [SetVariable("s7_p1_progress", 0), SetVariable("s7_p1_message", "Incorrect. Start over.")]
            )

        imagebutton:
            idle Transform("clock_piece3.png", zoom=0.20)
            hover Transform("clock_piece3.png", zoom=0.22)
            xalign 0.28
            yalign 0.72
            action If(
                s7_p1_progress == 2,
                [SetVariable("s7_p1_progress", 3), SetVariable("s7_p1_message", "")],
                [SetVariable("s7_p1_progress", 0), SetVariable("s7_p1_message", "Incorrect. Start over.")]
            )

        imagebutton:
            idle Transform("clock_piece4.png", zoom=0.20)
            hover Transform("clock_piece4.png", zoom=0.22)
            xalign 0.50
            yalign 0.72
            action If(
                s7_p1_progress == 3,
                [SetVariable("s7_p1_progress", 4), SetVariable("s7_p1_message", "Correct!")],
                [SetVariable("s7_p1_progress", 0), SetVariable("s7_p1_message", "Incorrect. Start over.")]
            )

    if s7_p1_progress == 4:
        textbutton "Continue":
            xalign 0.5
            yalign 0.92
            action Return()


label scene7_puzzle1_clock:

    $ s7_p1_progress = 0
    $ s7_p1_message = ""

    call screen clock_order_puzzle_screen

    return