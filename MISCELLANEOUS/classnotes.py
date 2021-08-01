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

        half_line = Line(
            plane.coords_to_point(0, 0.5),
            plane.coords_to_point(10, 0.5),
        )
        self.add(half_line)

        random.seed(time.time())
        coin_flips = [1]
        probabilities = [1]
        time_tracker = ValueTracker()
        time_max = 100

        def draw_flip_data(time):
            result = VGroup()

            while len(coin_flips) < time:
                # Add a coin flip
                coin_flips.append(random.choice([1, 0]))
                probabilities.append(coin_flips.count(1) / len(coin_flips))

            # Redraw the graph
            for i, (flip, probability) in enumerate(zip(coin_flips, probabilities)):
                dot = Dot()

                # Color
                if flip == 1:
                    dot.set_color(RED)
                else:
                    dot.set_color(BLUE)

                # Position
                dot.move_to(plane.coords_to_point(i, probability))

                result.add(dot)

            stretch_ratio = 10 / time
            for dot in result:
                dot_center = dot.get_center()
                dot_coords = plane.point_to_coords(dot_center)
                new_x_coord = stretch_ratio * dot_coords[0]
                dot.move_to(plane.coords_to_point(new_x_coord, dot_coords[1]))

            lines = []
            for start, end in zip(result[:-1], result[1:]):
                line = Line(start.get_center(), end.get_center())
                lines.append(line)
            result.submobjects = lines + result.submobjects
            return result

        probability_graph = always_redraw(
            lambda: draw_flip_data(time_tracker.get_value())
        )

        self.add(plane)
        self.add(probability_graph)
        self.play(
            time_tracker.animate.set_value(time_max), run_time=5, rate_func=linear
        )


class PiEstimate(Scene):
    def construct(self):
        scale_factor = 3
        square = Square().scale(scale_factor).set_color(RED)
        circle = Circle().scale(scale_factor).set_color(BLUE)
        group = VGroup(square, circle)
        group.to_edge(LEFT)
        self.add(group)

        points = []
        circle.points_inside_circle = 0
        time_tracker = ValueTracker()
        points_per_second = 80

        circle.pi_estimate = 0

        def update_points(mob):
            while time_tracker.get_value() > len(points) / points_per_second:
                # Add a point
                x_coord = square.get_left()[0] + (random.random() * square.get_width())
                y_coord = square.get_bottom()[1] + (
                    random.random() * square.get_height()
                )
                point = np.array([x_coord, y_coord, 0])
                points.append(point)
                dot = Dot().move_to(point)

                # Test if the dot is inside the cirle
                circle_center = circle.get_center()
                if (
                    scale_factor ** 2
                    >= (point[0] - circle_center[0]) ** 2
                    + (point[1] - circle_center[1]) ** 2
                ):
                    # Point is inside the circle.
                    mob.points_inside_circle += 1
                    dot.set_color(BLUE)
                else:
                    dot.set_color(RED)
                self.add(dot)

                # Update pi calculation
                """
                A_circle = pi * r^2
                A_square = (2r)^2 = 4r^2
                A_circle / A_square = pi / 4
                circle_points / square_points ~ pi / 4
                """
                mob.pi_estimate = 4 * mob.points_inside_circle / len(points)

        pi_is_near = MathTex("\\pi \\approx").shift(RIGHT)
        pi_mobject = DecimalNumber(num_decimal_places=5).next_to(pi_is_near, RIGHT)

        def update_pi_estimate(mob):
            mob.set_value(circle.pi_estimate)
            mob.next_to(pi_is_near, RIGHT)

        pi_mobject.add_updater(update_pi_estimate)
        self.add(pi_is_near, pi_mobject)

        circle.add_updater(update_points)

        time_max = 30

        self.play(
            time_tracker.animate.set_value(time_max),
            rate_func=linear,
            run_time=time_max,
        )
