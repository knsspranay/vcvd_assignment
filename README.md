## **KATTA PRANAY** **(S2510787046)**

## Assignment Description:
This tool implements the Pacejka "Magic Formula" for a tyre model based on the Pure Slip equations provided in the assignment (Tables 2 and 3).

## My Interpretation:
The generated plot shows **Brake Force (Fx)** and **Side Force (Fy)** against Longitudinal Slip. 
* **Side Force (Fy):** In this tool, Side force (Fy) is calculated using the pure lateral Pacejka equation for a fixed slip angle α. Since the assignment specifies the pure slip formulation from the reference paper, Fy is therefore independent of longitudinal slip κ in this simplified implementation. 
* **Combined Slip:** While real-world tyre behavior (and Figure 19 in the reference) shows Side Force decreasing as Longitudinal Slip increases (due to the Friction Circle/Ellipse limit), the Pure Slip formulas provided do not mathematically account for this coupling.

**Run the main script (s2510787046.py) with the required arguments:**

python s2510787046.py --slip 2 --weight 1500 --mu 1.0
