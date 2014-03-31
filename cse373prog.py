import sys
def changeComponents(comp,toBeChangedComp,a):
  for i in range(len(a)):
    if(a[i] == toBeChangedComp):
      a[i] = comp
f = open(sys.argv[1],'r')
lines = [line.strip() for line in f]
f.close()

vertices = [0 for i in range(int(lines[1])+1)]
#vertex array of size numOfVertices + 1 because we start at vertex 1
#print(len(vertices))
count = 2
component = 1
#count loops through our edges
while count < int(lines[0]) + 2:
  for x in lines[count].split(' '):
    if(vertices[int(x)] == 0):
      vertices[int(x)] = component
    else:
      toBeChangedComp = vertices[int(x)]
      changeComponents(component,toBeChangedComp,vertices)
  component += 1          
  count += 1

uniqueComps = []
numOfComps = 0
for v in range(1,len(vertices)):
  if(vertices[v] != 0 and vertices[v] not in uniqueComps):
    uniqueComps.append(vertices[v])
for i in range(1,len(vertices)):
  if(vertices[i] == 0):
    numOfComps += 1
  elif(vertices[i] in uniqueComps):
    numOfComps += 1
    uniqueComps.remove(vertices[i])
print(numOfComps)


