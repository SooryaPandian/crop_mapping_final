import geopandas as gpd

# Load your shapefile
shapefile_path = "test/dataPoints/AllMarkersExport.shp"  # update if needed
gdf = gpd.read_file(shapefile_path)

# List all available columns (features)
print("Available columns in shapefile:")
print(gdf.columns.tolist())

# Check for specific required columns
required_columns = ['id', 'type', 'crpname_eg', 'geometry']
print("\nChecking for required columns:")

missing_columns = []
for col in required_columns:
    if col in gdf.columns:
        print(f"✅ Column '{col}' exists.")
    else:
        print(f"❌ Column '{col}' is missing.")
        missing_columns.append(col)

if missing_columns:
    print("\nThe following required columns are missing:")
    print(missing_columns)
    print("Please ensure the shapefile contains these columns before proceeding.")
else:
    # Display all unique values in the 'type' column
    if 'type' in gdf.columns:
        print("\nUnique values in 'type' column:")
        print(gdf['type'].unique())
