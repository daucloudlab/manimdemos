from manim import *

class CodemyIntro(Scene):
    def construct(self):
        r = ValueTracker(0.25)
        circle_out = always_redraw(lambda:Circle(radius = r.get_value()*4,
        stroke_width=5, stroke_color=DARK_GREY, fill_color = PURPLE, fill_opacity=0.25))
        
        circle_in = always_redraw(lambda:Circle(radius = r.get_value()*3,
        stroke_width=5, stroke_color=YELLOW, fill_color = YELLOW, fill_opacity=0.15))
        
        name1 = always_redraw(lambda:Text("CODEMY.KZ")
        .set_color_by_gradient(GREEN, PINK)
        .set_height(r.get_value()*1)
        .move_to(circle_in.get_center()))
        
        line = always_redraw(lambda:Line(stroke_width=10, stroke_color=YELLOW)
        .set_width(4*r.get_value()*3.1415).next_to(circle_out, DOWN, buff=0.4))

        name2 = always_redraw(lambda:Text("COding acaDEMY")
        .set_height(r.get_value()*0.25)
        .next_to(name1, DOWN, buff=0.1))
        
        name3 = Text("Программалауды Үйренейік!").set_height(0.5).next_to(name2, DOWN, 0.6)

        self.play(LaggedStart(Create(circle_out), DrawBorderThenFill(circle_in), 
        Write(name1), Write(name2), run_time = 5, lag_ratio=0.75))
        self.play(ReplacementTransform(circle_in.copy(), line, run_time=3))
        self.play(r.animate.set_value(0.8), run_time = 10)
        self.wait()
        self.play(Write(name3), run_time = 5)
        self.wait()        

