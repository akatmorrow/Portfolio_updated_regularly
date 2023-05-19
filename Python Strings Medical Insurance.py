#!/usr/bin/env python
# coding: utf-8

# # Python Strings: Medical Insurance Project

# You are a doctor who needs to clean up medical patient records, which are currently stored in one large string.
# 
# In this project, you will use your new knowledge of Python strings to obtain and clean up medical data so that it is easier to read and analyze.
# 
# Let's get started!

# ## Working with Strings

# 1. First, take a look at the code in the code block below.
# 
#    The string `medical_data` stores the medical records for ten individuals. Each record is separated by a `;` and contains the name, age, BMI (body mass index), and insurance cost for an individual, in that order.
#    
#    Print `medical_data` to see the output below the code block.

# In[1]:


medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""
print(medical_data)


# 2. We want the insurance costs to be represented in US dollars.
# 
#    Replace all instances of `#` in `medical_data` with `$`. Store the result in a variable called `updated_medical_data`.
#    
#    Print `updated_medical_data`.

# In[2]:


updated_medical_data = medical_data.replace('#', '$')
print(updated_medical_data)


# 3. We want to calculate the number of medical records in our data.
# 
#    Create a variable called `num_records` and initialize it at 0.

# In[3]:


num_records = 0


# 4. Next, write a `for` loop to iterate through the `updated_medical_data` string. Inside of the loop, add `1` to `num_records` when the current character is equal to `$`.

# In[4]:


for character in updated_medical_data:
    if character == '$':
        num_records += 1


# 5. Outside of the loop, print `num_records` with the following message:
# 
#    ```
#    There are {num_records} medical records in the data.
#    ```

# In[5]:


print(('There are {} medical records in the data'.format(num_records)))


# ## Splitting Strings

# 6. The medical data in its current form is difficult to analyze. An essential job for a data scientist is to clean up data so that it's easy to work with.
# 
#    Let's start off by splitting the `updated_medical_data` string into a list of each record. Remember that each medical record is separated by a `;` in the string.
#    
#    Store the result in a variable called `medical_data_split` and print this variable.

# In[6]:


medical_data_split = updated_medical_data.split(';')
print(medical_data_split)


# 7. Our data is now stored in a list, but it is still hard to read. Let's split each medical record into its own list.
# 
#    First, define an empty list called `medical_records`.

# In[7]:


medical_records = []


# 8. Next, iterate through `medical_data_split` and for each record, split the string after each comma (`,`) and append the split string to `medical_records`.
# 
#    Print `medical_records` after the loop.

# In[8]:


for record in medical_data_split:
    split_string = record.split(',')
    medical_records.append(split_string)
print(medical_records)


# ## Cleaning Data

# 9. Our data is now slightly more readable. However, it is not properly formatted - it contains unnecessary whitespace.
# 
#    To fix this, let's start by creating an empty list called `medical_records_clean`.

# In[9]:


medical_records_clean = []


# 10. Next, use a `for` loop to iterate through `medical_records`.
# 
#     Inside of the loop, create an empty list called `record_clean`. We'll use this list to store a formatted version of each medical record.

# In[10]:


for record in medical_records:
    record_clean = []
    for item in record: 
        record_clean.append(item.strip())
    medical_records_clean.append(record_clean)


# 11. After the `record_clean` variable, create a nested `for` loop that goes through each `record`:
# 
#     ```py
#     for item in record
#     ```
#     
#     Inside of this loop, append `item.strip()` to `record_clean` to remove any whitespace from the string.

# In[ ]:





# 12. Finally, we need to add each cleaned up record to `medical_records_clean`.
# 
#     Outside of the nested `for` loop, append `record_clean` to `medical_records_clean`.

# In[ ]:





# 13. Print `medical_records_clean` outside of the `for` loops to see the output.
# 
#     You should see output that is formatted and much easier to read.

# In[11]:


print(medical_records_clean)


# ## Analyzing Data

# 14. Our data is now clean and ready for analysis.
# 
#     For example, to print out the names of each of the ten individuals, we can use the following loop:
#     ```py
#     for record in medical_records_clean:
#       print(record[0])
#     ```
#     
#     Add this loop to the code block below and run it.

# In[12]:


for record in medical_records_clean:
    uppercase = []
    for item in record:
        uppercase.append(str(item.upper()))
    print(uppercase[0])


# 15. You want all of the names in the medical records to be uppercase characters.
# 
#     In the `for` loop, update `records[0]` before the `print` statement so that all of the characters are uppercase.
#     
#     Run the code to see the result.

# In[ ]:





# 16. Let's store each name, age, BMI, and insurance cost in separate lists.
# 
#     To start, create four empty lists:
#     - `names`
#     - `ages`
#     - `bmis`
#     - `insurance_costs`

# In[13]:


names = []
ages = []
bmis = []
insurance_costs =[]


# 17. Next, iterate through `medical_records_clean` and for each record:
#     - Append the name to `names`.
#     - Append the age to `ages`.
#     - Append the BMI to `bmis`.
#     - Append the insurance cost to `insurance_costs`.

# In[14]:


for record in medical_records_clean:
    names.append(record[0])
    ages.append(record[1])
    bmis.append(record[2])
    insurance_costs.append(record[3])


# 18. Print `names`, `ages`, `bmis`, and `insurance_costs` outside of the loop.
# 
#     Make sure the output is what you expect.

# In[15]:


print(names)
print(ages)
print(bmis)
print(insurance_costs)


# 19. Now that all of our data is in separate lists, we can easily perform analysis on that data. Let's calculate the average BMI in our dataset.
# 
#     First, create a variable called `total_bmi` and set it equal to 0.

# In[16]:


total_bmi = 0


# 20. Next, use a `for` loop to iterate through `bmis` and add each `bmi` to `total_bmi`.
# 
#     Remember to convert `bmi` to a float.

# In[17]:


for bmi in bmis:
    total_bmi += float(bmi)


# 21. After the for loop, create a variable called `average_bmi` that stores the `total_bmi` divided by the length of the `bmis` list.
# 
#     Print out `average_bmi` with the following message:
#     ```
#     Average BMI: {average_bmi}
#     ```

# In[18]:


average_bmi = total_bmi / len(bmis)
print('Average BMI: ' + str(average_bmi))


# ## Extra

# 22. Congratulations! In this project, you used Python strings to transform and clean up medical data.
# 
#     As a data scientist, it's important that you have clean and accurate data before you analyze it. You now have a better idea of the data preparation process moving forward.
#     
#     If you'd like extra practice with Python strings, here are some suggestions to get you started:
#     - Calculate the average insurance cost in `insurance_costs`. You will have the remove the `$` in order to calculate this.
#     - Write a for loop that outputs a string for each individual in the following format:
#     ```
#     Marina is 27 years old with a BMI of 31.1 and an insurance cost of $7010.0.
# Markus is 30 years old with a BMI of 22.4 and an insurance cost of $4050.0.
#     ...
#     ...
#     
#     Happy coding!

# In[ ]:





# In[ ]:




