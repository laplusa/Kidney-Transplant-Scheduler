#!  /usr/bin/env  python3
'''
本代码实现了基于database.txt的数据建立wij的匹配度，并以此建立匹配的图结构
主要变量含义：
w[i][j]——第i组供体与第j组受体的匹配度(0 or 1)
blood_type[i]——第i个个体的血型
hcl_dr[i]——第i个个体的HCL-DR类型
hcl_a[i]——第i个个体的HCL-A类型
hcl_b[i]——第i个个体的HCL-B类型
blood_w[i][j]——第i组供体与第j组受体的血型匹配度(0 or 1)
hcl_w[i][j]——第i组供体与第j组受体的HCL匹配度(0 or 1)

图结构：邻接表并可视化实现
见代码注释
'''
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


import sys
f = open('b.input', 'w')
sys.stdout = f
sys.stderr = f      # redirect std err, if necessary


data=np.loadtxt('database.txt',dtype=str,delimiter='\n')
#print(data[0][-10])
length=len(data)
blood_type=[]
hcl_dr=[]
hcl_a=[]
hcl_b=[]
for i in range(length):
	if data[i][-15]=='A':
		blood_type.append(1)
	if data[i][-15]=='B':
		blood_type.append(2)
	if data[i][-16]=='A':
		blood_type.append(3)
	if data[i][-15]=='O':
		blood_type.append(4)
	if data[i][-10]=='1':
		hcl_dr.append(1)
	else:
		hcl_dr.append(2)
	if data[i][-6]=='1':
		hcl_a.append(1)
	else:
		hcl_a.append(2)
	if data[i][-2]=='1':
		hcl_b.append(1)
	else:
		hcl_b.append(2)
#print(blood_type)
#print(hcl_dr)
#print(hcl_a)
#print(hcl_b)
llength=int(length/2)
w=np.zeros((llength,llength))
blood_w=np.zeros((llength,llength))
hcl_w=np.zeros((llength,llength))
#print(w)
for i in range(llength):
	for j in range(llength):
		if blood_type[2*j+1]==4:
			if blood_type[2*i]==4:
				blood_w[i][j]=1
		if blood_type[2*j+1]==3:
			blood_w[i][j]=1
		if blood_type[2*j+1]==2:
			if blood_type[2*i]==2 | blood_type[2*i]==4:
				blood_w[i][j]=1
		if blood_type[2*j+1]==1:
			if blood_type[2*i]==1 | blood_type[2*i]==4:
				blood_w[i][j]=1
num_hcl=np.zeros((llength,llength))
sum_vex=0
for i in range(llength):
	for j in range(llength):
		if hcl_dr[2*i]==hcl_dr[2*j+1]:
			num_hcl[i][j]=num_hcl[i][j]+1
		if hcl_a[2*i]==hcl_a[2*j+1]:
			num_hcl[i][j]=num_hcl[i][j]+1
		if hcl_b[2*i]==hcl_b[2*j+1]:
			num_hcl[i][j]=num_hcl[i][j]+1
for i in range(llength):
	for j in range(llength):
		if num_hcl[i][j]>1:
			hcl_w[i][j]=1
for i in range(llength):
	for j in range(llength):
		if blood_w[i][j]==1 and blood_w[j][i]==1:
			if hcl_w[i][j]==1 and hcl_w[j][i]==1:
				if i < j:
					sum_vex=sum_vex+1
print(llength,sum_vex)
for i in range(llength):
	for j in range(llength):
		if blood_w[i][j]==1 and blood_w[j][i]==1:
			if hcl_w[i][j]==1 and hcl_w[j][i]==1:
				if i < j:
					print(i,j,1)
print(-1,-1,-1)
#输出临界矩阵形式的w
#print(w)

#以下程序实现无相图的结构
class Node:
	def __init__(self,value):
		self.value=value     #节点的特征值
		self.nexts=[]             #节点的邻居节点（供体)
		self.lasts=[]              #节点的邻居节点（受体）
		self.come=0            #节点的入度
		self.out=0               #节点的出度
class GGraph:
	def __init__(self):
		self.nodes={}
ggraph=GGraph()
for i in range(llength):
	for j in range(llength):
		if i not in ggraph.nodes:
			ggraph.nodes[i]=Node(i)
		if j not in ggraph.nodes:
			ggraph.nodes[j]=Node(j)
		if w[i][j]==1:
			toNode=ggraph.nodes[i]
			fromNode=ggraph.nodes[j]
			toNode.nexts.append(j)
			fromNode.lasts.append(i)
			toNode.out+=1
			fromNode.come+=1
#print(ggraph.nodes[3].nexts)

#以下程序实现基于邻接矩阵实现图的可视化
G=nx.Graph()
for i in range(llength):
	G.add_node(i+1)
for i in range(llength):
	for j in range(llength):
		if w[i][j]==1:
			G.add_edge(i+1,j+1)
nx.draw(G)
plt.show()
