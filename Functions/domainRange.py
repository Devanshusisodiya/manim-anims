import numpy as np 
from manim import *


class DomainRange(Scene):
    def construct(self):
        self.wait(1) #INTITIAL WAIT TIME

        # SETTING UP OF THE SCENE -----------------------------------------------------

        function = Tex(r'f(',r'x',r')',r'=',r'x^2',r'+5')
        function_rep = Tex(r'f(',r'x',r')',r'=',r'x^2',r'+5')

        
        setA = Ellipse(arc_center=ORIGIN+0.4*LEFT, height=4, width=2, color=BLUE)
        setA.shift(ORIGIN+3*LEFT)
        setA_text = Tex('Set A')
        setA_text.next_to(setA, UP)

        setB = Ellipse(height=5, width=2, color=BLUE)
        setB.shift(ORIGIN+3*RIGHT)
        setB_text = Tex('Set B')
        setB_text.next_to(setB, UP)

        self.play(
            Write(function),
        )

        domain = [Integer(1),Integer(2),Integer(3),Integer(4)]
        codomain = [Tex(r'1^2'),Tex(r'2^2'),Tex(r'3^2')]
        codomain_set_func_dis = [r'6',r'9',r'14']
        codomain_set = [Integer(6),Integer(9),Integer(14),Integer(20),Integer(25)]

        for ind in range(3):
            func_in = domain[ind]
            func_sq = codomain[ind]
            func_res = codomain_set_func_dis[ind]
            func_in.shift(function[1].get_center())
            func_sq.shift(function[4].get_center()) 

            function_cont = Tex(r'=',func_res)
            function_cont.next_to(function, RIGHT)
              
            # INNER ANIMATIONS --------------------------------------------------------------

            self.play(
                Transform(function[1], func_in),
                Transform(function[4], func_sq),
                Write(function_cont)
            )
            self.wait(1)
            self.play(
                FadeOut(function_cont)
            )


        pos_domain = [ORIGIN+UP, ORIGIN, ORIGIN+DOWN]
        pos_codomain = [ORIGIN+2*UP, ORIGIN+UP, ORIGIN, ORIGIN+DOWN, ORIGIN+2*DOWN]
        for i in range(len(pos_domain)):
            domain[i].shift(pos_domain[i])
        for i in range(len(pos_codomain)):
            codomain_set[i].shift(pos_codomain[i])


        domain_group = VGroup(domain[0], domain[1], domain[2])
        domain_group.shift(2.5*LEFT)
        codomain_group = VGroup(codomain_set[0], codomain_set[1], codomain_set[2], codomain_set[3], codomain_set[4])
        codomain_group.shift(3*RIGHT)

        # ANIMATIONS -------------------------------------------------------------------
        self.play(
            FadeOut(function_cont),
            Transform(function, function_rep),
        )
        self.wait(1)
        self.play(
            function.animate.move_to(ORIGIN+3*UP)
        )
        self.play(
            Write(setA_text),
            Write(setB_text),
            Create(setA),
            Create(setB),
        )
        self.play(
            Write(domain_group),
            Write(codomain_group),
        )
        
        arrow1 = always_redraw(lambda: Arrow(start=domain_group[0].get_center(), end=codomain_group[0].get_center()))
        arrow2 = always_redraw(lambda: Arrow(start=domain_group[1].get_center(), end=codomain_group[1].get_center()))
        arrow3 = always_redraw(lambda: Arrow(start=domain_group[2].get_center(), end=codomain_group[2].get_center()))

        self.play(
            Create(arrow1),
            Create(arrow2),
            Create(arrow3),
        )
        self.play(domain_group.animate.shift(0.5*UP))
        
        domain[3].next_to(domain_group, 2*DOWN)
        
        self.play(
            Write(domain[3])
        )
        self.play(
            Indicate(domain[3])
        )

        arrow4 = always_redraw(lambda: Arrow(start=domain[3].get_center(), end=codomain_group[0].get_center()))
        arrow_arr = [Arrow(start=domain[3].get_center(), end=codomain_group[i].get_center()) for i in [4,1,3,2]]


        self.play(
            Create(arrow4),
        )

        for i in arrow_arr:
            arrow_ch = always_redraw(lambda : i)
            self.play(
                ReplacementTransform(arrow4, arrow_ch, lag_ratio=0)
            )
            arrow4 = arrow_ch
            # self.wait(0.5)
        self.play(
            FadeOut(arrow4),
        )

        self.wait(1)# FINAL WAIT TIME

