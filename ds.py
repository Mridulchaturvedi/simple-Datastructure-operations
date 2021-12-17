print('\n\n\n \033[1m\033[95m\033[96m---------------- L I N K E D  L I S T  O P E R A T I O N  ----------------- \n\n\033[0m' )

class Node:
    def __init__(self,data):
        self.index = 0
        self.data = data
        self.next=None
           

class linkedlist:
    def __init__(self):
        self.head = None
        self.end = None
        self.length = 0

    
    def insert(self,index,data):
        print('\ninserted New element',data,'at index',index)

        if  0<  index > self.length:
            print('incorrect Index or Index Out of Range :--  Range is ',self.length)

        else:
            if index == self.length:
                link.Append(data)

            elif index == 0:
                link.appendbeg(data)

            else:
                temp = self.head

                while temp.next:
                    temp = temp.next
                     
                    
                    if temp.index == index-1:
                        new = Node(data)
                        curr = temp.next
                        


                        temp.next = new
                        temp = new
                        temp.next = curr
                    else:
                        pass
            self.length +=1
                    
                
                        
            link.index()
                   

    def Append(self,data):
        
        if self.end:
            link.appendend(data)

        else:
            link.appendbeg(data)

        self.length += 1  
        
        link.index()
        


    def appendend(self,data):
            node = Node(data)
            self.end.next = node
            self.end = node
            link.index()


    def appendbeg(self,data):
        if self.head:
            curr = self.head
            node = Node(data)
            self.head = node
            self.head.next=curr
            self.end = self.head
            link.index()
        else:
            node = Node(data)
            self.head = node            
            self.end = self.head
            link.index()
          
         
    def index(self):
        count = 0
        temp = self.head

        while temp.next:
            temp.index = count
            count+=1 
            temp = temp.next
            

    def printe(self):
        temp = self.head    
        while (temp):
            print (temp.data)
            
            temp = temp.next
            
    def middle(self):
        if self.length %2==0:
            indexe = self.length/2
            temp = self.head
            while temp.next:
                temp = temp.next
                if temp.index == indexe:
                    print(temp.data,'&',temp.next.data,'Both can be consider middle element as list is EVEN :-- Element found at Indexes ',temp.index,',',temp.next.index)
        else:
            indexe = (self.length+1)/2
            temp = self.head
            while temp.next:
                temp = temp.next
                if temp.index == indexe:
                    print(temp.data,'is middle element found at Index',temp.index)
            
            
            
    def deleteNode(self, key):

        print("\nDeleating element :--",key)
         
        temp = self.head
 
        
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
 
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
 
        if(temp == None):
            return
 
    
        prev.next = temp.next
 
        temp = None
        
        
        link.index()
        
        self.length -=1
        
    def size(self):
        print(self.length)
    
            
            
            
               


if __name__=='__main__':
 
    link = linkedlist()

    link.Append(7)
    link.Append(2)
    link.Append(3)
    link.Append(5)
    link.Append(7)
    link.Append(8)
    
    print('\033[1m\033[92mlist Before inserting any element :- \033[0m')
    link.printe()
    
   
    print('\033[1m\033[92m\n\nInserting Element :- \033[0m')
    link.insert(0,20)
    link.insert(3,4)
    print('\033[1m\033[92m\n\nNew list after insertion :- \033[0m')
    link.printe()
    
    
    
    link.deleteNode(5)
    print('\033[1m\033[92m\n\nNew list after Deleting Node :- \033[0m')
    link.printe()
    
    
    
    print('\033[1m\033[92m\n\nMiddle Element :- \033[0m')
    link.middle()
    
    
    print('\033[1m\033[92m\n\nSize of List is :- \033[0m')
    link.size()

print('\n\n\n \033[1m\033[95m\033[96m---------------- S T A C K   O P E R A T I O N S ----------------- \n\n' )

class Stack:
    def __init__(self):
         self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    def print(self):
        for i in self.items:
            
            print(i)
    
    
print('\033[1m\033[92m\n\nPushing elements to Stack :- \033[0m')
s = Stack()
for i in range(11):
    s.push(i)
s.print()

num = int(input("how many items You want to insert :- "))

for i in range(num):
    n = input("Enter element :-")

    s.push(n)
    
    

print('\033[1m\033[92m\n\nPoping elements from Stack :- \033[0m')
s.pop()
s.print()

print('\n\n\n \033[1m\033[95m\033[96m---------------- A R R A Y   O P E R A T I O N S ----------------- \n\n\033[0m' )


arr = [25, 11, 7, 75, 56];  

print(arr)
     
max = arr[0];    
     
for i in range(0, len(arr)):
    
    if(arr[i] > max):  
        max = arr[i];
        
        

total = 0      
 
for i in arr:
    
    total = i+total
print('Total is == ',total)
           
print("Largest element present in given array: " + str(max));   



print('\n\n\n \033[1m\033[95m\033[96m---------------- P A T T E R N ----------------- \n\n\033[0m' )
n=5

for i in range(n):
    for x in range(5-i):
        m = str(x)
        print(1+i,end=' ')
    print()
        
    

print('\n\n\n \033[1m\033[95m\033[96m---------------- R E V E R S E  S T R I N G ----------------- \n\n\033[0m' )
txt = "Hello World"
print(txt)
print(txt[::-1])
   
    