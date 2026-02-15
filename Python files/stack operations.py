# cook your dish here
class stack:
    
    def __init__(self):
        self.stk=[]
        self.premax=[-1]
        self.premin=[-1]
        
    def push(self,ele):
        if self.stk:
            #print(self.stk,self.premax,self.premin)
            self.premax.append(max(self.premax[-1],ele))
            self.premin.append(min(self.premin[-1],ele))
        else:
            self.premax.append(ele)
            self.premin.append(ele)
        self.stk.append(ele)
        
    def pop(self):
        self.stk.pop()
        self.premax.pop()
        self.premin.pop()
        
    def grt_ele_at_top(self):
        return self.stk[-1]

    def get_max(self):
        return self.premax[-1]

    def get_min(self):
        return self.premin[-1]
    

obj=stack()
obj.push('abcd')
print('Stack is', obj.stk)
print('Maximum is',obj.get_max())
print('Minimum is',obj.get_min())
obj.push('ab')
print('Stack is', obj.stk)
print('Maximum is',obj.get_max())
print('Minimum is',obj.get_min())
obj.push('ert')
print('Stack is', obj.stk)
print('Maximum is',obj.get_max())
print('Minimum is',obj.get_min())
obj.push('om')
print('Stack is', obj.stk)
print('Maximum is',obj.get_max())
print('Minimum is',obj.get_min())
obj.push('aditya')
print('Stack is', obj.stk)
print('Maximum is',obj.get_max())
print('Minimum is',obj.get_min())
obj.push('afrd')
print('Stack is', obj.stk)
print('Maximum is',obj.get_max())
print('Minimum is',obj.get_min())
obj.push('trythr')
print('Stack is', obj.stk)
print('Maximum is',obj.get_max())
print('Minimum is',obj.get_min())
print(obj.stk)
obj.pop()
print('Stack is', obj.stk)
print('Maximum is',obj.get_max())
print('Minimum is',obj.get_min())
print(obj.stk)
        
