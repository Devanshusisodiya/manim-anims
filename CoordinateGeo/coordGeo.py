from os import replace
from manim import *
from numpy.core.numeric import base_repr

class DistanceFormula(Scene):
    def construct(self):

        #-------------------------------------------------
        intro_text = MathTex("\\text{Coordinate Geometry}", color=BLUE).shift(ORIGIN)
        self.play(Write(intro_text))
        self.play(FadeOut(intro_text))

        form1 = MathTex("\\text{Distance Formula}").shift(2*UP+4*RIGHT)
        form2 = MathTex("\\text{Section Formula}").next_to(form1, DOWN)
        self.play(Write(VGroup(form1, form2)))
        self.play(FadeOut(form2))
        
        # GRAPHING
        axes = Axes(
            x_range=(-1, 9),
            x_length=7,
            y_range=(-1, 9),
        ).shift(2*LEFT)
        self.play(Create(axes))


        point_A = Dot(axes.c2p(2,2))
        point_A_label = MathTex("(","x_1",",","y_1",")","A").scale(0.7).next_to(point_A, UP+0.001*LEFT)
        point_B = Dot(axes.c2p(7,7))
        point_B_label = MathTex("(","x_2",",","y_2",")","B").scale(0.7).next_to(point_B, UP+RIGHT)
        self.play(
            Write(point_A_label),
            Write(point_B_label),
            Create(point_A),
            Create(point_B)
        )
        
        y1_line = Line(start=axes.c2p(2,0), end=axes.c2p(2,2), color=BLUE) #x1
        x1_line = Line(start=axes.c2p(0,2), end=axes.c2p(2,2), color=BLUE) #y1
        y2_line = Line(start=axes.c2p(7,0), end=axes.c2p(7,7), color=BLUE) #x2
        x2_line = Line(start=axes.c2p(0,7), end=axes.c2p(7,7), color=BLUE) #y2


        x1_copy = x1_line.copy().shift(1.5*DOWN)
        x2_copy = x2_line.copy().shift(4.35*DOWN)
        y2_copy = y2_line.copy().next_to(y2_line, RIGHT)
        y1_copy = y1_line.copy().shift(4*RIGHT)
        


        distance = Line(start=axes.c2p(2,2), end=axes.c2p(7,7))
        dist_label = MathTex("d").next_to(distance.get_center(), UP)

        base = Line(start=axes.c2p(2,2), end=axes.c2p(7,2), color=ORANGE)
        base_label = MathTex("x_2","-","x_1").scale(0.7).next_to(base.get_center(), DOWN)
        perp = Line(start=axes.c2p(7,2), end=axes.c2p(7,7), color=ORANGE)
        perp_label = MathTex("y_2","-","y_1").scale(0.7).next_to(perp.get_center(), RIGHT)

        self.play(
            Create(distance),
            Write(dist_label)
        )
        self.play(
            Indicate(point_A_label[1]),
            ReplacementTransform(point_A_label[1].copy(), x1_line))
        self.play(
            Indicate(point_B_label[1]),
            ReplacementTransform(point_B_label[1].copy(), x2_line))
        self.play(
            Indicate(point_A_label[3]),
            ReplacementTransform(point_A_label[3].copy(), y1_line))
        self.play(
            Indicate(point_B_label[3]),
            ReplacementTransform(point_B_label[3].copy(), y2_line))


        self.play(ReplacementTransform(x2_line.copy(), x2_copy))
        self.play(ReplacementTransform(x1_line.copy(), x1_copy))
         

        self.play(
            Transform(VGroup(x1_copy, x2_copy), base),
            Write(base_label)
        )
        
        self.play(
            Transform(VGroup(y1_copy, y2_copy), perp),
            Write(perp_label)
        )

        self.wait(1)
        # FINAL WAIT TIME