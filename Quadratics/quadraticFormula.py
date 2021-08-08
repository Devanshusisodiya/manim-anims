from os import write
from manim import *

class QFormula(Scene):
    def construct(self):
        self.wait(1) # INITIAL WAIT

        intro = MathTex('\\text{Let us derive the }', '\\text{quadratic formula}').shift(ORIGIN)
        intro[1].set_color(BLUE)

        self.play(Write(intro))
        self.wait(1)
        self.play(FadeOut(intro))


        #  FIRST EQUATION ANIM 
        tlist = ['ax^2','+','b','x','+','c','=','0']

        eq = MathTex(*tlist).shift(ORIGIN)
        self.play(Write(eq))

        # step0 = Text()

        tlist[0] = 'x^2'
        tlist[2] = '\\frac{b}{a}'
        tlist[5] = '\\frac{c}{a}'
        eq1 = MathTex(*tlist).shift(ORIGIN)

        step0 = MathTex('\\text{Dividing both }', '\\text{lhs rhs }', '\\text{by the coefficient of } x^2').shift(2.5*DOWN)
        step0[1].set_color(BLUE)
        self.play(Write(step0))
        self.play(FadeOut(step0))

        self.play(Transform(eq, eq1))
        self.play(eq.animate.shift(3.5*UP))
        

        # SECOND EQUATION ANIM
        eq1_0 = MathTex('x^2','+','\\frac{b}{a}','x').shift(ORIGIN + LEFT)
        eq1_1 = MathTex('+','\\frac{c}{a}').next_to(eq1_0, RIGHT) 
        eq1Group = VGroup(eq1_0, eq1_1)

        nterm = '\\frac{b^2}{4a^2}'
        lhst = MathTex('+', nterm).next_to(eq1Group, RIGHT)
        rhst = MathTex('=', nterm)

        step1_0 = MathTex('\\text{Halfing and Sqauring coefficient of }','x').shift(2*DOWN)
        step1_0[1].set_color(BLUE)
        step1_1 = MathTex('\\text{then adding to lhs and rhs}').next_to(step1_0, DOWN)
        stepGroup = VGroup(step1_0, step1_1)

        for i in stepGroup:
            self.play(
                Write(i)
            )


        self.play(Write(eq1Group))
        self.play(eq1Group.animate.shift(LEFT),)
        self.play(Write(lhst))
        self.play(lhst.animate.shift(LEFT))

        rhst.next_to(lhst, RIGHT)
        self.play(
            Write(rhst)
        )

        eq1Group.add(lhst, rhst)
        groupCopy = eq1Group.copy()
        self.play(
            groupCopy.animate.next_to(eq, DOWN)
        )

        self.play(FadeOut(stepGroup))

        # THIRD EQUATION ANIM


        step2 = MathTex('\\text{Transposing the constant term}').shift(2.5*DOWN)

        self.play(
            Write(step2)
        )
        
        ntermsGroup = VGroup(lhst, rhst)
        self.play(
            eq1_1.animate.shift(1.5*DOWN),
            ntermsGroup.animate.next_to(eq1_0, RIGHT)
        )

        eq1_1ch = MathTex('-','\\frac{c}{a}').next_to(ntermsGroup, RIGHT)
        self.play(Transform(eq1_1, eq1_1ch))

        self.play(FadeOut(step2))

        eq1NewGroupCopy = VGroup(eq1_0, lhst, rhst, eq1_1).copy()
        self.play(
            FadeOut(groupCopy),
            eq1NewGroupCopy.animate.next_to(eq, DOWN)
        )
        

        # FOURTH EQUATION ANIM

        eq2_0 = VGroup(eq1_0, lhst)
        eq2_1 = VGroup(rhst, eq1_1)

        step2_1 = MathTex('\\text{Writing lhs in the form of }','(a+b)^2','\\text{, then solving}').shift(2*DOWN)
        step2_1[1].set_color(BLUE)

        rhsCh = MathTex('=','\\frac{b^2-4ac}{4a^2}').next_to(lhst, RIGHT)
        lhsCh = MathTex('\\left(x+\\frac{b}{2a}\\right)^2').next_to(rhsCh, LEFT)

        self.play(Write(step2_1))

        self.play(
            Transform(eq2_0, lhsCh),
            Wait(2),
            Transform(eq2_1, rhsCh)
        )

        self.play(FadeOut(step2_1))

        # FIFTH EQUATION ANIM

        eq2Group = VGroup(eq1_0, eq2_1)
        eq2GroupCopy = eq2Group.copy()
        self.play(
            eq2GroupCopy.animate.next_to(eq1NewGroupCopy, DOWN),
            eq1Group.animate.next_to(eq2GroupCopy, 0.5*DOWN)
        )   

        eq2_lhst1 = MathTex('+\\frac{b}{2a}').next_to(eq2_1, LEFT)
        eq2_lhst0 = MathTex('x').next_to(eq2_lhst1, LEFT)

        eq2_0Groupch = VGroup(eq2_lhst0, eq2_lhst1) 
        eq2_1ch = MathTex('=','\\pm\\frac{\\sqrt{b^2-4ac}}{2a}').next_to(eq2_0, RIGHT)

        self.play(
            Transform(eq2_0, eq2_0Groupch),
            Transform(eq2_1, eq2_1ch)
        )

        self.play(eq2_0[1].animate.shift(DOWN))
        self.play(eq2_1.animate.next_to(eq2_0[0], RIGHT))
        eq2_lhst1ch = MathTex('-\\frac{b}{2a}').next_to(eq2_1, RIGHT)
        self.play(Transform(eq2_0[1], eq2_lhst1ch))
        finGroup = VGroup(eq2_0, eq2_1)
        self.play(finGroup.animate.next_to(eq2GroupCopy, 2*DOWN))        

        self.wait(1) # FINAL WAIT