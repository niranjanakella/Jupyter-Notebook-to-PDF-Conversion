#!/usr/bin/env python
# coding: utf-8

# In[44]:


#Import the PDF convertion library
import pdfkit
import os

#Path to the folder containing the jupyternotebook.html file
os.chdir(r'C:/Users/niran/Desktop/ipynb_to_pdf/')


# In[46]:


#Path to the wkhtmltopdf executable file
path_wkhtmltopdf =r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

#Assigning a variable to the pdfkit configuration
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)


# In[47]:


#Converting HTML file to PDF file
#Format of Code:- pdfkit.from_file('Path to HTML file', 'Path to destination file.pdf', configuration = config)
pdfkit.from_file('jupyternotebook.html', 'jupyternotebook.pdf',configuration=config)

