
def buildTree(path):
  directoryTree = []
	contents = os.listdir(path)
	for i in contents:

		absPath = os.path.join(path, i)
		if os.path.isfile(absPath):
			if i.split('.')[-1] in listCodeFiles:
				directoryTree.append(absPath)
		elif os.path.isdir(absPath):
			subDirectoryTree = buildTree(absPath)
			if subDirectoryTree:
				directoryTree.append(subDirectoryTree)
	return directoryTree

def copyTree(srcpath, destpath, tree):
	for i in tree:
		if isinstance(i, basestring):
			relPath = os.path.relpath(i, srcpath)
			newPath = os.path.join(destpath, relPath)
			d = os.path.dirname(newPath)

			if not os.path.exists(d):
				os.makedirs(d)
			shutil.copy2(i, newPath)
		else:
			copyTree(srcpath, destpath, i)
	return True

if __name__=='__main__':
	import sys
	import os
	import shutil

	listCodeFiles = ['py', 'c', 'cpp', 'java', 'jar']
	srcPath = sys.argv[1]
	destPath = sys.argv[2]

	tree = buildTree(srcPath)
	print copyTree(srcPath, destPath, tree)

