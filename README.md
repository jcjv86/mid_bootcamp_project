# MID BOOTCAMP PROJECT



## Historic of airplane crashes 1908 - 2009



### The following dataset contains a historic with registered plane crashes all over the world, since the first in 1908 until the last registered in 2009.



The original dataset provides information on date, time, location, operator, flight no., route, type of aircraft (or model), registration (if any), cn/in (ICAO serial number of the aircraft), people on board, fatalities (or passengers and or crew deaths), ground (ground casualties, aircraft occupiers excluded), and a summary about the aircraft incident.


After thoroughly cleaning the source dataset (which took almost 4 days due to the high cardinality of aircraft models and operators, and the poorly written locations), I have plotted the most relevant information in tableau:

- Deaths by aircraft type
- Deaths by operator
- Total deaths VS passenger or ground casualties.
- Biggest accidents - by passenger or ground casualties.
- Some possible causes (4): Storm, bomb, sabotage or explosive decompression.


Also, created additional datasets with 50 values each, done with pandas groupby function after the main dataset was cleaned. They can be found in *data/cleaned* folder:

- Biggest accidents (total and civil).
- Deadliest operator (total and civil).
- Deadliest model (total and civil).
- Deadliest operator and model (total and civil).
- Ground deaths (total and civil).


Notebook folder contains the **exploratory notebook**, which was used to clean and explore the data, and the **main notebook**, where the grouping was made and then exported as additional datasets.


I have finally used tableau to help visualizing the data and build a presentation for it via story:



**[Link to the final presentation](https://public.tableau.com/app/profile/juan.jimenez7376/viz/MidBootcampProject-Airlinecasualties1907-2009/HistoryofAircraftAccidents?publish=yes)**






*Dataset source*
*https://data.world/data-society/airplane-crashes*