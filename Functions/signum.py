import numpy as np 
from manim import *


class SignumFunction(GraphScene):
    def construct(self):

        self.wait(1) # INITIAL WAIT TIME
        #config
        self.x_min = -3
        self.x_max = 3
        self.y_min = -2
        self.y_max = 2
        self.graph_origin = ORIGIN + 2*LEFT 
        
        self.setup_axes(animate=True)
# SETTING UP OF THE SCENE ------------------------------------------
   
        def signum0(x):
            return -1
        def signum1(x):
            return 1

        point0 = Dot(self.coords_to_point(0,1))
        point1 = Dot(self.coords_to_point(0,-1))
        point_org = Dot(ORIGIN + 2*LEFT, color=YELLOW)

        signum_graph0 = self.get_graph(signum0, x_min=-2, x_max=0, color=PURPLE)
        signum_graph1  = self.get_graph(signum1, x_min=0, x_max=2, color=PURPLE)

        fx0 = TexMobject(r'-1; x < 0')
        fx1 = TexMobject(r'0; x = 0')
        fx2 = TexMobject(r'1; x > 0')
        fx0.shift(ORIGIN+6*RIGHT+3*UP)
        fx1.shift(ORIGIN+6*RIGHT+2*UP)
        fx2.shift(ORIGIN+6*RIGHT+UP)

        fx_group = VGroup(fx0, fx1, fx2)
        fx_brace = Brace(fx_group, LEFT)
        fx_label = TexMobject(r'f(x) =')
        fx_label.next_to(fx_brace, LEFT)

# ANIMATIONS -------------------------------------------------------

        self.play(
            Write(fx_label),
            GrowFromCenter(fx_brace),
            Write(fx_group)
        )
        
        self.play(
            ShowCreation(signum_graph0),
            ShowCreation(signum_graph1)
        )
        self.play(
            ShowCreation(point0),
            ShowCreation(point1),
            ShowCreation(point_org)
        )


        self.wait(1) # FINAL WAIT TIME