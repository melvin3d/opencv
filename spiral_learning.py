import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def draw_spiral():
    """Example from chatGTP on how to calculate a ponytail."""

    def bezier_3d(P0, P1, P2, P3, t_vals):
        """Returns a 3D Bézier curve given 4 control points and parameter t"""
        return (
            (1 - t_vals)[:, None] ** 3 * P0
            + 3 * (1 - t_vals)[:, None] ** 2 * t_vals[:, None] * P1
            + 3 * (1 - t_vals)[:, None] * t_vals[:, None] ** 2 * P2
            + t_vals[:, None] ** 3 * P3
        )

    # Parameter t
    t = np.linspace(0, 5, 500)

    # Common base point (where hair is tied)
    base = np.array([0, 0, 0])

    # Slight offsets for natural spread
    offsets = [
        np.array([-0.2, 0.1, 0]),
        np.array([0.2, -0.1, 0]),
        np.array([0.0, 0.2, 0]),
    ]

    # Control points for each curve
    curves = []
    for offset in offsets:
        P0 = base + offset  # Root of the hair
        P1 = P0 + np.array([0, 0, -1])  # Initial fall
        P2 = P0 + np.array([0.5 * offset[0], 0.5 * offset[1], -3])  # Mid curve
        P3 = P0 + np.array([offset[0], offset[1], -6])  # End (fall due to gravity)

        curve = bezier_3d(P0, P1, P2, P3, t)
        curves.append(curve)

    # Plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    for curve in curves:
        ax.plot(curve[:, 0], curve[:, 1], curve[:, 2], lw=2)

    ax.set_title("3 Ponytail Curves")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")  # type: ignore
    ax.view_init(elev=20, azim=-60)  # type: ignore
    plt.show()


def single_spiral():
    """Creates a single spiral."""

    # Parameters
    a = 0  # Starting radius
    b = 0.2  # Controls the spacing between turns

    # Theta range (angle in radians)
    theta = np.linspace(0, 6 * np.pi, 1000)  # 3 full turns

    # Polar equation of Archimedean spiral
    r = a + b * theta

    # Convert to Cartesian coordinates for plotting
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Plotting
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, label="Archimedean Spiral")
    plt.title("Single Curve Spiral")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("equal")  # Keep aspect ratio square
    plt.grid(True)
    plt.legend()
    plt.show()


def helix():
    """Draws a three dimentional spiral aka helix."""

    # Parameters
    r = 10  # Radius of the helix
    c = 1.0  # Step size along z-axis
    t = np.linspace(0, 18 * np.pi, 1000)  # Range of angles (4 full turns)

    # Parametric equations
    x = r * np.cos(t)
    y = r * np.sin(t)
    z = c * t

    # Plotting
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(x, y, z, label="3D Helix", color="mediumblue")
    ax.set_title("3D Single Curve Spiral (Helix)")
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")  # type: ignore
    ax.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    draw_spiral()
    # single_spiral()
    # helix()
