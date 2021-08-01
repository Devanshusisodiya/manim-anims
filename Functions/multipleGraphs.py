import numpy as np 
from manim import *


class MultipleGraphs(GraphScene):
    def construct(self):
        self.wait(1) # INITIAL WAIT TIME
        #config
        self.x_min = -5
        self.x_max = 5
        self.y_min = -3
        self.y_max = 7
        self.graph_origin = ORIGIN + 2*DOWN

        self.setup_axes(animate=True)
# SETTING UP OF THE SCENE -------------------------------------------------

        def sine(x):
            return np.sin(x)
        def exp(x):
            return np.exp(x)
        def log(x):
            return np.log(x)

        
        sine_graph = self.get_graph(sine, x_min=self.x_min+1, x_max=self.x_max-1, color=BLUE)
        exp_graph = self.get_graph(exp, x_min=self.x_min+1, x_max=self.x_max-1, color=BLUE)
        log_graph = self.get_graph(log, x_min=0.01, x_max=self.x_max-1, color=BLUE)

# ANIMATIONS --------------------------------------------------------------
        self.play(
            ShowCreation(sine_graph)
        )
        self.wait(1)
        self.play(
            Transform(sine_graph, exp_graph)
        )
        self.wait(1)
        self.play(
            Transform(sine_graph, log_graph)
        )
        self.wait(1) # FINAL WAIT TIME