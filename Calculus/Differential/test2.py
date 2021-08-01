from manim import *
import numpy as np

class Test(Scene):
    def construct(self):

        plane_config = dict(
            axis_config = { 
                "include_tip": True, "include_numbers" : True,
                "include_ticks" : True, "line_to_number_buff" : 0.05,
                "stroke_color" : WHITE, "stroke_width": 0.5,
                "number_scale_val" : 0.4,
                "tip_scale": 0.5,
            },
            x_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : DOWN, "stroke_color" : WHITE,
                "x_min" : -3, "x_max" : 3, "unit_size": 5/6, 
                "numbers_to_show": range(-3, 4, 1),
            },
            y_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : UR, "stroke_color" : WHITE,
                "x_min" : 0, # not y_min
                "x_max" : 15,  # not y_max
                "unit_size": 1/5, "numbers_to_show": range(0, 16, 3),
            },
            background_line_style = {
                "stroke_width" : 1, "stroke_opacity" : 0.75,
                "stroke_color" : GREEN_C,
            },
            x_line_frequency=1/5
        )
        plane = NumberPlane(**plane_config)
        plane.shift(RIGHT*3 + 3*DOWN)

        self.play(
            ShowCreation(plane),
            run_time=3
        )

class Test2(GraphScene):

    def construct(self):
        self.x_min = -4
        self.x_max = 4 
        self.x_axis_width = 6
        self.y_min = -1
        self.y_max = 16
        self.y_axis_height = 6
        self.graph_origin = ORIGIN+3*DOWN + 3.5*LEFT
        # self.y_axis_label = "f(x)"

        self.wait(1)

        self.setup_axes(animate=True)

        def poly(x):
            return x**2
        graph_intro1 = self.get_graph(poly, x_min=-3.6, x_max=3.6, color=BLUE)

        self.play(ShowCreation(graph_intro1))

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

        # label_3 = MathTex("3")     
        # label_3dx = MathTex("3+dx")
        # label_9 = MathTex("3^2")
        # label_9dx = MathTex("(3+dx)^2")

        # label_3.shift(self.coords_to_point(3,-1))
        # label_9.shift(self.coords_to_point(-0.4,9))
        # label_9dx.shift(self.coords_to_point(-1.5,12.1))

        # step1 = MathTex("(3+dx)^2", "-3^2", "\\over","dx")
        # step1_ex = MathTex("(3+dx)^2", "-", "3^2", "\\over","dx")
        # step1.shift(ORIGIN+3*RIGHT)
        # step1_ex.shift(ORIGIN+3*RIGHT)

        # self.play(label_9dx.copy().animate.shift(ORIGIN+3*RIGHT))
        
        
        # label_3dx.shift(self.coords_to_point(3+0.5,-0.5))
        # graph_text = Tex(                                              # TEXT TO BE WRITTEN
        #     "For a small change in x, what",
        #     "is the corresponding change in f(x)"
        # )

        # graph_text[0].shift(ORIGIN+6.7*RIGHT+3*UP)
        # graph_text[1].next_to(graph_text[0], DOWN)

        # self.play(ShowCreation(graph_intro1))
        # self.add(label_3, label_9, label_9dx)
        # self.play(
        #     ReplacementTransform(label_9dx.copy(), step1[0]),
        #     ReplacementTransform(label_9.copy(), step1[1]),
        #     run_time=3
        # )
        
        # self.play(Write(step1))

        # self.play(Write(graph_text))

        # def get_exp(pow):
        #     inp = "(dx)^%s=0"%pow
        #     exp = MathTex(inp)
        #     exp.shift(ORIGIN)
        #     return exp

        # step_init = get_exp("2")
        # self.play(ShowCreation(step_init))
        # for i in ["3","4","5","n"]:
        #     step_ex = get_exp(i)
        #     self.play(Transform(step_init, step_ex))
        #     self.wait(0.5)

        self.wait(1)



