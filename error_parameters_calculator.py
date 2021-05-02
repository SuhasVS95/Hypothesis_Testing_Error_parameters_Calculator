#!/usr/bin/env python
# coding: utf-8

# ## <center>Error Parameters Calculator</center>

# ### Problem Statement:
# 
# This error calculator function calculates the different parameter with the given data. The parameters include:
# 
# **1. Sample Size(n)**<br>
# **2. Type I Error(alpha)**<br>
# **3. Type II Error(beta)**<br>
# **4. Population Mean**<br>
# **5. Sample Mean**<br>
# **6. Population Standard Deviation**<br>
# 
# **How does it work?**
# 
# 1. Select the error parameter number from above list.
# 2. Enter the asked required data.
# 3. Get the calculated output of the required parameter.
# 4. Repeat steps 1,2,3 for different parameters to be calculated continuing the code.
# 5. When you wish to quit select "n".
# 
# **Note: To get a final summary of all the calculations of the parameters that you have done, click on the SUMMARY REPORT button.**


# In[2]:


import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sns
import random
from scipy.stats import shapiro


# In[3]:


def calculate_sample_size():
    
    print("Required parameters for sample size calculation:")
    print("--------------------------------------------------------------------------")
    
    alpha=float(input("Enter alpha value:"))
    beta=float(input("Enter beta value:"))
    sigma=float(input("Enter sigma value:"))
    mu_pop=float(input("Enter population mean value:"))
    xbar=float(input("Enter sample mean value:"))
    
    z_alpha=st.norm.isf(alpha)
    z_beta=st.norm.ppf(beta)
    n1=((z_alpha+z_beta)*sigma)**2
    n2=(mu_pop-xbar)**2
    n=n1/n2
    print("Calculated Z_Alpha:",z_alpha)
    print("Calculated Z_Beta:",z_beta)
    
    print("--------------------------------------------------------------------------")
    print("The sample size for your above requirement of parameters is:",np.ceil(n))
    print("--------------------------------------------------------------------------")


# In[4]:


def calculate_beta():
    
    print("Required parameters for beta calculation:")
    print("--------------------------------------------------------------------------")
    
    alpha=float(input("Enter alpha value:"))
    n=float(input("Enter sample size value:"))
    sigma=float(input("Enter sigma value:"))
    mu_pop=float(input("Enter population mean value:"))
    xbar=float(input("Enter sample mean value:"))
    
    z_alpha=st.norm.isf(alpha)
    z_beta=((np.sqrt(n)*(mu_pop-xbar))/sigma)-z_alpha
    beta=st.norm.cdf(z_beta)
    
    print("Calculated Z_Alpha:",z_alpha)
    print("Calculated Z_Beta:",z_beta)

    print("--------------------------------------------------------------------------")
    print("The Type II error(beta) for your above requirement of parameters is:",round(beta,2))
    print("--------------------------------------------------------------------------")


# In[5]:


def calculate_alpha():
    
    print("Required parameters for alpha calculation:")
    print("--------------------------------------------------------------------------")
    
    beta=float(input("Enter beta value:"))
    n=float(input("Enter sample size value:"))
    sigma=float(input("Enter sigma value:"))
    mu_pop=float(input("Enter population mean value:"))
    xbar=float(input("Enter sample mean value:"))
    
    z_beta=st.norm.ppf(beta)
    z_alpha=((np.sqrt(n)*(mu_pop-xbar))/sigma)-z_beta
    alpha=st.norm.cdf(z_alpha)
    
    print("Calculated Z_Alpha:",z_alpha)
    print("Calculated Z_Beta:",z_beta)
    
    print("--------------------------------------------------------------------------")
    print("The Type I error(alpha) for your above requirement of parameters is:",round(1-alpha,2))
    print("--------------------------------------------------------------------------")


# In[6]:


