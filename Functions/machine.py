import numpy as np 
from manim import *


class Machine(Scene):
    def construct(self):

        self.wait(1) # INITIAL WAIT TIME

# SETTING UP OF SCENE --------------------------------------------------
        machine_box = Square(side_length=2, color=BLUE)
        machine_text = TexMobject(r"\text{Machine}(", r"f", r")")
        machine_text_replace = TexMobject(r"\text{Machine}(", r"g", r")")
        machine_text.next_to(machine_box, UP)
        machine_text_replace.next_to(machine_box, UP)

# OUTER ANIMATIONS --------------------------------------------------------------

        self.play(
            FadeIn(machine_box),
            Write(machine_text)
        )

# AUXILLARY SCENE 1 ---------------------------------------------------------------
        for inp, out in zip([r'2',r'3',r'5', r'x'], [r'4',r'6',r'10',r'2x']):
            # SETTING UP OF SCENE --------------------------------------
            machine_in = TexMobject(inp)
            machine_out = TexMobject(out)

            machine_in.shift(5*LEFT)
            machine_out.shift(ORIGIN)
            # INNER ANIMATIONS ------------------------------------------------
            self.play(
                Write(machine_in)
            )
            self.play(
                machine_in.animate.shift(5*RIGHT)
            )
            self.play(
                Transform(machine_in, machine_out)
            )
            self.play(
                machine_in.animate.shift(5*RIGHT)
            )
            self.play(
                FadeOut(machine_in)
            )
#-----------------------------------------------------------------------------------
        self.wait(1)
        self.play(
            Transform(machine_text[1], machine_text_replace[1])
        )

# AUXILLARY SCENE 2 ---------------------------------------------------------------
        for inp, out in zip([r'2',r'3',r'5', r'x'], [r'6',r'11',r'27',r'x^2+2']):
            # SETTING UP OF SCENE --------------------------------------
            machine_in = TexMobject(inp)
            machine_out = TexMobject(out)

            machine_in.shift(5*LEFT)
            machine_out.shift(ORIGIN)
            # INNER ANIMATIONS ------------------------------------------------
            self.play(
                Write(machine_in)
            )
            self.play(
                machine_in.animate.shift(5*RIGHT)
            )
            self.play(
                Transform(machine_in, machine_out)
            )
            self.play(
                machine_in.animate.shift(5*RIGHT)
            )
            self.play(
                FadeOut(machine_in)
            )


        self.wait(1) # FINAL WAIT TIME