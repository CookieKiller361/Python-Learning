#just some beginner Pandas code 
import pandas as pd

#Pandas Series
data=[1,2,3]

testSeries=pd.Series(data)
print(f'{testSeries}\n')

#Pandas Series with index
testSeries= pd.Series(data, index=["test1","test2","test3"])
print(testSeries)

#item call by index number
print(f'\n{testSeries[0]}\n')

#item call by label
print(f'{testSeries["test2"]}')

#key/value like dictionary Panda Series
data1={"test1":1, "test2":2, "test3":3}
testSeries=pd.Series(data1)
print(f'\n{testSeries}')

#panda DataFrame
dictionarylike={
    "test1":[1,2,3,4],
    "test2":[5,6,7,8]
}

testDataFrame=pd.DataFrame(dictionarylike)
print(f'\n{testDataFrame}')

#loc funktion in DataFrames
print(f'\n{testDataFrame.loc[0]}')

#Dataframe with index
testDataFrame=pd.DataFrame(dictionarylike, index=["test1","test17","sushi","apple"])
print(f'\n{testDataFrame}')

#row by call by label from index
print(f'\n{testDataFrame.loc["test17"]}')

#load Data into the DataFrame
print("\n")
import_csv_Data = pd.read_csv('data.csv')

print(import_csv_Data.to_string())
print("\n")
print(import_csv_Data)

#Load Data from a json file into the DataFrame
testjson=pd.read_json('testjson.json')
print(f'\n{testjson.to_string()}')