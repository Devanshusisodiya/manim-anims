import numpy as np 
from manim import *

class Test(Scene):
    def construct(self):
        self.wait(1) # INITIAL WAIT TIME

        # SETTING UP OF THE SCENE --------------------------------------------------
        # INITIAL STEP - 0
        step0 = MathTex(r'y',r'=')
        step0_1 = MathTex(r'x-3')
        step0_2 = MathTex(r'(x+2)')
        fracline0 = Line(start=ORIGIN, end=ORIGIN+1.25*RIGHT, stroke_width=2.5)
        fracline0.shift(step0[1].get_center()+0.35*RIGHT)
        step0_1.next_to(fracline0, UP)
        step0_2.next_to(fracline0, DOWN)

        step0_group = VGroup(step0, step0_1, step0_2)

        # STEP - 1
        step1 = MathTex(r'yx+2y=x-3')

        step1.shift(ORIGIN+UP)

        # STEP - 2
        step2 = MathTex(r'yx-x=-3-2y')

        step2.shift(ORIGIN)

        # STEP - 3
        step3 = MathTex(r'x',r'(1-y)',r'=')
        step3_1 = MathTex(r'3+2y')
        step3_2 = MathTex(r'1-y')
        fracline3 = Line(start=ORIGIN, end=ORIGIN+1.25*RIGHT, stroke_width=2.5)
        step3.shift(ORIGIN+1.25*DOWN)

        fracline3.shift(step3[2].get_center()+0.35*RIGHT)
        step3_1.next_to(step3[2], RIGHT)
        step3_2.next_to(fracline3, DOWN)

        step3_group = VGroup(step3, step3_1)
        step3_group2 = VGroup(step3[2], step3_1, step3_2, fracline3)


        # ANIMATIONS ---------------------------------------------------------------
        self.play(
            *[Write(elements) for elements in step0_group],
            ShowCreation(fracline0),
        )
        self.play(
            step0[0].animate.next_to(step0[1], 7.5*LEFT),
            step0_2.animate.next_to(step0[1], LEFT),
            step0_1.animate.next_to(step0[1], RIGHT),
            FadeOut(fracline0),
        )
        self.play(
            step0_group.animate.shift(ORIGIN+2*UP),
        )
        #-------------------
        self.play(Write(step1))
        #-------------------
        self.play(Write(step2))
        #-------------------
        self.play(
            *[Write(elements) for elements in step3_group],
        )
        self.play(
            step3_1.animate.next_to(fracline3, UP),
            ReplacementTransform(step3[1], step3_2),
            ShowCreation(fracline3),
        )
        self.play(
            step3_group2.animate.next_to(step3[0], RIGHT)
        )
        # IMPORTANT ADDITION -----------------------------------------
        
        step3_group2.add(step3[0])
        
        #-------------------------------------------------------------
        self.play(
            FadeOut(step0_group),
            FadeOut(step1),
            FadeOut(step2),
            step3_group2.animate.shift(ORIGIN+1.25*UP),
        )
        #---------------------------
        fin_rect = SurroundingRectangle(step3_group2, buff=0.1)
        self.play(
            ShowCreation(fin_rect),
        )

        
        self.wait(1) # FINAL WAIT TIME
