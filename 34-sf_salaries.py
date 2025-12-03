import pandas as pd

def chief_string(job_title):
    if 'chief' in job_title.lower().split():
        return True
    else:
        return False
    
sal = pd.read_csv("data/salaries.csv")
print(sal.head())

print(sal['BasePay'].mean())
print(sal['OvertimePay'].max())
print(sal[sal['EmployeeName'] == "JOSEPH DRISCOLL"]["TotalPayBenefits"])
print(sal[sal["TotalPayBenefits"] == sal["TotalPayBenefits"].max()]) # Highest TotalPayBenefits 
print(sal.iloc[sal['TotalPayBenefits'].argmin()])
print(sal.groupby('Year')['BasePay'].mean())  
print(sal['JobTitle'].nunique()) # Number of unique job title
print(sal['JobTitle'].value_counts().head(5))
print(sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)) # counts the number of jobtitle == 1 in year 2013
# How many people have chief in their job titles
print(sum(sal['JobTitle'].apply(lambda x: chief_string(x))))