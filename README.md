# nasig_2021
Files for geographic subject analysis project


## About this project
This project is a work-in-progress. I am also still learning to code, so there is inevitably more efficient, easier ways to do this. Feedback is always welcome, as are collaborations. Feel free to get in touch :)

This project was initiated as a type of collection diversity audit. I wanted to see if we could use the structured bibliographic metadata in libraries to assess how diverse our collections are (and perhaps answer other questions as well). This analysis examined over 2.7 million geographic subject headings (field 651 subfield a), as a surrogate measure for diversity. Tools used included SQL (the freely available SQLiteStudio) and python (predominantly the libraries pymarc and pandas), so that the process can be reused by other libraries, regardless of the systems they use or the budgets they have.

## About these files
- To extract the data from my source marc records, I used this program : https://github.com/JordanPedersen/pymarc-extraction
- The extracted data is available here if you want to play around with it (let me know if you find anything interesting!), filename : joined_nohead.txt.zip
- The SQL queries I used to clean my data is available in this repository, filename : SQL_cleaning_final
- The cleaned dataset is available here (joined with https://www.kaggle.com/petersorensen360/iso3166countrieswithregionalcodes) filename : NASIG_split.zip
- The Jupyter notebook is available here, filename : NASIG_final.ipynb
- The Jupyter notebook is also available as a .py file here, filename : NASIG_final.py