def calculate_population_mean():
    
    print("Required parameters for population mean calculation:")
    print("--------------------------------------------------------------------------")
    
    alpha=float(input("Enter alpha value:"))
    n=float(input("Enter sample size value:"))
    sigma=float(input("Enter sigma value:"))
    beta=float(input("Enter beta value:"))
    xbar=float(input("Enter sample mean value:"))
    
    z_alpha=st.norm.isf(alpha)
    z_beta=st.norm.ppf(beta)
    mu_pop=(((z_alpha+z_beta)*sigma)/np.sqrt(n))+xbar
    
    print("Calculated Z_Alpha:",z_alpha)
    print("Calculated Z_Beta:",z_beta)
    
    print("--------------------------------------------------------------------------")
    print("The population mean for your above requirement of parameters is:",np.ceil(mu_pop))
    print("--------------------------------------------------------------------------")


# In[7]:


def calculate_sample_mean():
    
    print("Required parameters for sample mean calculation:")
    print("--------------------------------------------------------------------------")
    
    alpha=float(input("Enter alpha value:"))
    n=float(input("Enter sample size value:"))
    sigma=float(input("Enter sigma value:"))
    beta=float(input("Enter beta value:"))
    mu_pop=float(input("Enter population mean value:"))
    
    z_alpha=st.norm.isf(alpha)
    z_beta=st.norm.ppf(beta)
    xbar=mu_pop-(((z_alpha+z_beta)*sigma)/np.sqrt(n))
    
    print("Calculated Z_Alpha:",z_alpha)
    print("Calculated Z_Beta:",z_beta)
    
    print("--------------------------------------------------------------------------")
    print("The sample mean for your above requirement of parameters is:",round(xbar,2))
    print("--------------------------------------------------------------------------")


# In[8]:


def calculate_sigma():
    
    print("Required parameters for sigma calculation:")
    print("--------------------------------------------------------------------------")
    
    alpha=float(input("Enter alpha value:"))
    n=float(input("Enter sample size value:"))
    beta=float(input("Enter beta value:"))
    xbar=float(input("Enter sample mean value:"))
    mu_pop=float(input("Enter population mean value:"))
    
    z_alpha=st.norm.isf(alpha)
    z_beta=st.norm.ppf(beta)
    sigma=(np.sqrt(n)*(mu_pop-xbar))/(z_alpha+z_beta)
    
    print("Calculated Z_Alpha:",z_alpha)
    print("Calculated Z_Beta:",z_beta)

    print("--------------------------------------------------------------------------")
    print("The population std for your above requirement of parameters is:",round(sigma,2))
    print("--------------------------------------------------------------------------")


# In[9]:


def error_param():
    
    print("Hi!!! Welcome to ERROR CALCULATOR!!!")
    print()
    
    while(1):
        print("Please select the number of the respective parameter you like to calculate:")
        print()
        print("1. Sample Size(n)\n\n2. Type I Error(alpha)\n\n3. Type II Error(beta)\n\n4. Population Mean\n\n5. Sample Mean\n\n 6.Sigma")
        print("--------------------------------------------------------------------------")
        inp=(input("Enter the number:"))

        if inp in ["1","2","3","4","5","6"]:
            if inp=="1":
                calculate_sample_size()
            elif inp=="2":
                calculate_alpha()
            elif inp=="3":
                calculate_beta()
            elif inp=="4":
                calculate_population_mean()
            elif inp=="5":
                calculate_sample_mean()
            elif inp=="6":
                calculate_sigma()
        else:
            print("Please enter the valid number in the range [1,2,3,4,5,6]")
            break
        print("Do you want to continue:y/n")
        te=input()
        if(te=='y'):
            pass
        elif(te=='n'):
            print()
            print("You have opted to quit.")
            print("Thank you for using the Error Calculator")
            break
        else:
            print("Invalid Command:",te)
            print("please enter y for Yes, n for No")
            print("Run the tool again!!!")
            break





