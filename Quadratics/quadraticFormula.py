from manim import *

class QFormula(Scene):
    def construct(self):
        self.wait(1) # INITIAL WAIT


        #  FIRST EQUATION ANIM 
        tlist = ['ax^2','+','b','x','+','c','=','0']

        eq = MathTex(*tlist).shift(ORIGIN)
        self.play(Write(eq))

        tlist[0] = 'x^2'
        tlist[2] = '\\frac{b}{a}'
        tlist[5] = '\\frac{c}{a}'
        eq1 = MathTex(*tlist).shift(ORIGIN)
        self.play(Transform(eq, eq1))
        self.play(eq.animate.shift(1.5*UP))
        

        # SECOND EQUATION ANIM
        eq1_0 = MathTex('x^2','+','\\frac{b}{a}','x').shift(ORIGIN + LEFT)
        eq1_1 = MathTex('+','\\frac{c}{a}').next_to(eq1_0, RIGHT) 
        eq1Group = VGroup(eq1_0, eq1_1)

        nterm = '\\frac{b^2}{4a^2}'
        lhst = MathTex('+', nterm).next_to(eq1Group, RIGHT)
        rhst = MathTex('=', nterm)
        self.play(
            Write(eq1Group),
            eq1Group.animate.shift(LEFT),
            Write(lhst),
            lhst.animate.shift(LEFT)
        )
        rhst.next_to(lhst, RIGHT)
        self.play(
            Write(rhst)
        )

        eq1Group.add(lhst, rhst)
        groupCopy = eq1Group.copy()
        self.play(
            FadeOut(eq),
            groupCopy.animate.shift(1.5*UP)
        )

        # THIRD EQUATION ANIM
        ntermsGroup = VGroup(lhst, rhst)
        self.play(
            eq1_1.animate.shift(1.5*DOWN),
            ntermsGroup.animate.next_to(eq1_0, RIGHT)
        )
        eq1_1ch = MathTex('-','\\frac{c}{a}').next_to(ntermsGroup, RIGHT)
        self.play(ReplacementTransform(eq1_1, eq1_1ch))

        # FOURTH EQUATION ANIM
        self.play(
            FadeOut(groupCopy)
        )

        eq2_0 = VGroup(eq1_0, lhst)
        eq2_1 = VGroup(rhst, eq1_1ch)

        rhsCh = MathTex('=','\\frac{b^2-4ac}{4a^2}').next_to(lhst, RIGHT)
        lhsCh = MathTex('\\left(x-\\frac{b}{2a}\\right)^2').next_to(rhsCh, LEFT)
        self.play(
            Transform(eq2_0, rhsCh),
            Transform(eq2_1, lhsCh)
        )

        # FIFTH EQUATION ANIM
        


        self.wait(1) # FINAL WAIT