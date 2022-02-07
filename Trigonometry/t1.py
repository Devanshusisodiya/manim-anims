from manim import *
import numpy as np

class T1(Scene):
    def construct(self):
        
        # INITIAL WAIT TIME
        self.wait()

        CUSTORG = ORIGIN

        # TRIANGLE SPECIFICS
        triangle = RightAngleTriangle(CUSTORG,CUSTORG + 3*RIGHT, 3*UP, color=RED).get().shift(4.5*LEFT)
        rangle = RightAngle(triangle[0], triangle[1], quadrant=(1,1))
        phi = Angle(triangle[1], triangle[2], quadrant=(-1,1))
        theta = Angle(triangle[0], triangle[2], quadrant=(-1,-1), other_angle=True)

        # CREATING LABELS 
        A = Tex("$A$").shift(triangle.get_edge_center(UP+LEFT) + 0.3*UP)
        B = Tex("$B$").shift(triangle.get_edge_center(DOWN+LEFT) + 0.3*LEFT)
        C = Tex("$C$").shift(triangle.get_edge_center(DOWN+RIGHT) + 0.3*RIGHT)
        phiLabel = Tex("$\phi$").shift(phi.get_edge_center(DOWN) + 0.3*DOWN + 0.1*RIGHT)
        thetaLabel = Tex("$\\theta$").shift(theta.get_edge_center(UP) + 0.3*LEFT)
        
        # PERP, BASE AND HYPO LABELS
        perpT = Tex("Perpendicular").scale(0.7).shift(triangle[1].get_center() + 1.2*LEFT)
        baseT = Tex("Base").scale(0.7).shift(triangle[0].get_center() + 0.3*DOWN)
        hypoT = Tex("Hypotenuse").scale(0.7).shift(triangle[2].get_center() + 1.2*RIGHT)
        
        perpP = Tex("Perpendicular").scale(0.7).shift(triangle[0].get_center() + 0.3*DOWN)
        baseP = Tex("Base").scale(0.7).shift(triangle[1].get_center() + 1.2*LEFT)
        hypoP = Tex("Hypotenuse").scale(0.7).shift(triangle[2].get_center() + 1.2*RIGHT)

        # GROUPS TO HANDLE MOBJECTS
        angleLabelGroup = VGroup(phiLabel, thetaLabel)
        sideLabelGroupTheta = VGroup(perpT, baseT, hypoT)
        sideLabelGroupPhi = VGroup(baseP, perpP, hypoP)
        tGroup = VGroup(triangle, rangle, theta, phi, A, B, C, phiLabel, thetaLabel)

        self.play(Create(tGroup))

        # SUPPORTING TEXT AND ANIMS 

        supText1 = Tex("Using angle sum property").scale(0.7).shift(3*UP + 3*RIGHT)
        supText2 = Tex("$\\angle ABC$ + $\\angle BCA$ + $\\angle CAB$ = $180^{\circ}$").scale(0.7).next_to(supText1, DOWN)
        supText3 = Tex("$\Rightarrow$", "$90^{\circ}$", " + ", "$\\theta$ + $\phi$ =", "$180^{\circ}$").scale(0.7).next_to(supText2, DOWN)
        supText4 = Tex("$\\theta$ + $\phi$ = ","$180^{\circ}$ - $90^{\circ}$").scale(0.7).next_to(supText3, DOWN)
        supText5 = Tex("$\\theta$ + $\phi$ = $90^{\circ}$").scale(0.7).next_to(supText4, DOWN)
        supText6 = Tex("$\\therefore$ $\\theta$ and $\phi$ are complementary").scale(0.7).next_to(supText5, DOWN)

        supText = VGroup(supText1, supText2, supText3, supText4)

        # WRITING 3 EQUATIONS
        for i in range(len(supText)-1):
            self.play(Write(supText[i]))
        
        # SOME TRICKS UP ME SLEEVE HEHE
        self.play(ReplacementTransform(supText3[3].copy(), supText4[0]))
        self.play(ReplacementTransform(VGroup(supText3[1].copy(), supText3[-1].copy()), supText4[1]))
        supText.add(supText5, supText6)
        self.play(Write(supText[-2]))
        self.play(Write(supText[-1]))

        # CONSIDERATION OF THETA
        
        considerLabel = Tex("considering ","$\\theta$").set_color(BLUE).shift(2*UP)
        cBackground = BackgroundRectangle(considerLabel, fill_opacity=0.8, buff=0.6)

        self.play(
            Create(cBackground),
            Write(considerLabel)
        )
        self.play(FadeOut(VGroup(cBackground, considerLabel)))
        
        # SHOWING PERP AND BASE FOR THETA
        self.play(ReplacementTransform(thetaLabel.copy(), sideLabelGroupTheta[0]))
        self.play(ReplacementTransform(thetaLabel.copy(), sideLabelGroupTheta[1]))
        self.play(Write(sideLabelGroupTheta[2]))

        sine = Tex("sin$\\theta$ = $\\frac{AB}{AC}$", "$\ldots$ 1").scale(0.7).shift(DOWN + 3*LEFT)
        cosine = Tex("cos$\phi$ = $\\frac{AB}{AC}$", "$\ldots$ 2").scale(0.7).next_to(sine, DOWN)
        
        self.play(Write(sine))
        self.play(FadeOut(sideLabelGroupTheta))
        
        # SHOWING PERP AND BASE FOR PHI

        considerLabel = Tex("considering ","$\phi$").set_color(BLUE).shift(2*UP)
        self.play(
            Create(cBackground),
            Write(considerLabel)
        )
        self.play(FadeOut(VGroup(cBackground, considerLabel)))

        self.play(ReplacementTransform(phiLabel.copy(), sideLabelGroupPhi[0]))
        self.play(ReplacementTransform(phiLabel.copy(), sideLabelGroupPhi[1]))
        self.play(Write(sideLabelGroupPhi[2]))

        self.play(Write(cosine))
        self.play(FadeOut(sideLabelGroupPhi))

        # CONCLUSION
        conc1 = Tex("from 1 and 2").scale(0.7).next_to(cosine, DOWN)
        conc2 = Tex("sin$\\theta$ = cos$\phi$").scale(0.7).next_to(conc1, DOWN)
        conc3 = Tex("sin$\\theta$ = cos($90-\\theta$)").scale(0.7).next_to(conc2, DOWN)

        conc = VGroup(conc1, conc2, conc3)
        concOnScreen = VGroup(sine, cosine)
        for i in range(len(conc)):
            if i == len(conc) - 1:
                self.play(Write(conc[i]))
            else:
                concOnScreen.add(conc[i])
                self.play(Write(conc[i]))
        
        self.play(
            FadeOut(concOnScreen),
            conc3.animate.next_to(triangle[0], DOWN)
        )

        # REST OF THE FORMULAS
        considerLabel = Tex("Similarly").set_color(BLUE).shift(2*UP)
        self.play(
            Create(cBackground),
            Write(considerLabel)
        )
        self.play(FadeOut(VGroup(cBackground, considerLabel)))
        
        conc4 = Tex("cos$\\theta$ = sin($90-\\theta$)").scale(0.7).next_to(conc3, DOWN)
        conc5 = Tex("tan$\\theta$ = cot($90-\\theta$)").scale(0.7).next_to(conc4, DOWN)
        conc6 = Tex("cot$\\theta$ = tan($90-\\theta$)").scale(0.7).next_to(conc5, DOWN)
        conc7 = Tex("sec$\\theta$ = cosec($90-\\theta$)").scale(0.7).next_to(conc6, DOWN)
        conc8 = Tex("cosec$\\theta$ = sec($90-\\theta$)").scale(0.7).next_to(conc7, DOWN)

        self.play(
            Write(VGroup(conc4,conc5,conc6,conc7,conc8))
        )

        # MOVING FORMULAS
        self.play(
            FadeOut(supText),
            VGroup(conc3, conc4, conc5, conc6, conc7, conc8).animate.shift(3.5*UP + 6*RIGHT)
        )

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
