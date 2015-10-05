arcpy.Erase_analysis("U:/GIS/projects/transit/tasks/201405_transit/data/input/census.gdb/tracts_2010","U:/GIS/projects/transit/tasks/201405_transit/data/input/census_hydro.gdb/Areal_Hydrography","U:/GIS/data/census/2010/tracts.gdb/tracts_2010_era_hydro","#")

statesList = ["01","02","04","05","06","08","09","10","11","12","13","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","44","45","46","47","48","49","50","51","53","54","55","56","72"]

for i in statesList:
	arcpy.Select_analysis("U:/GIS/data/census/2010/tracts.gdb/tracts_2010_era_hydro","U:/GIS/data/census/2010/state/tracts_2010_state_"+i+".shp",""""STATEFP10" = '"""+i+"""'""")

	