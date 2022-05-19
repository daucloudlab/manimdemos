from manim import *

class ManimCELogo(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_m = MathTex(r'\mathbb{M}', fill_color = logo_black).scale(7)
        ds_m.shift(2.25*LEFT + 1.5*UP)

        circle = Circle(color = logo_green, fill_opacity = 1).shift(LEFT)
        square = Square(color = logo_blue, fill_opacity = 1).shift(UP)
        triangle = Triangle(color = logo_red, fill_opacity=1).shift(RIGHT)

        logo = VGroup(triangle,  square, circle, ds_m)
        logo.move_to(ORIGIN)

        self.add(logo)

class BraceAnnotation(Scene):
    def construct(self):
        dot1 = Dot([-2, -1, 0])
        dot2 = Dot([2, 1, 0])
        line = Line(start=dot1.get_center(), end = dot2.get_center()).set_color(ORANGE)
        b1 = Brace(line)
        b1_text = b1.get_text("Horizontal distance")
        
        b2 = Brace(line, direction=line.copy().rotate(PI/2).get_unit_vector())
        b2_text = b2.get_tex("x-x_1")
        self.add(dot1, dot2, line, b1, b1_text, b2, b2_text)

class VectorArrow(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN, [2,2,0], buff=0)
        numberplane = NumberPlane()
        origin_text = Text("(0,0)").next_to(dot, DOWN)
        tip_text = Text("(2,2)").next_to(arrow.get_end(), UP)
        self.add(numberplane, dot, arrow, origin_text, tip_text)

class BooleanOperations(Scene):
    def construct(self):
        ellipse1 = Ellipse(
            width = 4, height = 5, fill_opacity = 0.5, color = BLUE, stroke_width = 10
        ).move_to(LEFT)
        ellipse2 = ellipse1.copy().set_color(RED).move_to(RIGHT)
        bool_ops_text = MarkupText("<u>Boolean Operation</u>").next_to(ellipse1, UP*3)
        ellipse_group = Group(bool_ops_text, ellipse1, ellipse2).move_to(3*LEFT)
        self.play(FadeIn(ellipse_group))

        i = Intersection(ellipse1, ellipse2, color = GREEN, fill_opacity=0.5)
        self.play(i.animate.scale(0.25).move_to(RIGHT*5+UP*2.5))
        intersection_text = Text("Intersection", font_size=23).next_to(i, UP)
        self.play(FadeIn(intersection_text))

        u = Union(ellipse1, ellipse2, color=ORANGE, fill_opacity=0.5)
        union_text = Text("Union", font_size=23)
        self.play(u.animate.scale(0.3).next_to(i, DOWN, buff=union_text.height*3))
        union_text.next_to(u, UP)
        self.play(FadeIn(union_text))

        e = Exclusion(ellipse1, ellipse2, color = YELLOW, fill_opacity = 0.5)
        exclusion_text = Text("Exclusion", font_size = 23)
        self.play(e.animate.scale(0.3).next_to(u, DOWN, buff=exclusion_text.height*3.5))
        exclusion_text.next_to(e, UP)
        self.play(FadeIn(exclusion_text))

        d = Difference(ellipse1, ellipse2, color = PINK, fill_opacity=0.5)
        difference_text = Text("Difference", font_size = 23)
        self.play(d.animate.scale(0.3).next_to(u, LEFT, buff = difference_text.height*3.5))
        difference_text.next_to(d, UP)
        self.play(FadeIn(difference_text))


class PointMovingOnShapes1(Scene):
    def construct(self):
        circle = Circle(radius = 1, color = BLUE)
        dot = Dot()
        dot2 = dot.copy().shift(RIGHT)
        self.add(dot)

        line = Line([3, 0, 0],[5, 0, 0])
        self.add(line)

        self.play(GrowFromCenter(circle))
        self.play(Transform(dot, dot2))
        self.play(MoveAlongPath(dot, circle), run_time = 2, rate_func = linear)
        self.play(Rotating(dot, about_point=[2,0,0]), run_time = 1.5)
        self.wait()

class PointMovingOnShapes2(Scene):
    def construct(self):
        rect = Square(side_length = 2, color = BLUE)
        top_of_rect = rect.get_boundary_point(UP)
        
        dot = Dot(color=ORANGE).shift(top_of_rect)
        self.play(GrowFromCenter(rect))
        self.add(dot)
        self.play(MoveAlongPath(dot, rect), run_time = 3, rate_func=linear)
        self.play(dot.animate.move_to([0,1,0]))

class PointMovingOnShapes3(Scene):
    def construct(self):
        # constants
        STOPS = [.25, .5, .75, 1.0]

        # make mobs
        path = Ellipse(color=WHITE).scale(5)
        tracker = ValueTracker(0)
        square = Square(color=RED).scale(.5).move_to(path.point_from_proportion(0))
        square.add_updater(
            lambda m: m.move_to(path.point_from_proportion(tracker.get_value()))
            )

        # animate mobs
        self.add(path, square)

        for stop in STOPS:
            # move to next position
            self.play(
                tracker.animate.set_value(stop),
                run_time=2.0, rate_func=linear
                )
            # pause, do something, pause
            self.wait(.5)
            self.play(
                Rotate(square, 4*PI),
                rate_func=linear,
                run_time=2.0,
                )
            self.wait(.5)

        # done! wait and exit
        self.wait(2)
        
class MovingAround(Scene):
    def construct(self):
        square = Square(color = BLUE, fill_opacity=1)
        self.play(square.animate.shift(LEFT))
        self.play(square.animate.set_fill(ORANGE))
        self.play(square.animate.scale(0.3))
        self.play(square.animate.rotate(0.4))

class MovingAngle(Scene):
    def construct(self):
        rotation_center = LEFT
        
        theta_tracker = ValueTracker(110)

        line1 = Line(LEFT, RIGHT)
        line_moving = Line(LEFT, RIGHT)
        line_ref = line_moving.copy()

        line_moving.rotate(theta_tracker.get_value()*DEGREES, about_point=rotation_center)
        a = Angle( line1, line_moving, radius = 0.5, other_angle=False)
        tex = MathTex(r"\theta").move_to(
            Angle(
                line1, line_moving, radius=0.5 + 3*SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )

        self.add(line1, line_moving, a, tex)
        


        self.wait(3)

        line_moving.add_updater(lambda x: x.become(line_ref.copy()).rotate(theta_tracker.get_value()*DEGREES,
            about_point=rotation_center))
        
        a.add_updater(lambda x : x.become(Angle(line1, line_moving, radius=0.5, other_angle=False)))

        tex.add_updater(lambda x : x.move_to(
            Angle(line1, line_moving, radius=0.5+3*SMALL_BUFF, other_angle=False).point_from_proportion(0.5)
        ))

        self.play(theta_tracker.animate.set_value(40))
        self.play(theta_tracker.animate.increment_value(140))
        self.play(tex.animate.set_color(RED), run_time = 1)
        self.play(theta_tracker.animate.set_value(350))

class MovingDots(Scene):
    def construct(self):
        d1, d2 = Dot(color=BLUE), Dot(color = GREEN)
        dg = VGroup(d1, d2).arrange(RIGHT, buff=1)
        l1 = Line(d1, d2).set_color(RED)
        # l1 = Line(d1.get_center(), d2.get_center()).set_color(RED)
        # self.add(d1, d2, l1)
        self.add(dg, l1)

        x = ValueTracker(0)
        y = ValueTracker(0)

        d1.add_updater(lambda z : z.set_x(x.get_value()))
        d2.add_updater(lambda z : z.set_y(y.get_value()))
        l1.add_updater(lambda z : z.become(Line(d1, d2)))

        self.wait(3)
        self.play(x.animate.set_value(5))
        self.play(y.animate.set_value(4))
        self.wait()


class MovingGroupToDestination(Scene):
    def construct(self):
        group = VGroup(Dot(LEFT), Dot(ORIGIN), Dot(RIGHT, color=RED), Dot(2*RIGHT)).scale(1.4)
        dest = Dot([4, 3, 0], color = YELLOW)

        self.add(group, dest)
        self.wait(3)
        self.play(group.animate.shift(dest.get_center() - group[2].get_center()))
        self.wait()

class MovingFrameBox(Scene):
    def construct(self):
        text = MathTex('\\frac{d}{dx}f(x)g(x)=', 'f(x)\\frac{d}{dx}g(x)','+',
        'g(x)\\frac{d}{dx}f(x)')
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff=.1)
        framebox2 = SurroundingRectangle(text[3], buff=.1)
        self.play(Create(framebox1))

        self.wait()

        self.play(ReplacementTransform(framebox1, framebox2))

        self.wait()

class SinCosFunctionPlot(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-10, 10.3, 1],
            y_range=[-1.5, 1.5, 1],
            x_length = 10,
            axis_config={"color":GREEN},
            x_axis_config = {
                "numbers_to_include":np.arange(-10, 10.1, 2),
                "numbers_with_elongated_ticks":np.arange(-10, 10.1, 2)
            },
            tips = False
        )
        axes_labels = axes.get_axis_labels()
        sin_graph = axes.plot(lambda x:np.sin(x), color = BLUE)
        cos_graph = axes.plot(lambda x:np.cos(x), color = RED)
        sin_label = axes.get_graph_label(sin_graph, label = "\\sin(x)", x_val=-10, direction=UP/2)
        cos_label = axes.get_graph_label(cos_graph, label = "\\cos(x)")

        vert_line = axes.get_vertical_line(
            axes.i2gp(TAU, cos_graph),
            color=YELLOW, line_func = Line
        )
        line_label = axes.get_graph_label(
            cos_graph, "x = 2\pi", x_val=TAU, direction=UR, color=WHITE
        )

        plot = VGroup(axes, sin_graph, cos_graph, vert_line)
        labels = VGroup(axes_labels, sin_label, cos_label, line_label)

        self.add(plot, labels)

        self.wait()