class Test1(GraphScene):
    def construct(self):
        #config
        self.x_min = -4
        self.x_max = 4
        self.y_min = 0
        self.y_max = 9
        self.graph_origin = ORIGIN + 3*DOWN

        self.wait(1) # INITIAL WAIT TIME
        # SETTING UP OF THE SCENE -----------------------------------------------
        self.setup_axes(animate=True)

        def func(x):
            return x**2

        graph = self.get_graph(func, x_min=-3, x_max=3, color=YELLOW)

        x_tracker = ValueTracker(-3)

        dot = Dot(self.coords_to_point(-3,9))
        dot.add_updater(lambda d: d.move_to(self.coords_to_point(x_tracker.get_value(), func(x_tracker.get_value()))))

        # point_val0 = MathTex(r')').add_updater(lambda d: d.next_to(dot, LEFT))
        # point_val1 = MathTex(r',').add_updater(lambda d: d.next_to(dot, 6*LEFT+0.15*DOWN))
        # point_val2 = DecimalNumber(0, show_ellipsis=False, num_decimal_places=2).add_updater(lambda d: d.set_value(func(x_tracker.get_value())))
        # point_val2.add_updater(lambda d: d.next_to(dot, 1.5*LEFT))
        # point_val3 = DecimalNumber(0, show_ellipsis=False, num_decimal_places=2).add_updater(lambda d: d.set_value(x_tracker.get_value()))
        # point_val3.add_updater(lambda d: d.next_to(dot, 7*LEFT))
        # point_val4 = MathTex(r'(').add_updater(lambda d: d.next_to(dot, 8*LEFT))

        point_val0 = MathTex(r')').shift(ORIGIN+1.5*RIGHT)
        point_val1 = MathTex(r',').shift(ORIGIN+0.15*DOWN)
        point_val2 = DecimalNumber(0, show_ellipsis=False, num_decimal_places=2, include_sign=True).add_updater(lambda d: d.set_value(func(x_tracker.get_value()))).shift(ORIGIN+0.75*RIGHT)
        point_val3 = DecimalNumber(0, show_ellipsis=False, num_decimal_places=2, include_sign=True).add_updater(lambda d: d.set_value(x_tracker.get_value())).shift(ORIGIN+0.75*LEFT)
        point_val4 = MathTex(r'(').shift(ORIGIN+1.5*LEFT)

        coords_group1 = VGroup(point_val4, point_val3, point_val1, point_val2,  point_val0).add_updater(lambda g: g.next_to(dot, LEFT))
        coords_group2 = VGroup(point_val4, point_val3, point_val1, point_val2,  point_val0).add_updater(lambda g: g.next_to(dot, RIGHT))

        h_line = always_redraw(lambda :
                               DashedLine(start=self.coords_to_point(0,func(x_tracker.get_value())), end=self.coords_to_point(x_tracker.get_value(), func(x_tracker.get_value())), color=WHITE))
        v_line = always_redraw(lambda :
                               self.get_vertical_line_to_graph(x_tracker.get_value(), graph, line_class=DashedLine, color=WHITE))


        # T-TRACKERS
        # T = Triangle(start_angle=np.pi/2, color=WHITE)
        # T.set_height(MED_SMALL_BUFF).set_fill(WHITE, 1)
        # T.add_updater(lambda t: t.move_to(self.coords_to_point(x_tracker.get_value(),0)))

        # T2 = Triangle(start_angle=2*np.pi, color=WHITE)
        # T2.set_height(MED_SMALL_BUFF).set_fill(WHITE, 1)
        # T2.add_updater(lambda t: t.move_to(self.coords_to_point(0,func(x_tracker.get_value()))))

        # T.move_to(self.coords_to_point(x_tracker.get_value(),0), UP)
        # T2.move_to(self.coords_to_point(0,func(x_tracker.get_value())), RIGHT)

        # ANIMATIONS ------------------------------------------------------------
        self.play(
            Write(coords_group1),
            ShowCreation(h_line),
            ShowCreation(v_line),
            #ShowCreation(T),
            #ShowCreation(T2),
        )
        self.play(
            ShowCreation(graph),
            ShowCreation(dot),
            #Write(point_val0),
            #Write(point_val1),
            #Write(point_val2),
            #Write(point_val3),
            #Write(point_val4),
            #*[Write(elements) for elements in dot_follower]
        )
        self.play(
            x_tracker.animate.set_value(0), run_time=3.5
        )
        self.remove(coords_group1)
        self.add(coords_group2)
        self.play(
            x_tracker.animate.set_value(3), run_time=3.5
        )

        self.wait(1) # FINAL WAIT TIME

