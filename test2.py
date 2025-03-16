#import attenuation coefficient for each thickness from NIST database
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def get_attenuation_coefficients(energies, material):
    """
    Fetches mass attenuation coefficients (μ/ρ) from NIST XCOM for a given material.
    """
    url = "https://physics.nist.gov/cgi-bin/Xcom/xcom2"
    data = {
        "Output": "TXT",
        "Material": material,
        "PhotonEnergies": " ".join(map(str, energies)),
        "Submit": "Submit"
    }
    
    response = requests.post(url, data=data)
    if response.status_code != 200:
        raise Exception("Failed to retrieve data from NIST XCOM.")
    
    text = response.text.splitlines()
    
    mu_rho_values = []
    for line in text:
        parts = line.split()
        if len(parts) == 2:
            try:
                energy, mu_rho = float(parts[0]), float(parts[1])
                mu_rho_values.append((energy, mu_rho))
            except ValueError:
                continue
    
    return dict(mu_rho_values)

# Load photon energies from the .txt file
file_path = "7314376.txt"  # Update this if the filename is different
data = pd.read_csv(file_path, delim_whitespace=True)
energies = data["energy_[keV]"].values

# Get attenuation coefficients for Lead and Aluminum
lead_mu_rho = get_attenuation_coefficients(energies, "Pb")
aluminum_mu_rho = get_attenuation_coefficients(energies, "Al")

# Define material densities
density_lead = 11.34  # g/cm³
density_aluminum = 2.7  # g/cm³

# Compute linear attenuation coefficients
results = []
for energy in energies:
    mu_lead = lead_mu_rho.get(energy, np.nan) * density_lead if energy in lead_mu_rho else np.nan
    mu_aluminum = aluminum_mu_rho.get(energy, np.nan) * density_aluminum if energy in aluminum_mu_rho else np.nan
    results.append([energy, mu_lead, mu_aluminum])

# Save results to CSV
output_df = pd.DataFrame(results, columns=["Energy (keV)", "Mu (Lead) cm^-1", "Mu (Aluminum) cm^-1"])
output_df.to_csv("attenuation_coefficients.csv", index=False)

print("Attenuation coefficients saved to attenuation_coefficients.csv")
