'''
You have decided to build a pyramid of stones on this new year. The simple rule is that the top level of the pyramid must consist of 1 stone, the second level must consist of 1 + 2 = 3 stones, the third level must have 1 + 2 + 3 = 6 stones, and so on.

Effectively, the i-th level of the pyramid contains 1 + 2 + ... + (i - 1) + i stones.

You have got n stones and have to build a pyramid from them.

Team Masai wants to know what is the maximum height of the pyramid that you can make using the given stones.
'''

####Tetrahedral numbers

n = int(input())

lists = []
if n<=10000:
    for i in range(100):
        lists = lists + [int(i*(i+1)*(i+2)/6)]



    for j in range(100):
        if lists[j]> n:
            print(j-1)
            break
        else:
            continue 
else:
    print("Overload")

## Simple You don't have to calculate all upto 100
## Just use Sn=i(i+1)/2 while Sn<no.ofstones: h+=1


'''
You are working for Masai Airline. There are n passengers with 2 bags each (one check-in and other hand bag). The limitation for check-in bag is 15kgs and that for hand bag is 7kgs. You are given 2 arrays: First array contains weight of check-in bag of ith passenger. Similarly, second array contains weights of hand bag of ith passenger. Print "Boarding" (without quotes) if the passenger clears both luggage weight limits of Masai Airline, else print "Stop" (without quotes).

Please note that 15 kgs and 7 kgs are inclusive.

Input Format

First line contains n (number of passengers)

Second line contains n positive integers which are the weights of check-in bag of ith passenger.

Third line contains n positive integers which are the weights of hand bag of ith passenger.

Constraints

n<1000

Output Format

Output "Boarding" (without quotes) or "Stop" (without quotes) of the passenger meets criteria of Masai Airlines.

Sample Input 0

4
12 14 15 6
8 5 7 4
Sample Output 0

Stop
Boarding
Boarding
Boarding
Explanation 0

Since, the hand bag of first person is 8kgs (greater than 7kgs), therefore stopped.

'''


n = int(input())
lug = list(map(int,input().split()))
hand = list(map(int,input().split()))

def board(lug,hand):
    i = lug 
    y = hand
    if i>15 or y > 7:
        flag = "Stop"
        print(flag)
    else:
        flag ="Boarding"
        print(flag)

answer = list(map(board,lug,hand))


'''
	JEE is one of the most prestigious exams. You need to implement ranking rule in it. Given marks of Physics, Chemistry and Mathematics of two students, Find out the winner using below rules:

=> If total marks of one student is greater than other, he/she wins

=> If total marks of both the students are same, then the one having more marks in Maths wins. In case their marks in maths are also same, the one whose marks in Physics is more wins the game.

Input Format

First line of input contains 3 space separated integers which is the marks in physics, chemistry and mathematics respectively of first student

Second line of input contains 3 space separated integers which is the marks in physics, chemistry and mathematics respectively of second student

Constraints

Marks < 36000

Output Format

Output "First" (without quotes) if first student wins.

In all other case print "Second"

'''




n = input()
n2 = input()
ins_1 = list(map(int,n.split()))
ins_2 = list(map(int,n2.split()))


if sum(ins_1)>sum(ins_2):
    print("First")
else:
    print("Second")


##Carparking prob

#SIr answ

#list of tuples -new concept

k = int(input())
arrival = list(map(int,input().split()))
depart = list(map(int,input().split()))

flag = True
li = []
cnt = 0
for i in arrival:
    li.append((i,'a'))
for i in depart:
    li.append((i,'d'))
li.sort()

for i in range(len(li)):
     if li[i][1] == 'a':
	    cnt += 1
	else:
	    cnt -= 1
	if cnt >k:
	   flag = False
	
if flag:
    print("Possible")
else:
    print("Not Possible")
	
	
	''' 
You are given scores of last N matches of two different batsmen in form of arrays. Your task is to print the ceil value of better average among the two in case that value is even. If that value is not even, print -1.

Input Format

First line contains the number of matches N.

Second line contains N space separated integers describing scores of first batsman. Third line contains N space separated integers descibing scores of second batsman.

Constraints

N<100

Output Format

Print an integer which can either be ceil of better average of the two batsmen or -1 depending upon the ceil of better average.

Sample Input 0

3
10 20 30
40 80 60
Sample Output 0

60
Explanation 0

Here, the number of matches is 3. And average of first batsman is 20 while average of second batsman is 60. Since 60>20 and 60 is also even, 60 is the output. 	 
'''	 
	 
	 
	 

