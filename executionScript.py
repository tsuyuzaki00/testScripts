''' LibraryReload '''
#from mgear_guide._tools.UI import mgearVisExportUI as UI; reload(UI);
''' Run '''
#from mgear_guide._tools.Maya.Execute import mgearExportCurves as ps
from scriptsInTools.Maya.Execute import multiCopySkinWeight as ps
reload(ps); ps.main()

#import pymel.core as pm
#import maya.cmds as cmd