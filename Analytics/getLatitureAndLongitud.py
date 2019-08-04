import pandas as pd
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyAK7bhwFBja9fm9I78AJ8pfpfnCP4xf2cM')

df = pd.read_excel('table.xlsx')
print(df)

def requestData(x):
    y = gmaps.geocode(x)
    if (len(y) > 0):
        return y[0]['geometry']['location']
    else:
        return {'lng': 0, 'lat': 0}

df['latitud'] = (df['direccion'] + ', ' + df['ciudad']).apply(lambda x : requestData(x))

df['longitud'] = df['latitud'].apply(lambda x : x['lng'])
df['latitud'] = df['latitud'].apply(lambda x : x['lat'])
print(df['latitud'])

df.to_excel('final.xlsx')