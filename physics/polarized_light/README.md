# Polarized Light Visualization

This project visualizes the concept of polarized light and the effect of a polarizing filter using Python, NumPy, and Matplotlib.

## Directory Structure

```
polarized_light
├── src
│   └── polarized_light.py
├── requirements.txt
└── README.md
```

## Installation

Create and activate a virtual environment:

```bash
python -m venv venv
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the animation:
```bash
python src/polarized_light.py
```

## Dependencies

- numpy
- matplotlib

## Scientific Background

This animation demonstrates how light can be polarized and how a polarizing filter affects it.  
- At first, the light is **elliptically polarized**: its electric field traces an ellipse in the x-y plane as it moves along the z-axis.  
- Halfway through the animation, a **polarizer** (shown as a white plane) is introduced. The polarizer only allows the x-component of the electric field to pass, blocking the y-component.  
- After the polarizer, the light becomes **linearly polarized**: the electric field oscillates only in the x-direction.

This is a fundamental concept in optics, with practical applications in sunglasses, LCD screens, photography, and more.
