import numpy as np

class TyreModel:
    """
    Magic Formula tyre model.
    """
    def __init__(self):
        # Side force Coefficients
        self.coeffs_fy = {
            'a1': -22.1, 'a2': 1011, 'a3': 1078, 'a4': 1.82, 'a5': 0.208, 'a6': 0.000, 'a7': -0.354, 'a8': 0.707
        }
        # Brake force Coefficients
        self.coeffs_fx = {
            'a1': -21.3, 'a2': 1144, 'a3': 49.6, 'a4': 226, 'a5': 0.069, 'a6': -0.006, 'a7': 0.056, 'a8': 0.486
        }
        # Camber Coefficients
        self.coeffs_camber_fy = {
            'a9': 0.028, 'a10': 0.000, 'a11': 14.8, 'a12': 0.022
        }

    def _calculate_parameters(self, fz_kn, coeffs):
        d_val = coeffs['a1'] * (fz_kn**2) + coeffs['a2'] * fz_kn
        e_val = coeffs['a6'] * (fz_kn**2) + coeffs['a7'] * fz_kn + coeffs['a8']
        return d_val, e_val

    def calculate_side_force(self, slip_angle_deg, fz_newton, camber_angle_deg=0):
        fz_kn = fz_newton / 1000.0
        alpha = slip_angle_deg
        gamma = camber_angle_deg
        
        c_val = 1.30
        d_val, e_val = self._calculate_parameters(fz_kn, self.coeffs_fy)
        
        delta_sh = self.coeffs_camber_fy['a9'] * gamma
        delta_sv = (self.coeffs_camber_fy['a10'] * (fz_kn**2) + 
                    self.coeffs_camber_fy['a11'] * fz_kn) * gamma
        
        bcd = self.coeffs_fy['a3'] * np.sin(
            self.coeffs_fy['a4'] * np.arctan(self.coeffs_fy['a5'] * fz_kn)
        )
        
        b_val = 0 if (c_val * d_val) == 0 else bcd / (c_val * d_val)
        
        phi_input = alpha + delta_sh
        phi = (1 - e_val) * phi_input + (e_val / b_val) * np.arctan(b_val * phi_input)
        
        return d_val * np.sin(c_val * np.arctan(b_val * phi)) + delta_sv

    def calculate_brake_force(self, longitudinal_slip_percent, fz_newton):
        fz_kn = fz_newton / 1000.0
        kappa = longitudinal_slip_percent
        
        c_val = 1.65
        d_val, e_val = self._calculate_parameters(fz_kn, self.coeffs_fx)
        
        numerator = self.coeffs_fx['a3'] * (fz_kn**2) + self.coeffs_fx['a4'] * fz_kn
        denominator = c_val * d_val * np.exp(self.coeffs_fx['a5'] * fz_kn)
        
        b_val = 0 if denominator == 0 else numerator / denominator
        
        phi = (1 - e_val) * kappa + (e_val / b_val) * np.arctan(b_val * kappa)
        return d_val * np.sin(c_val * np.arctan(b_val * phi))