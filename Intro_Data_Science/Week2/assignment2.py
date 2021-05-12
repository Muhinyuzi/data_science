import pandas as pd

df = pd.read_csv("datasets/NISPUF17.csv", index_col=0)

print(df.head())
#print(df.columns)
#print(df['EDUC1'].head())
#print(df['P_NUMFLU'].head())
#print(df[["CBF_01","P_NUMFLU"]].head(20))
#df2 = df[["CBF_01","P_NUMFLU"]].dropna()
#print(df2.head(40))
#print(len(df2))
#df3 = df2[df2["CBF_01"] == 1]
#df4 = df2[df2["CBF_01"] == 2]
#print(df3.head(10))
#print(df4.head(10))
df1 = df[["SEX","P_NUMVRC","HAD_CPOX"]].dropna()
#print(df1.head(20))
df2 = df1[df1["P_NUMVRC"] > 0.0]
#print(df2.head(20))
df3 = df2[["SEX","HAD_CPOX"]]
#number of all who got at least on dose
#print(df3.head(20))
#dataframe for those who had chicken pox
df4 = df3[df3["HAD_CPOX"] == 1] 
#number of those who had CPOX
total_had_cpox = len(df4)
print(total_had_cpox)
df4_male = df4[df4["SEX"] == 1] 
total_had_cpox_male = len(df4_male)
df4_female = df4[df4["SEX"] == 2]
total_had_cpox_female = len(df4_female)
#ratio_had_cpox_male = float(total_had_cpox_male/total_had_cpox)
#ratio_had_cpox_female = float(total_had_cpox_female/total_had_cpox)


#datframe for those who did not have chicken pox
df5 = df3[df3["HAD_CPOX"] == 2]
#number of those who had not CPOX
total_had_not_cpox = len(df5)
print(total_had_not_cpox)
df5_male = df5[df5["SEX"] == 1] 
total_had_not_cpox_male = len(df5_male)
df5_female = df5[df5["SEX"] == 2]
total_had_not_cpox_female = len(df5_female)
#ratio_had_not_cpox_male = float(total_had_not_cpox_male/total_had_not_cpox)
#ratio_had_not_cpox_female = float(total_had_not_cpox_female/total_had_not_cpox)

ratio_male = float(total_had_cpox_male/total_had_not_cpox_male)
ratio_female = float(total_had_cpox_female/total_had_not_cpox_female)
print(ratio_male,ratio_female)


def proportion_of_education():
    # your code goes here
    # YOUR CODE HERE
    a = 0
    b = 0
    c = 0
    d = 0
    dict1 = {"less than high school":0,
    "high school":0,
    "more than high school but not college":0,
    "college":0}
    import pandas as pd
    df = pd.read_csv("datasets/NISPUF17.csv", index_col=0)
    df = df['EDUC1']
    for educ in df:
    	if educ == 1:
    		a += 1
    	if educ == 2:
    		b += 1 
    	if educ == 3:
    		c += 1
    	if educ == 4:	    		  		
            d += 1
    total = len(df)      
    a = float(a) / total
    b = float(b) /total
    c = float(c) /total
    d = float(d) /total   	 
    dict1["less than high school"] = a
    dict1["high school"] = b
    dict1["more than high school but not college"] = c
    dict1["college"] = d
    return dict1


    #raise NotImplementedError()
#print(type(proportion_of_education()))
#print(len(proportion_of_education()) == 4)
#print("less than high school" in proportion_of_education().keys())
#print(proportion_of_education())   

df = pd.read_csv('datasets/NISPUF17.csv', index_col=0)
df2 = df[["CBF_01","P_NUMFLU"]].dropna()
print(df2.head(10))
def average_influenza_doses():
    # YOUR CODE HERE
    import pandas as pd
    df = pd.read_csv('datasets/NISPUF17.csv', index_col=0)
    df2 = df[["CBF_01","P_NUMFLU"]].dropna()
    df3 = df2[df2["CBF_01"] == 1]
    df4 = df2[df2["CBF_01"] == 2]
    df5 = df3["P_NUMFLU"]
    df6 = df4["P_NUMFLU"]
    total1 = float(len(df5))
    total2 = float(len(df6))
    a = 0.0
    b = 0.0
    for dose in df5:
        a += dose
    for dose in df6:
        b += dose
    total = float(a + b)    
    received_breast_milk = float(a) / total1
    not_received_breast_milk = float(b) / total2

    return (received_breast_milk,not_received_breast_milk)
    #return (a,b)

    #raise NotImplementedError()

print(average_influenza_doses())  
print(type(average_influenza_doses()))
print(len(average_influenza_doses())==2)  


def chickenpox_by_sex():
    # YOUR CODE HERE
    import pandas as pd
    dict1 = {"male":0.0,"female":0.0}
    df = pd.read_csv("datasets/NISPUF17.csv", index_col=0)
    df1 = df[["SEX","P_NUMVRC","HAD_CPOX"]].dropna()
    #dataframe of all who got at least on dose
    df2 = df1[df1["P_NUMVRC"] > 0.0]
    df3 = df2[["SEX","HAD_CPOX"]]
    #dataframe for those who had chicken pox
    df4 = df3[df3["HAD_CPOX"] == 1] 
    df4_male = df4[df4["SEX"] == 1] 
    total_had_cpox_male = len(df4_male)
    df4_female = df4[df4["SEX"] == 2]
    total_had_cpox_female = len(df4_female)
    #datframe for those who did not have chicken pox
    df5 = df3[df3["HAD_CPOX"] == 2]
    df5_male = df5[df5["SEX"] == 1] 
    total_had_not_cpox_male = len(df5_male)
    df5_female = df5[df5["SEX"] == 2]
    total_had_not_cpox_female = len(df5_female)
    ratio_male = float(total_had_cpox_male/total_had_not_cpox_male)
    ratio_female = float(total_had_cpox_female/total_had_not_cpox_female)
    dict1 = {"male":ratio_male,"female":ratio_female}
    return dict1
    #raise NotImplementedError()
#print(len(chickenpox_by_sex())==2)
#print(chickenpox_by_sex()) 


def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd
    
    # this is just an example dataframe
    #df=pd.DataFrame({"had_chickenpox_column":np.random.randint(1,3,size=(100)),
                   #"num_chickenpox_vaccine_column":np.random.randint(0,6,size=(100))})
    df = pd.read_csv("datasets/NISPUF17.csv", index_col=0)
    df = df[df["HAD_CPOX"] > 3]
    df1 = df[["P_NUMVRC","HAD_CPOX"]].dropna()    

    # here is some stub code to actually run the correlation
    corr, pval=stats.pearsonr(df1["HAD_CPOX"],df1["P_NUMVRC"])
    
    # just return the correlation
    return corr   

print(corr_chickenpox())

df = pd.read_csv("datasets/NISPUF17.csv", index_col=0)
df = df[df["HAD_CPOX"] > 3]
print(df["HAD_CPOX"].head())
df1 = df[["P_NUMVRC","HAD_CPOX"]].dropna()
#print(df1.head(100))     