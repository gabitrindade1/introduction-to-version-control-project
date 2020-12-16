__December 15, 2020__


### Explore US Bikeshare Data
This project was written as a prerequisite to conclude Udacity’s Programming for Data Science with Python nanodegree program. It uses Python to answer some questions about bikeshare trip data collected from three US cities, Chicago, New York City, and Washington. The code was written to collect the data, compute descriptive statistics, and create an interactive experience in the terminal that presents the answers to user’s questions.

### Software required
* Python 3
* A text editor, such as VSCode or Atom
* A terminal application

### Files used
* bikeshare.py
* chicago.csv
* washington.csv
* new-york-city.csv

### Datasets
The datasets used were provided by [Motivate]( https://www.motivateco.com/), a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.
All the three data files used for this project are a condensed version of these original files [Chicago](https://www.divvybikes.com/system-data), [New York City](https://www.citibikenyc.com/system-data), [Washington](https://www.capitalbikeshare.com/system-data), which were much larger and messier. The data files that were used contain randomly selected data for the first six months of 2017 and these same core six columns for the three cities:
* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)
The Chicago and New York City files also have the following two columns:
* Gender
* Birth Year

### References
Dealing with invalid inputs:
* https://youtu.be/JGztEBLGj5E?list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye

Adding time delays to the code:
* https://youtu.be/kchC5KLZSZ4?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6
* https://realpython.com/python-sleep/

Displaying colored text:
* https://youtu.be/0hBIhkcA8O8

Dealing with issues related to the "month" and "day of week" extraction from "Start Time":
* https://stackoverflow.com/questions/60214194/error-in-reading-stock-data-datetimeproperties-object-has-no-attribute-week
* https://github.com/pandas-dev/pandas/issues/22830
* https://knowledge.udacity.com/questions/340489
* https://www.geeksforgeeks.org/python-calendar-module/

Dealing with issues related to displaying dataset:
* https://stackoverflow.com/questions/25628496/getting-wider-output-in-pycharms-built-in-console

Dealing with issues related to displaying raw data:
* https://knowledge.udacity.com/questions/2132
* https://knowledge.udacity.com/questions/88906
* https://knowledge.udacity.com/questions/237695
