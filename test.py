import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Filter the data from year 2000 to the most recent year
    recent_data = df[df['Year'] >= 2000]

    # Perform linear regression on the recent data
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])

    
    # Predict sea level rise in 2050 based on the recent data
    year_2050 = 2050
    predicted_sea_level_2050_recent = slope_recent * year_2050 + intercept_recent

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data')
    # Create first line of best fit
    plt.plot(recent_data['Year'], slope_recent * recent_data['Year'] + intercept_recent, color='red', label='Line of Best Fit (2000-Present)')
    # Perform linear regression on the recent data
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])

    # Predict sea level rise in 2050 based on the recent data
    year_2050 = 2050
    predicted_sea_level_2050_recent = slope_recent * year_2050 + intercept_recent

    # Generate predicted sea levels for the years in the dataset
    predicted_sea_levels = slope_recent * recent_data['Year'] + intercept_recent

    print(predicted_sea_levels.tolist())
    # Convert the result into a list of rounded values
    result_list = [round(value, 15) for value in slope_recent * recent_data['Year'] + intercept_recent]

    # Print the list
    #print(result_list)
    # Create second line of best fit
    plt.scatter(year_2050, predicted_sea_level_2050_recent, color='green', label='Predicted Sea Level in 2050 (2000-Present)')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()