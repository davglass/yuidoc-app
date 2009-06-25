#
#  YUIDocGUIAppDelegate.py
#  YUIDocGUI
#
#  Created by Dav Glass on 6/25/09.
#  Copyright __MyCompanyName__ 2009. All rights reserved.
#

from objc import YES, NO, IBAction, IBOutlet
from Foundation import *
from AppKit import *
from subprocess import call, PIPE, Popen




class YUIDocGUIAppDelegate(NSObject):
    sourcepath = objc.ivar(u"sourcepath")
    savepath = objc.ivar(u"savepath")
    tmpPath = '/tmp/yuidoc/'
    projectname = objc.ivar(u"projectname")
    projecturl = objc.ivar(u"projecturl")
    projectversion = objc.ivar(u"projectversion")
    showprivate = objc.ivar(u"showprivate")
    ext_js = objc.ivar(u"ext_js")
    ext_as = objc.ivar(u"ext_as")
    ext_py = objc.ivar(u"ext_py")
    ext_php = objc.ivar(u"ext_php")
    ext_pl = objc.ivar(u"ext_pl")
    ext_rb = objc.ivar(u"ext_rb")
    ext_cs = objc.ivar(u"ext_cs")
    ext_java = objc.ivar(u"ext_java")

    def applicationDidFinishLaunching_(self, sender):
        self.ext_js = True
        self.showprivate = True
        self.projectname = 'My Project'
        NSLog("Application did finish launching.")
    
    @IBAction
    def generate_(self, value):
        templatePath = './yuidoc/template'
        cmd = './yuidoc/bin/yiudoc.py %s -p %s -o %s -t %s -v %s' % (self.sourcepath, self.tmpPath, self.savepath, templatePath, self.projectversion)
        NSLog("Run: %s" % cmd)

