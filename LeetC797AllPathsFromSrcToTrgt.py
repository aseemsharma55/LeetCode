def allpathsfromsrctotarget(graph):
  #get the end node
  end = len(graph) - 1

  def dfs(source, currpath, result):
    #the source above is the zero we would always have, currpath is the path we wanna make note of and result is the resulting array
    if source == end:  #checking if the end has been reached
      result.append(
        currpath)  #if yes then add this path taken to the resulting array

    for i in graph[source]:  #visit each neighbor of the zeroth index
      dfs(
        i, currpath + [i], result
      )  #recursion on each neighbor of zero and therefore adding each neighbor to our path

  #have a resulting array
  result = []
  #call dfs helper function with 0 as the node, a path with 0 in it always and the resulting array
  dfs(0, [0], result)
  return result


graph = [[1, 2], [3], [3], []]
print(allpathsfromsrctotarget(graph))