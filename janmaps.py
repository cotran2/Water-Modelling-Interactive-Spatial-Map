"""
Functions for mapping leaks - creating choropleths, interactive mapping, etc
Author: Janice Zhuang
Python 2.7x

REQUIRES geopandas
"""
#-------------
import geopandas as gpd
#-------------

def countPtsInPoly(points_gdf, areas_gdf):
    # Counting points in each polygon
    # e.g. #leaks in area X
    # Returns a list
    polyPtsNo = [] # number of points in each polygon
    for poly in areas_gdf.geometry:
        PtsNo = 0 # number of points in polygon 'poly'
        for point in points_gdf.geometry:
            if point.within(poly):
                PtsNo += 1
        polyPtsNo.append(PtsNo)

    return polyPtsNo

def forceMask(allAreas_gdf, colName, ax):
    # Brute force method of masking areas with NO DATA (does NOT mean 0-values)
    # for choropleth maps
    # Returns geopandas plot
    # colName=name of column w/ applicable data, ax=matplotlib subplot used
    maskedArea = []
    for i in range(0,len(allAreas_gdf)):
        if allAreas_gdf[colName][i] == 0:
            maskedArea.append(allAreas_gdf.geometry[i])
    gdf_masked = gpd.GeoSeries(maskedArea)

    return gdf_masked.plot(ax=ax, color='white')