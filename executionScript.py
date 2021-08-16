''' LibraryReload '''
#from MayaLibrary import setCurves as ml; reload(ml);
''' Run '''
#from scriptsInTools.singleRun import skinPaintValue as ps
from scriptsInTools.Maya.Manager import selectBind as ps
reload(ps); ps.main()

#import pymel.core as pm
#import maya.cmds as cmd