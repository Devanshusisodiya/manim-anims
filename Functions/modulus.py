import numpy as np 
from manim import *

class Modulus(GraphScene):

    def construct(self):
        self.wait(1) #INTITIAL WAIT TIME

        #config
        self.x_min = -4
        self.x_max = 4
        self.y_min = -4
        self.y_max = 4
        self.graph_origin = ORIGIN
        self.x_labeled_nums = np.arange(self.x_min, self.x_max+1)
        self.y_labeled_nums = np.arange(self.y_min, self.y_max+1)


        # SETTING UP OF THE SCENE -----------------------------------------------

        def func(x):
            return np.floor(x)

        self.setup_axes(animate=True)
        graph0 = self.get_graph(func, x_min=-2, x_max=-1.001, color=YELLOW)
        dotcl0 = Dot(self.coords_to_point(-2,-2))
        dothl0 = Circle(radius=0.1, color=WHITE).shift(self.coords_to_point(-1,-2))

        graph1 = self.get_graph(func, x_min=-1, x_max=-0.001, color=YELLOW)
        dotcl1 = Dot(self.coords_to_point(-1,-1))
        dothl1 = Circle(radius=0.1, color=WHITE).shift(self.coords_to_point(0,-1))

        graph2 = self.get_graph(func, x_min=0, x_max=0.999, color=YELLOW)
        dotcl2 = Dot(self.coords_to_point(0,0))
        dothl2 = Circle(radius=0.1, color=WHITE).shift(self.coords_to_point(1,0))

        graph3 = self.get_graph(func, x_min=1, x_max=1.999, color=YELLOW)
        dotcl3 = Dot(self.coords_to_point(1,1))
        dothl3 = Circle(radius=0.1, color=WHITE).shift(self.coords_to_point(2,1))

        mod_group = VGroup(graph0, graph1, graph2, graph3, dotcl0, dothl0, dotcl1, dothl1, dotcl2, dothl2, dotcl3, dothl3)
        # ANIMATIONS ------------------------------------------------------------
        
        self.play(
            *[ShowCreation(element) for element in mod_group]
        )

        self.wait(1) # FINAL WAIT TIME

# class 