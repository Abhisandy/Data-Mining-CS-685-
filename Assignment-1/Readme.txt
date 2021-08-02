Data Preprocessing:

    • Data Integration :  Data is given in multiple files, So first we need to collect all the data in a single place. For this we used pandas Dataframe ( a tabular datastructure) , we collected all data from different raw data csv to a single Dataframe, so that we can process it further .

    • Attribute Selection :  There are various featues in csv files but we need only few (Date, District name, number of cases) to process our Data .  Also,  Data in First two csv is sligtly different from other csv’s . For that we concat first two csv in a different Dataframe and other csv’s in other Dataframe. First 2 csv contain indepenpent patient data while other csv’s contain number of patients in a district for a particular date .
      
      
    •  Data Cleaning : Some of the Attribute values are missing . So we ignore those tuples using .dropna() function from Dataframe.
The names in neighbor-district.json are different from names in covid-19 portal . For that we maintain a dictionary in which keys are names of neighbor-district.json and corresponding values are names of covid-19 portal . 
Also in data some of the entries are given as Negative values , we consider those data as no info is available for that district.
      
      For matching districts we used some logics behind : 
      
    1 . 	We created a function that gives us list of districts those are present in covid-19 portal but  	not  present in neighbor-district.json , Based on result we are able to correct some of the    	districts manually .

    2 .    Also , i use a Package named as FuzzyWuzzy form whcih i am able to guess wheather a 	same  named district is present in district-neighbor.json with almost same but with some 	wrong  characters in spelling .
	  

Processing of Data : After creating dictionary we merge some districts into one based on if these districts data are available or not in covid-19 portal . Based on corrected districts name we gave id to individual district and process data based on weeks , months and overall .

For calculation of mean and standard Deviation : For calculation of mean of all other neighbor districts , we used edge-graph.csv and for individual id (starting from 101) we get it’s corresponding 
neighbors using .iloc function and then make a list of values of all its neighbors values and then we can calculate mean and standard deviation(using pstdev function inside statistics package) .

For relationship of states and districts : For realtionship between states and dsitricts we used all raw data files from which we created a dictionary (key: id of district , value : state of district) , and then from this dictionary we created another dictionary (key: states , value : a list of all districts under it )
 
For Calculation of Z-Score : we get corresponding mean and standard deviation using .iloc and .loc function of pandas Dataframe.

For top hotspot and Coldspot : we created dictionary for each  week (or month , overall)  in which key : district , value : calculated value to determine hotspot(or coldspot) , which we sorted after each iteration of loop and store top 5 values in csv using .writerow function of csv and there are some cases in which no entries is found we use 'NA' for those entries in csv files.
