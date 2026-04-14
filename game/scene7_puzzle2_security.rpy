default s7_sec_progress = 0
default s7_sec_message = ""
default s7_sec_failed = False
default s7_sec_done = False
default s7_sec_time_left = 10
default s7_sec_order = []


init python:
    import random

    def s7_make_order():
        nodes = ["A", "B", "C", "D"]
        random.shuffle(nodes)
        return nodes

    def s7_click_node(node):
        expected = store.s7_sec_order[store.s7_sec_progress]

        if node == expected:
            store.s7_sec_progress += 1
            store.s7_sec_message = "Node " + node + " accepted"

            if store.s7_sec_progress >= 4:
                store.s7_sec_done = True
                store.s7_sec_message = "OVERRIDE COMPLETE"

            renpy.restart_interaction()
        else:
            store.s7_sec_failed = True
            store.s7_sec_message = "ACCESS DENIED"
            renpy.restart_interaction()

    def s7_tick_timer():
        if not store.s7_sec_failed and not store.s7_sec_done:
            store.s7_sec_time_left -= 1

            if store.s7_sec_time_left <= 0:
                store.s7_sec_time_left = 0
                store.s7_sec_failed = True
                store.s7_sec_message = "TIME OUT"

            renpy.restart_interaction()


transform blink_fast:
    alpha 1.0
    linear 0.35 alpha 0.2
    linear 0.35 alpha 1.0
    repeat


screen scene7_security_screen():

    tag puzzle
    modal True

    add Transform("security_bg.png", size=(1920, 1080))

    if not s7_sec_failed and not s7_sec_done:
        timer 1.0 action Function(s7_tick_timer) repeat True

    text "SECURITY SYSTEM OVERRIDE" xalign 0.5 yalign 0.06 size 42 color "#7df9ff"

    if s7_sec_time_left > 3:
        text "TIME: [s7_sec_time_left]" xalign 0.5 yalign 0.13 size 32 color "#ffffff"
    else:
        text "TIME: [s7_sec_time_left]" xalign 0.5 yalign 0.13 size 36 color "#ff4d4d" at blink_fast

    text "Enter the node sequence before time runs out." xalign 0.5 yalign 0.19 size 24 color "#d8faff"
    text "SEQUENCE: [s7_sec_order[0]]  →  [s7_sec_order[1]]  →  [s7_sec_order[2]]  →  [s7_sec_order[3]]" xalign 0.5 yalign 0.26 size 28 color "#9effa1"

    frame:
        xalign 0.5
        yalign 0.53
        xsize 900
        ysize 430
        background "#0a0f18cc"

        # side rails
        add Solid("#3a3f4a") xpos 40 ypos 40 xsize 36 ysize 300
        add Solid("#3a3f4a") xpos 824 ypos 40 xsize 36 ysize 300

        # left ports
        add Solid("#f4d03f") xpos 58 ypos 70 xsize 36 ysize 18
        add Solid("#e74c3c") xpos 58 ypos 145 xsize 36 ysize 18
        add Solid("#ff4fd8") xpos 58 ypos 220 xsize 36 ysize 18
        add Solid("#3498db") xpos 58 ypos 295 xsize 36 ysize 18

        # right ports
        add Solid("#3498db") xpos 806 ypos 70 xsize 36 ysize 18
        add Solid("#f4d03f") xpos 806 ypos 145 xsize 36 ysize 18
        add Solid("#e74c3c") xpos 806 ypos 220 xsize 36 ysize 18
        add Solid("#ff4fd8") xpos 806 ypos 295 xsize 36 ysize 18

        # wires appear as progress is made
        if s7_sec_progress >= 1:
            add Solid("#f4d03f") xpos 94 ypos 78 xsize 712 ysize 8

        if s7_sec_progress >= 2:
            add Solid("#e74c3c") xpos 94 ypos 153 xsize 712 ysize 8

        if s7_sec_progress >= 3:
            add Solid("#ff4fd8") xpos 94 ypos 228 xsize 712 ysize 8

        if s7_sec_progress >= 4:
            add Solid("#3498db") xpos 94 ypos 303 xsize 712 ysize 8

        # node buttons
        if not s7_sec_failed and not s7_sec_done:
            textbutton "A":
                xpos 180
                ypos 355
                xsize 120
                ysize 46
                action Function(s7_click_node, "A")

            textbutton "B":
                xpos 370
                ypos 355
                xsize 120
                ysize 46
                action Function(s7_click_node, "B")

            textbutton "C":
                xpos 560
                ypos 355
                xsize 120
                ysize 46
                action Function(s7_click_node, "C")

            textbutton "D":
                xpos 750
                ypos 355
                xsize 120
                ysize 46
                action Function(s7_click_node, "D")

    # status message at bottom
    if s7_sec_message != "":
        if s7_sec_failed:
            text "[s7_sec_message]" xalign 0.5 yalign 0.86 size 30 color "#ff5c5c"
        elif s7_sec_done:
            text "[s7_sec_message]" xalign 0.5 yalign 0.86 size 30 color "#7dff9b"
        else:
            text "[s7_sec_message]" xalign 0.5 yalign 0.86 size 28 color "#ffde59"

    if s7_sec_done or s7_sec_failed:
        textbutton "Continue":
            xalign 0.5
            yalign 0.93
            action Return()


label scene7_puzzle2_security:

    $ s7_sec_progress = 0
    $ s7_sec_message = ""
    $ s7_sec_failed = False
    $ s7_sec_done = False
    $ s7_sec_time_left = 10
    $ s7_sec_order = s7_make_order()

    call screen scene7_security_screen

    if s7_sec_failed:
        return "fail"
    else:
        return "success"