from manim import *
import  numpy as np


class OneOneFunctions(Scene):
    def construct(self):
        
        self.wait(1) #INITIAL WAIT TIME

        # SETUP OF THE SCENE ----------------------------------------------------
        ellipse1 = Ellipse(arc_center=ORIGIN, height=4, width=2, color=BLUE) #ellipse of domain
        ellipse2 = Ellipse(arc_center=ORIGIN+RIGHT, height=4, width=2, color=BLUE) #ellipse of codomain
        domain_label = TextMobject("Domain").next_to(ellipse1, UP)
        codomain_label = TextMobject("Codomain").next_to(ellipse2, UP)
        
        #function description
        function_label = TextMobject("A ","One One Function")
        function_label[1].set_color(BLUE)
        function_label.shift(3*DOWN)

        #values in domain
        a = Integer(5)
        b = Integer(6)
        c = Integer(2)

        #values in codomain
        d = Integer(3)
        e = Integer(7)
        f = Integer(9)


        #positioning the values
        a.shift(1*UP)
        b.shift(ORIGIN)
        c.shift(1*DOWN)
        d.shift(1*UP+RIGHT)
        e.shift(ORIGIN+RIGHT)
        f.shift(1*DOWN+RIGHT)


        domain = VGroup(domain_label, ellipse1, a, b, c) #defining domain vector group
        codomain = VGroup(codomain_label, ellipse2, d, e, f)#defining codomain vector group
        #-------------------------------------------------------------------------
        # ANIMATIONS -------------------------------------------------------------
        self.play(
            GrowFromCenter(ellipse1),
        )
        self.play(
            Write(a),
            Write(b),
            Write(c),
            Write(domain_label)
        )
        self.play(domain.animate.shift(2.5*LEFT))

        self.wait(1)    

        self.play(
            GrowFromCenter(ellipse2)
        )
        self.play(
            Write(d),
            Write(e),
            Write(f),
            Write(codomain_label)
        )
        self.play(codomain.animate.shift(2*RIGHT))
        #--------------------------------------------------------------------------
        # definition of mapping arrows is done later so as to accurately position them 

        #creating mapping arrows to values in domain and codomain
        arrow1 = always_redraw(lambda: 
                                Arrow(start=a.get_center(), end=d.get_center()))
        arrow2 = always_redraw(lambda:
                                Arrow(start=b.get_center(), end=e.get_center()))
        arrow3 = always_redraw(lambda: 
                                Arrow(start=c.get_center(), end=f.get_center()))
        
        #--------------------------------------------------------------------------
        self.play(
            ShowCreation(arrow1),
            ShowCreation(arrow2),
            ShowCreation(arrow3)
        )
        self.add(arrow1, arrow2, arrow3)
        self.play(
            Write(function_label)
        )
        self.wait(1)
        #---------------------------------------------------------------------------
        # changing arrows to different values

        arrow1_ch = always_redraw(lambda: 
                                Arrow(a.get_center(), e.get_center()))
        arrow2_ch = always_redraw(lambda: 
                                Arrow(b.get_center(), d.get_center()))

        #-------------------------------------------------------------------
        self.play(
            ReplacementTransform(arrow1, arrow1_ch),
            ReplacementTransform(arrow2, arrow2_ch)
        )

        arrow1_ch2 = always_redraw(lambda: 
                                Arrow(a.get_center(), f.get_center()))
        arrow3_ch = always_redraw(lambda: 
                                Arrow(c.get_center(), e.get_center()))
        
        self.play(
            ReplacementTransform(arrow3, arrow3_ch),
            ReplacementTransform(arrow1_ch, arrow1_ch2)
        )

        #initial arrows ---------------------------------------------------
        arrow1_init = always_redraw(lambda: 
                                Arrow(a.get_center(), d.get_center()))
        arrow2_init = always_redraw(lambda: 
                                Arrow(b.get_center(), e.get_center()))
        arrow3_init = always_redraw(lambda: 
                                Arrow(c.get_center(), f.get_center()))

        self.play(
            ReplacementTransform(arrow1_ch2, arrow1_init),
            ReplacementTransform(arrow2_ch, arrow2_init),
            ReplacementTransform(arrow3_ch, arrow3_init)
        )

        self.wait(2) #FINAL WAIT TIME

class OntoFunctions(Scene):
    def construct(self):
        
        self.wait(1) #INITIAL WAIT TIME

        # SETUP OF THE SCENE ----------------------------------------------------
        ellipse1 = Ellipse(arc_center=ORIGIN, height=4, width=2, color=BLUE) #ellipse of domain
        ellipse2 = Ellipse(arc_center=ORIGIN+RIGHT, height=4, width=2, color=BLUE) #ellipse of codomain
        domain_label = TextMobject("Domain").next_to(ellipse1, UP)
        codomain_label = TextMobject("Codomain").next_to(ellipse2, UP)
        
        #function description
        function_label = TextMobject("An ","Onto Function")
        function_label[1].set_color(BLUE)
        function_label.shift(3*DOWN)

        #values in domain
        a = Integer(5)
        b = Integer(6)
        c = Integer(2)

        #values in codomain
        d = Integer(3)
        e = Integer(7)
        f = Integer(9)

        g = Integer(10)

        #positioning the values
        a.shift(1*UP)
        b.shift(ORIGIN)
        c.shift(1*DOWN)
        d.shift(1*UP+RIGHT)
        e.shift(ORIGIN+RIGHT)
        f.shift(1*DOWN+RIGHT)


        shifting_values = VGroup(d, e, f)

        domain = VGroup(domain_label, ellipse1, a, b, c) #defining domain vector group
        codomain = VGroup(codomain_label, ellipse2, shifting_values)#defining codomain vector group
        #-------------------------------------------------------------------------
        # ANIMATIONS -------------------------------------------------------------
        self.play(
            GrowFromCenter(ellipse1),
        )
        self.play(
            Write(a),
            Write(b),
            Write(c),
            Write(domain_label)
        )
        self.play(domain.animate.shift(2.5*LEFT))

        self.wait(1)    

        self.play(
            GrowFromCenter(ellipse2)
        )
        self.play(
            Write(d),
            Write(e),
            Write(f),
            Write(codomain_label)
        )
        self.play(codomain.animate.shift(2*RIGHT))
        #--------------------------------------------------------------------------
        #definition of mapping arrows is done later so as to accurately position them 

        #creating mapping arrows to values in domain and codomain
        arrow1 = always_redraw(lambda: 
                                Arrow(start=a.get_center(), end=d.get_center()))
        arrow2 = always_redraw(lambda:
                                Arrow(start=b.get_center(), end=e.get_center()))
        arrow3 = always_redraw(lambda: 
                                Arrow(start=c.get_center(), end=f.get_center()))
        
        g.next_to(shifting_values, 0.75*DOWN)
        #--------------------------------------------------------------------------
        self.play(
            ShowCreation(arrow1),
            ShowCreation(arrow2),
            ShowCreation(arrow3)
        )
        self.add(arrow1, arrow2, arrow3)
        self.play(
            Write(function_label)
        )
        self.play(shifting_values.animate.shift(0.5*UP))
        self.play(
            Write(g)
        )
        self.play(
            Indicate(g)
        )

        self.wait(2) #FINAL WAIT TIME