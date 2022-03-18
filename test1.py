from manim import *

class Test(Scene):
    def construct(self):
        circle = Circle(radius=2.4, color=RED)
        self.play(Create(circle))

class Pith(Scene):
    def construct(self):
        square = Square(side_length=5, stroke_color = GREEN,
        fill_color = BLUE, fill_opacity=0.75)
        self.play(Create(square), run_time=3)
        self.wait()

class Testing(Scene):
    def construct(self):
        name = Text("Daulet").to_edge(UL, buff=0.5)
        square = Square(side_length=0.5, 
            fill_color = GREEN, fill_opacity=0.75).shift(LEFT*3)
        triangle = Triangle().scale(0.6).to_edge(DR)

        self.play(Write(name))
        self.play(DrawBorderThenFill(square), run_time = 2)
        self.play(Create(triangle))
        self.wait()

        self.play(name.animate.to_edge(UR), run_time = 5)
        self.play(square.animate.scale(2), triangle.animate.to_edge(DL), run_time = 5)
        self.wait()

class Getters(Scene):
    def construct(self):
        rect = Rectangle(color = WHITE, height = 3, width=2.5).to_edge(UL)
        circ = Circle().to_edge(DOWN)
        arrow = always_redraw(
            lambda: Line(start=rect.get_bottom(), end=circ.get_top(), buff=0.2).add_tip()
            )
        self.play(Create(VGroup(rect, circ, arrow)))
        self.wait()
        self.play(rect.animate.to_edge(UR), circ.animate.scale(0.5), run_time = 5)
        self.wait()

class Updaters(Scene):
    def construct(self):
        num = MathTex("ln(2)")
        rect = always_redraw(lambda:SurroundingRectangle(num, color=BLUE, fill_color = RED, 
        fill_opacity = 0.4, buff=0.5))
        name = always_redraw(lambda:Tex("Daulet").next_to(rect, DOWN, buff = 0.25))
        self.play(Create(VGroup(num, rect, name)))
        self.wait()
        self.play(num.animate.shift(RIGHT*2), run_time = 2)
        self.wait()

class Tracker(Scene):
    def construct(self):
        k = ValueTracker(5)
        num = always_redraw(lambda: DecimalNumber().set_value(k.get_value()))
        self.play(Create(VGroup(num)))
        self.wait()
        self.play(k.animate.set_value(0), run_time = 5, rate_functions = linear)
        self.wait()

class Graphing(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range = [-4, 4, 2], x_length = 7, y_range = [0, 16, 4], y_length = 8
        ).to_edge(DOWN).add_coordinates()
        labels = plane.get_axis_labels(x_label="x", y_label="f(x)")
        parab = plane.plot(lambda x : x**2, x_range=[-4, 4], color = GREEN)
        func_label = ( 
            MathTex("f(x) = {x}^{2}")
            .scale(0.6).
            next_to(parab, RIGHT, buff=0.5).
            set_color(GREEN)
        )
        self.play(DrawBorderThenFill(plane))
        self.play(Create(VGroup(labels, parab, func_label)))
        self.wait()

class UpdaterGraphing(Scene):
    def construct(self):
        k = ValueTracker(-4)
        ax = (
            Axes(x_range = [-4, 4, 1], y_range = [-2, 16, 2], x_length=10, y_length = 6)
            .to_edge(DOWN)
            .add_coordinates()
        ).set_color(WHITE)
        func = ax.plot(lambda x : x**2, x_range = [-4, 4], color = BLUE)
        slope = always_redraw(lambda:ax.get_secant_slope_group(
            x = k.get_value(), graph=func, dx=0.01, secant_line_color=GREEN, secant_line_length=3
        ))
        
        self.add(ax, func, slope)
        self.wait()
        self.play(k.animate.set_value(4), run_time = 3)
        self.wait()

HOME = "C:\\Users\\lenovo\\ManimFolder\\Test1\\images"
class ImagesDemo(Scene):
    def construct(self):
        im = ImageMobject(f"{HOME}\\task_p-4.png")
        self.play(FadeIn(im), run_time = 5)