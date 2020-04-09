set1 = set(input().split())
set2=set(input().split())
def check(set1,set2):
	if len(set1.union(set2))==len(set1):
		print("Is superset")
	else:
		print("Not a superset")
	