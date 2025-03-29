# Nuclear Instrumentation and Measurement Project 1

## Project Overview
This project involves determining the required shielding thickness for a mixed photon irradiation source to ensure accurate detector readings. The calculations are performed using Python to model attenuation for two different shielding materials: Lead (Pb) and Aluminum (Al).

The goal is to determine the thickness required to reduce the total photon count to **1 x 10^6 ± 1 x 10^5 counts per second** at different detector distances.
The full report can be seen in the document [NIM Project 1 Report.pdf](./NIM%20Project%201%20Report.pdf). The code can be found in the Jupyter Notebook file [project1.ipynb](./project1.ipynb). 

## Assumptions
1. The radioisotope is a **point source**.
2. **Intrinsic detection efficiency** is assumed to be **1**.
3. The detector is fast enough to avoid **deadtime losses**.
4. The detector is a **3-inch diameter cylindrical detector** facing the point source.
5. **Good geometry** is assumed due to collimators, so **buildup factors are ignored**.
6. The source activity is **1 Ci**, and its decay over the experiment is negligible.

## Methodology
- The intensity of photons reaching the detector is modeled using the attenuation equation:
  
  $$\[ I = I_0 e^{-\mu t} \]$$
  
  where:
  - $$\( I \)$$ = Transmitted intensity
  - $$\( I_0 \)$$ = Initial intensity
  - $$\( \mu \)$$ = Linear attenuation coefficient (from NIST data)
  - $$\( t \)$$ = Shielding thickness

- The **initial intensity** is calculated using the emission intensity and geometric efficiency:
  
$$ \epsilon_{geo} = \frac{\Omega}{4\pi} $$
  
  where $$\( \Omega \)$$ is calculated based on detector distance and geometry.

- Using **NIST attenuation data**, the required thickness is iteratively determined for Pb and Al.

## Data Requirements
- **Photon attenuation coefficients** for Lead and Aluminum must be obtained from **NIST (National Institute of Standards and Technology) Table 3**.
- The mass attenuation coefficient **(μ/ρ)** from NIST must be multiplied by the material's density:
  - **Pb** = 11.34 g/cm³
  - **Al** = 2.7 g/cm³

### Where to Get NIST Data
1. Visit [NIST XCOM Database](https://physics.nist.gov/PhysRefData/Xcom/html/xcom1.html)
2. Select **Photon Attenuation Coefficients**.
3. Enter the material name (Lead or Aluminum).
4. Download the table and extract **mass attenuation coefficients**.

## Running the Code
### Prerequisites
Ensure you have **Python** installed with the following packages:
```sh
pip install numpy scipy matplotlib pandas
```
### Transferring Files to Windows
1. **If received via email/drive:** Download and unzip the folder to your desired location.
2. **If transferred via USB:** Copy the folder and paste it into your working directory.
3. **If using a cloud service (Google Drive, Dropbox, etc.):** Download and extract it locally.

### Running the Jupyter Notebook
1. Open **Jupyter Notebook**.
2. Navigate to the project directory.
3. Open `project1.ipynb` and run the cells sequentially.

### Expected Output
- **Plots** showing the shielding thickness required at different distances for Lead and Aluminum.
- **Tabulated results** of calculated thicknesses.

## Conclusion
- Lead requires significantly **less thickness** than Aluminum due to its higher atomic number.
- The required thickness **decreases logarithmically** as the detector distance increases.
- The results align with theoretical expectations of photon attenuation and detector efficiency.

## Files in this Repository
- `project1.ipynb` - Jupyter Notebook containing calculations and plots.
- `NIM Project 1 Report.pdf` - Full project report.
- `7314374.pdf` - Original project description.


