from manim import *
from numpy import dot

# GRAPHICAL SOLUTIONS ANIMS

class LinEq1(Scene):
    def construct(self):

        # INTRO ANIM
        intro = MathTex(
            "\\text{Linear equations in ", "two variables}"
        ).shift(ORIGIN)
        intro[1].set_color(BLUE)

        self.play(Write(intro))
        self.play(FadeOut(intro[0]))
        self.wait(1)

        # FIRST ANIM

        eq_list = ["3", "x", "+", "2", "y", "+", "6", "=", "0"]
        eq = MathTex(*eq_list).shift(ORIGIN)

        example_text = MathTex(
            "\\text{for example, the equation below}"
        ).shift(ORIGIN+2*UP)

        self.play(Transform(intro[1], VGroup(eq[1], eq[4])))
        self.play(
            Write(example_text),
            Write(eq),
            FadeOut(intro[1])
        )
        self.play(
            Indicate(VGroup(eq[-1], eq[-2])),
        )
        self.play(
            eq.animate.shift(3*RIGHT+2*UP),
            FadeOut(example_text)
        )

        eq_rect = SurroundingRectangle(eq)
        self.play(Create(eq_rect))

        
        # SECOND ANIM

        def func(x):
            return (-6-3*x)/2

        ax = Axes(x_length=7).shift(2*LEFT)
        graph = ax.get_graph(func, x_range=(-4, 0),color=PURPLE_B)
        self.play(Create(ax))

        x = ValueTracker(0)
        y = ValueTracker(0)

        x_num_label = MathTex("x=").shift(4*RIGHT + UP)
        y_num_label = MathTex("y=").next_to(x_num_label, DOWN)
        
        x_num = (
            DecimalNumber(
                num_decimal_places=2,
                include_sign=True,
            )
            .next_to(x_num_label, RIGHT)
            .add_updater(lambda num: num.set_value(x.get_value()))   
        )

        y_num = (
            DecimalNumber(
                num_decimal_places=2,
                include_sign=True,
            )
            .next_to(y_num_label, RIGHT)
            .add_updater(lambda num: num.set_value(y.get_value()))
        )
        
        self.play(Write(VGroup(x_num_label, y_num_label, x_num, y_num)))
        
        dot = Dot(
            ax.c2p(0, 0)
        ).add_updater(lambda d: d.move_to(ax.c2p(x.get_value(), y.get_value())))

        self.play(Create(dot))

        temp_dot_group = VGroup()
        for _x,_y in [(0, -3), (-2, 0), (-4, 3)]:
            self.play(
                x.animate.set_value(_x),
                y.animate.set_value(_y)
            )
            temp_dot = Dot(ax.c2p(_x, _y))
            temp_dot_group.add(temp_dot)
            self.add(temp_dot)
            self.wait(1.5)

        self.play(Create(graph))
        self.play(
            FadeOut(VGroup(x_num_label, y_num_label, x_num, y_num, dot, temp_dot_group, eq_rect)),
            eq.animate.scale(0.7).next_to(graph, UP+0.5*LEFT)
        )

        self.play(FadeOut(VGroup(ax, graph, eq)))

        # SECOND ANIM

        conclusion1 = MathTex('\\text{but this line can have\n inifinitely many solutions}')
        example_text2 = MathTex('\\text{So, lets look at another example}')
        conclusion1.shift(ORIGIN)
        example_text2.next_to(conclusion1, DOWN)

        self.play(Write(conclusion1))
        self.play(Write(example_text2))
        self.play(FadeOut(VGroup(conclusion1, example_text2)))

        
        eq2 = MathTex("2","x","+","3","y","+","6","=","0").shift(ORIGIN)
        eq3 = MathTex("x","-","2","y","+","8","=","0").next_to(eq2, 1.5*DOWN)

        self.play(
            Write(eq2),
            Write(eq3)
        )
        self.play(
            VGroup(eq2, eq3)
            .animate
            .shift(4*RIGHT)
        )

        eq2_rect = SurroundingRectangle(eq2)
        eq3_rect = SurroundingRectangle(eq3)

        def func2(x):
            return (-6-2*x)/3
        def func3(x):
            return (x+8)/2


        ax2 = Axes(x_range=(-8, 4), y_range=(-4, 5), x_length=7, y_length=5).shift(2*LEFT)
        graph2 = ax2.get_graph(func2, x_range=(-8, 3), color=PURPLE_A)
        graph3 = ax2.get_graph(func3, x_range=(-7, 3), color=PURPLE_C)


        self.play(Create(ax2))

        self.play(Create(eq2_rect))
        self.play(FadeOut(eq2_rect))
        self.play(
            eq2
            .animate
            .scale(0.5)
            .move_to(ax2.c2p(-8, 4)),
            Create(graph2)
        )

        self.play(Create(eq3_rect))
        self.play(FadeOut(eq3_rect))
        self.play(
            eq3
            .animate
            .scale(0.5)
            .move_to(ax2.c2p(3, 6)),
            Create(graph3)
        )

        x.set_value(0)
        y.set_value(0)

        dot2 = Dot(
            ax2.c2p(0,0)
        ).add_updater(lambda d: d.move_to(ax2.c2p(x.get_value(), y.get_value())))

        self.play(Create(dot2)) 

        for _x,_y in [(0,-2),(-3,0),(0,4),(-36/7,10/7)]:
            self.play(
                x.animate.set_value(_x),
                y.animate.set_value(_y)
            )
            self.wait(1.5)

        dot_rect = SurroundingRectangle(dot2)
        sol_text = MathTex("\\text{So, solution is}").shift(4*RIGHT+2*UP)
        sol_x = MathTex("x=", "-\\frac{36}{7}").next_to(sol_text, 3*DOWN)
        sol_y = MathTex("y=", "\\frac{10}{7}").next_to(sol_x, DOWN)

        self.play(Write(sol_text))
        self.play(Create(dot_rect))
        self.play(FadeOut(dot_rect))
        self.play(ReplacementTransform(dot2, VGroup(sol_x, sol_y)))

        self.wait(2)


