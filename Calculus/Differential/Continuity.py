from manim import *
import numpy as np 

class Continuity(GraphScene):
    def construct(self):    
        self.wait(1)
        #config
        self.x_min=0
        self.x_max=11
        self.x_axis_width=6
        self.x_labeled_nums=np.arange(1,self.x_max)
        self.y_min=0
        self.y_max=10
        self.y_axis_length=5
        self.y_labeled_nums=np.arange(1,self.y_max)
        self.graph_origin=ORIGIN+5*LEFT+3*DOWN
        self.include_tip=True

        self.setup_axes(animate=True)

        def poly(x):
            return 0.1*(x-2)*(x-8)*(x-5)+5
        graph = self.get_graph(poly, x_min=0.5, x_max=9)
        self.add(graph)
        
        x = ValueTracker(2)
        x_val = DecimalNumber(num_decimal_places=4).shift(ORIGIN+5*RIGHT).add_updater(lambda d: d.set_value(x.get_value()))
        fx_val = DecimalNumber(num_decimal_places=4).shift(ORIGIN+5*RIGHT+UP).add_updater(lambda d: d.set_value(poly(x.get_value())))
        x_text = MathTex("x","=").next_to(x_val, LEFT)
        fx_text = MathTex("f(x)","=").next_to(fx_val, LEFT)
        
        def info_group_gen(x, func=poly):
            return VGroup(
                MathTex("%.4f"%x.get_value()).shift(ORIGIN+5*RIGHT),
                MathTex("%.4f"%func(x.get_value())).shift(ORIGIN+5*RIGHT+UP),
                MathTex("x","=").next_to(x_val, LEFT),
                MathTex("f(x)","=").next_to(fx_val, LEFT)
                )

        lhl_group = info_group_gen(x, poly)

        def dot_updater(dot):
            return dot.move_to(self.coords_to_point(x.get_value(), poly(x.get_value())))
        lhl_dot = Dot(self.coords_to_point(x.get_value(), poly(x.get_value())), color=RED, radius=0.04)
        rhl_dot = Dot(self.coords_to_point(x.get_value(), poly(x.get_value())), color=RED, radius=0.04)
        lhl_dot.add_updater(dot_updater)
        rhl_dot.add_updater(dot_updater)
        v_line = always_redraw(lambda: DashedLine(start=self.coords_to_point(x.get_value(),0),end=self.coords_to_point(x.get_value(),poly(x.get_value())), color=RED))
        h_line = always_redraw(lambda: DashedLine(start=self.coords_to_point(x.get_value(),poly(x.get_value())),end=self.coords_to_point(0,poly(x.get_value())), color=RED))


        x_is_3 = MathTex("\\text{Let's consider limit at }","x=3").shift(ORIGIN+RIGHT+2.5*UP)
        x_is_3[1].set_color(BLUE)
        x_line = DashedLine(start=self.coords_to_point(3,0), end=self.coords_to_point(3,poly(3)))
        lhl_text = MathTex("\\text{Visualising }","\\text{Left Hand Limit}").shift(ORIGIN+2.5*UP)
        lhl_text[1].set_color(RED)
        rhl_text = MathTex("\\text{Now }","\\text{Right Hand Limit}").shift(ORIGIN+2.5*UP)
        rhl_text[1].set_color(RED)
        lhl_approx_text = MathTex("LHL \\approx","6").shift(ORIGIN+2*DOWN+2*LEFT)
        lhl_approx_text[0].set_color(RED)
        # lhl_approx_text.add_background_rectangle()


        self.play(ShowCreation(graph))
        self.play(FadeInFrom(x_is_3))
        self.play(ReplacementTransform(x_is_3[1].copy(), x_line))
        self.play(FadeOut(x_is_3))
        self.play(Write(lhl_text))
        self.play(
            ShowCreation(v_line),
            ReplacementTransform(lhl_text[1].copy(), lhl_dot),
            ShowCreation(h_line),
        )
        self.play(ReplacementTransform(lhl_dot.copy(), lhl_group))
        self.add(x_val, fx_val, x_text, fx_text)
        self.remove(lhl_group)
        self.play(x.animate.set_value(2.9998), run_time=3)
        self.play(
            Write(lhl_approx_text[0]),
            ReplacementTransform(fx_text[0].copy(), lhl_approx_text[-1])
        )
        self.play(FadeOut(VGroup(x_val, fx_val, x_text, fx_text, lhl_text, lhl_dot, h_line, v_line)))

        x.set_value(4)
        rhl_group = info_group_gen(x)
        v_line = always_redraw(lambda: DashedLine(start=self.coords_to_point(x.get_value(),0),end=self.coords_to_point(x.get_value(),poly(x.get_value())), color=RED))
        h_line = always_redraw(lambda: DashedLine(start=self.coords_to_point(x.get_value(),poly(x.get_value())),end=self.coords_to_point(0,poly(x.get_value())), color=RED))
        self.play(Write(rhl_text))
        self.play(
            ShowCreation(v_line),
            ReplacementTransform(rhl_text[1].copy(), rhl_dot),
            ShowCreation(h_line),
        )
        self.play(ReplacementTransform(rhl_dot.copy(), rhl_group))
        self.add(x_val, fx_val, x_text, fx_text)
        self.remove(rhl_group)
        self.play(x.animate.set_value(3.0002), run_time=3)
        # self.play
        
        self.wait(1)