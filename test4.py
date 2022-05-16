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