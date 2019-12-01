'''
KAUSTUBH PANDEY
ROLL:S20160010041
CSE UG-4
'''
import queue
def cmp(a,b):
	if(a[0]<b[0]):
		return True
	elif(a[0]==b[0] and a[1]<b[1]):
		return True
	return False
def find(profit,pair,person):
	largest=[-999999,0]
	slargest=[-999999,0]
	for i in range(len(profit[0])):
		val = [profit[person][i]-pair[i],i]
		if(cmp(largest,val)):
			slargest=largest
			largest = val
		elif(cmp(slargest,val)):
			slargest = val
	return [largest,slargest]

def assignOptimal(profit,pair,person,assigned_persons,assigned_objs):
	largest,slargest = find(profit,pair,person)
	unAsgn_i,assigned_objs[largest[1]],assigned_persons[person]= assigned_objs[largest[1]],person,largest[1]
	pair[largest[1]] += (largest[0]-slargest[0])+(1/len(profit)) - 0.00001
	if(unAsgn_i!=-1):
		assigned_persons[unAsgn_i]=-1
	return unAsgn_i

def solveAssignmentProblem(profit):
	assigned_persons = [-1 for i in range(len(profit))]
	assigned_objs = [-1 for i in range(len(profit[0]))]
	pair = [0 for i in range(len(profit[0]))]
	unAsgn = queue.Queue()
	for i in range(len(profit)):
		if(assigned_persons[i]==-1):
			unAsgn.put(i)
	index,unAsgn_i=0,0
	while(not unAsgn.empty()):
		index = unAsgn.get()
		#print(index)
		unAsgn_i = assignOptimal(profit, pair, index, assigned_persons, assigned_objs)
		#print(unAsgn_i)
		if(unAsgn_i!=-1):
			unAsgn.put(unAsgn_i)
	summ=0
	for i in range(len(profit)):
		summ+=profit[i][assigned_persons[i]]
		print("Person "+str(i+1),"--> Object"+str(assigned_persons[i]+1))
	print("Total benefit :",summ)

profit = []
print("Enter the matrix: (Enter q to exit)")
while(True):
	s=input()
	if(s!='q'):
		profit.append(list(map(int,s.split())))
	else:
		break	
if(len(profit)==len(profit[0])):
	print("The problem is symmetric")
else:
	print("The problem is asymmetric")
solveAssignmentProblem(profit)

'''
KAUSTUBH PANDEY
ROLL:S20160010041
CSE UG-4
'''