#!/usr/bin/env python
#coding:utf8
import sys
import re #regular expression의 약자(정규 표현식)

path = "/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.nk"

def project(path):
	"""
	경로를 넣으면 project를 반환한다.
	"""
	#레귤러 익스프레션-괄호:그룹화,\S:문자열 검색,^/:아무거나,+:이상
	p = re.findall('/project/(\S[^/]+)', path.replace("\\","/")) 
	if len(p) != 1:
		return "","경로에서 project 정보를 가지고 올 수 없습니다."
	return p[0], None

if __name__ == "__main__":
	projectName, err = project(path)
	if err:
		print err
	print projectName
