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
import os
from cStringIO import StringIO




class YUIDocGUIAppDelegate(NSObject):
    myWindow = objc.IBOutlet()
    textView = objc.IBOutlet()
    generateButton = objc.IBOutlet()
    sourcepath = objc.ivar(u"sourcepath")
    savepath = objc.ivar(u"savepath")
    tmpPath = '/tmp/yuidoc/'
    project_name = objc.ivar(u"project_name")
    project_url = objc.ivar(u"project_url")
    project_version = objc.ivar(u"project_version")
    generate = objc.ivar(u"generate")
    showprivate = True
    _show_private = True
    _can_start = False
    
    ext = {
        'js': True,
        'as': False,
        'py': False,
        'php': False,
        'pl': False,
        'rb': False,
        'cs': False,
        'java': False
    }

    def applicationShouldTerminateAfterLastWindowClosed_(self, sender):
        return True


    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
        NSLog("SV: %s" % self.textView)
        NSLog("generateButton: %s" % self.generateButton)
        self.textView.insertText_('Logging will appear here.\n')
    
    @IBAction
    def setextjs_(self, value):
        self.ext['js'] = value.state()

    @IBAction
    def setextas_(self, value):
        self.ext['as'] = value.state()

    @IBAction
    def setextpy_(self, value):
        self.ext['py'] = value.state()

    @IBAction
    def setextphp_(self, value):
        self.ext['php'] = value.state()

    @IBAction
    def setextpl_(self, value):
        self.ext['pl'] = value.state()

    @IBAction
    def setextrb_(self, value):
        self.ext['rb'] = value.state()

    @IBAction
    def setextcs_(self, value):
        self.ext['cs'] = value.state()

    @IBAction
    def setextjava_(self, value):
        self.ext['java'] = value.state()

    @IBAction
    def setprivate_(self, value):
        self._show_private = value.state()

    @IBAction
    def setprojectname_(self, value):
        self.validate()

    @IBAction
    def setprojecturl_(self, value):
        self.validate()

    @IBAction
    def setprojectversion_(self, value):
        self.validate()

    @IBAction
    def setsourcepath_(self, value):
        self.validate()

    @IBAction
    def setsavepath_(self, value):
        self.validate()

    def validate(self):
        #self.logoutput = 'Logging will show here.'
        #NSLog("LOG: %s" % self.logoutput)
        NSLog("VALIDATE: ")
        self._can_start = False
        self.generateButton.setEnabled_(False)
        NSLog("VALIDATE: %s" % self.sourcepath)
        if self.project_version and self.project_name and self.project_url and self.sourcepath and self.savepath:
            self.generateButton.setEnabled_(True)
            self._can_start = True
            

        NSLog("VALIDATE: %s" % self._can_start)
            
        

    @IBAction
    def generate_(self, value):
        if not self._can_start:
            NSBeginInformationalAlertSheet(
                u"Can not generate docs",
                u"OK", None, None, self.myWindow, None, None, None, None,
                u"Please fill in all fields, they are required.."
            )
            
            NSLog("Can not start, not enough info")
            return

        self.textView.insertText_('Doc generation starting, please wait..\n')
        self.generateButton.setTitle_('Generating..')
        
        ##This is a hack and needs to be fixed..
        yuidocPath = "%s/YUIDocGUI.app/Contents/Resources/yuidoc" % os.path.abspath('./')
        templatePath = '%s/template' % yuidocPath
        ext = []
        for i in self.ext.keys():
            if self.ext[i]:
                ext.append(".%s" % i)
        
        args = [
            '%s/bin/yuidoc.py' % yuidocPath,
            self.sourcepath.path(),
            '-p', self.tmpPath,
            '-o', self.savepath.path(),
            '-t', templatePath,
            '-v', self.project_version,
            '-e', ','.join(ext)
        ]
        if self._show_private:
            args.append('-s')

        NSLog("Run: %s" % args)
        NSLog('Path: %s' % yuidocPath)
        return True
        #call(args)
        error_file = open('/tmp/yuidoc.log', 'w+')
        
        logoutput = ''
        retcode = call(args, stderr=error_file, stdout=error_file)
        if retcode > 0:
            logoutput = 'ERROR\n\n'

        f = open('/tmp/yuidoc.log')
        logoutput = "%s %s" % (logoutput, f.read())
        NSLog("LOG: %s" % logoutput)
        
        self.textView.insertText_('%s\nDocs finished..' % logoutput)
        NSLog("Docs finished..")
        self.generateButton.setTitle_('Generate Docs')


