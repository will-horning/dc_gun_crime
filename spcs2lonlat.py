"""
The crime data all uses state plane coordinates for the location, to plot 
these in Leaflet those coords need to be converted to latitude and 
longitude. I'm using the gdal package (pip install gdal) to do this, but
I was unable to get gdal working inside virtualenv to if you want to run 
this script you'll have to install gdal at the global level.
"""

from osgeo import ogr, osr
import sys, csv

MD_SPCS_CODE = 26985
LATLON_CODE = 4326
WKT_FORMAT_STRING = 'POINT (%i %i)'

if __name__ == '__main__':
    INPUT_PATH = sys.argv[1]
    source = osr.SpatialReference()
    source.ImportFromEPSG(MD_SPCS_CODE)
    target = osr.SpatialReference()
    target.ImportFromEPSG(LATLON_CODE)
    transform = osr.CoordinateTransformation(source, target)
    with open(INPUT_PATH, 'rb') as f:
        reader = csv.DictReader(f, delimiter=',')
        new_fields = reader.fieldnames + ['LON', 'LAT']
        print ','.join(new_fields)
        for row in reader:
            coord = float(row['BLOCKXCOORD']), float(row['BLOCKYCOORD'])
            point = ogr.CreateGeometryFromWkt(WKT_FORMAT_STRING % coord)
            point.Transform(transform)
            row['LON'], row['LAT'] = str(point.GetX()), str(point.GetY())
            print ','.join([row[field] for field in new_fields])
