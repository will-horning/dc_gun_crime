Correlating Gunshots With Crime Reports
----------------------------------------
The goal of this project is to get a rough idea of police involved shooting incidents. The DC city government has released crime reports for the period of 2011-2013 giving the time, location (within a city block) and type of crime. DC also has a [ShotSpotter](http://www.shotspotter.com/) system in place (a network of devices spread across the city that can detect a gunshot by the sound to within a 100-meter radius).

I've taken both these sets of data to find every ShotSpotter event that occurs within a half hour before and a half hour after the time of a crime report and within 100 meters of the crime location. You can see the location of these events on the map, as well as a breakdown of the types of crimes shown. It should be noted that there is a noticeable spike in ShotSpotter incidents around Independence Day and New Years Eve, due to the fireworks at those times, so any events around those times are marked with a teal color.

You can find all of the source data in the data folder, as well as JSON dumps of the data after its been loaded into MongoDB.

This is still very preliminary work, so I can't make any guarantees as to the accuracy of how the data is depicted here.

Licenses and Attribution:
-------------------------

- Shotspotter Data is from a FOIA request made by Muckrock.com, you can see the details and download the data here: [https://www.muckrock.com/foi/washington-48/dc-shotspotter-reports-6418/](https://www.muckrock.com/foi/washington-48/dc-shotspotter-reports-6418/).

- Crime reports are courtesy of [data.dc.gov](http://data.dc.gov), Disclaimer:
    > The data made available here has been modified for use from its original 
    > source, which is the Government of the District of Columbia. Neither the 
    > District of Columbia Government nor the Office of the Chief Technology 
    > Officer (OCTO) makes any claims as to the completeness, accuracy or 
    > content of any data contained in this application; makes any 
    > representation of any kind, including, but not limited to, warranty of 
    > the accuracy or fitness for a particular use; nor are any such warranties 
    > to be implied or inferred with respect to the information or data 
    > furnished herein. The data is subject to change as modifications and 
    > updates are complete. It is understood that the information contained in 
    > the web feed is being used at one's own risk.

- Map icons are courtesy of [mapicons.nicolasmollet.com](http://mapicons.nicolasmollet.com/), 
    License: [Creative Commons Attribution-Share Alike 3.0 Unported](http://creativecommons.org/licenses/by-sa/3.0/)
