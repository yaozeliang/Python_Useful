
# coding: utf-8

# ## List Compresion

# In[1]:


work = ['work','eat','sleep','read']
verb_now = [w+'ing'for w in work]
verb_now


# In[7]:


divided_by_three = [x for x in range(20) if x % 3==0 ]
divided_by_three


# In[9]:


random = [-1,0,2,34,56,45,67,89,92,34]
odd = [n for n in random if n%2]
odd


# In[10]:


even = [n for n in random if n%2==0]
even


# In[11]:


doubled = [x*2 for x in random]
doubled


# In[14]:


squares = [(x,x**2)for x in range(1,6)]
squares


# In[19]:


colors=['red','color','green','blue','rose','grey']
colors_upper = [c.upper() for c in colors]
colors_upper


# In[20]:


colors_cap=[c.capitalize() for c in colors]
colors_cap


# In[27]:


colors_r = [c for c in colors if c.startswith('r',0,1)==True]
colors_r


# In[22]:


red=[c for c in colors if c=='red']
red


# In[28]:


number=4321
digits = [int(d) for d in str(number)]
digits


# In[31]:


matrix = [[ r*3+i for i in range(1,4)] for r in range(4)]
matrix


# In[33]:


postive_negative = [-4,-3,-2,-1.0,1,2,3,4,5]
postive= [n for n in postive_negative if n>0]
postive


# In[37]:


def get_vowel_names(names):
    vowels = ['a','e','i','o','u']
    result = [n for n in names if n[0].lower() in vowels]
    return result

people=['Ann','Bob','Ali','Ubuntu','John']
get_vowel_names(people)


# ## Dict Compresion

# In[39]:


pet_counts={'cat':6,'dog':5,'hamster':7,'bird':3}
too_many=[]
for pet,num in pet_counts.items():
    if num>4:
        too_many.append(pet)
        
too_many


# In[42]:


too_many = [
    pet
    for pet,num in pet_counts.items()
    if num>4
]

too_many


# In[50]:


letters = {
    "A":4,
    'b':5,
    'a':6,
    'c':2,
    'B':9
}

letters_count={
    k.lower():letters.get(k.lower(),0)+letters.get(k.upper(),0)
    for k in letters.keys()
}

letters_count


# In[52]:


ex1 = {str(i):i for i in [1,2,3,4]}
ex1


# In[53]:


fruits=['apple','mango','banana','cherry']
ex2 = {f:len(f) for f in fruits}
ex2


# In[57]:


fruits_cap = {f:f.capitalize() for f in fruits}
fruits_cap


# In[64]:


{f:i for i,f in enumerate(fruits)}


# In[68]:


person=dict(name='yao',age=18,city='beijing')
reverse_person={v:k for k,v in person.items()}
reverse_person


# In[69]:


{k*2: k**2 for k in range(10) if k%2==0 }


# In[76]:


test={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
bigger_than_two = {k:v for (k,v) in test.items() if v>2}
bigger_than_two


# In[77]:


triple_con = {k:v for (k,v) 
              in test.items()
              if v>2
              if v%2==0
              if v%3==0}
triple_con


# In[78]:


odd_even = {k:('even' if v%2==0 else 'odd')for (k,v) in test.items()}
odd_even


# ## Set Compresion

# In[80]:



squared={x**2 for x in [1,1,2,2]}
squared


# In[81]:


{s for s in [1,2,3,4,2,3]}


# In[82]:


{s for s in [1,2,3] if s%2}


# In[85]:


words = ['aoole','orange','lemon','lime']
first_letters= set(w[0] for w in words)
first_letters


# In[86]:


{w[0] for w in words}

