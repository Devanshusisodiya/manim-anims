from manim import *
from manim.utils import tex
import numpy as np

class Test(GraphScene):
    def construct(self):

        self.wait(1)

        intro = Tex('\\text{This video is ','Calculus',' in a nutshell}').shift(ORIGIN)
        intro[1].set_color(BLUE)
        self.play(Write(intro))
        self.play(FadeOut(intro))

        diff_text = Tex('\\text{Differentiation}').set_color(BLUE).shift(ORIGIN)
        self.play(Write(diff_text))

        x = ValueTracker(1.5)
        dx = ValueTracker(1)

        # DIFFERENTIATION
        self.x_min=-1
        self.x_max=11
        self.x_axis_width=6
        self.x_labeled_nums=np.arange(1, self.x_max)
        self.y_min=-1
        self.y_max=10
        self.y_axis_length=5
        self.y_labeled_nums=np.arange(1, self.y_max)
        self.graph_origin=ORIGIN+5*LEFT+2.5*DOWN

        self.play(FadeOut(diff_text))
        self.setup_axes(animate=True)

        def poly(x):
            return 0.1*(x + 3-5)*(x - 3-5)*(x-5)+5

        graph = self.get_graph(poly, x_min=0.5, x_max=9, color=BLUE)
        slope = always_redraw(lambda: self.get_secant_slope_group(x.get_value(), graph, dx=dx.get_value(), secant_line_length=5, secant_line_color=YELLOW, df_line_color=YELLOW, dx_line_color=YELLOW))
        self.play(Create(graph))

        t1 = MathTex("\\text{we first define change in }","y","\\text{ w.r.t }","x").shift(2.5*UP+RIGHT)
        deltayx = MathTex("\\text{rate of change =}", "\\frac{\\Delta y}{\\Delta x}").shift(3*RIGHT)
        self.play(Write(t1))
        self.play(Write(deltayx))
        self.play(Unwrite(t1))

        self.play(Create(slope))
        self.play(x.animate.set_value(2), run_time=3)

        t2_0 = MathTex("\\text{since the change is quite large}", "(\\Delta x = 1)").shift(3.5*UP+RIGHT)
        t2_1 = MathTex("\\text{we choose to write }", "\\Delta", "\\text{ in rate of change expression}").next_to(t2_0, DOWN)
        self.play(Write(t2_0))
        self.play(Write(t2_1))
        self.play(
            Unwrite(t2_0),
            Unwrite(t2_1)
        )

        t3 = MathTex("\\text{on approximating change in }", "x", "\\text{ to 0}").shift(3*UP+RIGHT)
        self.play(Write(t3))
        self.play(dx.animate.set_value(0.001), run_time=3)
        self.play(FadeOut(t3))

        t4_0 = MathTex("\\text{now }", "\\Delta", "\\text{ changes to }", "d").shift(3.5*UP+RIGHT)
        t4_1 = MathTex("\\text{which signifies infinitesimaly small change}").next_to(t4_0, DOWN)

        dyx = MathTex("\\frac{dy}{dx}").next_to(deltayx[0], RIGHT)
        self.play(Write(t4_0))
        self.play(ReplacementTransform(deltayx[1], dyx))
        self.play(Write(t4_1))
        self.play(
            FadeOut(t4_0),
            FadeOut(t4_1),
            FadeOut(deltayx[0]),
            FadeOut(dyx)
        )

        t5 = MathTex("\\text{the ", "Maxima", " of the graph}").shift(3*RIGHT)
        t5[1].set_color(BLUE)
        self.play(Write(t5))
        self.play(x.animate.set_value(3.268), run_time=3)
        t5ch = MathTex("\\text{Minima}").next_to(t5[0], RIGHT).set_color(BLUE)
        self.play(Transform(t5[1], t5ch))
        self.play(x.animate.set_value(6.728), run_time=3)

        # ---------------

        self.play(
            FadeOut(t5),
            FadeOut(slope),
            FadeOut(graph),
            FadeOut(self.axes)
        )

        # INTEGRATION

        intro2 = MathTex("\\text{Integration}").shift(ORIGIN).set_color(BLUE)
        self.play(Write(intro2))
        self.play(FadeOut(intro2))

        self.x_min=-1
        self.x_max=11
        self.x_axis_width=6
        self.y_min=-1
        self.y_max=10
        self.y_axis_length=5
        self.graph_origin=ORIGIN+4*LEFT+2.5*DOWN
        self.include_tip=True
        #setting up axes
        self.setup_axes(animate=False)

        def poly(x):
            return 0.1*(x + 3-5)*(x - 3-5)*(x-5)+5
        def square(x):
            return x**2/4
        graph = self.get_graph(poly, x_min=0.5, x_max=9)
        graph_rects = self.get_graph(square, x_min=0, x_max=5)
        self.add(graph)

        rrect_list = self.get_riemann_rectangles_list(
            graph, 7, max_dx=1, x_min=2, x_max=9, fill_opacity=0.6
        )
        init_rects = rrect_list[0]

        flat_rects = self.get_riemann_rectangles(self.get_graph(lambda x: 0), dx=1, x_min=2, x_max=9)
        self.add(flat_rects)
        self.play(ReplacementTransform(flat_rects, init_rects))
        
        w_brace = BraceLabel(init_rects[-1], "w", DOWN)
        h_brace = BraceLabel(init_rects[-1], "h_i", RIGHT)
        approx_area_text = MathTex("Area=","\\sum_{i=1}^{%s}"%len(rrect_list[0]),"h_iw").shift(ORIGIN+4*RIGHT+2*UP)

        self.play(GrowFromCenter(w_brace))
        self.play(GrowFromCenter(h_brace))
        self.play(ReplacementTransform(init_rects.copy(), approx_area_text))
        self.play(FadeOut(h_brace))

        for i in range(1,4):
            w_brace_dup = BraceLabel(rrect_list[i][-1], "w", DOWN)
            area_text_dup = MathTex("Area=","\\sum_{i=1}^{%s}"%len(rrect_list[i]),"h_iw").shift(ORIGIN+4*RIGHT+2*UP)

            self.play(
                Transform(init_rects, rrect_list[i]),
                Transform(w_brace, w_brace_dup),
                Transform(approx_area_text[1], area_text_dup[1])
            )
    
        dw_brace = BraceLabel(init_rects[-1], "dw", DOWN)
        area_text = MathTex("Area=","\\sum_{i=1}^{\\infty}","h_idw").shift(ORIGIN+4*RIGHT+2*UP)
        self.play(
            Transform(w_brace, dw_brace),
            Transform(approx_area_text[1], area_text[1]),
            Transform(approx_area_text[-1], area_text[-1]),
        )

        for i in range(5,7):
            w_brace_dup = BraceLabel(rrect_list[i][-1], "dw", DOWN)

            self.play(
                Transform(init_rects, rrect_list[i]),
                Transform(w_brace, w_brace_dup),
            )

        self.wait(1)

        # -----------

        self.wait(1)