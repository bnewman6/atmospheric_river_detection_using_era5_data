# atmospheric_river_detection_using_era5_data
I used the Cheyenne supercomputer to simulate and analyze integral water vapor transport. Using this data, I wrote a Python program to detect atmospheric rivers.

![image](https://github.com/bnewman6/atmospheric_river_detection_using_era5_data/assets/114265369/2d5009e8-d4ae-41b9-ae0f-263ba776f4c2)
Filtered data highlighting an atmospheric river running through the western United States

## Inspiration
An atmospheric river (AR) is a stream of water vapor that traditionally moves from the tropics away from the equator. If an AR reaches land that is not prepared for the heavy rainfall that ARs bring, it can be devastating for both humans and animals living there. I wanted to create a program that detects ARs before they reach land in order to predict where rainfall may occur and ensure civilians are prepared for potential heavy rain.

## What it does
There are two components of this project: the Python program and the plotting. The Cheyenne supercomputer allowed for this project to be possible and for results to be observable. The Python program takes a data file, in this case for integrated water vapor transport (IVT), and filters it based on the given guidelines. Then, I plot that output file using an NCAR Command Language script that shows the filtered data that clearly highlights atmospheric rivers.

## How I built it
The Python program is meant to take in the nc file for IVT provided by the European Reanalysis (ERA5). It first converts the data into an array in order to loop through the points. I wrote my code to run through a specific date and time within the dataset, but it works for any range of dates/times. Looping through each point, it checks if the value qualifies against the definition of an atmospheric river. Examples of specific measures I checked were IVT magnitude and northward IVT. If the data point did not qualify according to the definition, it was set to 0, thus not appearing in the final plot. The last thing the program does is convert the data arrays into the output nc files.

The next aspect of this project was plotting the output files to show to detected atmospheric rivers. I used the NCAR Command Language (NCL) to create a script to graph the data. In this project, I was very focused on a specific atmospheric river called the Pineapple Express, which runs from Hawaii to west/northwest North America. In my NCL script, I have the domain set as the Pineapple Express region.

## Challenges I ran into
My full focus on this project was during an 8-week Summer research internship with the UMD FIRE Program. A major challenge I ran into was deciding how complex I wanted my program to be based on the time I had in the internship. I concluded on the Python program I ended up writing. After writing the Python code, it was difficult to assure everything was correct due to the time it took to run the program. Initially, I was running it through the data for the entire globe every six hours for an entire month period. In order to more quickly analyze my program, I narrowed in to just the Pineapple Express region on a specific time of a specific day I knew had an atmospheric river. This helped me get results much faster and be able to know that the program had worked.

## Accomplishments that I'm proud of
I am proud of the Python program I wrote and the research I did to learn all about atmospheric rivers. I used this knowledge in the program in order to successfully detect atmospheric rivers and highlight them in a dataset.

## What I learned
I acquired many skills ranging from Python skills to Bash to NCL to learning about the atmosphere. Additionally, I strengthened my ability to collaborate with my professor and also with fellow interns working on other research.

## What's next for Atmospheric River Detection Using ERA5 Data
I plan on further improving the program by adding more filters to make the results more precise. Then, I will add to the program a section that calculates and predicts the future rainfall location as a result of the atmospheric river.

## Links to Annotated Bibliography and Presentation
https://docs.google.com/document/d/1mpNeMwwkUHWvbehLlHORiMYOWsg9eWBLUp-qHbLaEk0/edit?usp=sharing
https://docs.google.com/presentation/d/1P1cyBP6kZ-Z0iWtT0vq2AETFM83YIbyrsD6BPDQaxQA/edit?usp=sharing
