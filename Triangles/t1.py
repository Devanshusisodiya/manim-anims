from tokenize import cookie_re
from manim import *
import numpy as np

class T1(Scene):
    def construct(self):

        self.wait(1)
        # INITIAL WAIT TIME
        
        A = 2*LEFT
        B = 4*RIGHT
        C = 3*UP


        # LITTLE TRIANGLE FOR BASE AND PERPENDICULAR DEMO
        # YOU MIGHT WANNA RESIZE USING COORDINATES WHICH ARE LESS FAR OFF

        demoTriangle = CustomTriangle(3*LEFT, ORIGIN, 3*UP+RIGHT, color1=BLUE, color2=RED, color3=YELLOW).getTriangleGroup()
        dottedBase = DashedLine(ORIGIN, ORIGIN + RIGHT)
        dottedPerp = DashedLine(ORIGIN + RIGHT, 3*UP + RIGHT)

        angle = RightAngle(dottedBase, dottedPerp, length=0.3, quadrant=(-1,1))

        # angle = Angle(demoTriangle[0], demoTriangle[1], radius=0.4, other_angle=False, quadrant=(-1,1))

        self.play(Create(demoTriangle))
        self.play(Create(dottedBase))
        self.play(Create(dottedPerp))
        self.play(Create(angle))


        self.wait(1)
        # FINAL WAIT TIME


class CustomTriangle(Mobject):
    def __init__(self, p1, p2, p3, color1, color2, color3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
    
    def getTriangleGroup(self):
    
        l1 = Line(
            start = np.array(self.p1),
            end = np.array(self.p2),
            color = self.color1
        )
        l2 = Line(
            start = np.array(self.p2),
            end = np.array(self.p3),
            color = self.color2
        )
        l3 = Line(
            start = np.array(self.p3),
            end = np.array(self.p1),
            color = self.color3
        )
        tGroup = VGroup(l1, l2, l3)

        return tGroup
