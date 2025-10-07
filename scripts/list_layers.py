import os, csv
from arcpy import mapping

cwd = os.getcwd()

outfile = 'layers.csv'
fields = ['mxd_name', 'mxd_location', 'layer_name', 'data_source', 'description']
rows = []

for f in os.listdir(cwd):
    if f.endswith('.mxd'):
        mxd_name = '=HYPERLINK("' + cwd + '\\' + f + '", "' + f + '")'
        mxd_path = '=HYPERLINK("' + cwd + '", "' + cwd + '")'
        mxd = arcpy.mapping.MapDocument(f)
#        Enable df and give extra argument to arcpy.mapping.ListLayers to only return layers from a specified data frame
#        df = arcpy.mapping.ListDataFrames(mxd, 'Layers')
        for l in arcpy.mapping.ListLayers(mxd):
            l_name = l.longName
            ds = l.dataSource
            desc = l.description
            rows.append({'mxd_name': mxd_name, 'mxd_location': mxd_path, 'layer_name': l_name, 'data_source': ds, 'description': desc})

with open(outfile, 'wb') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames = fields)
    csvwriter.writeheader()
    csvwriter.writerows(rows)
