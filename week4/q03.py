from math import pi

def fertilizer_area(outer_radius : float, inner_radius : float) -> float:
    if outer_radius <= inner_radius:
        raise ValueError("Outer radius must be greater than inner radius!")

    return pi * (outer_radius**2 - inner_radius**2)

outer_radius = float(input("Outer Radius: "))
inner_radius = float(input("Inner Radius: "))

try:
    print(f"Effective Usable Area: {fertilizer_area(outer_radius, inner_radius):.3f}")
except Exception as e:
    print(e)
