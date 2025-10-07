import os
import arcpy

arcpy.env.workspace = 'F:/workspace/data.gdb'
arcpy.env.overwriteOutput = True

outWorkspace = 'F:/outworkspace/otherdata.gdb'

try:
    for infc in arcpy.ListFeatureClasses():
        outfc = os.path.join(outWorkspace, infc)
        outcrs = arcpy.SpatialReference(7856)
        # GDA94 -> GDA2020 conformal transformation = 'GDA_1994_To_GDA2020' (8446); GDA94 -> GDA2020 conformal and distortion transformation = 'GDA_1994_To_GDA2020_1' (8447) (Not recommended for use on Queensland data sets due to distortions at the state borders. https://www.icsm.gov.au/sites/default/files/GDA2020TechnicalManualV1.1.1.pdf)
        transformMethod = arcpy.SpatialReference(8446)
        incrs = arcpy.SpatialReference(28356)

        # arcpy.management.Project(in_dataset, out_dataset, out_coor_system, {transform_method}, {in_coor_system}, {preserve_shape}, {max_deviation}, {vertical})
        arcpy.Project_management(infc, outfc, outcrs, transformMethod, incrs)
        print(arcpy.GetMessages())

except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
    
except Exception as ex:
    print(ex.args[0])
