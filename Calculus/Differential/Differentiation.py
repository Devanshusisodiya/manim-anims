from manim import *
import numpy as np

class Differentiation(GraphScene, MovingCameraScene):
    def setup(self):
        GraphScene.setup(self)
    def construct(self):
        self.wait(1) # INITIAL WAIT TIME 
        self.camera.frame.save_state()       
        #config
        self.x_min = -4
        self.x_max = 4 
        self.x_axis_width = 6
        self.x_labeled_nums = np.arange(0, 3+1, 3)
        self.y_min = -1
        self.y_max = 16
        self.y_axis_height = 6
        self.y_labeled_nums = np.arange(0, self.y_max+1, 9)
        self.graph_origin = ORIGIN+3*DOWN + 3*LEFT
        self.y_axis_label = r"f(x)"


        intro_text1 = MathTex("\\text{Differentiation is the"," rate of change"," of one quantity w.r.t another}")
        intro_text2 = MathTex("\\text{What is rate of change of }","f(x)","\\text{ w.r.t }","x","\\text{ ?}")
        intro_text1[1].set_color(BLUE)
        intro_text2[1].set_color(BLUE)
        intro_text2[3].set_color(BLUE)

        self.play(
            Write(intro_text1),
            run_time=2
        )
        self.play(FadeOut(intro_text1),)
        self.wait(1)
        self.play(
            Write(intro_text2),
        )
        self.play(FadeOut(intro_text2),)


        self.setup_axes(animate=True)
        def poly(x):
            return x**3 + 3
        def trig(x):
            return 2*np.sin(x)
        def exp(x):
            return np.exp(x)
        def log(x):
            return np.log(x)
        def func(x):
            return x**2

        graph_intro1 = self.get_graph(poly, x_min=-2, x_max=3, color=BLUE)
        graph_intro2 = self.get_graph(trig, x_min=self.x_min, x_max=self.x_max, color=PURPLE)
        graph_intro3 = self.get_graph(log, x_min=0.1, x_max=self.x_max, color=YELLOW)
        graph_intro4 = self.get_graph(exp, x_min=self.x_min, x_max=self.x_max, color=RED)

        graph_label1 = self.get_graph_label(graph=graph_intro1, label="x^3+3", x_val=1, direction=RIGHT, color=graph_intro1.color)
        graph_label2 = self.get_graph_label(graph=graph_intro1, label="sinx", x_val=1,direction=4*RIGHT, color=graph_intro2.color)
        graph_label3 = self.get_graph_label(graph=graph_intro1, label="log|x|", x_val=1, direction=RIGHT, color=graph_intro3.color)
        graph_label4 = self.get_graph_label(graph=graph_intro1, label="e^x", x_val=1, direction=2*RIGHT, color=graph_intro4.color)

        self.play(
            ShowCreation(graph_intro1),
            Write(graph_label1)
        )
        self.play(
            Transform(graph_intro1, graph_intro2),
            Transform(graph_label1, graph_label2)
        )
        self.play(
            Transform(graph_intro1, graph_intro3),
            Transform(graph_label1, graph_label3)
        )
        self.play(
            Transform(graph_intro1, graph_intro4),
            Transform(graph_label1, graph_label4)
        )
        self.play(FadeOut(graph_intro1), FadeOut(graph_label1))
    

        graph = self.get_graph(func, x_min=-3.6, x_max=3.6, color=BLUE)
        graph_label = self.get_graph_label(graph, label="x^2", x_val=-3.6)

        graph_text = Tex(
            "For a small change in x",
            "what is the corresponding change in f(x)"
        )
        graph_text[0].shift(ORIGIN+6.7*RIGHT+3*UP)
        graph_text[1].next_to(graph_text[0], DOWN)

        x = ValueTracker(3)         # THE MOST IMPORTANT VALUE TRACKERS
        dx = ValueTracker(0.5)

        v_line1 = always_redraw(lambda: self.get_vertical_line_to_graph(x.get_value(), graph, line_class=DashedLine, color=WHITE))
        v_line2 = always_redraw(lambda: self.get_vertical_line_to_graph(x.get_value()+dx.get_value(), graph, line_class=DashedLine, color=WHITE))
        h_line1 = always_redraw(lambda: DashedLine(start=self.coords_to_point(x.get_value(), func(x.get_value())), end=self.coords_to_point(0, func(x.get_value())), color=WHITE))
        h_line2 = always_redraw(lambda: DashedLine(start=self.coords_to_point(x.get_value()+dx.get_value(), func(x.get_value()+dx.get_value())), end=self.coords_to_point(0, func(x.get_value()+dx.get_value())), color=WHITE))

        dx_line = always_redraw(lambda: Line(start=self.coords_to_point(x.get_value(),0.2),end=self.coords_to_point(x.get_value()+dx.get_value(), 0.2), color=YELLOW))
        dx_arrow = Arrow(start=self.coords_to_point(5,3),end=self.coords_to_point(3, 0))
        dx_label = MathTex(r'dx').shift(self.coords_to_point(5,3.2))
        dx_label[0].set_color(YELLOW)

        dy_controller = ValueTracker(0)
        dy_line_wiggle = always_redraw(lambda: Line(start=self.coords_to_point(3.5,dy_controller.get_value()),end=self.coords_to_point(3.5,12.25), color=YELLOW))
        dx_line_wiggle = Line(start=self.coords_to_point(3,9),end=self.coords_to_point(3.5,9), color=YELLOW)

        slope = always_redraw(lambda: self.get_secant_slope_group(x.get_value(), graph, dx=dx.get_value(), include_secant_line=False, df_line_color=YELLOW, dx_line_color=YELLOW, df_label="dy", dx_label="dx"))


        small_dx_text = MathTex("\\text{small change in }","x","=","dx")
        small_fx_text = MathTex("\\text{small change in }","f(x)","=","dy")
        rate_of_change_text = MathTex("\\text{rate of change }","=","\\frac{dy }{dx}")

        small_dx_text[1].set_color(BLUE)
        small_dx_text[3].set_color(YELLOW)
        small_fx_text[1].set_color(BLUE)
        small_fx_text[3].set_color(YELLOW)
        rate_of_change_text[2].set_color(YELLOW)

        small_dx_text.shift(ORIGIN+3*RIGHT+3*UP)
        small_fx_text.next_to(small_dx_text, DOWN)
        rate_of_change_text.next_to(small_dx_text, 3*DOWN)

        xdx_dot = Dot(point=self.coords_to_point(x.get_value()+dx.get_value(),0), color=YELLOW)
        fxdx_dot = Dot(point=self.coords_to_point(0,func(x.get_value()+dx.get_value())), color=YELLOW)
        xdx_label = MathTex("3+dx").shift(ORIGIN+3*RIGHT)
        fxdx_label = MathTex("(3+dx)^2").shift(ORIGIN+3*RIGHT)
        xdx_indicate_rect = Square(side_length=0.5, color=YELLOW).shift(self.coords_to_point(3,-1))
        fxdx_indicate_rect = Square(side_length=0.5, color=YELLOW).shift(self.coords_to_point(-0.4,9))


        self.play(
            ShowCreation(graph),
            Write(graph_label),     
        )
        self.play(
            Write(small_dx_text),
        )
        self.play(
            Write(small_fx_text),
        )
        self.play(
            Write(rate_of_change_text),
        )
        self.play(
            FadeOut(small_dx_text),FadeOut(small_fx_text),FadeOut(rate_of_change_text),
        )


        self.play(self.camera.frame.animate.scale(0.2).move_to(self.coords_to_point(3,0)))
        self.play(ShowCreation(xdx_indicate_rect))
        self.wait(1)
        # self.play(FadeOut(xdx_indicate_rect))
        self.play(
            Restore(self.camera.frame),
            ShowCreation(v_line1),
        )

        self.play(
            self.camera.frame.animate.scale(0.2).move_to(self.coords_to_point(0,9)),
            ShowCreation(h_line1),
        )
        self.play(ShowCreation(fxdx_indicate_rect))
        self.wait(1)
        # self.play(FadeOut(fxdx_indicate_rect))
        self.play(Restore(self.camera.frame),)
        
        self.play(
            ShowCreation(dx_line)
        )
        self.play(
            ShowCreation(dx_arrow),
            Write(dx_label),
        )
        self.play(
            FadeOut(dx_label),
            FadeOut(dx_line),
            FadeOut(dx_arrow),
        )

        self.play(Write(xdx_label),)
        self.play(Transform(xdx_label, xdx_dot),)
        self.play(
            ShowCreation(v_line2),
        )
        self.play(Write(fxdx_label),)
        self.play(Transform(fxdx_label, fxdx_dot),)        
        self.play(
            ShowCreation(h_line2),
        )

        dy_dx_label = MathTex("dy \\over","dx")
        dy_dx_label.shift(ORIGIN + 2*RIGHT)

        self.play(ShowCreation(dy_line_wiggle),)
        self.wait(1)
        self.play(dy_controller.animate.set_value(9), run_time=3)
        self.wait(1)
        self.play(ReplacementTransform(dy_line_wiggle.copy(), dy_dx_label[0]), run_time=2)#
        self.play(ShowCreation(dx_line_wiggle),)
        self.wait(1)
        self.play(ReplacementTransform(dx_line_wiggle.copy(), dy_dx_label[1]), run_time=2)#
        self.wait(1)
        # self.play(ReplacementTransform(dy_line_wiggle.copy(), dy_dx_label[0]), run_time=2)
        # self.play(ReplacementTransform(dx_line_wiggle.copy(), dy_dx_label[1]), run_time=2)
        self.play(FadeOut(dy_dx_label))


        # #---------------------------------------------------------------------------------------------------------------

        def get_dy_dx(step):
            dy_dx = MathTex(r"\frac{dy}{dx}\Bigr|_{x=3}")
            eq = MathTex("=")
            unit_step = VGroup(dy_dx, eq, step)
            unit_step.arrange(RIGHT)
            unit_step.shift(ORIGIN+3*RIGHT+3*UP)
            return unit_step

        def get_exp(pow):
            inp = "(dx)^%s=0"%pow
            exp = MathTex(inp)
            exp.shift(ORIGIN+3*RIGHT+UP)
            return exp

        step1 = get_dy_dx(MathTex("(3+dx)^2-3^2 \\over","dx"))
        step2 = get_dy_dx(MathTex("3^2+2\\cdot 3\\cdot dx+(dx)^2-3^2 \\over","dx"))
        step3 = get_dy_dx(MathTex("2\\cdot 3\\cdot dx +(dx)^2 \\over","dx"))
        step4 = get_dy_dx(MathTex("2\\cdot 3\\cdot dx \\over","dx"))
        step5 = get_dy_dx(MathTex("6"))

        self.play(ShowCreation(step1))
        self.play(Transform(step1, step2))
        self.play(Transform(step1, step3))

        step_init = get_exp("2")
        self.play(ShowCreation(step_init))
        for i in ["3","4","5","n"]:
            step_ex = get_exp(i)
            self.play(Transform(step_init, step_ex))
            self.wait(0.5)
        self.play(FadeOut(step_init),)

        self.play(Transform(step1, step4))
        self.play(Transform(step1, step5))
        
        self.wait(1) # FINAL WAIT TIME