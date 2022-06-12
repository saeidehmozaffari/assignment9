#!/usr/bin/env python
# coding: utf-8

# In[10]:


class fraction:
    def __init__(self,s,m):
        self.sorat=s
        self.makhraj=m
    def summ(self,k):
        result=fraction(0,0)
        result.sorat=self.sorat*k.makhraj+k.sorat*self.makhraj
        result.makhraj=self.makhraj*k.makhraj
        return result
    def mull(self,k):
        result=fraction(None,None)
        result.sorat=self.sorat*k.sorat
        result.makhraj=self.makhraj*k.makhraj
        return result
        
    def subb(self,k):
        result=fraction(None,0)
        result.sorat=self.sorat*k.makhraj-k.sorat*self.makhraj
        result.makhraj=self.makhraj*k.makhraj
        return result
        
    def divv(self,k):
        result=fraction(0,None)
        result.sorat=self.sorat*k.makhraj
        result.makhraj=k.sorat*self.makhraj
        return result
        
    def show(self):
        print(self.sorat,'/',self.makhraj)
        
        
kasr1=fraction(3,5)
kasr1.show()
kasr2=fraction(4,3)
kasr2.show()
c=kasr1.mull(kasr2)
c.show()
c2=kasr1.summ(kasr2)
c2.show()
c3=kasr2.subb(kasr1)
c3.show()
c4=kasr1.divv(kasr2)
c4.show()


# In[ ]:




