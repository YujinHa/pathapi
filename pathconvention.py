class PathConvention:
	root = "/project"
	project = ""
	seq = ""
	shot = ""
	task = "" 
	user = ""
	ext = ""
	ver = 1

	def filepath(self):
		return "%s_%s_%s_v%03d%s" % (self.seq, self.shot, self.task, self.ver, self.ext)

	def dirpath(self):
		return "%s/%s/%s/%s/%s/%s" % (self.root, self.project, self.seq, self.shot, self.task, self.user)

	def fullpath(self):
		return self.dirpath() + "/" + self.filepath()

	def lin2winNetdrive(self):
		return "Z:" + self.fullpath().replace("/","\\")

	def lin2winUnc(self):
		return "\\\\10.0.0.10" + self.fullpath().replace("/","\\")
p = PathConvention()
p.project = "circle"
p.seq = "FOO"
p.shot = "0010"
p.task = "model"
p.user = "yujin"
p.ext = ".mb"
print p.filepath()
print p.dirpath() 
print p.fullpath()
print p.lin2winNetdrive()
print p.lin2winUnc()
