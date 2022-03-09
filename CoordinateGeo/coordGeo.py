from os import replace
from turtle import down
from manim import *
from numpy.core.numeric import base_repr

class DF(Scene):
    def construct(self):

        # INTRO -----------------------------------------------------------------------
        intro = MathTex("\\text{Coordinate Geometry}", color=BLUE).shift(ORIGIN)
        self.play(Write(intro))
        self.play(FadeOut(intro))

        # SUB SCENE 1 ------------------------------------------------------------------
        # FORMULAS
        distForm = MathTex("\\text{Distance Formula}").shift(2*UP+4*RIGHT)
        secForm = MathTex("\\text{Section Formula}").next_to(distForm, DOWN)
        self.play(Write(VGroup(distForm, secForm)))
        self.play(FadeOut(secForm))
        
        # GRAPHING 
        axes = Axes(
            x_range=(-1, 9),
            x_length=7,
            y_range=(-1, 9),
        ).shift(2*LEFT)

        self.play(
            Create(axes),
            distForm.animate.scale(0.7).shift(UR))

        # USING MATHTEX BECAUSE ANIM REQUIRES SO
        # SOME DEGREE OF MANIPULATION REQUIRED
        # THESE ARE THE POINTS ON THE GRAPH
        A = Dot(axes.c2p(2,2))
        ALabel = MathTex("(","x_1",",","y_1",")","A").scale(0.7).next_to(A, UP + 0.01*LEFT)
        B = Dot(axes.c2p(7,7))
        BLabel = MathTex("(","x_2",",","y_2",")","B").scale(0.7).next_to(B, UP)
        C = Dot(axes.c2p(7,2))
        CLabel = Tex("$C$").scale(0.7).next_to(C, RIGHT)
        self.play(
            Write(ALabel),
            Write(BLabel),
            Create(A),
            Create(B)
        )
        
        # LINES CONNECTING AXES AND POINTS A, B
        y1_line = Line(start=axes.c2p(2,0), end=axes.c2p(2,2), color=BLUE) #x1
        x1_line = Line(start=axes.c2p(0,2), end=axes.c2p(2,2), color=BLUE) #y1
        y2_line = Line(start=axes.c2p(7,0), end=axes.c2p(7,7), color=BLUE) #x2
        x2_line = Line(start=axes.c2p(0,7), end=axes.c2p(7,7), color=BLUE) #y2

        x1_copy = x1_line.copy().shift(1.5*DOWN)
        x2_copy = x2_line.copy().shift(4.35*DOWN)
        y2_copy = y2_line.copy().next_to(y2_line, RIGHT)
        y1_copy = y1_line.copy().shift(4*RIGHT)
        
        # SOME LABELS
        distance = Line(start=axes.c2p(2,2), end=axes.c2p(7,7))
        distanceLabel = MathTex("d").next_to(distance.get_center(), UP)

        base = Line(start=axes.c2p(2,2), end=axes.c2p(7,2), color=ORANGE)
        baseLabel = MathTex("x_2","-","x_1").scale(0.7).next_to(base.get_center(), DOWN)
        perp = Line(start=axes.c2p(7,2), end=axes.c2p(7,7), color=ORANGE)
        perpLabel = MathTex("y_2","-","y_1").scale(0.7).next_to(perp.get_center(), RIGHT)

        self.play(
            Create(distance),
            Write(distanceLabel))

        # ANIM FOR CREATING LINES
        for i, j in zip([ALabel, BLabel], [x1_line, x2_line]):
            self.play(
                Indicate(i[1]),
                ReplacementTransform(i[1].copy(), j))
        for i, j in zip([ALabel, BLabel], [y1_line, y2_line]):
            self.play(
                Indicate(i[3]),
                ReplacementTransform(i[3].copy(), j))

        # SHOWING DIFFERENCE BETWEEN LINES
        # ONLY SOME OF THIS IS DYNAMIC

        # CREATING BASE LINE
        for i, j in zip([x2_line, x1_line],[x2_copy, x1_copy]):
            self.play(ReplacementTransform(i.copy(), j))
        self.play(
            Transform(VGroup(x1_copy, x2_copy), base),
            Write(baseLabel)
        )

        # CREATING PERPENDICULAR
        for i, j in zip([y2_line, y1_line],[y2_copy, y1_copy]):
            self.play(ReplacementTransform(i.copy(), j))
        self.play(
            Transform(VGroup(y1_copy, y2_copy), perp),
            Write(perpLabel)
        )

        # FINALLY DISPLAYING C
        self.play(
            Write(C),
            Write(CLabel))
        #--------------------------------------------------------------------------------------
        # SUB SCENE 2--------------------------------------------------------------------------
        # WRITING THE FORMULA
        form1 = Tex("Considering $\\triangle$ABC").scale(0.7).shift(4*RIGHT)
        form2 = Tex("$AB^2 = BC^2 + AC^2$").scale(0.7).next_to(form1, DOWN, aligned_edge=LEFT)
        form3 = Tex("$d^2 =$", "$(x_2 - x_1)^2$", "$+$", "$(y_2 - y_1)^2$").scale(0.7).next_to(form2, DOWN, aligned_edge=LEFT)
        form4 = Tex("$d =$", "$\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$").scale(0.7).next_to(form3, DOWN, aligned_edge=LEFT)
        
        formula = VGroup(form1, form2, form3, form4)

        for i in range(2):
            self.play(Write(formula[i]))
        # SOME TRICKS UP ME SLEEVE, HEHE
        self.play(Write(form3[0]))
        self.play(ReplacementTransform(baseLabel.copy(), form3[1]))
        self.play(Write(form3[2]))
        self.play(ReplacementTransform(perpLabel.copy(), form3[-1]))
        #
        self.play(Write(formula[-1]))

        self.wait(1)
        # FINAL WAIT TIME