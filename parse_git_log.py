'''
This document helps use parse our git commits so we 
can make them more easily readable and clickable
in our Readme.
'''

import os
import datetime
import git # pip install GitPython


repo = git.Repo(os.getcwd())

master = repo.head.reference

with open("parsed_log.md", "w+") as parsed_log:
	for commit in master.log():
		if "commit" in commit.message:
			commit_mess = commit.message.replace("commit: ", "").replace("commit (initial): ", "")
			line = "[{message}](../../tree/{commit}/)".format(message=commit_mess, commit=commit.newhexsha)
			parsed_log.write(line)
			parsed_log.write("\n\n")