class FunctionDefinition(Scene):
    def construct(self):
        
        self.wait(1) #INITIAL WAIT TIME

        # SETUP OF THE SCENE ----------------------------------------------------
        setA = Ellipse(arc_center=ORIGIN, height=4, width=2, color=BLUE)
        setA_text = Tex('Set A')
        setA_text.next_to(setA, UP)

        setB = Ellipse(arc_center=ORIGIN, height=4, width=2, color=BLUE)
        setB_text = Tex('Set B')
        setB_text.next_to(setB, UP)

        
        #values in domain
        a = Integer(1)
        b = Integer(2)
        c = Integer(3)

        g = Integer(4)

        #values in codomain
        d = Integer(6)
        e = Integer(9)
        f = Integer(14)
        h = Integer(20)
        i = Integer(25)


        #positioning the values
        a.shift(1*UP)
        b.shift(ORIGIN)
        c.shift(1*DOWN)
        
        d.shift(2*UP)
        e.shift(1*UP)
        f.shift(ORIGIN)
        h.shift(1*DOWN)
        i.shift(2*DOWN)


        shifting_values = VGroup(a, b, c)

        domain = VGroup(setA_text, setA, shifting_values) #defining domain vector group
        codomain = VGroup(setB_text, setB, d, e ,f, h, i)#defining codomain vector group
        #-------------------------------------------------------------------------
        # ANIMATIONS -------------------------------------------------------------
        self.play(
            GrowFromCenter(setA),
        )
        self.play(
            Write(a),
            Write(b),
            Write(c),
            Write(setA_text),
        )
        self.play(domain.animate.shift(2.5*LEFT))
        self.wait(1)    
        self.play(
            GrowFromCenter(setB)
        )
        self.play(
            Write(d),
            Write(e),
            Write(f),
            Write(h),
            Write(i),
            Write(setB_text),
        )
        self.play(codomain.animate.shift(2*RIGHT))
        
        arrow1 = always_redraw(lambda: Arrow(start=a.get_center(), end=d.get_center()))
        arrow2 = always_redraw(lambda: Arrow(start=b.get_center(), end=e.get_center()))
        arrow3 = always_redraw(lambda: Arrow(start=c.get_center(), end=f.get_center()))

        self.play(
            Create(arrow1),
            Create(arrow2),
            Create(arrow3),
        )

        self.play(shifting_values.animate.shift(0.5*UP))                           

        #--------------------------------------------------------------------------
        #definition of mapping arrows is done later so as to accurately position them 



        g.next_to(shifting_values, 2*DOWN)
        self.play(Write(g))
        self.play(Indicate(g))

        arrow4 = always_redraw(lambda: Arrow(start=g.get_center(), end=d.get_center()))
        arrow4_ch = always_redraw(lambda: Arrow(start=g.get_center(), end=e.get_center()))
        arrow4_ch2 = always_redraw(lambda: Arrow(start=g.get_center(), end=f.get_center()))

        self.play(
            Create(arrow4),
        )
        self.play(
            ReplacementTransform(arrow4, arrow4_ch)
        )
        self.play(
            ReplacementTransform(arrow4_ch, arrow4_ch2)
        )        
        self.play(FadeOut(arrow4_ch2))

        self.wait(2) #FINAL WAIT TIME