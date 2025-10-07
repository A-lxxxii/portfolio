import os
from arcpy import mapping

cwd = os.getcwd()
outdir = cwd + '\\PDF'

os.mkdir(outdir)

for f in os.listdir(cwd):
    if f.endswith('.mxd'):
        mxd = arcpy.mapping.MapDocument(f)
        fname = os.path.basename(f)
        outpdf = outdir + fname + '.pdf'
        print(f + ' > ' + outpdf)
        arcpy.mapping.ExportToPDF(mxd, outpdf)
        del mxd