class Test2(Scene):
    def construct(self):
    
        self.wait(1) # INITIAL WAIT TIME

        # SETTING UP OF SCENE -----------------------------------------

        step0 = MathTex(r'f(x)',r'=').shift(ORIGIN+2*UP)
        fracline0 = Line(start=ORIGIN+2*UP, end=ORIGIN+1.5*RIGHT+2*UP, stroke_width=2.5).next_to(step0[1], RIGHT)
        step01 = MathTex(r'x^2-9').next_to(fracline0, 0.5*UP)
        step02 = MathTex(r'(x-3)').next_to(fracline0, 0.5*DOWN)

        fracline0_ch = Line(start=ORIGIN, end=ORIGIN+3*RIGHT, stroke_width=2.5).next_to(step0[1], RIGHT)
        step01_ch = MathTex(r'(x-3)',r'(x+3)').next_to(fracline0_ch, 0.5*UP)

        step0_group = VGroup(step0, step01, step02)
        self.play(
            *[Write(elements) for elements in step0_group],
            ShowCreation(fracline0),
        )
        step0_group.add(fracline0)

        self.play(
            Transform(fracline0, fracline0_ch),
            Transform(step01, step01_ch),
            step02.animate.next_to(fracline0_ch, DOWN),
        )

        step0_copy = step0_group.copy()
        self.add(step0_copy)
        self.play(
            step0_group.animate.shift(2*DOWN)
        )

        fracline0_ch2 = Line(start=ORIGIN, end=ORIGIN+1.5*RIGHT, stroke_width=2.5).next_to(step0[1], RIGHT)
        step01_transform = MathTex(r'0',r'(x+3)').next_to(fracline0_ch2, 0.5*UP)
        step02_transform = MathTex(r'0').next_to(fracline0_ch2, 0.5*DOWN)
        self.play(
            Transform(step02, step02_transform),
            Transform(fracline0, fracline0_ch2),
            Transform(step01, step01_transform),
        )

        step0_conclusion = TextMobject("This is ","invalid").next_to(step0_group, DOWN)
        step0_conclusion[1].set_color(BLUE)

        self.play(Write(step0_conclusion))
        self.play(
            FadeOut(VGroup(step0_conclusion, step0_group, step0_copy)),
        )

        # ----------------------------------------------------------------


        self.wait(1) # FINAL WAIT TIME

class Test3(Scene):
    def construct(self):
        limit_expression = self.get_limit_expression()
        limit_expression.shift(2*LEFT)
        limit_expression.to_edge(UP)

        evaluated_expressions = self.get_evaluated_expressions()
        evaluated_expressions.next_to(limit_expression, DOWN, buff = LARGE_BUFF)
        brace = Brace(evaluated_expressions[0][-1], DOWN)
        
        point = VectorizedPoint(limit_expression.get_right())
        expression = VGroup(
            limit_expression[1].copy(), 
            point, point.copy()
        )
        self.add(limit_expression)

        for next_expression in evaluated_expressions:
            next_expression.move_to(evaluated_expressions[0], RIGHT)
            self.play(
                Transform(
                    expression, next_expression,
                ),
            )
            self.wait(0.5)
        self.wait(2)

    def get_limit_expression(self):
        lim = MathTex("\lim_", "{dx", "\\to 0}")
        #lim.set_color_by_tex("dx", self.dx_color)
        ratio = self.get_expression("dx")
        ratio.next_to(lim, RIGHT)
        limit_expression = VGroup(lim, ratio)
        return limit_expression

    def get_evaluated_expressions(self):
        result = VGroup()
        for num_zeros in range(1, 7+1):
            dx_str = "0." + "0"*num_zeros + "1"
            expression = self.get_expression(dx_str)            
            dx = float(dx_str)
            ratio = ((2+dx)**3-2**3)/dx
            ratio_mob = MathTex("%.6f\dots"%ratio)
            group = VGroup(expression, Tex("="), ratio_mob)
            group.arrange(RIGHT)
            result.add(group)
        return result

    def get_expression(self, dx):
        result = MathTex(
            "{(2 + ", str(dx), ")^3 - 2^3 \over", str(dx)
        )
        #result.set_color_by_tex(dx, self.dx_color)
        return result
    
        
        self.wait(1)

