import requests as r



def getweather(lat,long):
    response = r.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m,wind_speed_10m,wind_direction_10m,rain')
    if response.ok:
        data = response.json()
        #print(data)
        return data['current']
    else:
        response.raise_for_status()
    

def getlocation_coor(lat,long):
    response = r.get(f'https://geocode.maps.co/reverse?lat={lat}&lon={long}&accept-language=en&api_key=6ac909ca4103b625262307ofuf46433')
    if response.ok:
        data = response.json()
        #print(data)
        return data['display_name']
    else:
        response.raise_for_status()

def getlocation_pincode(pcd,country = 'india'):
    response = r.get(f'https://geocode.maps.co/search?postalcode={pcd}&country={country}&accept-language=en&api_key=6ac909ca4103b625262307ofuf46433')
    if response.ok:
        data = response.json()
        #print(data)
        return data[0]
    else:
        response.raise_for_status()
    

def main():
    user = int(input('Enter input type for weather, coordinates(1) and pincode(2):'))
    if user == 1:
        lat = float(input('Enter the latitudes:'))
        long = float(input('Enter the longitudes;'))
        if not -90<lat<90 and -180<long<180:
            print('Invalid latitude or longitude , input out of range:')
        else:
            weather = getweather(lat,long)
            name = getlocation_coor(lat,long)
            print(f'The location {name} has')
            print(f'''\t\tTemperature: {weather['temperature_2m']}
                     Rain: {weather['rain']}
                     Wind Speed: {weather['wind_speed_10m']}
                     Wing Direction: {weather['wind_direction_10m']}''')

    elif user == 2:
        pcd = int(input('Enter the Pincode ranging from 110001 to 899999:'))
        if not 110000<pcd<900000:
            print('The input is out of the range:')
        else:
            loc = getlocation_pincode(pcd)
            weather = getweather(loc['lat'],loc['lon'])
            print(f'''Location name:{loc['display_name']}
                      Temperature: {weather['temperature_2m']}
                     Rain: {weather['rain']}
                     Wind Speed: {weather['wind_speed_10m']}
                     Wing Direction: {weather['wind_direction_10m']}''')
            
                     

main()
