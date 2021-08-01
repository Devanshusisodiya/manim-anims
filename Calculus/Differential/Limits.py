from manim import *
import numpy as np

class Limits(GraphScene, MovingCameraScene):
    def setup(self):
        GraphScene.setup(self)
    def construct(self):
        #SUBSIDIARY OF CALCTEST
        self.camera.frame.save_state()
        #config
        self.x_min = 0
        self.x_max = 15
        self.x_axis_width = 7
        self.x_axis_label = "t"
        self.x_labeled_nums = np.arange(self.x_min, self.x_max+1)
        self.y_min = 0
        self.y_max = 10
        self.y_axis_length = 10
        self.y_axis_label = "s"
        self.y_labeled_nums = np.arange(self.y_min, self.y_max+1)
        self.graph_origin = ORIGIN + 3*DOWN + 5*LEFT

        self.wait(1) # INITIAL WAIT TIME

        self.setup_axes(animate=True)

        def func(x):
            L = 10 #curves maximum value
            x_0 = 7.5 #value of sigmoid point
            k = 0.6 #growth rate
            return L/(1+np.exp((-1)*k*(x-x_0)))
        graph = self.get_graph(func, x_min=self.x_min, x_max=self.x_max)
        self.play(
            ShowCreation(graph),
        )

        x_track = ValueTracker(3)
        dx_track = ValueTracker(3)
           
        h_line1 = always_redraw(lambda: DashedLine(start=self.coords_to_point(x_track.get_value(), func(x_track.get_value())),end=self.coords_to_point(0, func(x_track.get_value()))))
        v_line1 = always_redraw(lambda: self.get_vertical_line_to_graph(x_track.get_value(), graph, line_class=DashedLine, color=WHITE))
        h_line2 = always_redraw(lambda: DashedLine(start=self.coords_to_point((x_track.get_value()+dx_track.get_value()), func(x_track.get_value()+dx_track.get_value())),end=self.coords_to_point(0, func(x_track.get_value()+dx_track.get_value()))))
        v_line2 = always_redraw(lambda: self.get_vertical_line_to_graph((x_track.get_value()+dx_track.get_value()), graph, line_class=DashedLine, color=WHITE))

        line_group = VGroup(v_line1, v_line2, h_line1, h_line2,)
        self.play(
            ShowCreation(line_group),
        )

        self.play(
            x_track.animate.set_value(4),
            #xdx_track.animate.set_value(7),
            run_time=2
        )

        slope = always_redraw(lambda:
                              self.get_secant_slope_group(x_track.get_value(), graph, dx=dx_track.get_value(), dx_line_color=YELLOW, df_line_color=YELLOW, secant_line_length=5))
        self.play(ShowCreation(slope))
        
        dval = DecimalNumber(0,
                                show_ellipsis=False,
                                num_decimal_places=2).add_updater(lambda d: d.set_value(func(x_track.get_value()+dx_track.get_value())-func(x_track.get_value())))
        dval_label = Tex("distance =")
        dgroup = VGroup(dval_label, dval)
        dgroup.arrange(RIGHT)
        dgroup.add_updater(lambda g: g.next_to(self.coords_to_point((x_track.get_value()+dx_track.get_value()),func(x_track.get_value())+(func(dx_track.get_value()))/2)))
        self.play(Write(dgroup))
        self.wait(1)

        self.play(
            x_track.animate.set_value(10),
            run_time=2
        )
        self.play(
            FadeOut(line_group),
            FadeOut(dgroup),
            FadeOut(slope),
        )

        zoom_coord_x = 10
        self.play(self.camera.frame.animate.scale(0.2).move_to(self.coords_to_point(zoom_coord_x,0)))
        self.wait(1)
        indicate_rect = Square(side_length=0.5, color=YELLOW).shift(self.coords_to_point(zoom_coord_x,-0.7))
        self.play(ShowCreation(indicate_rect))   
        self.wait(0.5)
        self.play(FadeOut(indicate_rect))
        self.play(Restore(self.camera.frame))


        self.play(ShowCreation(line_group))
        self.play(ShowCreation(slope))
        self.play(dx_track.animate.set_value(0.5), run_time=0.5)
        self.wait(1)
        
        speed_eq = Tex("speed ","=").shift(ORIGIN+4*RIGHT)
        speed_line = Line(start=ORIGIN, end=ORIGIN+RIGHT, stroke_width=2.5).next_to(speed_eq[1], RIGHT)
        speed_df = DecimalNumber(0, num_decimal_places=2).add_updater(lambda d: d.set_value(func(x_track.get_value()+dx_track.get_value())-func(x_track.get_value()))).next_to(speed_line, UP, buff=0.1)
        speed_dx = DecimalNumber(0, num_decimal_places=1).add_updater(lambda d: d.set_value((x_track.get_value()+dx_track.get_value())-x_track.get_value())).next_to(speed_line, DOWN, buff=0.1)
        speed_group = VGroup(speed_df, speed_line, speed_dx)

        ds_dt = MathTex(
            r"\frac{ds}{dt}"
        ).next_to(speed_eq[1], RIGHT)
        #speed_res = DecimalNumber(0, num_decimal_places=2).add_updater(lambda d: d.set_value(speed_df.get_value()/speed_dx.get_value())).next_to(speed_line, RIGHT)
        self.play(
            Write(speed_eq),
            Write(speed_group)
        )

        self.wait(1)
        self.play(dx_track.animate.set_value(0.1), run_time=3)
        self.wait(1) # FINAL DELAY

        self.play(
            FadeOut(speed_group),
            Write(ds_dt)
        )

        self.wait(1) # FINAL WAIT TIME

        ### WRITE COMMENTS TO KEEP TRACK OF WHAT IS HAPPENING