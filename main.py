def on_button_pressed_a():
    basic.show_leds("""
        # . . . .
                . # . . .
                . . # . .
                . . . # .
                . . . . #
    """)
    basic.pause(1000)
    basic.show_leds("""
        . . . . #
                . . . # .
                . . # . .
                . # . . .
                # . . . .
    """)
    basic.pause(1000)
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
    """)
    basic.pause(1000)
    basic.show_leds("""
        # . # . #
                . # # # .
                # # # # #
                . # # # .
                # . # . #
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)
