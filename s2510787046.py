import argparse
import numpy as np
import matplotlib.pyplot as plt

# Import the TyreModel class from my other file
from s2510787046_tire import TyreModel

def main():
    parser = argparse.ArgumentParser(description="Tyre Model Simulation")
    parser.add_argument("--slip", type=float, required=True, help="Slip angle in degrees")
    parser.add_argument("--weight", type=float, required=True, help="Vehicle weight in kg")
    parser.add_argument("--mu", type=float, default=1.0, help="Friction coefficient")

    args = parser.parse_args()

    # Calculate Load (Fz) on each wheel
    g = 9.81
    fz_total = args.weight * g
    fz_per_wheel = fz_total / 4.0

    slip_range = np.linspace(0, 100, 100)

    model = TyreModel()
    
    fx_results = []
    fy_results = []

# Loop through every slip percentage to calculate the forces
    for kappa in slip_range:
        fx = model.calculate_brake_force(kappa, fz_per_wheel)
        fy = model.calculate_side_force(args.slip, fz_per_wheel)
        fx_results.append(fx * args.mu)
        fy_results.append(fy * args.mu)

    plt.figure(figsize=(10, 6))
    plt.plot(slip_range, fx_results, label='Brake force -Fx [N]', color='blue', linewidth=2)
    plt.plot(slip_range, fy_results, label='Side force Fy [N]', color='red', linestyle='--', linewidth=2)
    
    plt.title(f"Force vs Slip (Weight: {args.weight}kg, Slip Angle: {args.slip}deg)")
    plt.xlabel("Longitudinal slip - x [%]")
    plt.ylabel("Force [N]")
    plt.xlim(0, 100)
    plt.ylim(bottom=0)
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend()
    plt.savefig(f"forces_plot_slip{args.slip}.png")
    print("Plot generated successfully!! well done young padawan!! MAY THE FORCE BE WITH YOU!!")

if __name__ == "__main__":
    main()