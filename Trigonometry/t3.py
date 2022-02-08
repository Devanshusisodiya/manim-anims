from manim import *
import numpy as np
from scipy.fftpack import shift

class T3(Scene):
    def construct(self):
        # INITIAL WAIT TIME
        # self.wait()

        CUSTORG = 3*RIGHT

        # TRIANGLE SPECIFICS
        triangle = RightAngleTriangle(CUSTORG, CUSTORG + 3*RIGHT, CUSTORG + 2*UP, color=RED).get()
        rangle = RightAngle(triangle[0], triangle[1])
        theta = Angle(triangle[0], triangle[2], radius=0.7, quadrant=(-1,-1), other_angle=True)
        thetaLabel = Tex("$\\theta$").scale(1).shift(theta.get_edge_center(UP) + 0.3*LEFT)
        
        # PERP, BASE AND HYPO LABELS
        perp = Tex("P").scale(0.7).shift(triangle[1].get_center() + 0.2*LEFT)
        base = Tex("B").scale(0.7).shift(triangle[0].get_center() + 0.3*DOWN)
        hypo = Tex("H").scale(0.7).shift(triangle[2].get_center() + 0.5*RIGHT)
        
        # TRIANGLE GROUPS
        tGroup = VGroup(triangle, rangle, theta, thetaLabel, perp, base, hypo)

        # SUB SCENE 1----------------------------------------------------------------------------------
        # INTRO 
        intro = Tex("Trignometric Identities")
        self.play(Write(intro))
        self.play(FadeOut(intro))
        
        # DISPLAYING THE IDENTITIES
        id1 = Tex("$sin^2\\theta + cos^2\\theta = 1$")
        id2 = Tex("$1 + tan^2\\theta = sec^2\\theta$").next_to(id1, DOWN, aligned_edge=LEFT)
        id3 = Tex("$1 + cot^2\\theta = cosec^2\\theta$").next_to(id2, DOWN, aligned_edge=LEFT)

        idGroup = VGroup(id1, id2, id3)
        self.play(Write(idGroup))

        # REMOVE 2ND AND 3RD IDENTITY AND INDENTIFY 1ST
        self.play(
            idGroup[0].animate.shift(3*UL),
            FadeOut(VGroup(idGroup[1], idGroup[2])))


        # PROVING 1ST IDENTITY
        step1 = Tex("$sin^2\\theta + cos^2\\theta$").shift(LEFT + 2*UP)
        step2 = Tex("$= (\\frac{P}{H})^2 + (\\frac{B}{H})^2$").next_to(step1, DOWN, aligned_edge=LEFT)
        step3 = Tex("$= \\frac{P^2}{H^2} + \\frac{B^2}{H^2}$").next_to(step2, DOWN, aligned_edge=LEFT)
        step4 = Tex("$= \\frac{P^2+B^2}{H^2}$").next_to(step3, DOWN, aligned_edge=LEFT)
        step5 = Tex("$= \\frac{H^2}{H^2}$").next_to(step4, DOWN, aligned_edge=LEFT)
        step5Replace = Tex("= 1").next_to(step4, DOWN, aligned_edge=LEFT)

        stepGroup = VGroup(step1, step2, step3, step4, step5,)

        # DISPLAYING THE TRIANGLE AND STEPS
        self.play(Create(tGroup))
        self.play(Write(stepGroup))
        self.play(Transform(stepGroup[-1], step5Replace))   

        # REMOVING FROM THE ScREEN
        self.play(FadeOut(VGroup(
            tGroup,
            stepGroup
        )))

        # SUB SCENE 1 END ------------------------------------------------------------------
        # SUB SCENE 2 ----------------------------------------------------------------------
        # CHANGING IDENTITY
        idGroup[1].shift(3*UL + UP)
        self.play(Transform(idGroup[0], idGroup[1]))

        # PROOF TEXT
        proofText1 = Tex("using identity 1, $sin^2\\theta + cos^2\\theta = 1$").scale(0.7)
        proofText2 = Tex("dividing LHS, RHS by $cos^2\\theta$").scale(0.7).next_to(proofText1, DOWN)
        proof = VGroup(proofText1, proofText2)
        
        self.play(Write(proof))
        self.play(proof.animate.shift(2*UP))

        step1 = Tex("$\\frac{sin^2\\theta + cos^2\\theta}{cos^2\\theta} = \\frac{1}{cos^2\\theta}$")
        step2 = Tex("$ \\frac{sin^2\\theta}{cos^2\\theta} + \\frac{cos^2\\theta}{cos^2\\theta} = sec^2\\theta$").next_to(step1, DOWN ,aligned_edge=LEFT)
        step3 = Tex("$(\\frac{sin\\theta}{cos\\theta})^2 + 1 = sec^2\\theta$").next_to(step2, DOWN ,aligned_edge=LEFT)
        step4 = Tex("$tan^2\\theta + 1 = sec^2\\theta$").next_to(step3, DOWN ,aligned_edge=LEFT)

        stepGroup = VGroup(step1, step2, step3, step4)
        # SOME ANIMATIONS
        self.play(Write(stepGroup[0]))
        self.play(Write(stepGroup[1]))
        self.play(ReplacementTransform(stepGroup[1].copy(), stepGroup[2]))
        self.play(ReplacementTransform(stepGroup[2].copy(), stepGroup[3]))

        self.play(
            FadeOut(proof),
            stepGroup.animate.shift(2*UP)
        )
        self.play(FadeOut(stepGroup))

        # SUB SCENE 2 END -----------------------------------------------------------------------------
        # SUB SCENE 3 ---------------------------------------------------------------------------------
        # CHANGING IDENTITY
        idGroup[2].shift(3*UL + 1.7*UP)
        self.play(Transform(idGroup[0], idGroup[2]))

        # PROOF TEXT
        proofText1 = Tex("using identity 1, $sin^2\\theta + cos^2\\theta = 1$").scale(0.7)
        proofText2 = Tex("dividing LHS, RHS by $sin^2\\theta$").scale(0.7).next_to(proofText1, DOWN)
        proof = VGroup(proofText1, proofText2)
        
        self.play(Write(proof))
        self.play(proof.animate.shift(2*UP))

        step1 = Tex("$ \\frac{sin^2\\theta + cos^2\\theta}{sin^2\\theta} = \\frac{1}{sin^2\\theta}$")
        step2 = Tex("$ \\frac{sin^2\\theta}{sin^2\\theta} + \\frac{cos^2\\theta}{sin^2\\theta} = cosec^2\\theta$").next_to(step1, DOWN ,aligned_edge=LEFT)
        step3 = Tex("$ 1 + (\\frac{cos\\theta}{sin\\theta})^2= cosec^2\\theta$").next_to(step2, DOWN ,aligned_edge=LEFT)
        step4 = Tex("$ 1 + cot^2\\theta = cosec^2\\theta$").next_to(step3, DOWN ,aligned_edge=LEFT)

        stepGroup = VGroup(step1, step2, step3, step4)
        # SOME ANIMATIONS
        self.play(Write(stepGroup[0]))
        self.play(Write(stepGroup[1]))
        self.play(ReplacementTransform(stepGroup[1].copy(), stepGroup[2]))
        self.play(ReplacementTransform(stepGroup[2].copy(), stepGroup[3]))

        self.play(
            FadeOut(proof),
            stepGroup.animate.shift(2*UP)
        )
        self.play(FadeOut(*self.mobjects))


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