n = int(input())
fir = list(map(int,input().split()))
sec = list(map(int,input().split()))

def avg(x):
    avg = sum(x)/len(x)
    return int(avg)


best = max(avg(fir),avg(sec))

if best%2==0:
    print(best)
else:
    print(-1)
	
	
'''
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. For example, the word anagram can be rearranged into nag a ram.

Given 2 phrases, write a program that detects if both are anagrams of each other.

If both are anagrams, print "True"

Else print "False"

Input Format

First line of input contains first phrase

Second line of input contains second phrase

Constraints

Length of each phrase < 1000

Output Format

Output a string based on conditions mentioned above

Sample Input 0

anagram
nag a ram
Sample Output 0

True

'''
orig = input()
anagram = input().split()
str_ana=""

for i in anagram:
    str_ana += str(i)


sorted_ana = ''.join(sorted(str_ana))
sorted_orig = ''.join(sorted(orig))


if sorted_ana == sorted_orig:
    
    print(True)
else:
    print(False)
	
'''
	
You are given 3 parameters of two different cricket teams in World Cup Final.

First parameter : Score

Second parameter : Score in super over

Third parameter : Total number of fours scored in the inning.

If first parameter of any one team is greater than other then that team wins.

If first parameter of both the teams are same, then the team whose second parameter is greater wins the match.

In case the second parameter is also same, then the team that has higher value of third parameter wins the game.

Input Format

First line contains the three discussed parameter for New Zealand

Second line contains three discussed parameters for England

Constraints

All parameters < 10000

Output Format

Output "England" (without quotes) if England wins the game, else print "New Zealand" if New Zealand wins the game.

Sample Input 0

241 15 21
241 15 26
Sample Output 0

England
'''
zea_sc = list(map(int,input().split()))
eng_sc = list(map(int,input().split()))


ans=""
for i in range(len(eng_sc)):
    z = zea_sc[i] 
    e=eng_sc[i] 
    if z>e:        
        ans = "New Zealand"
        break       
    elif e>z:      
        ans = "England"
        break
    else:
        i+=1
print(ans)

'''
There is a long queue of people in front of ATMs. Due to withdrawal limit per person per day, people come in groups to withdraw money.

Groups come one by one and line up behind the already present queue. The groups have a strange way of arranging themselves. In a particular group, the group members arrange themselves in increasing order of their height(not necessarily strictly increasing). Effectively, all people who have lined up in increasing order of height form one group
Find the minimum number of groups that can be observed in the queue?

Input Format

The first line of input contains one positive integer N. The second line contains N space-separated integers H[i] denoting the height of i-th person. Each group has group members standing in increasing order of their height.

Constraints

N <= 1000000

H[i] <= 1000000

Output Format

Print the minimum number of groups that are at least present in the queue?

Sample Input 0

6
1 2 4 3 5 8
Sample Output 0

2

'''

    

n = int(input())
gp=list(map(int,input().split()))
count = 0
set = []

for i in gp:
    if i > gp.index(i)+1:
        count+=1
            
print(count)


'''
	
For last N days, you did nothing but eat, sleep and code.

A close friend of you kept an eye on you for last N days. For every single minute of the day, he kept track of your actions and prepared a log file.

The log file contains exactly N lines, each line contains a string of length 1440 ( i.e. number of minutes in 24 hours of the day). The string is made of characters E, S, and C only; representing Eat, Sleep and Code respectively. ith character of the string represents what you were doing during ith minute of the day.

Your friend is now interested in finding out the maximum of longest coding streak of the day - X. He also wants to find the longest coding streak of N days - Y. Coding streak means number of C's without any E or S in between.

See sample test case for clarification.

Input Format

First line of each file contains N - number of days.

Following N lines contains a string of exactly 1440 length representing his activity on that day.

Constraints

1 ≤ N ≤ 365

String consists of characters E, S, and C only.

String length is exactly 1440.

Note: The sample test case does not follow the given constraints on string length to avoid large data. It is meant only for explanation. We assure you that the hidden test files strictly follow the constraints.

Output Format

Print X and Y separated by a space in a single line.

Sample Input 0

4
SSSSEEEECCCCEECCCC
CCCCCSSSSEEECCCCSS
SSSSSEEESSCCCCCCCS
EESSSSCCCCCCSSEEEE
Sample Output 0

7 9
'''


ins = int(input())
arr = input().split('\n')
for i in range(ins-1):
    arr+=input().split('\n')
