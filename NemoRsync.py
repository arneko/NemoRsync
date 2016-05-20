#!/usr/bin/python2

import os
import sys
from urlparse import urlparse
import urllib2
from gi.repository import Gtk, Gdk

#Need --protect-args so I don't need to do any further magic with the paths (e.g. " "->"\\\ "), using --inplace should be optional
rsync_args="-aP --protect-args --inplace"
#Will try integrating zenity later
use_Zenity=False 

def rsyncify(uri):
    """Produces an rsync compatible path"""
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
    elif(data.scheme=="file"):
        rsync_url="\"%s\""%(path)
    else:
        os.system("zenity --error \"NemoRsync is made for local and ssh/sftp transfers only!\"")
    return rsync_url

#Get clipboard if it's copied files
clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
result = clipboard.wait_for_contents(Gdk.Atom.intern("x-special/gnome-copied-files", False))
str_clipboard=result.get_data()

dest_uri=sys.argv[1]
dest_rsync_path=rsyncify(target_uri)

#rsync file by file
for clipboard_uri in str_clipboard.splitlines()[1:]:
    src_rsync_path=rsyncify(clipboard_uri)
    if use_Zenity:
        #This was taken from http://www.davidverhasselt.com/zenity-rsync-and-awk/ and would probably work for folders.
        cmd="rsync %s %s %s |awk -f rsync.awk |zenity --progress --title \"Backing up USB-Stick\" --text=\"Scanning...\" --percentage=0 --auto-kill"%(rsync_args,src_rsync_path,dest_rsync)
    else:
        cmd="rsync %s %s %s"%(rsync_args,src_rsync_path,dest_rsync)
    #Execute command
    os.system(cmd)
