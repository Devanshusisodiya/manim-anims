import numpy as np 
from manim import *

class VerticalLineTest(GraphScene):
    def construct(self):
        #config
        self.x_min = 0
        self.x_max = 10
        self.y_min = -5
        self.y_max = 5
        self.graph_origin = ORIGIN + 4*LEFT
        self.x_axis_width = 6
        
        # SETTING UP OF THE SCENE --------------------------------------------------
        self.wait(1) # INITIAL WAIT TIME        
        self.setup_axes(animate=True)

        def func0(x):
            return np.sqrt(x)
        def func1(x):
            return -np.sqrt(x)

        graph0 = self.get_graph(func0, x_min=0, x_max=8, color=PURPLE)
        graph1 = self.get_graph(func1, x_min=0, x_max=8, color=PURPLE)
        
        dot_start = Dot(self.coords_to_point(4,2))
        dot_end = Dot(self.coords_to_point(4,-2))

        vertical_line = Line(start=dot_start.get_center()+1.5*UP, end=dot_end.get_center()+1.5*DOWN, color=WHITE)
        line_positive = always_redraw(lambda: 
                                      DashedLine(start=self.coords_to_point(4,2), end=self.coords_to_point(0,2)))
        line_negative = always_redraw(lambda: 
                                      DashedLine(start=self.coords_to_point(4,-2), end=self.coords_to_point(0,-2)))
        int_positive = Integer(2)
        int_negative = Integer(-2)
        int_positive.shift(self.coords_to_point(-0.4, 2))
        int_negative.shift(self.coords_to_point(-0.7, -2))

        # ANIMATIONS ---------------------------------------------------------------

        self.play(
            ShowCreation(graph0),
            ShowCreation(graph1),
        )
        self.play(
            ShowCreation(vertical_line)
        )
        self.play(
            vertical_line.animate.shift(2*RIGHT),
        )
        self.play(
            vertical_line.animate.shift(4*LEFT),
        )
        self.play(
            vertical_line.animate.shift(2*RIGHT),
        )
        self.play(
            ShowCreation(line_positive),
            ShowCreation(line_negative),
            Write(int_positive),
            Write(int_negative),
        )


        self.wait(1) # FINAL WAIT TIME 