#### Max of code streaks
cout = []
for i in range(ins):
    count=0
    count_max=0
    kk = arr[i]
    for y in kk:
        if y=='C':
            count+=1
        else:
            if count_max<count:
                count_max = count
            count=0
    cout.append(count_max)
#Longest code streak
arr_streak = ""
for i in arr:
    arr_streak+=i
con =0
con_max=0
for i in arr_streak:
    if i=='C':
        con+=1
    else:
        if con_max<con:
            con_max = con
        con=0
#Display
print(max(cout),con_max)

''' Even Sub Arrays
You are given an array A of N elements. Write a program that counts the number of sub-arrays of A in which sum of all the elements is an even number.
'''

n = int(input())
arr = list(map(int,input().split()))
##Optimised Alg

cnt_odd = 0
cnt_even =1
sumi = 0
count = 0



for i in range( n): 

    
    sumi =  sumi + arr[i]
    if sumi%2 ==0:
        cnt_even+=1
    else:
        cnt_odd+=1


count = cnt_odd*(cnt_odd-1)/2 +cnt_even*(cnt_even-1)/2 
print(int(count))





'''
https://www.hackerrank.com/contests/cohort-5-module-1-3-2-2/challenges/challenge-1d

New Year Celebration is coming near and DG is hosting a party for it, To make sure the party goes well she wants order in the party.There are two counters one of ice-cream and other for Cold-drinks.
On ice-cream counter the line was formed in form of Queue and on drinks counter the line was formed in order of Stacks.

She gave the management of the party to NV, NV made a plan to ask the manager following types of query.
Query types:
1 X : Number X enter the Queue. 
2 X : Number X enter the Stack.
3   : Output whoever is in-front of the queue.
4   : Output whoever is on-top of the stack
5   : Which person is in-front of queue get out of queue and enters the stack.
Note: If the Queue or Stack is empty then output "-1"

Input Format

The first line of input will contain Q, which is the number queries.

The next Q lines will different queries based upon query types given.
Constraints

1<=Q<=10^5

1<=X<=10^9

Output Format

Output will consist of integers based upon Query types.If Query type is 3 then Output whoever is in-front of the queue, if Query type is 4 Output whoever is on-top of the stack


Sample Input 0

7
1 4
2 3
1 2
3
4
5
4
'''
n = int(input())

stk =[]# stack LIFO
q = []#queue FIFO

while n >0:
    ins = input().split()
    
    if ins[0]=='2':
#stk.append(ins[1])
        stk.insert(0,ins[1])
        
    elif ins[0]=='1':
        q.append(ins[1])

    
    elif ins[0]=='4':
		if len(stk)>0:
		
          print(stk [0])
		else:
			print(-1)
    
    elif ins[0]=='3':
		if len(q)>0:
        	print(q[0])
		else:
			print(-1)
    else: ##'5'
        front_q = q.pop(0)
        stk.insert(0,front_q)
        
        
    
    n-=1
	

''''
Given a string of lowercase characters in range ascii[‘a’..’z’]. You can perform one operation on this string in which you can selects a pair of adjacent lowercase letters that match, and delete them.

For instance, the string aab could be shortened to b in one operation.

Your task is to delete as many characters as possible using this method and print the resulting string. If the final string is empty, print "Empty String" (without quotes).

Please note that characters can be deleted only if they form a pair and are same(i.e from aaa we can only delete 2 a's and will be left with a single a).

I know there exists a simple implementation based solution of this question, but please try to come up with an approach that uses stack data structure to solve the purpose

Input Format

First and the only line contains string

Constraints

Length of string < 1000

Output Format

If the final string is empty, print Empty String; otherwise, print the final non-reducible string.

Sample Input 0

aaabccddd
Sample Output 0

abd
Explanation 0

You can perform the following sequence of operations to get the final string:

aaabccddd -> abccddd -> abddd -> abd

'''


i = input()
stack = []

for y in i:
    stack.append(y)
    
    

for i in stack:
    
    if i==stack[stack.index(i)+1]:
        
        stack.remove(i) # pop just doesn't work
        stack.remove(i)
               
    
print(''.join(stack))

