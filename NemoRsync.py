#!/usr/bin/python2

import os
import sys
from urlparse import urlparse
import urllib2
from gi.repository import Gtk, Gdk

rsync_args="-aP --protect-args --inplace"
#Will try integrating zenity later
use_Zenity=False 

def rsyncify(uri):
    """Produces a rsync compatible path"""
    data = urlparse(uri)
    path = urllib2.unquote(data.path)
    if(data.scheme=="sftp"):
        user=data.username
        host = data.hostname
        #Get proper unqouted path
        if(user is not None):
            rsync_url="\"%s@%s:%s\""%(user,host,path)
        elif(host is not None):
            rsync_url="\"%s:%s\""%(host,path)
    else:
        rsync_url="\"%s\""%(path)    
    return rsync_url


target_uri=sys.argv[1]

#Get clipboard if it's copied files
clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
result = clipboard.wait_for_contents(Gdk.Atom.intern("x-special/gnome-copied-files", False))
str_clipboard=result.get_data()

#rsync file by file
for clipboard_uri in str_clipboard.splitlines()[1:]:
    rsync_url1=rsyncify(clipboard_uri)
    rsync_url2=rsyncify(target_uri)
    if use_Zenity:
        #This was taken from http://www.davidverhasselt.com/zenity-rsync-and-awk/ and would probably work for folders.
        cmd="rsync %s %s %s |awk -f rsync.awk |zenity --progress --title \"Backing up USB-Stick\" --text=\"Scanning...\" --percentage=0 --auto-kill"%(rsync_args,rsync_url1,rsync_url2)
    else:
        cmd="rsync %s %s %s"%(rsync_args,rsync_url1,rsync_url2)   
    print type(result)
    os.system(cmd)

