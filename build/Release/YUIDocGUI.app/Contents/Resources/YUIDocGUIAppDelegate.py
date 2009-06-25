#
#  YUIDocGUIAppDelegate.py
#  YUIDocGUI
#
#  Created by Dav Glass on 6/25/09.
#  Copyright __MyCompanyName__ 2009. All rights reserved.
#

from Foundation import *
from AppKit import *
import objc

class YUIDocGUIAppDelegate(NSObject):
	sourcePath = objc.ivar(u"sourcepath")
	savePath = objc.ivar(u"savepath")
	tmpPath = '/tmp/yuidoc/'
	projectName = objc.ivar(u"projectname")
	projectURL = objc.ivar(u"projecturl")
	projectVersion = objc.ivar(u"projectversion")
	showPrivate = objc.ivar(u"showprivate")
	
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
	
	def setGenerate_(self, value):
		NSLog("Hopefully this is when Generate is clicked...")