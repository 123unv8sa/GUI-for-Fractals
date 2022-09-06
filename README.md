# Fractals in Python

The following code are referenced from [itsliterallymonique's](https://medium.com/nerd-for-tech/programming-fractals-in-python-d42db4e2ed33) write-up.

Each of the links to their individual git repositories are as follows:

1. [The Koch Fractal](https://github.com/itsliterallymonique/Koch-Fractal-o_O.git)
2. [The Barnsley Fern](https://github.com/itsliterallymonique/Barnsley-Fern)
3. [The Mandelbrot Set](https://github.com/itsliterallymonique/Mandelbrot-Set.git)

The files kf.py, ms,py and bf.py are mainly sourced from [itsliterallymonique's] github posts linked above with a few modifications.
# Requirements

For this exercise, we will create a new environment.
This exercise assumes an installation of conda or Anaconda is present on the system.
We will name the environment "fractals". Do that with:

    conda create --name fractals

We then need to install some packages that will be used to build the fractals.
If you want to try a minimal system, run:

    conda install numpy matplotlib

If instead you wish to clone the setup in this repository, do:

    conda create --name fractals --file requirements.txt

Important!!!
Aside from the requirements in file requirements.txt, we need to install tkinter [ie: tk and tcl] using the following code in command prompt:

pip install tk
pip install tcl

Make sure that tk-0.1.0 and tcl-0.2 are installed.

Then, to run the code, look for file ["selector_upgrade_1.py"]. This is the main file which will run the GUI to call the various functions to display the 3 fractals. After run, wait a moment till the GUI pops up, then use the dropdown menu to select the type of fractal to be displayed. To show the examples, click on [Show sample] button. To close the displayed sample(s), click on [Reset] button. To close the entire GUI, click on [Exit] button.