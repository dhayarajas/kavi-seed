"""
Data generation and simulation for AIRS-GSeed framework.
Generates synthetic multi-modal data for training and evaluation.
"""

import numpy as np
import pandas as pd
from scipy import signal
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os


class DataGenerator:
    """Generate synthetic multi-modal agricultural data."""
    
    def __init__(self, seed=42):
        np.random.seed(seed)
        self.seed = seed
        
    def generate_uav_rgb(self, n_images=100, img_size=(256, 256)):
        """Generate synthetic UAV RGB images with disease patterns."""
        images = []
        labels = []
        
        for i in range(n_images):
            # Base healthy vegetation (green)
            img = np.zeros((*img_size, 3))
            img[:, :, 1] = np.random.uniform(0.4, 0.7, img_size)  # Green channel
            
            # Add disease patterns for some images
            if np.random.random() < 0.4:  # 40% have disease
                # Leaf spot (brown patches)
                n_spots = np.random.randint(5, 15)
                for _ in range(n_spots):
                    x, y = np.random.randint(0, img_size[0], 2)
                    r = np.random.randint(10, 30)
                    y_coords, x_coords = np.ogrid[:img_size[0], :img_size[1]]
                    mask = (x_coords - x)**2 + (y_coords - y)**2 <= r**2
                    img[mask, 0] = np.random.uniform(0.3, 0.5)  # Brown
                    img[mask, 1] = np.random.uniform(0.2, 0.4)
                    img[mask, 2] = np.random.uniform(0.1, 0.3)
                
                labels.append(1)  # Diseased
            else:
                labels.append(0)  # Healthy
            
            images.append(img)
        
        return np.array(images), np.array(labels)
    
    def generate_multispectral(self, n_images=100, img_size=(128, 128)):
        """Generate synthetic multispectral images (RGB, Red-edge, NIR)."""
        images = []
        
        for i in range(n_images):
            # 5 bands: R, G, B, Red-edge, NIR
            img = np.zeros((*img_size, 5))
            
            # Healthy vegetation: high NIR, moderate red-edge
            img[:, :, 4] = np.random.uniform(0.6, 0.9, img_size)  # NIR
            img[:, :, 3] = np.random.uniform(0.4, 0.7, img_size)  # Red-edge
            img[:, :, 0] = np.random.uniform(0.2, 0.4, img_size)  # Red
            img[:, :, 1] = np.random.uniform(0.3, 0.6, img_size)  # Green
            img[:, :, 2] = np.random.uniform(0.1, 0.3, img_size)  # Blue
            
            # Stress reduces NIR and red-edge
            if np.random.random() < 0.4:
                stress_mask = np.random.random(img_size) < 0.3
                img[stress_mask, 4] *= 0.6  # Reduced NIR
                img[stress_mask, 3] *= 0.7  # Reduced red-edge
                img[stress_mask, 0] *= 1.2  # Increased red
            
            images.append(img)
        
        return np.array(images)
    
    def generate_thermal(self, n_images=100, img_size=(64, 64)):
        """Generate synthetic thermal images."""
        images = []
        
        for i in range(n_images):
            # Base temperature: 25-30°C for healthy canopy
            temp = np.random.normal(27.5, 2.0, img_size)
            
            # Stress increases temperature (water stress)
            if np.random.random() < 0.3:
                stress_mask = np.random.random(img_size) < 0.25
                temp[stress_mask] += np.random.uniform(2, 5)
            
            images.append(temp)
        
        return np.array(images)
    
    def generate_soil_sensor_data(self, n_days=100, n_sensors=5):
        """Generate synthetic soil sensor time series."""
        data = []
        
        base_date = datetime(2023, 6, 1)
        
        for sensor_id in range(n_sensors):
            dates = [base_date + timedelta(days=d, hours=h*15//60) 
                    for d in range(n_days) for h in range(0, 96, 1)]  # 15-min intervals
            
            # Soil moisture: seasonal pattern with noise
            days = np.arange(len(dates))
            moisture = 50 + 20 * np.sin(2 * np.pi * days / 30)  # Monthly cycle
            moisture += np.random.normal(0, 5, len(dates))
            moisture = np.clip(moisture, 20, 80)
            
            # Soil temperature: diurnal + seasonal
            temp = 25 + 5 * np.sin(2 * np.pi * days / 365)  # Seasonal
            temp += 3 * np.sin(2 * np.pi * np.arange(len(dates)) / 96)  # Diurnal
            temp += np.random.normal(0, 1, len(dates))
            
            # EC (electrical conductivity)
            ec = 1.5 + 0.5 * np.sin(2 * np.pi * days / 30)
            ec += np.random.normal(0, 0.2, len(dates))
            ec = np.clip(ec, 0.5, 3.0)
            
            df = pd.DataFrame({
                'timestamp': dates,
                'sensor_id': sensor_id,
                'soil_moisture_vwc': moisture,
                'soil_temperature': temp,
                'ec': ec
            })
            
            data.append(df)
        
        return pd.concat(data, ignore_index=True)
    
    def generate_hyperspectral_seed(self, n_samples=500, n_wavelengths=2151):
        """Generate synthetic hyperspectral seed spectra."""
        # Wavelength range: 400-2500 nm
        wavelengths = np.linspace(400, 2500, n_wavelengths)
        
        spectra = []
        labels = {
            'germination_rate': [],
            'fungal_presence': [],
            'aflatoxin_ppb': []
        }
        
        for i in range(n_samples):
            # Base spectrum: healthy seed
            spectrum = np.ones(n_wavelengths) * 0.5
            
            # Add absorption features
            # Water absorption at 1450, 1940 nm
            spectrum[abs(wavelengths - 1450) < 50] *= 0.7
            spectrum[abs(wavelengths - 1940) < 50] *= 0.6
            
            # Protein absorption at 2180 nm
            spectrum[abs(wavelengths - 2180) < 30] *= 0.8
            
            # Add noise
            spectrum += np.random.normal(0, 0.02, n_wavelengths)
            
            # Degrade spectrum for unhealthy seeds
            is_unhealthy = np.random.random() < 0.3
            if is_unhealthy:
                # Reduced reflectance (darker)
                spectrum *= np.random.uniform(0.7, 0.9)
                # Additional absorption features (fungal)
                spectrum[abs(wavelengths - 1650) < 40] *= 0.75
                
                germination = np.random.uniform(40, 70)
                fungal = 1
                aflatoxin = np.random.lognormal(2, 1)  # Log-normal distribution
            else:
                germination = np.random.uniform(75, 95)
                fungal = 0
                aflatoxin = np.random.lognormal(0.5, 0.5)
            
            spectra.append(spectrum)
            labels['germination_rate'].append(germination)
            labels['fungal_presence'].append(fungal)
            labels['aflatoxin_ppb'].append(aflatoxin)
        
        return np.array(spectra), wavelengths, labels
    
    def generate_storage_iot(self, n_days=90, n_units=5):
        """Generate synthetic storage IoT sensor data."""
        data = []
        
        base_date = datetime(2023, 11, 1)
        
        for unit_id in range(n_units):
            dates = [base_date + timedelta(days=d, minutes=m*5) 
                    for d in range(n_days) for m in range(288)]  # 5-min intervals
            
            # Temperature: controlled storage (20-25°C) or ambient (varies)
            is_controlled = np.random.random() < 0.5
            if is_controlled:
                temp = 22 + np.random.normal(0, 1, len(dates))
            else:
                temp = 25 + 5 * np.sin(2 * np.pi * np.arange(len(dates)) / 288)  # Diurnal
                temp += np.random.normal(0, 2, len(dates))
            
            # RH: 60-70% ideal, higher = risk
            rh = 65 + 10 * np.sin(2 * np.pi * np.arange(len(dates)) / 288)
            rh += np.random.normal(0, 3, len(dates))
            rh = np.clip(rh, 40, 85)
            
            # CO₂: increases with spoilage
            co2 = 400 + np.random.normal(0, 50, len(dates))
            # Add spoilage events
            spoilage_days = np.random.choice(range(30, n_days), size=2, replace=False)
            for day in spoilage_days:
                start_idx = day * 288
                co2[start_idx:] += np.linspace(0, 500, len(dates) - start_idx)
            
            co2 = np.clip(co2, 400, 2000)
            
            # VOC: binary/qualitative (0 or 1)
            voc = np.zeros(len(dates))
            for day in spoilage_days:
                start_idx = day * 288
                voc[start_idx:] = 1
            
            df = pd.DataFrame({
                'timestamp': dates,
                'storage_unit_id': unit_id,
                'temperature': temp,
                'rh': rh,
                'co2': co2,
                'voc': voc
            })
            
            data.append(df)
        
        return pd.concat(data, ignore_index=True)
    
    def generate_weather_data(self, n_days=120):
        """Generate synthetic weather data."""
        dates = [datetime(2023, 6, 1) + timedelta(days=d) for d in range(n_days)]
        
        # Temperature: seasonal pattern
        days = np.arange(n_days)
        temp_max = 32 + 5 * np.sin(2 * np.pi * days / 120) + np.random.normal(0, 2, n_days)
        temp_min = temp_max - 8 + np.random.normal(0, 1, n_days)
        
        # Precipitation: random events
        precip = np.random.exponential(2, n_days)
        precip[precip > 20] = 0  # Some dry days
        
        # RH: inverse of temperature
        rh_mean = 70 - (temp_max - 25) * 2 + np.random.normal(0, 5, n_days)
        rh_mean = np.clip(rh_mean, 40, 90)
        
        # Solar radiation
        solar = 20 + 5 * np.sin(2 * np.pi * days / 120) + np.random.normal(0, 2, n_days)
        solar = np.clip(solar, 10, 30)
        
        # Wind speed
        wind = 5 + np.random.exponential(2, n_days)
        wind = np.clip(wind, 2, 15)
        
        df = pd.DataFrame({
            'date': dates,
            'temp_max': temp_max,
            'temp_min': temp_min,
            'precipitation': precip,
            'rh_mean': rh_mean,
            'solar_radiation': solar,
            'wind_speed': wind
        })
        
        return df


if __name__ == '__main__':
    # Generate sample data
    gen = DataGenerator()
    
    print("Generating synthetic data...")
    rgb_images, rgb_labels = gen.generate_uav_rgb(n_images=50)
    ms_images = gen.generate_multispectral(n_images=50)
    thermal_images = gen.generate_thermal(n_images=50)
    soil_data = gen.generate_soil_sensor_data(n_days=30)
    seed_spectra, wavelengths, seed_labels = gen.generate_hyperspectral_seed(n_samples=100)
    storage_data = gen.generate_storage_iot(n_days=30)
    weather_data = gen.generate_weather_data(n_days=60)
    
    print(f"Generated {len(rgb_images)} RGB images")
    print(f"Generated {len(ms_images)} multispectral images")
    print(f"Generated {len(thermal_images)} thermal images")
    print(f"Generated {len(soil_data)} soil sensor records")
    print(f"Generated {len(seed_spectra)} seed spectra")
    print(f"Generated {len(storage_data)} storage records")
    print(f"Generated {len(weather_data)} weather records")