class Test4(Scene):
    def construct(self):

        method = TextMobject("Direct Substitution ", "method")
        method[0].set_color(BLUE)

        fx = MathTex("f(","x",")")
        limfx = MathTex("\lim_","{x\\to","a","}")
        limfx.set_color_by_tex("a", YELLOW)
        
        self.play(Write(method))
        self.play(FadeOut(method))
        self.play(Write(fx))
        self.play(FadeOut(fx))
        
        fx.next_to(limfx, RIGHT)
        fxa = MathTex("a").set_color(YELLOW).shift(fx[1].get_center())

        self.play(Write(limfx), Write(fx))
        self.play(
            ReplacementTransform(limfx[-2].copy(), fxa),
            FadeOut(fx[1]),
        )

class Test5(Scene):
    def construct(self):

        x_list = ["3.1", "3.001"]

        def get_expression(x):
            expr = MathTex(
                "f(x)=","(",str(x),"-3)","(",str(x),"+3) \over", "(",str(x),"-3)"
            )
            return expr

        def get_eval_expressions():
            result = VGroup()
            
            exp = get_expression(x_list[0])
            result.add(exp)
            result.arrange(LEFT)
            return result


        eval_exp = get_eval_expressions()
        self.add(eval_exp)


class Test6(Scene):     # ANOTHER WAY TO IMPLEMENT Test3

    def construct(self):

        def get_expression(dx):
            result = MathTex(
                "{(2 + ", str(dx), ")^3 - 2^3 \over", str(dx)
            )
            return result

        def get_limit_expression():
            lim = MathTex("\lim_", "{dx", "\\to 0}")
            #lim.set_color_by_tex("dx", self.dx_color)
            ratio = get_expression("dx")
            ratio.next_to(lim, RIGHT)
            limit_expression = VGroup(lim, ratio)
            return limit_expression

        def get_evaluated_expressions():
            result = VGroup()
            for num_zeros in range(1, 7+1):
                dx_str = "0." + "0"*num_zeros + "1"
                expression = get_expression(dx_str)            
                dx = float(dx_str)
                ratio = ((2+dx)**3-2**3)/dx
                ratio_mob = MathTex("%.6f\dots"%ratio)
                group = VGroup(expression, Tex("="), ratio_mob)
                group.arrange(RIGHT)
                result.add(group)
            return result

            #result.set_color_by_tex(dx, self.dx_color)

        limit_expression = get_limit_expression()
        limit_expression.shift(2*LEFT)
        limit_expression.to_edge(UP)

        evaluated_expressions = get_evaluated_expressions()
        evaluated_expressions.next_to(limit_expression, DOWN, buff = LARGE_BUFF)
        brace = Brace(evaluated_expressions[0][-1], DOWN)
        
        point = VectorizedPoint(limit_expression.get_right())
        expression = VGroup(
            limit_expression[1].copy(), 
            point, point.copy()
        )
        self.add(limit_expression)

        for next_expression in evaluated_expressions:
            next_expression.move_to(evaluated_expressions[0], RIGHT)
            self.play(
                Transform(
                    expression, next_expression,
                ),
            )
            self.wait(0.5)
        self.wait(2)

