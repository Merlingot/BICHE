# Matplotlib :
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
plt.ion()
# Numpy :
import numpy as np
class Cameleon:
    """
    This is a class to create a matplotlib graphic using a non-pyplot format.
    It consist in a simplification of the normally hard implementation of the
    figure into a tkinter frame.

    Attributes:
        parent : tkinter frame in which the graphic is placed in.
        Fig : Figure object of the matplotlib class analogue to pyplot.figure
        axes : Matplotlib Axis object created to plot data
        Line : Matplotlib Line object created to update data in the given axis
        canvas : Matplotlib object that generates the 'drawing' in a tkinter
        frame it is mainly used to update the graphic in real time.
        toolbar : Matplotlib toolbar normally under any pyplot graph.
    """
    def __init__(self, parent, axis_name=['', ''], figsize=[1, 1]):
        """
        The constructor for the GraphicFrame Class.

        Parameters:
            parent : tkinter Frame object where the object is placed in.
            axis_name : This is a list of two strings that will be respectivly
            the x and y axis name. (Should be Latex friendly)
            figsize : This is the initial figure size (The figure size is
            automaticly updated when the window is changed in size)
        """
        self.parent = parent
        self.Fig = Figure(dpi=100, figsize=figsize)
        # Adjusting the axis in the figure and setting up necessary parameters
        # for naming the axis
        self.axes = self.Fig.add_axes([0.1, 0.1, 0.87, 0.87])
        self.axes.set_aspect('auto', adjustable='box')
        self.axes.set_adjustable('box')
        #self.Line, = self.axes.plot([], [])
        self.axes.tick_params(axis='both', which='major', labelsize=8)
        self.axes.grid()
        self.axes.set_xlabel(r'' + axis_name[0])
        self.axes.set_ylabel(r'' + axis_name[1])
        #Creating toolbar for convinience reason and canvas to host the figure
        self.canvas = FigureCanvasTkAgg(self.Fig, parent)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(expand=True, fill='both')

    def change_dimensions(self, event):
        """
        This function is a way to update the size of the figure when you change
        the size of your window automaticly it takes the width of your parent
        and the dpi of your figure to update the height and width.

        How to set it up : Your_Frame.bind('<Configure>', Your_Graph.change_dimensions)

        Parameters:
            event: An event is an object in tkinter that is created when you
            click on the screen. See the given documentation for the specifics.
            This parameter automaticly sent through when you click on the
            line.
        """
        width = event.width/self.Fig.get_dpi()
        height = event.height/self.Fig.get_dpi()
        self.Fig.set_size_inches(w=width, h=height)

    def update_graph(self):
        """
        This function is a compilation of two line to update the figure canvas
        so it update the values displayed whitout recreating the figure in the
        tkinter frame.

        """
        self.Fig.canvas.draw()
        self.Fig.canvas.flush_events()

    def destroy_graph(self):
        """
        This function is a compilation of two line to destroy a graph ie if
        you want to replace it or just get rid of it. It does not destroy the
        class itself so creating the canvas and the toolbar would make it
        appear the same way it was before.

        """
        self.canvas.get_tk_widget().destroy()
        self.toolbar.destroy()

    def log_scale(self):
        """
        This function is changing the y axis to make it a logarithmic scale.
        """
        self.axes.set_yscale('log')
        self.update_graph()

    def lin_scale(self):
        """
        This function is changing/reverting the y axis back to a linear scale.
        """
        self.axes.set_yscale('linear')
        self.update_graph()

