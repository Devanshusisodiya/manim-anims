from manim import *

class BondCleavage(Scene):
    def construct(self):
        self.wait(1)

        c1 = Tex("C").shift(ORIGIN+2*LEFT).scale(2)
        c2 = Tex("C").shift(ORIGIN+2*RIGHT).scale(2)
        bond1 = Line(start=ORIGIN+1.5*LEFT, end=ORIGIN, stroke_width=7)
        bond2 = Line(start=ORIGIN, end=ORIGIN+1.5*RIGHT, stroke_width=7)
        ue1 = Dot(ORIGIN+1.5*LEFT, color=RED)
        ue2 = Dot(ORIGIN+1.5*RIGHT, color=RED)

        self.wait(0.5)

        self.add(c1, c2, bond1, bond2)
        self.play(
            Transform(bond1, ue1),
            Transform(bond2, ue2)
        )
        self.wait(1)