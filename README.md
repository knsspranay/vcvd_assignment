**KATTA PRANAY**
**(S2510787046)**

## Assignment Description
This project implements the Pacejka "Magic Formula" for a tyre model based on the Pure Slip equations provided in the lecture materials (Tables 2 and 3).

## My Interpretation:
The generated plot shows **Brake Force (Fx)** and **Side Force (Fy)** against Longitudinal Slip. 
* **Side Force (Fy):** In this model, Side Force remains constant across the slip range because the implementation utilizes the **Pure Slip** equations for a fixed slip angle. 
* **Combined Slip:** While real-world tyre behavior (and Figure 19 in the reference) shows Side Force decreasing as Longitudinal Slip increases (due to the Friction Circle/Ellipse limit), the Pure Slip formulas provided do not mathematically account for this coupling.

**Run the main script (s2510787046.py) with the required arguments:**

python s2510787046.py --slip 2 --weight 1500 --mu 1.0
