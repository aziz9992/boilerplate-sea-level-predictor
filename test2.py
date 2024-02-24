import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read the CSV file into a DataFrame
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='CSIRO Adjusted Sea Level')
    #print(df['Year'])
    #print(df['CSIRO Adjusted Sea Level'])
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level (mm)')
    plt.title('CSIRO Adjusted Sea Level Over Time')

    # Get slope and y-intercept using linregress
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create line of best fit
    line_x = range(1880, 2051)  # Years from 1880 to 2050
    line_y = slope * line_x + intercept
    # Format line_y values
    line_y_formatted = [f"{y:.16f}" for y in line_y]
    # Convert string representation of floats to integers
    line_y = [float(y) for y in line_y_formatted]
    #print(line_y_integers)
    # Plot the line of best fit
    plt.plot(line_x, line_y_formatted, color='red', label='Line of Best Fit')

    # Predict sea level rise in 2050
    sea_level_2050 = slope * 2050 + intercept
    plt.text(2050, sea_level_2050, f'Predicted Sea Level in 2050: {sea_level_2050:.2f} mm', verticalalignment='bottom')

    # Filter data from year 2000 to the most recent year
    recent_data = df[df['Year'] >= 2000]

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='CSIRO Adjusted Sea Level')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level (mm)')
    plt.title('CSIRO Adjusted Sea Level Over Time')

    # Get slope and y-intercept using linregress for recent data
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])

    # Create line of best fit for recent data
    line_x_recent = range(2000, 2051)  # Years from 2000 to 2050
    line_y_recent = slope_recent * line_x_recent + intercept_recent

    # Plot the line of best fit for recent data
    plt.plot(line_x_recent, line_y_recent, color='green', label='Line of Best Fit (2000-2050)')

    # Predict sea level rise in 2050 based on recent data
    sea_level_2050_recent = slope_recent * 2050 + intercept_recent
    plt.text(2050, sea_level_2050_recent, f'Predicted Sea Level in 2050 (2000-2050): {sea_level_2050_recent:.2f} mm', verticalalignment='bottom')
    # Format line_y values
    line_y_recent_formatted = [f"{y:.16f}" for y in line_y_recent]
    # Convert string representation of floats to integers
    line_y_recent = [float(y) for y in line_y_recent_formatted]
    print(line_y_recent)
    # Display the plot
    plt.legend()
    plt.grid(True)
    plt.show()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
   
draw_plot()