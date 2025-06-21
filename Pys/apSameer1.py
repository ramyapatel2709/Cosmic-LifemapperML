import pandas as pd
from io import StringIO

# Simulated CSV_DATA embedded directly (replace with full data string as needed)
CSV_DATA = """
planet_name,planet_radius,star_temperature,orbital_distance,atmospheric_pressure,stellar_luminosity,planet_mass,eccentricity,orbital_period,albedo,host_star_metallicity,host_star_age
Kepler-22b,2.4,5518,0.85,1.2,0.79,5.4,0.02,289.9,0.3,0.05,4.0
Proxima Centauri b,1.1,3042,0.0485,0.9,0.0017,1.3,0.0,11.2,0.1,-0.04,4.9
TRAPPIST-1e,0.92,2559,0.028,0.8,0.0005,0.77,0.01,6.1,0.1,0.04,7.6
Gliese 667 Cc,1.54,3700,0.125,1.1,0.013,3.8,0.15,28.1,0.25,0.02,2.9
HD 40307g,2.1,4977,0.6,1.5,0.23,7.1,0.22,197.8,0.35,-0.06,5.1
Kepler-186f,1.11,3755,0.356,1.0,0.04,1.4,0.04,129.9,0.2,0.01,3.7
LHS 1140b,1.43,3131,0.09,1.2,0.0035,6.6,0.05,24.7,0.15,-0.05,5.5
Wolf 1061c,1.6,3500,0.084,0.7,0.01,4.3,0.12,17.9,0.3,-0.02,3.4
Kepler-62f,1.41,4925,0.72,1.3,0.21,3.3,0.09,267.3,0.32,0.00,6.2
Tau Ceti e,1.9,5344,0.55,0.9,0.52,4.5,0.05,168.1,0.28,-0.1,7.0
GJ 667 C f,1.5,3700,0.155,1.1,0.013,4.6,0.16,35.0,0.27,0.02,3.1
Kepler-452b,1.6,5757,1.05,1.4,1.04,5.0,0.04,384.8,0.3,0.04,6.0
K2-18b,2.6,3503,0.143,1.6,0.02,8.0,0.15,33.0,0.35,0.05,4.8
Kepler-438b,1.12,3748,0.166,1.0,0.02,1.5,0.11,35.2,0.19,0.03,3.8
Kepler-440b,1.86,3995,0.242,1.3,0.04,4.8,0.18,63.3,0.31,0.01,5.2
Ross 128b,1.35,3192,0.049,0.9,0.004,1.8,0.04,9.9,0.2,-0.02,6.0
Kepler-62e,1.61,4925,0.43,1.25,0.21,3.4,0.08,122.4,0.32,0.00,6.3
HD 219134b,1.6,4699,0.038,1.5,0.26,4.5,0.03,3.1,0.3,0.04,7.1
Kepler-10c,2.35,5627,0.24,1.5,0.79,14.0,0.06,45.3,0.28,0.1,8.0
GJ 273b,1.2,3370,0.091,1.1,0.006,2.9,0.07,18.6,0.22,0.0,5.6
Kapteyn b,1.1,3570,0.168,1.0,0.01,4.8,0.1,48.6,0.3,-0.86,11.5
K2-3d,1.5,3896,0.207,1.3,0.03,2.7,0.05,44.6,0.29,0.04,4.1
HD 85512b,1.4,4715,0.26,1.1,0.19,3.6,0.05,58.4,0.32,-0.16,5.3
Kepler-62d,1.43,4925,0.12,1.2,0.21,3.9,0.11,18.2,0.27,0.0,6.2
Kepler-145b,1.7,5350,0.36,1.3,0.45,4.5,0.12,64.0,0.3,0.03,5.7
Gliese 832c,1.5,3472,0.163,1.2,0.012,5.4,0.07,36.1,0.28,0.05,6.8
K2-18c,2.3,3503,0.07,1.4,0.02,7.2,0.1,9.2,0.33,0.05,4.8
Ross 128c,1.1,3192,0.13,0.8,0.004,1.2,0.02,16.0,0.15,-0.02,6.0
Kepler-20e,0.87,5500,0.05,1.0,0.76,0.8,0.02,6.1,0.2,0.05,6.4
K2-155d,1.6,4900,0.17,1.3,0.18,3.2,0.08,40.2,0.3,0.03,5.9
Kepler-186c,1.3,3755,0.13,1.1,0.04,2.5,0.07,29.8,0.23,0.01,3.7
Luyten b,1.1,3200,0.09,1.0,0.005,2.0,0.06,19.4,0.18,-0.03,7.1
Gliese 667 Cf,1.8,3700,0.16,1.2,0.013,5.7,0.12,39.6,0.29,0.02,3.1
Wolf 1061b,1.4,3500,0.035,0.95,0.01,1.5,0.04,4.9,0.2,-0.02,3.4
GJ 667 Ce,1.2,3700,0.05,0.9,0.013,2.3,0.03,7.2,0.19,0.02,3.1
Kepler-62c,0.54,4925,0.05,0.6,0.21,0.1,0.03,12.4,0.1,0.00,6.2
HD 97658b,2.3,5119,0.08,1.5,0.33,8.0,0.05,9.5,0.34,-0.23,6.5
K2-18e,1.7,3503,0.19,1.1,0.02,3.7,0.1,33.4,0.29,0.05,4.8
Kepler-138d,1.2,3800,0.17,1.0,0.045,2.1,0.07,33.0,0.22,0.0,3.9
GJ 667 Cb,1.54,3700,0.05,1.1,0.013,4.5,0.02,7.2,0.27,0.02,3.1
Ross 128b2,1.3,3192,0.06,1.0,0.004,3.2,0.04,10.5,0.2,-0.02,6.0
Kepler-22c,1.9,5518,0.95,1.3,0.79,6.2,0.05,302.0,0.3,0.05,4.0
GJ 273c,1.5,3370,0.15,1.4,0.006,4.3,0.1,32.1,0.27,0.0,5.6
K2-3b,1.6,3896,0.08,1.3,0.03,2.6,0.04,10.1,0.3,0.04,4.1
Kepler-20f,1.05,5500,0.35,1.0,0.76,1.1,0.06,69.7,0.25,0.05,6.4
GJ 667 Cd,1.3,3700,0.08,1.1,0.013,3.1,0.07,15.3,0.26,0.02,3.1
Kepler-36b,1.5,5900,0.13,1.2,1.1,4.1,0.04,13.8,0.28,0.06,5.5
LHS 1140c,1.1,3131,0.04,1.0,0.0035,1.7,0.02,6.9,0.17,-0.05,5.5
Wolf 1061d,1.8,3500,0.15,1.2,0.01,5.0,0.08,60.3,0.3,-0.02,3.4
GJ 667 Ce2,1.4,3700,0.12,1.1,0.013,3.6,0.05,27.0,0.27,0.02,3.1
Kepler-452c,1.3,5757,1.1,1.1,1.04,2.7,0.04,410.1,0.28,0.04,6.0
K2-18f,1.2,3503,0.22,1.0,0.02,2.4,0.05,42.5,0.25,0.05,4.8
Kepler-1606b,1.6,4800,0.52,1.4,0.19,5.6,0.13,128.3,0.31,-0.02,5.5
GJ 273d,1.4,3370,0.12,1.2,0.006,3.7,0.06,26.4,0.28,0.0,5.6
K2-3c,1.5,3896,0.12,1.3,0.03,3.1,0.08,24.6,0.3,0.04,4.1
Kepler-11f,2.5,5660,0.25,1.5,1.01,8.4,0.07,46.7,0.34,0.06,5.0
Gliese 832b,2.0,3472,0.20,1.6,0.012,7.2,0.14,36.0,0.32,0.05,6.8
HD 97658c,1.6,5119,0.13,1.3,0.33,3.9,0.04,15.3,0.3,-0.23,6.5
Kepler-144b,1.7,5600,0.46,1.2,0.78,4.2,0.06,75.5,0.29,0.04,5.7
LHS 1140d,1.1,3131,0.07,1.0,0.0035,1.9,0.03,14.5,0.2,-0.05,5.5
Wolf 1061e,1.3,3500,0.11,1.1,0.01,3.0,0.07,22.8,0.28,-0.02,3.4
GJ 667 Cf2,1.2,3700,0.14,1.0,0.013,2.9,0.06,30.7,0.27,0.02,3.1
Kepler-62b,1.0,4925,0.05,1.0,0.21,1.0,0.02,10.3,0.2,0.0,6.2
"""


