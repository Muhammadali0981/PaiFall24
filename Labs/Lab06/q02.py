import pandas as pd 


data = {
    
    'title': ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E"],
    'revenue': [2500000,1500000,3000000,1000000,4000000],
    'budget' : [800000,500000, 900000, 200000,600000],
    'runtime' : [123, 120, 90, 80, 130]
}


df = pd.DataFrame(data)

sorted_data = df.sort_values(by='runtime', ascending=False)

print(sorted_data)