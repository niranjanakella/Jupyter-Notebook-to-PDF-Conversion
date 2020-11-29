# Jupyter-Notebook-to-PDF-Conversion
## Conversion Mechanism
<hr>
<p>To convert a '.ipynb' Jupyter Notebook file into PDF, it should be intially be converted into a HTML file and then be converted into a pdf file for better representation.</p>
<br>

## Libraries and tools to be installed
<hr>

- Install "**nbconvert**" tool through pip.
~~~
pip install nbconvert
~~~
 **Note**:- If you have installed Anaconda and you are running the above command on cmd (Windows Terminal) then **nbconvert** will only be accessable to applications using cmd flow. So, please run the above command even on Anaconda Prompt.
 <br>
 <br>

-  Download the "**wkhtmltopdf**" library/tool to convert the '.html' file to '.pdf' : - <a href="https://wkhtmltopdf.org/downloads.html" target="_blank">HERE</a>
- Install the "**pdfkit**" library through the following command
```
pip install pdfkit
```
<br>

## Jupyter Notebook to PDF <hr>

**Mechanism**:- JupyterNotebook --> HTML --> PDF
<br>
<br>


- Convert Jupyter Notebook to HTML file. In the below command mention the complete path of your jupyter notebook (Example: jupyter nbconvert --to html C:\Users\niran\Desktop\ipynb_to_pdf\mynotebook.ipynb).
<br>

-  Perform the below operation in Jupyter Terminal.
```
jupyter nbconvert --to html Yournotebook.ipynb
```
Jupyter Terminal can be found here:-
<p align = "center"><img src = "https://github.com/niranjanstudy06/Jupyter-Notebook-to-PDF-Conversion/blob/main/img/Jupyter_Terminal.png?raw=true"></img></p>

- Further convert the HTML file into PDF file through the <a href="https://github.com/niranjanstudy06/Jupyter-Notebook-to-PDF-Conversion/blob/main/PDF_Converter.py" target="_top">PDF_Converter.py</a> file.

**Note**: - Go through the  <a href="https://github.com/niranjanstudy06/Jupyter-Notebook-to-PDF-Conversion/blob/main/PDF_Converter.py" target="_top">PDF_Converter.py</a> file keenly.