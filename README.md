# election_tracker
#### Installation Guide

In QGIS (3.2)

Plugin > Manage and Install Plugins > Install From Zip > Choose "election_plugin.zip"

#### System Requirement
QGIS (3.2+), Python (3.7), PyQt5. The computer must have two times the size of the shapefile in available memory.

### Software Requirements
Polygon Shapefile

* A field attribute that functions as a foreign key when joining with CSV file. The polygon shapefile must also have a minimum of 1 polygon.
CSV file
* ALL COLUMN HEADINGS MUST BE LESS THAN 8 CHARACTERS IN LENGTH
* A column that functions as a foreign key when joining with Shapefile.
* A column that functions as population (all values must be positive Integers).
* (Optional)
* A column that can function as percentage chance (from 0-100 in integer) when using a random filter (Optional).
* A column that can represent the polygon state win(1)/lose(0)/undecided(-1). (1, 0, -1 must be the only values in column).

#### Input Section
The directory explorer only allows the user to add .shp to Shapefile field and .csv to CSV File field. Click Load files next to add the provided files into memory. The program WILL NOT work unless Load files has been triggered.

#### Choosing fields
* Shapefile Join Field (Required): Field attribute in the Shapefile that functions as a foreign key when joining with the CSV file.

* CSV Join Field (Required): Column in the CSV file that functions as a foreign key when joining with the Shapefile file.

* Choose Election Results Field: Column in the CSV file that represent the polygon state. (Choose None if all the polygons need to be labeled as undecided)

* Choose Weight Field (Required): Column in the CSV file that represents the weight that determines win/lose. Example: population/electoral vote.
* Choose Bias weight Field: Column in the csv that represents the chance of winning (if polygon is undecided). Default value is 50 if nothing is provided.
* Choose Prediction Field (Required): (Default Bottom Up)
  * Bottom Up: This filter starts by adding the polygons with the smallest weight (taking into account already determined polygons) and continues to add up the next smallest polygons until the threshold (50% or more of the total weight) is met and/or cleared or the election is a determined loss.
  * Top Down: This filter starts by adding the polygons with the largest weight (taking into account already determined polygons) and continues to add up the next largest weight until the threshold (50% or more of the total weight) is met and/or cleared or the election is a determined loss.
  * Random: This filter assumes every polygon has a 50/50 chance to be won/lost and visits every unassigned polygon to determine if it is won or lost.
  * Random With Bias: This filter will use the field “Bias weight” to increase or decrease the percentage chance of the polygon being determined as won or lost, if there is no value in “Bias weight” it assumes a 50% chance.
  * Simulated With Bias (100 iterations): Runs Random With Bias 100 times and records each won and loss. The symbology is updated with won configuration if won count is greater than or equal to loss count and vice versa.
  
#### Submit Fields

The joined QgsVectorLayer is added to the canvas (including updated symbology if Choose Election Results Field is provided).

#### Select Tool
Enable Select Tool (Check Box): The joined QgsVectorLayer is added to the canvas (including updated symbology if Choose Election Results Field is provided).
* Won Button: Any selected items chosen when this button is toggled are marked as Lost.
* Lost Button: Any selected items chosen when this button is toggled are marked as Lost.
* Undecided Button: Any selected items chosen when this button is toggled are marked as Undecided.
* Submit Outcomes Button: Any selected items chosen when this button is pressed are marked as the current toggled radio button.
* Reset Button: Reset Button resets all of the polygons elec_result attribute to the provided election result in csv (default to undecided if no field is selected)
3

#### Output Report (Check Box)

The enables the user to specify the directory to output the .txt file to.

#### Run Analysis
* Stops the Select Tool.
* Runs analysis with the prediction filter chosen.
* Reports the results of the current selected filter in the textbox below.
* If output report has been checked, the program runs all the prediction filters and outputs the result to the provided location.
* The current layer’s symbology is updated according to the chosen prediction filter.

#### Textbox below Run Analysis
* Information is often updated in the textbox to guide the user
* Display the status of the active tool (this is visible when using a large shapefile).
