from manim import *

class QFormula(Scene):
    def construct(self):
        self.wait(1) # INITIAL WAIT

        tlist = ['ax^2','','+','b','x','+','c','','','=0']

        eq = MathTex(*tlist).shift(ORIGIN)
        self.play(Write(eq))

        tlist[0] = 'x^2'
        tlist[3] = '\\frac{b}{a}'
        tlist[6] = '\\frac{c}{a}'
        eq2 = MathTex(*tlist).shift(ORIGIN)
        self.play(
            Transform(eq, eq2)
        )
        tlist[7] = '+'
        tlist[8] = '\\frac{b^2}{4a^2}'
        tlist[-1] = '=\\frac{b^2}{4a^2}'
        eq3 = MathTex(*tlist).shift(ORIGIN)
        self.play(
            Transform(eq, eq3)
        )

        self.wait(1) # FINAL WAIT