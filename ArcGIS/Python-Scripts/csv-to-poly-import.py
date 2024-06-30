import arcpy
import csv
import os

arcpy.env.overwriteOutput = True

input_csv = r"input-file-path"
out_gdb = r"output-.gdb-project"
out_name = "output-name"
out_fc_path = os.path.join(out_gdb, out_name)

source_sr = arcpy.SpatialReference(4269)  # Source spatial reference NAD83
target_sr = arcpy.SpatialReference(4326)  # ArcGIS Topography Map WGS1984

# Create a blank output feature class with the target spatial reference
out_fc = arcpy.management.CreateFeatureclass(out_path=out_gdb,
                                             out_name=out_name,
                                             geometry_type="POLYGON",
                                             spatial_reference=target_sr)

# Open CSV and read WKT
with open(input_csv, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    with arcpy.da.InsertCursor(out_fc, ["SHAPE@"]) as icurs:
        for row in csvreader:
            wkt_geom = row[0]
            try:
                # Create geometry from WKT in source spatial reference
                geom_from_wkt = arcpy.FromWKT(wkt_geom, source_sr)

                # Project geometry to target spatial reference
                projected_geom = geom_from_wkt.projectAs(target_sr)

                # Insert the projected geometry into the feature class
                icurs.insertRow([projected_geom])

            except Exception as e:
                print(f"Failed to convert or project geometry: {wkt_geom}; Error: {str(e)}")

# Code from https://community.esri.com/t5/arcgis-pro-questions/how-to-convert-wkt-polygon-data-in-csv-file-into/td-p/1304292