#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


# Create a DataFrame with the structured data
vehicle1 = pd.DataFrame({
    'Temperature (°C)': [26, 26, 26, 26, 26],
    'Humidity (%)': [61, 61, 61, 61, 61],
    'CO2 Level': [54.25, 54.25, 54.15, 54.15, 54.15]
})

# Create subplots for Temperature, Humidity, and CO2 Level
plt.figure(figsize=(12, 4))

# Temperature plot
plt.subplot(131)
plt.plot(vehicle1.index, vehicle1['Temperature (°C)'], label='Temperature (°C)', color='red')
plt.xlabel('Sample')
plt.ylabel('Temperature (°C)')
plt.title('Temperature')

# Humidity plot
plt.subplot(132)
plt.plot(vehicle1.index, vehicle1['Humidity (%)'], label='Humidity (%)', color='blue')
plt.xlabel('Sample')
plt.ylabel('Humidity (%)')
plt.title('Humidity')

# CO2 Level plot
plt.subplot(133)
plt.plot(vehicle1.index, vehicle1['CO2 Level'], label='CO2 Level', color='green')
plt.xlabel('Sample')
plt.ylabel('CO2 Level')
plt.title('CO2 Level')

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()


# In[3]:


# Create a DataFrame with the structured data
vehicle2 = pd.DataFrame({
    'Temperature (°C)': [36, 36, 36, 36, 36, 36],
    'Humidity (%)': [22, 22, 22, 22, 21, 21],
    'CO2 Level': [61.58, 61.58, 61.78, 61.00, 61.68, 61.88]
})

# Create subplots for Temperature, Humidity, and CO2 Level
plt.figure(figsize=(12, 4))

# Temperature plot
plt.subplot(131)
plt.plot(vehicle2.index, vehicle2['Temperature (°C)'], label='Temperature (°C)', color='red')
plt.xlabel('Sample')
plt.ylabel('Temperature (°C)')
plt.title('Temperature')

# Humidity plot
plt.subplot(132)
plt.plot(vehicle2.index, vehicle2['Humidity (%)'], label='Humidity (%)', color='blue')
plt.xlabel('Sample')
plt.ylabel('Humidity (%)')
plt.title('Humidity')

# CO2 Level plot
plt.subplot(133)
plt.plot(vehicle2.index, vehicle2['CO2 Level'], label='CO2 Level', color='green')
plt.xlabel('Sample')
plt.ylabel('CO2 Level')
plt.title('CO2 Level')

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()


# In[4]:


# Create a DataFrame with the structured data
vehicle3 = pd.DataFrame({
    'Temperature (°C)': [19, 19, 19, 19, 19, 19],
    'Humidity (%)': [69, 69, 69, 69, 69, 70],
    'CO2 Level': [54.55, 54.55, 54.55, 54.55, 54.55, 54.55]
})

# Create subplots for Temperature, Humidity, and CO2 Level
plt.figure(figsize=(12, 4))

# Temperature plot
plt.subplot(131)
plt.plot(vehicle3.index, vehicle3['Temperature (°C)'], label='Temperature (°C)', color='red')
plt.xlabel('Sample')
plt.ylabel('Temperature (°C)')
plt.title('Temperature')

# Humidity plot
plt.subplot(132)
plt.plot(vehicle3.index, vehicle3['Humidity (%)'], label='Humidity (%)', color='blue')
plt.xlabel('Sample')
plt.ylabel('Humidity (%)')
plt.title('Humidity')

# CO2 Level plot
plt.subplot(133)
plt.plot(vehicle3.index, vehicle3['CO2 Level'], label='CO2 Level', color='green')
plt.xlabel('Sample')
plt.ylabel('CO2 Level')
plt.title('CO2 Level')

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()


# In[5]:


# Create DataFrames for 'vehicle1,' 'vehicle2,' and 'vehicle3' with the respective means
vehicle1 = pd.DataFrame({
    'Parameter': ['Temperature', 'Humidity', 'CO2 Level'],
    'Mean': [26, 61, 54.25]
})

vehicle2 = pd.DataFrame({
    'Parameter': ['Temperature', 'Humidity', 'CO2 Level'],
    'Mean': [36, 22, 61.72]
})

vehicle3 = pd.DataFrame({
    'Parameter': ['Temperature', 'Humidity', 'CO2 Level'],
    'Mean': [19, 69, 54.55]
})

# Create a figure with three subplots for Temperature, Humidity, and CO2 Level means
plt.figure(figsize=(15, 5))

# vehicle means plot (line plot)
plt.subplot(131)
plt.plot(vehicle1['Parameter'], vehicle1['Mean'], label='vehicle1', marker='o', color='red')
plt.plot(vehicle2['Parameter'], vehicle2['Mean'], label='vehicle2', marker='o', color='blue')
plt.plot(vehicle3['Parameter'], vehicle3['Mean'], label='vehicle3', marker='o', color='green')
plt.xlabel('Parameter')
plt.ylabel('Mean Value')
plt.title('Vehicle Conditions')
plt.legend()

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()


# In[ ]:




