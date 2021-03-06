from manim import *

class OpeningManim(Scene):
    def construct(self):
        title = Tex(r"This is some \LaTeX")
        basel = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}")
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeIn(basel, shift=DOWN),
        )
        self.wait()

        transform_title = Tex("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*(FadeOut(obj, shift=DOWN) for obj in basel)),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = Tex("This is a grid", font_size=72)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeIn(grid_title, shift=UP),
            Create(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()
        
class UsingBraces(Scene):
    #Using braces to group text together
    def construct(self):
        eq1A = Text("4x + 3y")
        eq1B = Text("=")
        eq1C = Text("0")
        eq2A = Text("5x -2y")
        eq2B = Text("=")
        eq2C = Text("3")
        eq1B.next_to(eq1A,RIGHT)
        eq1C.next_to(eq1B,RIGHT)
        eq2A.shift(DOWN)
        eq2B.shift(DOWN)
        eq2C.shift(DOWN)
        eq2A.align_to(eq1A,LEFT)
        eq2B.align_to(eq1B,LEFT)
        eq2C.align_to(eq1C,LEFT)

        eq_group=VGroup(eq1A,eq2A)
        braces=Brace(eq_group,LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.add(eq1A, eq1B, eq1C)
        self.add(eq2A, eq2B, eq2C)
        self.play(GrowFromCenter(braces),Write(eq_text))

class PositioningDemo(Scene):
    def construct(self):
        plane = NumberPlane()

        #next_to
        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN)
        green_dot.next_to(red_dot, RIGHT+UP)

        #shift
        s = Square(color = ORANGE)
        s.shift(2*UP + 4*RIGHT)

        #move_to
        c = Circle(color = PURPLE)
        c.move_to([-3,-2,0])

        #align_to
        c2 = Circle(radius = 0.5, color = RED, fill_opacity=0.5)
        c3 = c2.copy().set_color(YELLOW)
        c4 = c2.copy().set_color(ORANGE)
        c2.align_to(s, UP)
        c3.align_to(s, RIGHT)
        c4.align_to(s, UP+RIGHT)

        self.add(plane)
        self.add(red_dot, green_dot)
        self.add(s)
        self.add(c)
        self.add(c2,c3,c4)

class CriticalPoints(Scene):
    def construct(self):
        c = Circle(color = GREEN, fill_opacity = 0.5)
        self.add(c)

        for d in [[0,0,0], UP, UR, RIGHT, DR, DOWN, DL, LEFT, UL]:
            self.add(Cross(scale_factor=0.2).move_to(c.get_critical_point(d)))

        s = Square(color = RED, fill_opacity = 0.5)
        s.move_to([1,0,0], aligned_edge=LEFT)
        self.add(s)

class GroupingDemo(Scene):
    def construct(self):
        red_dot = Dot(color = RED)
        yellow_dot = Dot(color = YELLOW).next_to(red_dot, RIGHT)
        blue_dot = Dot(color = BLUE).next_to(red_dot, DOWN)
        dot_groups = VGroup(red_dot, yellow_dot, blue_dot)
        dot_groups.to_edge(RIGHT)
        self.add(dot_groups)

        circles = VGroup(*[Circle(radius=0.2) for _ in range(10)])
        circles.arrange(UP)
        self.add(circles)

        stars = VGroup(*[Star(color=YELLOW, fill_opacity=0.5).scale(0.2) for _ in range(20)])
        stars.arrange_in_grid(4, 5, buff=0.2).to_edge(LEFT)
        self.add(stars)

import numpy as np
from colour import Color
class BasicAnimationDemo(Scene):
    def construct(self):
        polys = VGroup(
            *[RegularPolygon(5, radius = 1, fill_opacity=0.5,
            color = Color(hue=j/5, saturation=1, luminance=0.5)) for j in range(5)]
        ).arrange(RIGHT)
        
        self.play(DrawBorderThenFill(polys), run_time = 2)
        self.play(
            Rotate(polys[0], PI, rate_func = linear),
            Rotate(polys[1], PI, rate_func = smooth),
            Rotate(polys[2], PI, rate_func = lambda t : np.sin(t*PI)),
            Rotate(polys[3], PI, rate_func = there_and_back),
            Rotate(polys[4], PI, rate_func = lambda t : 1 - abs(1-2*t)),
            run_time = 2
        )
        self.wait()

class LaggingGroupDemo(Scene):
    def construct(self):
        squares = VGroup(*[Square(color = Color(hue = j/20, saturation=1, luminance=0.5),
        fill_opacity=0.5) for j in range(20)]).arrange_in_grid(4,5).scale(0.75)

        self.play(AnimationGroup(*[FadeIn(s) for s in squares], lag_ratio = 0.15))

class AnimateMethodDemo(Scene):
    def construct(self):
        s = Square(color = ORANGE, fill_opacity = 0.5)
        c = Circle(color = GREEN, fill_opacity = 0.5)
        self.add(s, c)
        self.play(s.animate.shift(UP), c.animate.shift(DOWN), run_time = 3)
        self.play(VGroup(s, c).animate(run_time=3).arrange(RIGHT, buff=1))
        self.play(c.animate(rate_funct=linear).shift(RIGHT).scale(2))

class UpdaterDemo(Scene):
    def construct(self):
        red_dot = Dot(color=RED).shift(RIGHT)
        pointer = Arrow(ORIGIN, RIGHT).next_to(red_dot, LEFT)
        pointer.add_updater(lambda mobj: mobj.next_to(red_dot, LEFT))

        self.play(Create(red_dot), Create(pointer))
        self.play(red_dot.animate.shift(3*UP+5*RIGHT).scale(2), run_time=3)

class ValueTrackerDemo(Scene):
    def construct(self):
        line = NumberLine(x_range = [-5, 5])
        position = ValueTracker(0)
        pointer = Vector(DOWN).next_to(line, UP)
        self.add(line, pointer)

        pointer.add_updater(lambda mobj:mobj.next_to(line.number_to_point(position.get_value()), UP))
        
        self.wait()
        self.play(position.animate.set_value(4))
        self.play(position.animate.set_value(-2))

class ValueTrackerPlot(Scene):
    def construct(self):
        a = ValueTracker(1)
        ax = Axes(x_range=[-2, 2, 1], y_range = [-8.5, 8.5, 1], x_length = 4, y_length = 6)
        parabola = ax.plot(lambda x : x**2, color = RED)
        parabola.add_updater(
            lambda mob:mob.become(ax.plot(lambda x: a.get_value()*x**2, color=RED))
        )

        a_number = DecimalNumber(
            a.get_value(),
            color=RED,
            num_decimal_places=3,
            show_ellipsis=True
        )
        a_number.add_updater(
            lambda mob:mob.set_value(a.get_value()).next_to(parabola, RIGHT)
        )

        self.add(ax, parabola, a_number)
        self.play(a.animate(run_time=5).set_value(2))
        self.play(a.animate.set_value(-2))
        self.play(a.animate.set_value(1))
