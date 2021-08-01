from manim import *
import numpy as np

class Test(Scene):
    def construct(self):
        self.wait(1)

        machine_box = Rectangle(height=1, width=2 , color=BLUE, stroke_width=5)
        machine_text = TexMobject(r"\text{Machine}(", r"f", r")")
        machine_text_replace = TexMobject(r"\text{Machine}(", r"g", r")")
        machine_text.next_to(machine_box, UP)
        machine_text_replace.next_to(machine_box, UP)


        self.play(
            FadeIn(machine_box),
            Write(machine_text)
        )

        for inp, out in zip([r'2',r'3',r'5', r'x'], [r'4',r'6',r'10',r'2x']):
            # SETTING UP OF SCENE --------------------------------------
            machine_in = TexMobject(inp)
            machine_out = TexMobject(out)

            machine_in.shift(3*LEFT)
            machine_out.shift(ORIGIN)
            # INNER ANIMATIONS ------------------------------------------------
            self.play(Write(machine_in))
            self.play(machine_in.animate.shift(3*RIGHT))
            self.play(Transform(machine_in, machine_out))
            self.play(machine_in.animate.shift(3*RIGHT))
            self.play(FadeOut(machine_in))

        self.wait(1)

        mathway_text = Tex("Mathematical way of writing functions ").shift(ORIGIN+2*UP+2*LEFT)
        fx_text = MathTex("f(x)=2x").next_to(mathway_text, RIGHT)
        fx_text[0].set_color(BLUE)

        self.play(Write(mathway_text),)
        self.play(ReplacementTransform(machine_box.copy(), fx_text),)
        self.play(FadeOut(mathway_text), FadeOut(fx_text))
        self.wait(1)

        self.play(Transform(machine_text[1], machine_text_replace[1]))

        gx_text = MathTex("g(x)=x^2+2").shift(ORIGIN+2*UP)
        gx_text[0].set_color(BLUE)
        
        self.play(Write(gx_text))

        for inp, out in zip([r'2',r'3'], [r'6',r'11']):
            # SETTING UP OF SCENE --------------------------------------
            machine_in = TexMobject(inp)
            machine_out = TexMobject(out)

            machine_in.shift(3*LEFT)
            machine_out.shift(ORIGIN)
            # INNER ANIMATIONS ------------------------------------------------
            self.play(Write(machine_in))
            self.play(machine_in.animate.shift(3*RIGHT))
            self.play(Transform(machine_in, machine_out))
            self.play(machine_in.animate.shift(3*RIGHT))
            self.play(FadeOut(machine_in))

class Test2(Scene):
    def construct(self):
        self.wait(1)

        funcdef_text1 = Tex(
            "A ", "mathematical relation",
        )
        funcdef_text2 = Tex(
            "which gives ", "more than one output ", "for a ", "given input",
        )
        funcdef_text3 = Tex(
            "cannot ","be called a function",
        )
        funcdef_text1.set_color_by_tex("mathematical relation", YELLOW)
        funcdef_text2.set_color_by_tex("more than one output", BLUE)
        funcdef_text2.set_color_by_tex("given input", BLUE)
        funcdef_text3.set_color_by_tex("cannot", RED)

        funcdef_text1.shift(ORIGIN+2*UP)
        funcdef_text2.next_to(funcdef_text1, DOWN)
        funcdef_text3.next_to(funcdef_text2, DOWN)

        self.play(Write(funcdef_text1))
        self.play(Write(funcdef_text2))
        self.play(Write(funcdef_text3))
        self.play(FadeOut(funcdef_text1), FadeOut(funcdef_text2), FadeOut(funcdef_text3))

        def get_fxexp(rhs):
            eq_lhs = MathTex("f(x)=")
            fx_group = VGroup(eq_lhs, rhs)
            fx_group.arrange(RIGHT)
            return fx_group

        fx_rhs = MathTex("\\sqrt{x }")
        fx_exp = get_fxexp(fx_rhs)
        self.play(Write(fx_exp))

        for input in [r"\sqrt{9}", r"\pm3"]:
            rhs = MathTex(input)
            fx_expch = get_fxexp(rhs)
            self.play(Transform(fx_exp, fx_expch))
            self.wait(0.5)

        conc_text1 = Tex(
            "This relation gives ", "+3 ", "and ", "-3"
        )
        conc_text2 = Tex(
            "for the same input value ", "9"
        )
        conc_text1[1].set_color(YELLOW)
        conc_text1[-1].set_color(YELLOW)
        conc_text2[-1].set_color(YELLOW)
        conc_text_group = VGroup(conc_text1, conc_text2).arrange(DOWN).shift(ORIGIN+2*UP)

        self.play(Write(conc_text_group))
        self.play(conc_text_group.animate.move_to(ORIGIN), FadeOut(fx_exp))
        self.play(FadeOut(conc_text_group))

        self.wait(1)

class Test3(GraphScene):
    def construct(self):
        self.wait(1)
        #config
        self.x_min = -5
        self.x_max = 5
        self.x_axis_width = 8
        self.y_min = -20
        self.y_max = 30
        self.y_axis_height = 7
        self.graph_origin = ORIGIN+DOWN

        self.setup_axes(animate=True)

        def linear(x):
            a=2
            b=5
            return a*x+b
        def quadratic(x):
            a=1
            b=-5
            c=6
            return a*x**2 + b*x + c
        def cubic(x):
            a=-4
            b=3
            c=20
            d=6
            return a*x**3 + b*x**2 + c*x + d

        graph_lin = self.get_graph(linear, x_min=self.x_min, x_max=self.x_max)
        graph_lin_label = self.get_graph_label(graph_lin, label="f(x)=2x+5", x_val=self.x_max, direction=UP)
        graph_lin_label.scale(0.7)
        graph_quad = self.get_graph(quadratic, x_min=-2.5, x_max=self.x_max)
        graph_quad_label = self.get_graph_label(graph_quad, label="f(x)=x^2-5x+6", x_val=self.x_max, direction=UP)
        graph_quad_label.scale(0.7)
        graph_cube = self.get_graph(cubic, x_min=-2, x_max=self.x_max-2.2, color=RED)
        graph_cube_label = self.get_graph_label(graph_cube, label="f(x)=-4x^3+3x^2+20x+6", x_val=-2, direction=LEFT+UP)
        graph_cube_label.scale(0.7)

        self.play(
            ShowCreation(graph_lin),
            Write(graph_lin_label))
        self.play(
            ReplacementTransform(graph_lin, graph_quad),
            ReplacementTransform(graph_lin_label, graph_quad_label))
        self.play(
            ReplacementTransform(graph_quad, graph_cube),
            ReplacementTransform(graph_quad_label, graph_cube_label))

        self.wait(1)