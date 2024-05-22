from manim import *

config.tex_template.add_to_preamble("\\usepackage{pifont}")

class Image(Scene):
    def construct(self):
        import manimpango
        
        #Debai duoi day la de bai

        debai1 = Text(
            text="Câu 49. (Cụm Yên Phong 1-Bắc Ninh và Cẩm Khê-Phú Thọ 2024:) -Đã được dịch sang Tiếng Anh",
            font= "Times New Roman",
            color= YELLOW,
            weight=BOLD,
            slant=ITALIC
        ).scale(0.45).to_corner(UL).shift(0.3*UP)
        self.add(debai1)

        debai2 = Tex(
            r'Let $z,w\in\mathbb{C}$ satisfying: $|(z+2-i)(1+\sqrt{3}i)|=|z-\overline{z}|$'
        ).scale(0.7).to_corner(UL).shift(0.2*DOWN)
        self.add(debai2)

        debai3 = Tex(
            r' and $|w-5+i|=|w+1-2i|$'
        ).scale(0.7).next_to(debai2)
        self.add(debai3)

        debai4 = Tex(
            r'Find the smallest value of $|z-w|$'
        ).scale(0.7).to_corner(LEFT).shift(2.7*UP)
        self.add(debai4)

        dapanA=Tex(r'$A.\frac{\sqrt{5}}{2}$').scale(0.75).to_corner(LEFT).shift(2.3*UP)
        self.add(dapanA)
        dapanB=Tex(r'$B.\frac{28}{15}$').scale(0.75).shift(2.3*UP,2*LEFT)
        self.add(dapanB)
        dapanC=Tex(r'$C.\frac{\sqrt{30}}{6}$').scale(0.75).shift(2.3*UP,2*RIGHT)
        self.add(dapanC)
        dapanD=Tex(r'$D.\frac{6}{\sqrt{5}}$').scale(0.75).shift(2.3*UP,6*RIGHT)
        self.add(dapanD)

        solution=Text(
            text="Solution: Vu Dinh Thai",
            font = "Times New Roman",
            color= YELLOW,
            weight=BOLD,
            slant=ITALIC
        ).scale(0.5).shift(1.8*UP)
        self.add(solution)

        #Loi giai duoi day la loi giai
        dkz1 = MathTex(
            r'\bullet \ \ |(z+2-i)(1+\sqrt{3}i)|=|z-\overline{z}|'
        ).scale(0.7).to_corner(LEFT).shift(1.4*UP)
        self.add(dkz1)

        dkz2 = MathTex(
            r'\bullet \ \ |(z+2-i)(1+\sqrt{3}i)|^2=|z-\overline{z}|^2'
        ).scale(0.7).to_corner(LEFT).shift(1.4*UP)
        #self.play(Transform(dkz1,dkz2))

        dkz3 = MathTex(
            r'\bullet \ \ |(z+2-i)(1+\sqrt{3}i)|^2-|z-\overline{z}|^2=0'
        ).scale(0.7).to_corner(LEFT).shift(1.4*UP)
        #self.play(Transform(dkz2,dkz3))

        CALC1 = Tex(
            r'CALC z=100+0,01i  $\Rightarrow VT=$'
        ).scale(0.7).to_corner(LEFT).shift(0.95*UP)
        self.add(CALC1)

        DichsoZ_1 = MathTex(
            r'41619,92'
        ).scale(0.7).next_to(CALC1)
        #self.play(Write(DichsoZ_1))

        DichsoZ_2 = Tex(
            r'4 \ \ 16 \ \ 19, \ \ 92'
        ).scale(0.7).next_to(CALC1)
        self.add(DichsoZ_2)

        DichsoZ_3 = MathTex(
            r'4 \ \ \ 16 \ \ \ 20 \ \ -8'
        ).scale(0.7).shift(0.5*UP,0.7*LEFT)
        #self.play(Write(DichsoZ_3))

        DichsoZ_4 = MathTex(
            r'4x^2+16x+20-8y=0'
        ).scale(0.7).shift(0.5*UP,0.1*LEFT)
        self.add(DichsoZ_4)

        giai1 = MathTex(
            r'\Rightarrow y = \frac{x^2}{2}+2x+\frac{5}{2}'
        ).scale(0.7).shift(0.1*DOWN)
        giai1.set_color_by_tex("x", BLUE)
        self.add(giai1)

        dkw1 = MathTex(
            r'\bullet \ \  |w-5+i|=|w+1-2i|'
        ).scale(0.7).to_corner(LEFT).shift(0.8*DOWN)
        #self.add(dkw1)
        
        dkw2 = MathTex(
            r'\bullet \ \  |w-5+i|^2=|w+1-2i|^2'
        ).scale(0.7).to_corner(LEFT).shift(0.8*DOWN)
        #self.add(dkw2)

        dkw3 = MathTex(
            r'\bullet \ \  |w-5+i|^2-|w+1-2i|^2=0'
        ).scale(0.7).to_corner(LEFT).shift(0.8*DOWN)
        self.add(dkw3)

        CALC2 = Tex(
            r'CALC z=100+0,01i  $\Rightarrow VT=$'
        ).scale(0.7).to_corner(LEFT).shift(1.2*DOWN)
        self.add(CALC2)

        WDichso_1 = MathTex(
            r'-1178,94'
        ).scale(0.7).next_to(CALC2)
        #self.add(WDichso_1)

        WDichso_2 = MathTex(
            r'11 \ \ 78, \ \ 94'
        ).scale(0.7).next_to(CALC2)
        self.add(WDichso_2)

        WDichso_3 = MathTex(
            r'12 \ -21 \ -6'
        ).scale(0.7).shift(1.2*LEFT,1.6*DOWN)
        #self.add(WDichso_3)

        WDichso_4 = MathTex(
            r'12x-21-6y=0'
        ).scale(0.7).shift(0.7*LEFT,1.6*DOWN)
        self.add(WDichso_4)

        giai2 = MathTex(
            r'\Rightarrow y = 2x-\frac{7}{2}'
        ).scale(0.7).shift(2.2*DOWN,0.4*LEFT)
        giai2.set_color_by_tex("x", RED)
        self.add(giai2)

        #FadeOut


