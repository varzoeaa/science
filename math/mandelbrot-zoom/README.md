# Mandelbrot Zoom Animation

This project generates a zoom animation of the Mandelbrot set using Python. It utilizes NumPy for calculations and Matplotlib for visualization.

## Project Structure

```
mandelbrot-zoom
├── src
│   ├── mandelbrot.py      # Implementation of the Mandelbrot set algorithm
│   └── animation.py       # Functions to create zoom animation
├── requirements.txt       # List of dependencies
└── README.md              # Project documentation
```

## Installation

To set up the environment, you need to have Python installed on your machine. It is recommended to use a virtual environment. You can create one using the following commands:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

## Dependencies

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes:

- numpy
- matplotlib

## Usage

1. **Generate the Mandelbrot Set**: You can run the `mandelbrot.py` script to compute the Mandelbrot set for specified parameters.

2. **Create Zoom Animation**: Use the `animation.py` script to generate a zoom animation of the Mandelbrot set. This script will adjust the parameters of the Mandelbrot function to create a series of frames that can be compiled into a video.

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or features you would like to add.
