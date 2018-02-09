
# coding: utf-8

# In[3]:


name = input("Enter the name")
print(name[::-1])


# In[6]:


word = input("Input a word to reverse: ")
for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")

