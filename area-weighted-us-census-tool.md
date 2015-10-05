#Area-Weighted US Census Variables Tool
2010 Census Tracts.

#####Name ideas
* censusify
* geoBender
* geoShakedown 
* geoGravy
* geoCider
* geoTurtle
* geoCactus
* geoDrool
* geoBlast
* geoFrisell

##Geoprocessing steps for input Census Data

1. Intersect all Census Tracts with Area_Hydrography. All data at this point is in native geographic coordinate system from the US Census:

		GCS_North_American_1983
		WKID: 4269 Authority: EPSG

		Angular Unit: Degree (0.0174532925199433)
		Prime Meridian: Greenwich (0.0)
		Datum: D_North_American_1983
		  Spheroid: GRS_1980
		    Semimajor Axis: 6378137.0
		    Semiminor Axis: 6356752.314140356
		    Inverse Flattening: 298.257222101



2. Geoprocessing



		arcpy.Erase_analysis(".../census.gdb/tracts_2010",".../census_hydro.gdb/Areal_Hydrography",".../tracts.gdb/tracts_2010_era_hydro","#")

		statesList = ["01","02","04","05","06","08","09","10","11","12","13","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","44","45","46","47","48","49","50","51","53","54","55","56","72"]

		for i in statesList:
			arcpy.Select_analysis(".../tracts.gdb/tracts_2010_era_hydro",".../census/2010/state/tracts_2010_state_"+i+".shp",""""STATEFP10" = '"""+i+"""'""")

3. Uploaded all tracts by state with pgShapeLoader to Amazon RDS.

	http://docs.aws.amazon.com/AmazonRDS/latest/APIReference/	API_CopyDBClusterSnapshot.html


	https://us-west-2.console.aws.amazon.com/rds/home?region=us-west-2#db-snapshots:

	Copy snapshot to east coast.... 


4. Define SRID projections. 4269. 


5. Reproject
6. Area Cac? 