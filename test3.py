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
