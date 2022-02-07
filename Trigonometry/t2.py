from manim import *
import numpy as np

class T2(Scene):
    def construct(self):
        # INITIAL WAIT TIME
        # self.wait()

        CUSTORG = ORIGIN

        # UNCOMMENT FOR PRODUCTION RELEASE

        # TRIANGLE SPECIFICS
        triangle = RightAngleTriangle(CUSTORG,CUSTORG + 3*RIGHT, 3*UP, color=RED).get().shift(4.5*LEFT)
        rangle = RightAngle(triangle[0], triangle[1], quadrant=(1,1))
        theta = Angle(triangle[0], triangle[2], quadrant=(-1,-1), other_angle=True)

        # CREATING LABELS 
        A = Tex("$A$").shift(triangle.get_edge_center(UP+LEFT) + 0.3*UP)
        B = Tex("$B$").shift(triangle.get_edge_center(DOWN+LEFT) + 0.3*LEFT)
        C = Tex("$C$").shift(triangle.get_edge_center(DOWN+RIGHT) + 0.3*RIGHT)
        thetaLabel = Tex("$30^{\circ}$").scale(0.7).shift(theta.get_edge_center(UP) + 0.5*LEFT)
        
        # PERP, BASE AND HYPO LABELS
        perp = Tex("Perpendicular").scale(0.7).shift(triangle[1].get_center() + 1.2*LEFT)
        base = Tex("Base").scale(0.7).shift(triangle[0].get_center() + 0.3*DOWN)
        hypo = Tex("Hypotenuse").scale(0.7).shift(triangle[2].get_center() + 1.2*RIGHT)

        tGroup = VGroup(triangle, rangle, theta, A, B, C, thetaLabel)
        sideLabelGroup = VGroup(perp, base, hypo)
                
        self.play(Create(tGroup))
        self.play(Write(sideLabelGroup))

        # COPY OF TRIANGLE TO ENLARGE AND SHRINK
        tGroupCopy = tGroup.copy()
        self.play(FadeIn(tGroupCopy))
        self.play(tGroupCopy.animate.shift(2*DOWN + 6*RIGHT).scale(1.5))
        self.play(tGroupCopy.animate.shift(2*UP).scale(.5))
        self.play(FadeOut(tGroupCopy))

        # TRIGNOMETRIC VALUES
        sine = Tex("sin$30^{\circ}$ = $\\frac{1}{2}$").scale(0.7)
        cosine = Tex("cos$30^{\circ}$ = $\\frac{\sqrt{3}}{2}$").scale(0.7)
        tangent = Tex("tan$30^{\circ}$ = $\\frac{1}{\sqrt{3}}$").scale(0.7)
        cosecant = Tex("cosec$30^{\circ}$ = $2$").scale(0.7)
        secant = Tex("sec$30^{\circ}$ = $\\frac{2}{\sqrt{3}}$").scale(0.7)
        cotangent = Tex("cot$30^{\circ}$ = $\sqrt{3}$").scale(0.7)

        valGroup = VGroup(sine, cosine, tangent, cosecant, secant, cotangent).arrange(DOWN, buff=0.15).shift(3*RIGHT + 2*UP)

        self.play(Write(valGroup))

        # NOW REMOVE EVERYTHING
        self.play(FadeOut(VGroup(*self.mobjects)))

        # CREATING THE TABLE
        # DIFFERENT SET OF VALUES FOR ANIMATION
        valsSine0 = ["0", "1", "2", "3", "4"]
        valsSine1 = ["\\frac{0}{4}", "\\frac{1}{4}", "\\frac{2}{4}", "\\frac{3}{4}", "\\frac{4}{4}"]
        valsSine2 = ["\sqrt{\\frac{0}{4}}", "\sqrt{\\frac{1}{4}}", "\sqrt{\\frac{2}{4}}", "\sqrt{\\frac{3}{4}}", "\sqrt{\\frac{4}{4}}"]
        valsSine3 = ["0", "\\frac{1}{2}", "\\frac{1}{\sqrt{2}}", "\\frac{\sqrt{3}}{2}", "1"]


        t0 = MathTable(
            [valsSine0],
            col_labels=[Tex("$0^{\circ}$"), Tex("$30^{\circ}$"), Tex("$45^{\circ}$"), Tex("$60^{\circ}$"), Tex("$90^{\circ}$")],
            row_labels=[Tex("sin$\\theta$")]
        ).scale(0.7)

        self.play(Create(t0))

        for i in [valsSine1, valsSine2, valsSine3]:
            temp = MathTable(
                [i],
                col_labels = [Tex("$0^{\circ}$"), Tex("$30^{\circ}$"), Tex("$45^{\circ}$"), Tex("$60^{\circ}$"), Tex("$90^{\circ}$")],
                row_labels = [Tex("sin$\\theta$")]
            ).scale(0.7)

            self.play(Transform(t0, temp))

        t1 = MathTable(
            [
                valsSine3,
                ["", "", "", "", ""]
            ],
            col_labels=[Tex("$0^{\circ}$"), Tex("$30^{\circ}$"), Tex("$45^{\circ}$"), Tex("$60^{\circ}$"), Tex("$90^{\circ}$")],
            row_labels=[Tex("sin$\\theta$"), Tex("cos$\\theta$")]
        ).scale(0.7)

        self.play(Transform(t0, t1))

        for i in [
            ["1", "", "", "", ""],
            ["1", "\\frac{\sqrt{3}}{2}", "", "", ""],
            ["1", "\\frac{\sqrt{3}}{2}", "\\frac{1}{\sqrt{2}}", "", ""],
            ["1", "\\frac{\sqrt{3}}{2}", "\\frac{1}{\sqrt{2}}", "\\frac{1}{2}", ""],
            ["1", "\\frac{\sqrt{3}}{2}", "\\frac{1}{\sqrt{2}}", "\\frac{1}{2}", "0"],
        ]:
            temp = MathTable(
                [valsSine3, i],
                col_labels=[Tex("$0^{\circ}$"), Tex("$30^{\circ}$"), Tex("$45^{\circ}$"), Tex("$60^{\circ}$"), Tex("$90^{\circ}$")],
                row_labels=[Tex("sin$\\theta$"), Tex("cos$\\theta$")]
            ).scale(0.7)

            self.play(Transform(t0, temp))
        
        

        # FINAL WAIT TIME
        self.wait()

class RightAngleTriangle(Mobject):
    def __init__(self, p1, p2, p3, color):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.color = color
    def get(self):
        l0 = Line(start=self.p1, end=self.p2, color=self.color)
        l1 = Line(start=self.p1, end=self.p3, color=self.color)
        l2 = Line(start=self.p3, end=self.p2, color=self.color)
        return VGroup(l0, l1, l2)