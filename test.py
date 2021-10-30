from manim import *

class Test(Scene):
    def construct(self):
        # SETUP AXES CONDITIONS LATER
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=5,
            y_length=5,
            x_axis_config={
                "numbers_to_include": np.arange(0, 5),
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 5),
            },
            tips=False,
        )

        self.wait(1)

        intro = Tex('\\text{This video is ','Calculus',' in a nutshell}').shift(ORIGIN)
        intro[1].set_color(BLUE)
        self.play(Write(intro))
        self.play(FadeOut(intro))

        diff_text = Tex('\\text{Differentiation}').set_color(BLUE).shift(ORIGIN)
        self.play(Write(diff_text))

        x = ValueTracker(1.5)
        dx = ValueTracker(0.5)

        # DIFFERENTIATTION
        def poly(x):
            return 0.1*(x + 3-5)*(x - 3-5)*(x-5)
        def sq(x):
            return x**2

        self.play(Transform(diff_text, axes))
        graph = axes.get_graph(sq, x_range=[0,3], color=BLUE).scale(0.7)
        slope = always_redraw(lambda: axes.get_secant_slope_group(x.get_value(), graph, dx=dx.get_value(), include_secant_line=False))
        self.play(Create(graph))
        # self.play(Create(slope))
        # ----------------

        # INTEGRATION
        # -----------

        self.wait(1) # FINAL WAIT TIME