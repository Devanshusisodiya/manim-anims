from manim import *
import random
import time


class CoinFlip(Scene):
    def construct(self):
        plane_config = dict(
            axis_config={
                "include_tip": True,
                "include_numbers": True,
                "include_ticks": True,
                "line_to_number_buff": 0.05,
                "stroke_color": WHITE,
                "stroke_width": 0.5,
                "number_scale_val": 0.4,
                "tip_scale": 0.5,
            },
            x_axis_config={
                "exclude_zero_from_default_numbers": True,
                "label_direction": DOWN,
                "stroke_color": WHITE,
                "x_min": 0,
                "x_max": 10,
                "unit_size": 1,
                # "numbers_to_show": range(0, 6, 1),
                "numbers_to_show": [],
            },
            y_axis_config={
                "exclude_zero_from_default_numbers": True,
                "label_direction": UR,
                "stroke_color": WHITE,
                "x_min": 0,  # not y_min
                "x_max": 1,  # not y_max
                "unit_size": 6,
                "numbers_to_show": [0, 1],
            },
            background_line_style={
                "stroke_width": 1,
                "stroke_opacity": 0.75,
                "stroke_color": GREEN_A,
            },
        )
        plane = NumberPlane(**plane_config)
        plane.to_edge(RIGHT).shift(DOWN * 3)
        self.add(plane)

        coin_flips = []
        time_tracker = ValueTracker()
        dots_per_second = 10

        half_line = Line(plane.coords_to_point(0, 0.5), plane.coords_to_point(10, 0.5))
        self.add(half_line)

        random.seed(time.time())

        def draw_graph(time):
            while len(coin_flips) < time * dots_per_second:
                coin_flips.append(random.choice([0, 0, 1]))

            graph = VGroup()
            for i, flip in enumerate(coin_flips):
                dot = Dot()

                # Compute cumulative probability
                probability = coin_flips[: i + 1].count(1) / len(coin_flips[: i + 1])

                # Color
                if coin_flips[i] == 1:
                    dot.set_color(RED)
                else:
                    dot.set_color(BLUE)

                # Position
                dot.move_to(plane.coords_to_point(i, probability))
                graph.add(dot)

            stretch_ratio = 10 / (time * dots_per_second)
            for dot in graph:
                current_coords = plane.point_to_coords(dot.get_center())
                current_x = current_coords[0]
                dot.move_to(
                    plane.coords_to_point(current_x * stretch_ratio, current_coords[1])
                )

            lines = []
            for start, end in zip(graph[:-1], graph[1:]):
                line = Line(start.get_center(), end.get_center())
                lines.append(line)
            graph.submobjects = lines + graph.submobjects

            return graph

        graph = always_redraw(lambda: draw_graph(time_tracker.get_value()))

        self.add(graph)

        self.play(time_tracker.animate.set_value(10), run_time=10, rate_func=linear)


class PiEstimate(Scene):
    def construct(self):
        scale_factor = 3
        square = Square().scale(scale_factor).set_color(RED)
        circle = Circle().scale(scale_factor).set_color(BLUE)
        group = VGroup(square, circle)
        self.add(group)

        time_tracker = ValueTracker()
        points = []
        points_per_second = 200
        square.points_inside_circle = 0
        square.pi_estimate = 0

        def update_points(mob):
            while len(points) < time_tracker.get_value() * points_per_second:
                # Add a new point
                square_left = square.get_left()[0]
                square_bottom = square.get_bottom()[1]
                square_bottom_left = RIGHT * square_left + UP * square_bottom

                sample_x_val = random.random() * square.get_width()
                sample_y_val = random.random() * square.get_height()
                dot_postition = square_bottom_left + np.array(
                    [sample_x_val, sample_y_val, 0]
                )
                dot = Dot().move_to(dot_postition)

                """
                circle equation: 3^2 = x^2 + y^2
                3^2 >= px^2 + py^2
                """
                if 3 ** 2 >= dot_postition[0] ** 2 + dot_postition[1] ** 2:
                    dot.set_color(BLUE)
                    mob.points_inside_circle += 1
                else:
                    dot.set_color(RED)
                points.append(dot_postition)

                """
                A_square = s^2
                A_circle = pi * (s/2)^2
                A_circle / A_square = pi * (s/2)^2 / s^2
                                    = pi / 4
                """
                mob.pi_estimate = 4 * mob.points_inside_circle / len(points)
                self.add(dot)

        pi_approx = MathTex("\\pi \\approx").next_to(square, RIGHT)
        pi_mob = DecimalNumber().next_to(pi_approx, RIGHT)

        def update_pi_estimate(mob):
            mob.set_value(square.pi_estimate)

        pi_mob.add_updater(update_pi_estimate)
        self.add(pi_approx, pi_mob)

        square.add_updater(update_points)

        self.play(time_tracker.animate.set_value(10), rate_func=linear, run_time=10)
