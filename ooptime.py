#!/usr/bin/env python
# coding: utf-8

# In[10]:


class timee:
    def __init__(self,h,m,s):
        self.hour=h
        self.minute=m
        self.second=s
    def summ(self,t):
        result=timee(0,0,0)
        result.hour=self.hour+t.hour
        result.minute=self.minute+t.minute
        result.second=self.second+t.second
        if result.second>=60:
            result.second-=60
            result.minute+=1
        if result.minute>=60:
            result.minute-=60
            result.hour+=1
        return result
    def subb(self,t):
        result=timee(None,None,None)
        if self.second<t.second:
            if self.minute<1:
                self.hour-=1
                self.minute+=60
            else:
                self.minute-=1
                self.second+=60
        if self.minute<t.minute:
            self.hour-=1
            self.minute+=60
        result.hour=self.hour-t.hour
        result.minute=self.minute-t.minute
        result.second=self.second-t.second
        return result
    def timeTosecond(self):
        result=self.hour*3600+self.minute*60+self.second
        print(result) 
    def secondTotime(self):
        result=timee(0,0,0)
        result.hour=self//3600
        self=self%3600
        result.minute=self//60
        result.second=self%60
        return result
    def show(self):
        print(self.hour,':',self.minute,':',self.second)
t1=timee(12,10,21)
t2=timee(10,40,14)
t3=t1.summ(t2)
timee.show(t3)
t4=t1.subb(t2)
timee.show(t4)
timee.timeTosecond(t1)
t5=timee.secondTotime(43821)
timee.show(t5)


# In[ ]:




