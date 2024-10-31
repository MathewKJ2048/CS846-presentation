import os
import sys
import json

filepath = sys.argv[1]

print(filepath)

with open(filepath,'r') as file:
	data = json.load(file)

state = data["states"][0]

print(state)

def generate():
	s = "digraph G {\n"
	for st in data["states"]:
		s+=st +"[style=filled"
		if st is data["states"][0]:
			s+=",peripheries=2"
		if st is state:
			s+=",color=red"
		s+="];\n"
	for t in data["transitions"]:
		s1 = t[0]
		s2 = t[1]
		x = t[2]
		y = t[3]
		s+=s1+" -> "+s2+"[label=\""+t[2]+"/"+t[3]+"\"];\n"
	s+="}"
	return s

def update():
	with open("./graph.dot","w") as file:
		file.write(generate())
	os.system("dot -Tpng -Gsize=4,8\! -Gdpi=100 ./graph.dot > ./output.png")
	os.system("pix --fullscreen ./output.png")

update()



