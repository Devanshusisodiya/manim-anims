import numpy as np 
from manim import *

class OneOverX(GraphScene):
    def construct(self):
        self.wait(1) # INITIAL WAIT TIME

        #config
        self.x_min = -4
        self.x_max = 4
        self.y_min = -10
        self.y_max = 10
        self.y_axis_height = 7
        self.graph_origin = ORIGIN
        # SETTING UP OF THE SCENE -------------------------------------
        self.setup_axes(animate=True)
        def func(x):
            return 1/x

        dot0 = Dot(self.coords_to_point(-2,-0.5))
        graph0 = self.get_graph(func, x_min=-4, x_max=-0.1, color=BLUE)
        graph1 = self.get_graph(func, x_min=0.1, x_max=4, color=BLUE)

        xval = ValueTracker(-4)

        x = DecimalNumber(0,
                          show_ellipsis=False,
                          num_decimal_places=3)
        fx_val = Integer(0,
                         show_ellipsis=False,
                         num_decimal_places=2)
        x.add_updater(lambda val: val.set_value(xval.get_value()))
        fx_val.add_updater(lambda val: val.set_value(func(xval.get_value())))
        
        def point_updater(point):
            return point.move_to(self.coords_to_point(xval.get_value(), func(xval.get_value())))
        dot0.add_updater(point_updater)

        x_label = TexMobject(r'x=')
        fx_label = TexMobject(r'f(x)=')
        
        x_label.shift(ORIGIN+2*DOWN+2*RIGHT)
        fx_label.shift(ORIGIN+3*DOWN+2*RIGHT)
        x.next_to(x_label, RIGHT)
        fx_val.next_to(fx_label, RIGHT)
        data_group = VGroup(x_label, fx_label, x, fx_val, dot0)
        # ANIMATIONS --------------------------------------------------

        # self.play(
        #     ShowCreation(graph0),
        #     ShowCreation(graph1),
        # )
        self.play(
            *[ShowCreation(objs) for objs in data_group]
        )
        self.play(xval.animate.set_value(4), run_time=5)


        self.play(
            FadeOut(dot0),
            ShowCreation(graph0),
            ShowCreation(graph1),
        )


        self.wait(1) # FINAL WAIT TIME