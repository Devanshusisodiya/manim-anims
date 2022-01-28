from manim import *
import numpy as np

class C1(Scene):
    def construct(self):
        # INITIAL WAIT TIME
        self.wait()

        # INTRO SCENE -------------------------------------------

        introText = Tex("Let's introduce Circles").shift(ORIGIN)
        self.play(Write(introText))
        self.play(FadeOut(introText))

        # SUB SCENE 1 ---------------------------------------------------

        # CREATING DOTS FOR THE CIRCLE
        # DISPLAYING THEM AND DRAWING A CIRCLE OVER IT
        # FINALLY WILL REMOVE THE DOTS
        # AND DRAW A CIRCLE OVER IT

        CUSTORG = 2*LEFT

        dotGroup = VGroup()
        circleOrigin = Dot(CUSTORG)
        originLabel = MathTex("O").next_to(circleOrigin, buff=SMALL_BUFF)

        self.play(Create(VGroup(
            circleOrigin,
            originLabel
        )))
        for i in [30, 60, 90, 120, 150, 180]:
            l = Line(start=CUSTORG + LEFT, end=CUSTORG + RIGHT).rotate(i*DEGREES)
            d1 = Dot(point=l.get_start())
            d2 = Dot(point=l.get_end())
            dotGroup.add(d1)
            dotGroup.add(d2)
            self.play(
                Create(d1),
                Create(d2)
            )

        dotCircle = Circle(color=WHITE, arc_center=CUSTORG)
        self.play(Create(dotCircle))
        self.play(FadeOut(dotGroup))

        # SUB SCENE 2 --------------------------------------

        # JUST A BIGGER CIRCLE
        # HERE THE DESCRIPTION OF RADIUS AND CIRCUMFERENCE 
        # IS GIVEN
        bigCircle = Circle(radius=1.5, arc_center=CUSTORG)
        radius = Line(start=CUSTORG + ORIGIN, end=CUSTORG + 1.5*DOWN)

        self.play(ReplacementTransform(dotCircle, bigCircle))
        self.play(Create(radius))

        # TRANSFORMING RADIUS INTO ITS LABEL 
        # AND CIRCUMFERENCE INTO ITS LABEL
        radiusLabel = Tex("Radius").shift(CUSTORG + 2*RIGHT + 3*UP)
        circumLabel = Tex("Circumference").shift(CUSTORG + 2*RIGHT + 2*UP)
        self.play(ReplacementTransform(radius.copy(), radiusLabel))
        self.play(ReplacementTransform(bigCircle.copy(), circumLabel))

        # END SUB SCENE BY REMOVING MOBJECTS FROM THE SCREEN
        self.play(FadeOut(VGroup(
            bigCircle,
            radius,
            radiusLabel,
            circumLabel,
            circleOrigin,
            originLabel
        )))
        

        # SUB SCENE 2 --------------------------------------------------------

        bigCircle = Circle(radius=2, arc_center=CUSTORG)
        tangent = TangentLine(bigCircle, alpha=0.75, length=5)
        startLabel = MathTex("A").shift(tangent.get_start() + 0.5*LEFT)
        endLabel = MathTex("B").shift(tangent.get_end() + 0.5*RIGHT)
        tangentGroup = VGroup(tangent, startLabel, endLabel) # JUST CREATING A GROUP TO CONTROL TANGENT AND ITS LABELS AT ONCE

        # TANGENT CENTER WHEN IT IS DOWN
        tangCenterDown = tangent.get_center()

        self.play(
            Create(bigCircle), 
            Create(tangentGroup),
            Create(circleOrigin),
            Write(originLabel)
        )
        self.play(tangentGroup.animate.shift(0.5*UP))

        # TANGENT CENTER AND CUT LABELS WHEN IT IS UP
        tangCenterUp = tangent.get_center()
        leftCutLabel = MathTex("R").shift(tangCenterUp + 1.5*LEFT + 0.2*DOWN).scale(0.7)
        rightCutLabel = MathTex("S").shift(tangCenterUp + 1.5*RIGHT + 0.2*DOWN).scale(0.7)
        
        # GETTING THE TANGENT CENTER WHEN IT IS DOWN
        pointLabel = MathTex("P").shift(tangCenterDown + 0.5*DOWN).scale(0.7)

        self.play(Write(VGroup(leftCutLabel, rightCutLabel)))
        self.play(
            tangentGroup.animate.shift(0.5*DOWN),
            ReplacementTransform(
                VGroup(leftCutLabel, rightCutLabel), pointLabel)
        ) 

        points = tangent.get_points()
        dividedPoints = [np.array(points[0])]

        # DOTS ON THE TANGENT LINE
        pointsGroup = VGroup()

        for i in range(1,len(points)):
            el = np.array(points[i])
            temp = (dividedPoints[-1] + el) / 2
            dividedPoints.append(temp)
            dividedPoints.append(el)

        for i in dividedPoints:
            dot = Dot(i, radius=DEFAULT_SMALL_DOT_RADIUS, color=RED)
            pointsGroup.add(dot)

        pointsOnScreen = VGroup()
        for i in range(len(pointsGroup) // 2 + 1):
            pointsOnScreen.add(pointsGroup[i])
        
        self.play(Create(pointsOnScreen))


        h = {}
        ctr = 3
        for dot in pointsOnScreen:
            line = Line(start=dot.get_center(), end=CUSTORG)
            if ctr == 0:
                h[line] = MathTex("P").scale(0.7).shift(dot.get_center() + 0.5 * DOWN)
            else:
                h[line] = MathTex("P{}".format(ctr)).scale(0.7).shift(dot.get_center() + 0.5 * DOWN)
            ctr -= 1


        radiiOnScreen = VGroup()
        radiiLabels = VGroup()
        for i in h:
            radiiOnScreen.add(i)
            radiiLabels.add(h[i])
            self.play(
                Create(i),
                Write(h[i])
            )
            self.wait()

        # FADING OUT THE ALREADY ON SCREEN TANGENT LABEL
        self.play(FadeOut(pointLabel))

        # INDICATING RADIUS BEING THE SMALLEST
        for i in range(len(radiiOnScreen)):
            if i == len(radiiOnScreen)-1:
                self.play(radiiOnScreen[i].animate.set_color(RED))
            else:
                self.play(radiiOnScreen[i].animate.set_color(YELLOW))

        # SUPPORTING TEXT
        supText1 = Tex("Shortest distance between").scale(0.7).shift(3*UP + 2*RIGHT)
        supText2 = Tex("a point and a line is $\perp$ to the line").scale(0.7).next_to(supText1, DOWN)
        supText3 = Tex("$\Rightarrow$ OP $\perp$ AB").scale(0.7).next_to(supText2, DOWN)
        self.play(Write(VGroup(supText1, supText2, supText3)))

        # REMOVING ALL RADII EXCEPT TRUE RADIUS
        self.play(
            FadeOut(radiiOnScreen[:len(radiiOnScreen)-1]),
            FadeOut(radiiLabels[:len(radiiLabels)-1]),
            FadeOut(pointsOnScreen),
            radiiOnScreen[-1].animate.set_color(WHITE)
        )

        # ADDING ANGLE
        rangle = RightAngle(radiiOnScreen[-1], tangent, quadrant=(1,1))
        self.play(Create(rangle))

        # FINAL WAIT TIME
        self.wait() 