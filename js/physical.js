document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('planetSearch');
  const reportBox = document.getElementById('planetData');

  // Simulate auto-suggestions or model connection later here
  searchInput.addEventListener('input', (e) => {
    // Placeholder: send this input to your Python backend model later
    console.log('Searching for:', e.target.value);
  });

  searchInput.addEventListener('change', () => {
    // Replace this with real model output
    reportBox.innerHTML = `<pre class="text-white">
=== Exoplanet Report: Kepler-62b ===
Planet Radius (Earth radii): 1.00
Planet Mass (Earth masses): 1.00
Star Effective Temperature (K): 4925.0
Orbital Distance (AU): 0.050
Orbital Eccentricity: 0.020
Atmospheric Pressure (Earth atm): 1.00
Albedo: 0.20
Stellar Luminosity (Solar units): 0.210
Host Star Metallicity [Fe/H]: 0.000
Host Star Age (Gyr): 6.20
Habitability Score: 0.000
Cluster Assignment: 1 (Moderate to High Habitability Potential)
PCA Components: [-1.873, 1.568, -0.178]
Estimated Surface Temperature (K): 1004.4
Surface Gravity (Earth g): 1.00
Water Retention Potential: 0.000
Radiation Hazard Index: 1.000</pre>`;
  });
});
