import os

def chmod (**kwargs):

	"""
    CHMOD                         User Commands                        CHMOD
    NAME
        chmod - changes the permissions of file or directory
    SYNOPSIS
        chmod MODIFIER [FILE...]
    DESCRIPTION
        chmod changes the permissions of FILE, or directory, with MODIFIER,
		1st digit is owner, 2nd is group, 3rd is anyone.
        If no FILE is given,it will return an error.

	OPTIONS

	777 Modifier must be given as a number value

    EXAMPLE
        chmod 777 file.txt
    """
	if 'params' in kwargs:
		params = kwargs['params']
	else:
		return 'Error:  No or incorrect parameters given.'
	if 'path' in kwargs:
		path = kwargs['path']

	try:
		os.chmod(path[1]+params[1], int(params[0],8))
	except:
		return 'ERROR: No incorrect parameters given.'
