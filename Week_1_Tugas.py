#!/usr/bin/env python
# coding: utf-8

# # Week 1 Review Exercises
# 

# Q1. Data Types
# 
# What is the data type of the variable `pop`?

# In[1]:


pop = 5.8


# In[10]:


# use a suitable function to check your answer

type(pop)


# Q2. Which of the following is a valid variable name of of population below 15 years old?
# 

# In[14]:


# which line won't give an error? Comment out the ones that do!
15_years_and_below = 12.33
get_ipython().run_line_magic('_pop_15_below', '= 12.33')
_15&below_pop = 12.33
_15_below_pop = 12.33 #this line won't give an error


# Q3. What will be stored in `result`?

# In[15]:


result = 3 + 4 ** 2 - (5 // 2)

print(result)


# Q4. If Singapore has an estimated population of 5.85 million and the land area is 700 square kilometers, what is the population density (number of people per KM)? 
# 

# In[20]:


# Estimated total Population of Singapore, in millions
total_pop_millions = 5.85

# Total land area, in KM
land_area = 700

# How many people are there per KM?
total = total_pop_millions/land_area

print(total,"/Km^2")


# Q5. Write a function called `pop_density()` that receives two arguments:
# 1. the population, recorded in millions, `population_mil`
# 2. the land area, in square kilometres, `land_area_sqkm`
# 
# The function should calculate and return the population density. 
# 

# In[26]:


# Write the function here
def pop_density(population_mil,land_area_sqkm):

    density=population_mil/land_area_sqkm
    return density

density = pop_density(7.50, 1050)

print(f"Kepadatan penduduk: {density} penduduk per km^2")


# Q6. Call the function you have written to calculate and display the population density of Hong Kong: 7.50 million people in a land area of 1050 km squared 
# 

# In[27]:


# Call the function 
print(density)


# Q7. Using the `pop_density()` function, calculate the population density of Singapore and then use comparison operators to compare the population densities of Singapore and Hong Kong.
# 
# Singapore's population: 5.85 million
# Singapore's land area: 700 sq km
# 
# (Data From [Worldometers](http://worldometers.info))
# 

# In[30]:


# fungsi pop_density()
def pop_density(population,land_area):
    density=population/land_area
    return density

# Populasi dan area Singapura
singapore_population = 5.85 * 10**6  # 5.85 million
singapore_area = 700  # 700 km^2

# Kalkulasi kepadatan populasi Singapura menggunakan fungsi pop_density()
singapore_density = pop_density(singapore_population, singapore_area)

# Populasi dan area Hong Kong
hong_kong_population = 7.5 * 10**6  # 7.5 million
hong_kong_area = 1050  # 1050 km^2

# Kalkulasi kepadatan populasi Hong Kong menggunakan fungsi pop_density()
hong_kong_density = pop_density(hong_kong_population, hong_kong_area)

# Perbadingan kepadatan Singapura dan Hong Kong
if singapore_density > hong_kong_density:
    print("Singapura memiliki tingkat kepadatan penduduk lebih tinggi daripada Hong Kong.")
elif singapore_density < hong_kong_density:
    print("Singapura memiliki tingkat kepadatan penduduk lebih rendah daripada Hong Kong.")
else:
    print("Singapura dan Hong Kong tingkat kepadatan penduduk yang sama.")



# Q8. Let's add another area to compare: Macao's population is 0.65 million in a land area of 30 sq km. Find out whether Singapore's population density is higher than BOTH Hong Kong and Macao.

# In[34]:


# Populasi dan area Macao
macao_population = 0.65 * 10**6  # 0.65 million
macao_area = 30  # 30 km^2

# Kalkulasi kepadatan populasi Macao menggunakan fungsi pop_density()
macao_density = pop_density(macao_population, macao_area)

# Singapore's population density is higher than both Hong Kong AND Macao
if singapore_density > hong_kong_density and singapore_density > macao_density:
    print("Singapura memiliki tingkat kepadatan penduduk lebih tinggi daripada Hongkong dan Macao.")
elif singapore_density < hong_kong_density:
    print("Singapura memiliki tingkat kepadatan penduduk lebih rendah daripada Hong Kong.")
elif singapore_density < macao_density:
    print("Singapura memiliki tingkat kepadatan penduduk lebih rendah daripada Macao")
else:
    print("Singapura, Hong Kong dan Macao tingkat kepadatan penduduk yang sama.")


# Q9. Write a function called compare_density() that receives two arguments representing the population densities of two areas. The function will compare the two values and print one of the following strings:
# - “Area 1 has higher density”
# - “Area 2 has higher density”
# - “Both areas have the same density”

# In[38]:


# Write the function

def compare_density(density1, density2):
    
    if density1 > density2:
        print("Area 1 has higher density")
    elif density2 > density1:
        print("Area 2 has higher density")
    else:
        print("Both areas have the same density")


# Then we can test the function by passing the values of `sg_density` and `hk_density` as arguments.

# In[ ]:


compare_density(sg_density, hk_density)


# Q10. What will be the result of the following loop?
# 
# ```
# for year in range(2022, 2031, 2):
#     print(year)
# ```

# In[39]:


# Type in the code for the loop given above and execute to check your answer

for year in range(2022,2031,2):
    print(year)


# Q.11 Write a function projected_population() that receives three arguments:
# - Current population, in millions
# - Growth rate
# - Current year
# 

# The function should:
# - set the projected population to the current population
# - set the projected year to the current year
# - calculate the difference between the projected population and current population
# 
# while the difference is between -1 and 1:
# 1. print the projected year and the projected population
# 2. calculate the projected population = projected population + projected population * growth rate / 100
# 3. update the projected year 
# 4. recalculate the difference between the projected propulation and current population

# In[56]:


def projected_population(current_pop, growth_rate, current_year):
    # complete the function according to the guide

    projected_population = current_pop
    projected_year = current_year
    
    while -1 <= (projected_population - current_pop) <= 1:
        print(f"Year: {projected_year}, Population: {projected_population:.2f} million")
        
        projected_population += projected_population * growth_rate / 100
        projected_year += 1


# In[57]:


# testing with Thailand
print("Thailand's population growth")
projected_population(current_pop = 69.8, growth_rate = 0.3, current_year = 2020)


# Q.12 Write a function called `string_info()` which takes in a string argument and returns four values:
# - the first 3 characters
# - last 3 characters
# - the number of characters in the string
# - the string with each word capitalized

# In[54]:


def string_info(word): 
    # complete the function
    
    start = word[:3]
    end = word[-3:]
    num = len(word)
    title = ' '.join(word.title() for word in word.split())

    return start, end, num, title


# In[55]:


#calling the function
start, end, num, title = string_info("data science")

input_word = "data science"

result = string_info(input_word)
print("First 3 characters:", result[0])
print("Last 3 characters:", result[1])
print("Number of characters:", result[2])
print("Capitalized string:", result[3])


# In[52]:


# print what's returned
print(string_info("data science"))


# # Congratulations! 
# 
# You have reached the end of this notebook! Hope you have been able to practice and review the fundamental concepts in Python coding and we will do more next week!
