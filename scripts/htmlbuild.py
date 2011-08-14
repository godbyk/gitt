#!/usr/bin/python

import re

f = open("../chap4.tex")
data = f.read()
f.close()

data = data.replace(">", "&gt;") 
data = data.replace("<", "&lt;")


data = data.replace("``", '"')
data = data.replace("''", '"')

data = data.replace("\\%", "%")

data = data.replace("\n\n", "<br>")

data = data.replace("\\%", "&#37;")
data = data.replace("\\ ", "&nbsp;")
data = data.replace("\\_", "_")
data = data.replace("\\newline", "")

data = data.replace("\\ldots", "...")
data = data.replace("\\textasciitilde{}", "~")

plob = re.findall("(%.*?\n)", data, re.M)
for i in plob:
	data = data.replace(i, "")
	
plob = re.findall("(\\\\index\{(.*?)\})", data)
for i in plob:
	data = data.replace(i[0], "")

plob = re.findall("(\\\\indexgit\{(.*?)\})", data)
for i in plob:
	data = data.replace(i[0], '<span style="font-family:monospace;">git ' + i[1] + '</span>')

plob = re.findall("(\\\\clearpage)", data)
for i in plob:
	data = data.replace(i, "")

plob = re.findall("(\\\\cleardoublepage)", data)
for i in plob:
	data = data.replace(i, "")

plob = re.findall("(\\\\thoughtbreak)", data)
for i in plob:
	data = data.replace(i, " * * * ")

plob = re.findall("(\\\\textbf\{(.*?)\})", data)
for i in plob:
	data = data.replace(i[0], "<strong>" + i[1] + "</strong>")

plob = re.findall("(\\\\emph\{(.*?)\})", data)
for i in plob:
	data = data.replace(i[0], "<em>" + i[1] + "</em>")

plob = re.findall("(\\\\texttt\{(.*?)\})", data)
for i in plob:
	data = data.replace(i[0], '<span style="font-family:monospace;">' + i[1] + "</span>")

plob = re.findall("(\\\\subsubsection\{(.*?)\})", data)
for i in plob:
	data = data.replace(i[0], "<h4>" + i[1] + "</h4>")

plob = re.findall("(\\\\subsection\{(.*?)\})", data)
for i in plob:
	data = data.replace(i[0], "<h3>" + i[1] + "</h3>")

plob = re.findall("(\\\\section\{(.*?)\})", data)
for i in plob:
	data = data.replace(i[0], "<h2>" + i[1] + "</h2>")

plob = re.findall("(\\\\chapter\{(.*?)\})", data)
for i in plob:
	data = data.replace(i[0], "<h1>" + i[1] + "</h1>")

plob = re.findall("(\\\\begin\{trenches\}(.*?)\\\\end\{trenches\})", data, re.S)
for i in plob:
	data = data.replace(i[0], '<div style="padding:10px;">' + i[1] + "</div>")

plob = re.findall("(\\\\begin\{itemize\}((.*?)\\\\end\{itemize\}))", data, re.S)
for i in plob:
	data = data.replace(i[0], '<div style="padding:10px;"><ul>' + i[2] + "</ul></div>")
	listd = i[1]
	nasty = re.findall("(\\\\item(.*?)((?=\\\\item)|(?=\\\\end\{itemize\})))", listd, re.S)
	for j in nasty:
		data = data.replace(j[0], '<li>' + j[1] + '</li>')

plob = re.findall("(\\\\begin\{enumerate\}((.*?)\\\\end\{enumerate\}))", data, re.S)
for i in plob:
	data = data.replace(i[0], '<div style="padding:10px;"><ol>' + i[2] + "</ol></div>")
	listd = i[1]
	nasty = re.findall("(\\\\item(.*?)((?=\\\\item)|(?=\\\\end\{enumerate\})))", listd, re.S)
	for j in nasty:
		data = data.replace(j[0], '<li>' + j[1] + '</li>')

plob = re.findall("(\\\\begin\{code\}(.*?)\\\\end\{code\})", data, re.S)
for i in plob:
	code = i[1].replace("\n", "<br>")
	data = data.replace(i[0], '<div style="padding:10px;font-family:monospace;">' + code + "</div>")

plob = re.findall("(\\\\figuregit\{(.*?)\}\{(.*?)\}\{(.*?)\})", data, re.S)
for i in plob:
	data = data.replace(i[0], '<br>image:' + i[2] + ' - ' + i[3] + "<br>")

plob = re.findall("(\\\\figuregith\{(.*?)\}\{(.*?)\}\{(.*?)\})", data, re.S)
for i in plob:
	data = data.replace(i[0], '<br>image:' + i[2] + ' - ' + i[3] + "<br>")

plob = re.findall("(\\\\begin\{callout\}\{(.*?)\}\{(.*?)\}(.*?)\\\\end\{callout\})", data, re.S)
for i in plob:
	data = data.replace(i[0], '<div style="padding:20px;border:3px solid #000"><h3>' + i[1] + ' - ' + i[2] + '</h3>' + i[3] + "</div>")


f = open("testout.html", "w")
f.write(data)
f.close()