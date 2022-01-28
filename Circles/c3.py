from manim import *
import numpy as np

class C3(Scene):
    def construct(self):

        # INITIAL WAIT TIME
        self.wait()

        # INTRO SCENE ---------------------------------------------------------
        intro1 = Tex("Let's understand a bit more")
        intro2 = Tex("about Tangents").next_to(intro1, DOWN)

        self.play(Write(intro1), Write(intro2))
        self.play(FadeOut(VGroup(intro1, intro2)))

        # SUB SCENE 1 ---------------------------------------------------------
        # CUSTOM ORIGIN 
        CUSTORG = 2*LEFT

        center = Dot(CUSTORG)
        centerLabel = Tex("$O$").next_to(center, RIGHT)

        # CIRCLE AND THE FULL TANGENTS
        circle = Circle(radius=2, arc_center=CUSTORG)
        ftangent1 = TangentLine(circle, alpha=0.333, length=7) # LITTLE BIT OF 
        ftangent2 = TangentLine(circle, alpha=0.667, length=7) # HIT AND TRIAL FOR THE ALIGNMENT OF THE TANGENTS

        # ALL THE NECESSARY POINTS EXCEPT THE CENTER
        pointP = Dot(ftangent1.get_end())
        pointQ = Dot(ftangent1.get_center(), color=YELLOW, radius=0.06)
        pointR = Dot(ftangent2.get_center(), color=YELLOW, radius=0.06)
        pointPLabel = Tex("$P$").next_to(pointP, LEFT)
        pointQLabel = Tex("$Q$").next_to(pointQ, UP)
        pointRLabel = Tex("$R$").next_to(pointR, DOWN)

        # CREATING HALF TANGENTS
        htangent1 = Line(start=pointP, end=pointQ)
        htangent2 = Line(start=pointP, end=pointR)

        # CONSTRUCTIONS
        lineOQ = Line(start=center, end=pointQ)
        lineOR = Line(start=center, end=pointR)
        lineOP = Line(start=center, end=pointP)
        rangle1 = RightAngle(lineOQ, htangent1, quadrant=(-1,-1))
        rangle2 = RightAngle(lineOR, htangent2, quadrant=(-1,-1))

        self.play(
            Create(VGroup(circle, center)),
            Write(centerLabel)
        )
        self.play(
            Create(pointP),
            Write(pointPLabel)
        )
        self.play(
            Create(htangent1),
            Create(htangent2),
            Create(pointQ),
            Create(pointR),
            Write(pointQLabel),
            Write(pointRLabel)
        )
        self.play(Indicate(htangent1))
        self.play(Indicate(htangent2))

        # SUPPORTING TEXT
        theorem1 = Tex("The two tangents drawn to a circle")
        theorem2 = Tex("from an external point are equal in length").next_to(theorem1, DOWN)
        theorem = VGroup(theorem1, theorem2)
        tbackground = BackgroundRectangle(theorem, fill_opacity=0.8, buff=0.1)

        self.play(
            Create(tbackground),
            Write(theorem)
        )
        self.play(FadeOut(VGroup(tbackground, theorem)))


        toProve = Tex("to prove: PQ=PR").scale(0.7).shift(3*UP + 2*RIGHT)
        construction = Tex("construction: join OQ, OR and OP").scale(0.7).next_to(toProve, DOWN)
        
        proof1 = Tex("proof: consider $\\triangle$OPQ and $\\triangle$OPR").scale(0.7).shift(1.5*UP + 3.5*RIGHT)
        proof2 = Tex("OP=OP (common)").scale(0.7).next_to(proof1, DOWN)
        proof3 = Tex("OQ=OR (radii)").scale(0.7).next_to(proof2, DOWN)
        proof4 = Tex("$\\angle$OQP = $\\angle$ORP = $90^{\circ}$").scale(0.7).next_to(proof3, DOWN)
        proof = VGroup(proof1, proof2, proof3, proof4)

        self.play(Write(toProve))
        self.play(Write(construction))

        # CONSTRUCTING
        self.play(
            Create(lineOQ),
            Create(lineOR) ,
            Create(lineOP),
            Create(rangle1),
            Create(rangle2)
        )

        # WRITING PROOF
        for i in proof:
            self.play(Write(i))

        self.play(
            FadeOut(VGroup(toProve, construction)),
            proof.animate.shift(1.5*UP)
        )

        conc1 = Tex("$\\therefore \\triangle$OPQ $\cong$ $\\triangle$OPR").scale(0.7).next_to(proof4, 2*DOWN)
        conc2 = Tex("$\Rightarrow$ PQ=PR (C.P.C.T.)").scale(0.7).next_to(conc1, DOWN)
        concRect = SurroundingRectangle(conc2)

        self.play(Write(conc1))
        self.play(Write(conc2))
        self.play(Create(concRect))

        # FINAL WAIT TIME
        self.wait()