'''

Smaller Neighbour Element
(Very Imp*)
  
Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

Mathematically,

G[i] for an element A[i] is an element A[j] such that 
    j is maximum possible AND 
    j < i AND
    A[j] < A[i]
Note: Elements for which no smaller element exist, consider next smaller element as -1.

Input Format

First line contains an integer N denoting the number of elements in the array (not necessarily distinct).

Second line contains N space separated integers denoting the elements of the array.

Constraints

N < 100000

Output Format

Print N space separated integers denoting the array G.

Sample Input 0

8
39 27 11 4 24 32 32 1
Sample Output 0

-1 -1 -1 -1 4 24 24 -1



'''
n = int(input())
l = list(map(int,input().split()))


def cnt(l,i): # ith index
    
    st = l[0:i]
    st.reverse()
    z=0
    
    while len(st)>0 and st[0]>=l[i]:
        st.pop(0)
        
    if len(st)==0:
        z = -1
    else:
        z = st[0]
    return z
ans=[]   
for i in range(n):
    
    ans.append(cnt(l,i))  
print(*ans)

## Sir's optimised O(n) method
n = int(input())
l = list(map(int,input().split()))
st = [l[0]]

ans = [-1]
## Logic is almost same but we are keeping the track of the successful elements(meaning min elements) in the stack
for i in range(1,n):
    
    while len(st)!= 0 and st[0]>=l[i]:
        st.pop(0)
    if len(st)==0:
        ans.append(-1)
        
    else:
        ans.append(st[0])
    st.insert(0,l[i])    
    
print(*ans)
    
	'''
Mark and Competition

You have the marks of students in the form of an array, where arr[i] represents the marks of the ith student.

Since you are a curious kid, you want to find all the marks that are not smaller than those on its right side in the array.

Input Format

The first line of input will contain a single integer n denoting the number of students.

The next line will contain n space separated integers representing the marks of students.

Constraints

1 <= n <= 1000000

0 <= arr[i] <= 10000

Output Format

Output all the integers separated in the array from left to right that are not smaller than those on its right side.

Sample Input 0

6
16 17 4 3 5 2
Sample Output 0

17 5 2
Explanation 0

17, 5 and 2 are three integers present in the list which has no integers greater than it to its right (all the integers present in right of it)

'''

n = int(input())
q= list(map(int,input().split()))
 ## q - enque - append() deq - .pop(0)
    
## Take it a reverse way
q.reverse()
ans = [q[0]]
st_max = q[0]
for i in range(1,n):
    if q[i]>=st_max:
        ans.append(q[i])
        st_max = q[i]
        
ans.reverse()
print(*ans)


n = int(input())
l = list(map(int,input().split()))

s = []
q1=l
q2=[]
exp = 1
while exp<n+1:
    for i in q1:



        if i == exp: # It crosses 
            q2.append(i)   
            exp+=1
        elif len(s)>0 and exp==s[0]: #It enter the lane from stack
            z = s.pop(0)
            q2.append(z)
            exp+=1
            s.insert(0,i)  ## Really missed this line is crucial spend hr

        else:        
            s.insert(0,i)


out = q2+s

l.sort()


if l ==q2:
    print("yes")
else:
    print("no")

'''

Side lane - actual sir ans'''

while True:
    n = int(input())
    if n ==0:
        break
    else:
        numbers= list(map(int,input().split()))
        need = 1
        flag = "yes"
        s =[]
        for num in numbers:
            while len(s)!=0 and s[-1]==need:
                s.pop()
                need+=1
            if num==need:
                need+=1
            elif len(s)!=0 and s[-1]<num:
                flag = "no"
                break
            else:
                s.append(num)
        print(flag)
                



        
'''
Again a classical prob 

A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:

It contains no unmatched brackets.

The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
Given a string, you have to comment if it is balanced or not

Input Format

First line of input contains t which is the number of test cases present in the question

Each test case has a string

Constraints

t < 100

length of string < 100

Output Format

Print "balanced" if the string is balanced, otherwise print "not balanced" in case the string is not balanced

Sample Input 0

3
{([])}
()
([]
Sample Output 0

balanced
balanced
not balanced



'''

n = int(input())

dicte={'{':'}','(':')','[':']'}

i=0
def get_key(val): 
    for key, value in dicte.items(): 
         if val == value: 
             return key 
while i<n:
    
    l = input()   
    s = []
    
    flag = "balanced"
    for k in l:     
        if len(l)%2!=0:
            
            flag ="not balanced"
            
            
        
        if k in dicte.keys():
            
            s.insert(0,k)
            
        else:
            
   
            if len(s)>0 and k == dicte[s[0]]:
                s.pop(0)
            else:
                flag="not balanced"
                break 
            
    if len(s)!=0:
        flag="not balanced"
   
            
    print(flag)
    
    i+=1





























