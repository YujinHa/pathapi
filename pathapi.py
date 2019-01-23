#coding:utf8
import os

def Projects():
	root = "/project"
	if not os.path.exists(root):
		return [], "프로젝트가 존재하지 않습니다."
	projects = []
	for p in os.listdir(root):
		if p.startswith("."):
			continue
		if os.path.isfile(root+"/"+p):
			continue
		projects.append(p)
	return projects, None

if __name__=="__main__":
	plist, err = Projects() #Project()함수에서 리턴 값이 2개이므로 가능!
	if err:
		print err
	print plist
