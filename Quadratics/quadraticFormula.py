from manim import *

class QFormula(Scene):
    def construct(self):
        self.wait(1) # INITIAL WAIT

        eq = MathTex('a','x^2','+','b','x','+','c','=0').shift(ORIGIN)
        self.play(Write(eq))

        self.wait(1) # FINAL WAIT