import xarray as xr
import numpy as np

def calculate_total_magnitude(vertical_file, horizontal_file, output_file):
    # Load the vertical and horizontal data
    vertical_data = xr.open_dataset(vertical_file)
    horizontal_data = xr.open_dataset(horizontal_file)
    total_magnitude = vertical_data
    # Calculate the total magnitude
    for i in range(len(vertical_data)):
        for j in range(len(vertical_data[i])):
            for k in range(len(vertical_data[i][j])): # Data is structured in somewhat of a 3D array (note: date and coordinates)
                magnitude = (vertical_data[i][j][k] ** 2 + horizontal_data[i][j][k] ** 2) ** 0.5    # Calculate the magnitude
                if vertical_data[i][j][k] < 0:  # Revert to proper vertical orientation
                    magnitude = magnitude*(-1)
                if abs(magnitude) >= 250:       # Only keep data with IVT >= 250
                    total_magnitude[i][j][k] = magnitude
                else:
                    total_magnitude[i][j][k] = 0
                # Conditions to be added in future: length of AR, large enough vertical component

    # Create a new dataset to store the filtered data
    filtered_data = xr.Dataset(
        {
            'total_magnitude': total_magnitude
        },
        coords=vertical_data.coords
    )

    # Save the new dataset to a NetCDF file
    filtered_data.to_netcdf(output_file)

    # Close the input and output files
    vertical_data.close()
    horizontal_data.close()

    print(f"Filtered data saved to {output_file}.")

# Data input and output. Currently using data from 12/01/2010 - 12/31/2010
vertical_file = '/glade/scratch/bnewman6/e5.oper.an.vinteg.162_072_viwvn.ll025sc.2010120100_2010123123.nc'
horizontal_file = '/glade/scratch/bnewman6/e5.oper.an.vinteg.162_071_viwve.ll025sc.2010120100_2010123123.nc'
output_file = 'ivt.nc'

calculate_total_magnitude(vertical_file, horizontal_file, output_file)
