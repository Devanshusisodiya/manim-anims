import numpy as np 
from manim import *


class MachineGraph(GraphScene):
    def construct(self):
        self.wait(1) # INITIAL WAIT TIME
        #config
        self.x_min = 0
        self.x_max = 6
        self.y_min = 0
        self.y_max = 26
        self.y_axis_height = 7
        self.x_axis_width = 5
        self.graph_origin = ORIGIN + 5*LEFT + 3.5*DOWN

# SETTING UP OF GRAPH SCENE ------------------------------------------------
        self.setup_axes(animate=True)
        
        def func(x):
            return x**2
        graph = self.get_graph(func, x_min=0, x_max=5, color=PURPLE)

        fx_label = TexMobject(r'f(x) = ')
        x_label = TexMobject(r'x = ')
        fx_label.shift(ORIGIN + 2*RIGHT)
        x_label.shift(ORIGIN + 2*RIGHT + 1*DOWN)

        x_tracker = ValueTracker(1) # VALUE TRACKER FOR x
        
        v_line = always_redraw(lambda : 
                                    self.get_vertical_line_to_graph(x_tracker.get_value(), graph, line_class=DashedLine, color=WHITE))
        h_line = always_redraw(lambda: 
                                    DashedLine(start=self.coords_to_point(0,graph.underlying_function(x_tracker.get_value())), end=self.coords_to_point(x_tracker.get_value(), graph.underlying_function(x_tracker.get_value()))))
        point = Dot(self.coords_to_point(1,1))
        fx_val = DecimalNumber(0,
                               show_ellipsis=False,
                               n_decimal_places=2)
        x_val = DecimalNumber(0,
                               show_ellipsis=False,
                               n_decimal_places=2)
        fx_val.next_to(fx_label, RIGHT)
        x_val.next_to(x_label, RIGHT)
        
        point.add_updater(lambda p: p.move_to(self.coords_to_point(x_tracker.get_value(), func(x_tracker.get_value()))))      
        fx_val.add_updater(lambda d: d.set_value(func(x_tracker.get_value())))
        x_val.add_updater(lambda d: d.set_value(x_tracker.get_value()))

# ANIMATIONS ----------------------------------------------------------------
        self.play(
            ShowCreation(graph)
        )
        self.play(
            ShowCreation(v_line),
            ShowCreation(h_line),
            ShowCreation(point)
            )
        self.play(
            Write(fx_label),
            Write(x_label),
            Write(fx_val),
            Write(x_val)
        )
        self.add(fx_val, x_val, point)
        self.play(x_tracker.animate.set_value(5), run_time=3)

        self.wait(1) # FINAL WAIT TIME