# ALGEBRAIC SOLUTIONS ANIMS


class Substitution(Scene):
    def construct(self):

        self.wait(1) # INITIAL WAIT TIME

        # SUBSTITUTION METHOD

        # SCENE 1
        eq1_list = ['3','x','-','2','y','+','12','=','0']

        eq1 = MathTex(*eq1_list).shift(ORIGIN)
        eq2 = MathTex('4','x','-','y','+','8','=','0').next_to(eq1, 1.5*DOWN)

        self.play(
            Write(eq1),
            Write(eq2)
        )
        self.play(
            VGroup(eq1, eq2).animate.scale(0.7).to_corner(UL)
        )


        eq1_label = MathTex("...i").scale(0.7).next_to(eq1, 2*RIGHT)
        eq2_label = MathTex("...ii").scale(0.7).next_to(eq2, 2*RIGHT)
        eq1_rect = SurroundingRectangle(eq1)
        eq2_rect = SurroundingRectangle(eq2)

        self.play(
            Create(eq1_rect),
            Create(eq2_rect)
        )
        self.play(
            ReplacementTransform(eq1_rect, eq1_label),
            ReplacementTransform(eq2_rect, eq2_label)
        )

        eq1_0 = MathTex(*eq1_list).shift(2*UP)
        self.play(Write(eq1_0)) 
        
        # getting value of y in terms of x
        
        eq1_0group = VGroup()
        eq1_0group.add(eq1_0[:2].copy())
        self.play(
            eq1_0group[0].animate.next_to(eq1_0[1], DOWN)
        )
        eq1_0group.add(eq1_0[5:8].copy())
        self.play(
            eq1_0group[1].animate.next_to(eq1_0group[0], RIGHT)
        )
        eq1_0group.add(eq1_0[3:5].copy())
        self.play(
            eq1_0group[2].animate.next_to(eq1_0group[1], RIGHT)
        )

        eq_y = MathTex("\\frac{3x+12}{2}","=","2","y").next_to(eq1_0group, DOWN)
        
        self.play(
            ReplacementTransform(eq1_0group[:2].copy(), eq_y[0][:5]),
            Create(eq_y[0][-2]),
        )
        self.play(
            Create(eq_y[1]),
            ReplacementTransform(eq1_0group[2].copy(), eq_y[2:])
        )
        self.play(
            ReplacementTransform(eq_y[-2], eq_y[0][-1])
        )

        # derived y in terms of x
        
        eq_y_rect = SurroundingRectangle(eq_y)
        self.play(Create(eq_y_rect))
        self.play(
            eq_y.animate.scale(0.7).to_edge(LEFT),
            FadeOut(eq_y_rect)
        )
        eq_y_label = MathTex("...iii").scale(0.7).next_to(eq_y, 2*RIGHT)
        self.play(Write(eq_y_label))

        self.play(FadeOut(VGroup(eq1_0group, eq1_0)))

        # putting derived y into second equation

        eq2_list = ['4','x','-','\\frac{(3x+12)}{2}','+','8','=','0']
        
        eq2_0 = MathTex(*eq2_list).shift(2*UP)
        step0 = MathTex("\\text{On taking LCM}").next_to(eq2_0, DOWN)
        eq2_1 = MathTex("\\frac{8x-(3x+12)+16}{2}", "=", "0").next_to(step0, DOWN)

        self.play(Write(eq2_0))
        self.play(Write(step0))
        self.play(FadeOut(step0))
        self.play(Write(eq2_1))
        self.play(
            ReplacementTransform(eq2_1[0][-1].copy(), eq2_1[-1]),
            FadeOut(VGroup(eq2_1[0][-2], eq2_1[0][-1])),
            eq2_1[0][:13].animate.next_to(eq2_1[-2], LEFT)
        )
        self.play(VGroup(eq2_1[0][:13], eq2_1[-2], eq2_1[-1]).animate.next_to(eq2_0, DOWN))
        


        self.wait(2) # FINAL WAIT TIME