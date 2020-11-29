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

-  Download the "**wkhtmltopdf**" library/tool to convert the '.html' file to '.pdf' : - https://wkhtmltopdf.org/downloads.html
<br>

## Jupyter Notebook to PDF <hr>

**Mechanism**:- JupyterNotebook --> HTML --> PDF


- Convert Jupyter Notebook to HTML file. (Perform the below operation in Jupyter Terminal)
```
jupyter nbconvert --to html notebook.ipynb
```
Jupyter Terminal can be found here:-
<p align = "center"><img src = >