from manim import *
import numpy as np 

class Integration1(GraphScene):
    def construct(self):
        self.wait(1)
        #config
        self.x_min=-1
        self.x_max=11
        self.x_axis_width=6
        self.y_min=-1
        self.y_max=10
        self.y_axis_length=5
        self.graph_origin=ORIGIN+4*LEFT+3*DOWN
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

class Integration2(GraphScene):
    def construct(self):
        self.wait(1)
        #config
        self.x_min=-1
        self.x_max=11
        self.x_axis_width=6
        self.x_labeled_nums=np.arange(1, self.x_max)
        self.y_min=-1
        self.y_max=10
        self.y_axis_length=5
        self.y_labeled_nums=np.arange(1, self.y_max)
        self.graph_origin=ORIGIN+5*LEFT+2.5*DOWN
        self.include_tip=True

        self.setup_axes(animate=False)

        def poly(x):
            return 0.1*(x + 3-5)*(x - 3-5)*(x-5)+5
        graph = self.get_graph(poly, x_min=0.5, x_max=9)
        graph_label = self.get_graph_label(graph, "f(x)=0.1((x+3)-5)(x-3)-5)(x-5)+5", 7, DOWN+RIGHT).scale(0.7)
        self.add(graph, graph_label)

        dx = ValueTracker(1)
        rrect_list = self.get_riemann_rectangles_list(
            graph, 7, max_dx=dx.get_value(), x_min=2, x_max=9, fill_opacity=0.6
        )
        init_rects = rrect_list[0]
        flat_rects = self.get_riemann_rectangles(self.get_graph(lambda x: 0), dx=dx.get_value(), x_min=2, x_max=9)
        self.add(flat_rects)

        x_is_2 = MathTex("\\text{Let us consider }","x=2").shift(ORIGIN+RIGHT+2.5*UP)
        x_is_2[1].set_color(BLUE)
        dx_is_1 = MathTex("\\text{Since }","dx=1","\\text{, value of }","x\\text{ changes by }1").shift(ORIGIN+RIGHT+DOWN)
        dx_is_1[1].set_color(RED)
        dx_is_1[-1].set_color(RED)
        dx_is_half = MathTex("\\text{Now }","dx=0.5").shift(ORIGIN+RIGHT+3*UP)
        dx_is_half[1].set_color(RED)

        x = ValueTracker(2)
        x_val = DecimalNumber().shift(ORIGIN+5*RIGHT)
        fx_val = DecimalNumber().shift(ORIGIN+5*RIGHT+UP)
        x_val.add_updater(lambda d: d.set_value(x.get_value()))
        fx_val.add_updater(lambda d: d.set_value(poly(x.get_value())))
        x_text = MathTex("x=").next_to(x_val, LEFT)
        fx_text = MathTex("f(x)=").next_to(fx_val, LEFT)

        x_group = VGroup(x_text, x_val)
        x_group_dup = VGroup(MathTex("x=", color=WHITE), MathTex("2.00", color=WHITE))
        x_group_dup[1].shift(ORIGIN+5*RIGHT)
        x_group_dup[0].next_to(x_group_dup[1], LEFT)
        fx_group = VGroup(fx_text, fx_val)
        fx_group_dup = VGroup(MathTex("f(x)=", color=WHITE), MathTex("5.00", color=WHITE))
        fx_group_dup[1].shift(ORIGIN+5*RIGHT+UP)
        fx_group_dup[0].next_to(fx_group_dup[1], LEFT)
        info_rect_group = VGroup(x_val, fx_val, x_text, fx_text)

        self.play(Write(graph_label))
        self.play(FadeInFrom(x_is_2))
        self.play(ReplacementTransform(x_is_2[1].copy(), x_group_dup))
        self.add(x_group)
        self.remove(x_group_dup)
        self.play(FadeOut(x_is_2))
        self.play(ReplacementTransform(graph_label, fx_group_dup))
        self.add(fx_group)
        self.remove(fx_group_dup)

        self.play(ReplacementTransform(flat_rects[0], init_rects[0]))
        self.play(FadeInFrom(dx_is_1, UP))
        self.play(FadeOut(dx_is_1))
        for i in range(1, len(init_rects)):
            self.play(x.animate.set_value(i+2), run_time=1.5)
            self.play(ReplacementTransform(flat_rects[i], init_rects[i]))
            self.wait(0.5)

        self.play(FadeOut(init_rects))

        self.play(Write(dx_is_half))
        self.play(x.animate.set_value(2), run_time=0.5)
        self.play(FadeOut(dx_is_half))

        dx.set_value(0.5)
        init_rects = rrect_list[1]
        flat_rects = self.get_riemann_rectangles(self.get_graph(lambda x: 0), dx=dx.get_value(), x_min=2, x_max=9)
        self.add(flat_rects)
        
        x_vals = np.arange(2.5, len(init_rects), dx.get_value())
        self.play(ReplacementTransform(flat_rects[0], init_rects[0]))
        for i in range(1, 14):
            self.play(x.animate.set_value(x_vals[i]-dx.get_value()), run_time=1.5)
            self.play(ReplacementTransform(flat_rects[i], init_rects[i]))

        self.wait(1)