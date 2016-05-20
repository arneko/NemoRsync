# NemoRsync
Paste in Nemo using rsync/ssh

This nemo_action-script integrates into the context menu and allows any number of copied remote or local files/folders to be rsynced to a remote or local folder.

Installation:

Put the files NemoRsync.nemo_action and NemoRsync.py into the folder ~/.local/share/nemo/actions/ or /usr/share/nemo/actions and restart nemo. 

Usage:

Copy any number of files and folders, paste them somewhere else using "Rsync paste" in the context menu. Note that you cannot paste into folders by highlighting them and choosing "Rsync paste" on them for now. 

Known Issues:

Lots!
This works in principle but is one ugly hack.
There is no status indicator, so once you "pasted" you should see the files appear/grow.
I intend to remedy this using some awk magic and zenity.

 
