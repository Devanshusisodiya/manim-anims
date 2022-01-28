from manim import *
import numpy as np

class C2(Scene):
    def construct(self):
        # INITIAL WAIT TIME
        self.wait()
        
        # CUSTOM ORIGIN
        CUSTORG = 3*LEFT
        STROKE = 2

        circle = Circle(radius=3, arc_center=CUSTORG, stroke_width=STROKE)
        center = Dot(CUSTORG)

        tangent1 = TangentLine(circle, length=4, alpha=0, stroke_width=1)
        tangent2 = TangentLine(circle, length=4, alpha=0.01, stroke_width=1)
        self.add(circle, tangent1, tangent2, center)

        point = tangent1.get_center()

        radius = Line(start=center, end=point, stroke_width=STROKE)

        rangle1 = RightAngle(radius, tangent1, quadrant=(-1,1), length=1.2)
        rangle2 = RightAngle(radius, tangent2, quadrant=(-1,1), length=1)


        self.add(radius, rangle1, rangle2)
        




        # FINAL WAIT TIME
        self.wait()