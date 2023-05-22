# 3D-Delaunay-Triangulation-Visualizer
a 3D Delaunay Triangulation visualizer with alpha-shape computation

3D-Delaunay-Triangulation-Visualizer is a code repository that contains the implementation of a 3D Delaunay Triangulation visualizer with alpha-shape computation. This code allows you to generate a 3D plot of the Delaunay triangulation and highlight the simplices whose circumradius is less than or equal to a specified value of alpha.

## Installation (Without slider for changing alpha value)

To run this code, please follow the instructions below:

1. Clone this repository to your local machine using the following command:

   ```
   git clone https://github.com/TheRodzz/3D-Delaunay-Triangulation-Visualizer/.git
   ```
   
2. Change into the project directory:
  ```
  cd 3D-Delaunay-Triangulation-Visualizer
  ```
3. Install the required dependencies. Make sure you have Python and pip installed on your machine. Run the following command to install the dependencies:
  ```
  pip install numpy matplotlib scipy
  ```
4. This command will install the necessary libraries: NumPy, Matplotlib, and SciPy.

## Usage

To use this code, follow the steps below:

1. Open the code file (`alpha.py`) in your preferred Python IDE or text editor.

2. Modify the parameters `alp` and `nop` if desired:
   - `alp`: Set the value of alpha to determine the circumradius threshold for highlighting simplices.
   - `nop`: Set the number of random points to generate.

3. Run the code.

   ```bash
   python alpha.py
4. The code will generate a 3D plot of the Delaunay triangulation and display it. The highlighted simplices, whose circumradius is less than or equal to the specified alpha value, will be shown in the plot.

5. Adjust the plot as needed using the interactive navigation tools provided by Matplotlib.

6. Close the plot window to exit the program.

Feel free to explore the code and experiment with different values of alpha and the number of points to visualize various alpha-shapes.

## Installation (With slider to change alpha value)
Refer to the [Readme with Slider](https://github.com/TheRodzz/3D-Delaunay-Triangulation-Visualizer/blob/main/Readme%20with%20Slider.pdf) file for steps on how to run the alpha-with-slider.py code.
   


## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The code for the Delaunay triangulation and alpha-shape computation is based on [Three-Dimensional Alpha Shapes by HERBERT EDELSBRUNNER and ERNST P. MUCKE](https://www.cs.jhu.edu/~misha/Fall05/Papers/edelsbrunner94.pdf)