class Graph(Scene):
    def construct(self):
        import manimpango

        solution=Text(
            text="Solution: Vu Dinh Thai",
            font = "Times New Roman",
            color= YELLOW,
            weight=BOLD,
            slant=ITALIC
        ).scale(0.5).shift(1.8*UP)
        self.add(solution)   

        ax = Axes(
            x_range=[-6,7,1.5],x_length=5,
            y_range=[-10,13,3],y_length=4,
            tips=False
        ).shift(2.8*RIGHT,1.5*DOWN)
        pointO = Tex('O').scale(0.5).shift(2*DOWN,2.4*RIGHT)
        self.add(pointO)


        parab = ax.plot(lambda x: (x**2+2*x+2.5), x_range=[-4.5,2.5])
        parab.set_color_by_gradient(BLUE)

        z_label = MathTex(
            r'(P):y = \frac{x^2}{2}+2x+\frac{5}{2}'
        ).scale(0.6).shift(0.9*UP,1.1*RIGHT)
        z_label.set_color_by_tex("x",BLUE)
        self.add(z_label)

        line = ax.plot(lambda x: 2*x-3.5, x_range=[-3,7])
        line.set_color_by_gradient(RED)

        w_label = MathTex(
            r'(\triangle) : y=2x-\frac{7}{2}'
        ).scale(0.6).next_to(line).shift(0.9*LEFT,0.9*UP)
        w_label.set_color_by_tex("x",RED)
        self.add(w_label)

        line1 = ax.plot(lambda x: 2*x+2.5, x_range=[-6,6])
        line1.set_color_by_gradient(GREEN)

        dot_scene =Dot(ax.coords_to_point(0, 2.5), color=YELLOW, stroke_width=0.1)
        self.add(dot_scene)
        pointM = Tex('M').scale(0.5).shift(1.1*DOWN,2.4*RIGHT)
        self.add(pointM)

        self.add(ax, parab, line, line1)

        giai3 = MathTex(
            r'\bullet \ M(x_0,y_0)\in (d) : y=2x+C'
        ).scale(0.7).to_edge(LEFT).shift(1.4*UP)
        self.add(giai3)

        giai4 = Tex(
            r'M is tangent point of (P) and (d)'
        ).scale(0.7).to_edge(LEFT).shift(1*UP)
        self.add(giai4)

        giai5 = MathTex(
            r"""\Rightarrow f'(x_0)=2"""
        ).scale(0.7).to_edge(LEFT).shift(0.6*UP)
        self.add(giai5)

        giai6 = MathTex(
            r'\Leftrightarrow x_0 +2=2 \Leftrightarrow x_0=0 '
        ).scale(0.7).to_edge(LEFT).shift(0.2*UP)
        self.add(giai6)

        giai7 = MathTex(
            r'\Rightarrow M(0, \frac{5}{2})'
        ).scale(0.7).to_edge(LEFT).shift(0.5*DOWN)
        giai7.set_color_by_gradient(YELLOW)
        self.add(giai7)

        giai8 = MathTex(
            r'\bullet \ |z-w|_{min} = d(M,\triangle)'
        ).scale(0.7).to_edge(LEFT).shift(1.2*DOWN)
        self.add(giai8)

        giai9 = MathTex(
            r'= \frac{|2.0-\frac{5}{2} - \frac{7}{2}|}{\sqrt{2^2+1^2}} = \frac{6}{\sqrt{5}} '
        ).scale(0.7).to_edge(LEFT).shift(1.9*DOWN)
        self.add(giai9)

        rect = Rectangle(
            width=0.7,
            height=1.1,
            stroke_color = RED
        ).shift(2*DOWN,3.5*LEFT)
        self.add(rect)