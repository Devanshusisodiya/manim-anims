from manim import *
import numpy as np


class LinearGraphSlides(GraphScene):
    def construct(self):
        self.x_min = -5
        self.x_max = 5
        self.y_min = -5
        self.y_max = 5
        self.axes_color = WHITE
        self.x_axis_label = "$x$"
        self.y_axis_label = "$y$"
        self.x_labeled_nums = list(range(-5, 6, 1))
        self.y_labeled_nums = list(range(-5, 6, 1))
        self.graph_origin = RIGHT * 2
        self.x_axis_width = 7
        self.y_axis_height = 7

        a = ValueTracker(1)
        b = ValueTracker(0)
        self.setup_axes()

        func = self.get_graph(lambda x: x, x_min=-5, x_max=5, color=RED)

        a_slider = Line(start=LEFT * 5.5 + UP * 2, end=LEFT * 2.5 + UP * 2)
        b_slider = Line(start=LEFT * 5.5 + DOWN * 2, end=LEFT * 2.5 + DOWN * 2)
        a_label = Text("a value (slope)").scale(.4).next_to(a_slider, DOWN, buff=.1)
        b_label = Text("b value (y-intercept)").scale(.4).next_to(b_slider, DOWN, buff=.1)
        a_dot = Dot(point=LEFT * 3.5 + UP * 2)
        b_dot = Dot(point=LEFT * 4 + DOWN * 2)
        a_value = Text("1.0").scale(.3).next_to(a_dot, UP, buff=.1)
        b_value = Text("0.0").scale(.3).next_to(b_dot, UP, buff=.1)

        self.add(a_slider, b_slider, a_label, b_label, a_dot, b_dot, a_value, b_value)
        self.play(ShowCreation(func))
 
        def ReplaceGraph(mob):
            mob.become(
                self.get_graph(
                    lambda x: a.get_value() * x + b.get_value(),
                    x_min=-5, x_max=5, color=RED
                )
            )

        def MoveA(mob):
            mob.move_to([a.get_value() / 2 - 4, 2, 0])

        def MoveB(mob):
            mob.move_to([b.get_value() / 2 - 4, -2, 0])

        def ValueA(mob):
            atemp = str(round(a.get_value(), 1))
            mob.become(Text(atemp).scale(.3).next_to(a_dot, UP, buff=.1))

        def ValueB(mob):
            btemp = str(round(b.get_value(), 1))
            mob.become(Text(btemp).scale(.3).next_to(b_dot, UP, buff=.1))


        func.add_updater(ReplaceGraph)
        a_dot.add_updater(MoveA)
        b_dot.add_updater(MoveB)
        a_value.add_updater(ValueA)
        b_value.add_updater(ValueB)

        self.play(a.animate.set_value(3), rate_func=there_and_back, run_time=1.5)
        self.play(a.animate.set_value(-3), rate_func=there_and_back, run_time=1.5)
        self.play(b.animate.set_value(3), rate_func=there_and_back, run_time=1.5)
        self.play(b.animate.set_value(-3), rate_func=there_and_back, run_time=1.5)
