# car-sim

# Car Simulator

This repository contains a Python-based simulation environment for a race car navigating a track. It utilizes a kinematic bicycle model and Frenet coordinates to simulate vehicle dynamics and path planning.

## Features

* **Kinematic Bicycle Model**: Implementation of vehicle physics to track position and heading based on acceleration and steering inputs.
* **Race Track Generation**: Tools to build track boundaries using polylines, including helper functions for elliptical track shapes.
* **Centerline Calculation**: Automatically computes a center path between inner and outer track boundaries by calculating normal vectors and segment intersections.
* **Visualization**: Built-in support for plotting the inner curve, outer curve, and calculated centerline using Matplotlib.
* **Coordinate Systems**: Support for both standard Cartesian (x, y) coordinates and Frenet (s, $e_y$) coordinates for path-relative tracking.

## Project Structure

* `bicycle_model.py`: Defines the `KinematicBicycleModel` class, managing the car's state including arc length, lateral deviation, and velocity.
* `race_track.py`: Contains the `RaceTrack` class for track generation, centerline processing, and visualization.
* `README.md`: Project documentation.

## Getting Started

### Prerequisites

* Python 3.x
* NumPy
* Matplotlib

### Running the Simulation

You can visualize the default elliptical track by running the race track script directly:

```bash
python race_track.py

```

This will generate a track with an outer boundary and an inner boundary, then compute and display the resulting centerline.