def load_data_from_csv_string(csv_string):
    return pd.read_csv(StringIO(csv_string))

def generate_detailed_report(row):
    return f"""=== Exoplanet Report: {row['planet_name']} ===
Planet Radius (Earth radii): {row['Planet Radius (Earth radii)']}
Planet Mass (Earth masses): {row['Planet Mass (Earth masses)']}
Star Effective Temperature (K): {row['Star Effective Temperature (K)']}
Orbital Distance (AU): {row['Orbital Distance (AU)']}
Orbital Eccentricity: {row['Orbital Eccentricity']}
Atmospheric Pressure (Earth atm): {row['Atmospheric Pressure (Earth atm)']}
Albedo: {row['Albedo']}
Stellar Luminosity (Solar units): {row['Stellar Luminosity (Solar units)']}
Host Star Metallicity [Fe/H]: {row['Host Star Metallicity [Fe/H]']}
Host Star Age (Gyr): {row['Host Star Age (Gyr)']}
Habitability Score: {row['Habitability Score']}
Cluster Assignment: {row['Cluster Assignment']}
PCA Components: [{row['PCA 1']}, {row['PCA 2']}, {row['PCA 3']}]
Estimated Surface Temperature (K): {row['Estimated Surface Temperature (K)']}
Surface Gravity (Earth g): {row['Surface Gravity (Earth g)']}
Water Retention Potential: {row['Water Retention Potential']}
Radiation Hazard Index: {row['Radiation Hazard Index']}
"""


df_global = load_data_from_csv_string(CSV_DATA)

def get_all_planets():
    return df_global['planet_name'].dropna().unique().tolist()

def get_planet_details(planet_name: str) -> str:
    row = df_global[df_global['planet_name'].str.lower() == planet_name.lower()]
    if row.empty:
        return f"Planet '{planet_name}' not found."
    return generate_detailed_report(row.iloc[0])
