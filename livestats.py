#coding=utf-8
import requests
import sys
import csv
import numpy as np
import time
url = "https://api.covid19api.com/countries"
payload = {}
headers = {}
response = requests.request("GET", url, headers=headers, data = payload)
#print(response.text.encode('utf8'))
responseText = response.text
#print(responseText)
#print(type(response.text))
result = 0
countries = []

while(result != -1):
    result = responseText.find("\"Country\": \"")
    if(result != -1):
        responseText = responseText[result+12:]
        subResult = responseText.find("\"")
        subResponseText = responseText[:subResult]
        countries.append(subResponseText)
#print(countries)
#Getting Country Status since some dates
url = "https://api.covid19api.com/live/"
countryName = ""
urlMid = "/status/confirmed/date/2020-0"
month = 0
dash = "-"
date = 0
timeVal = "T23:59:59Z"
payload = {}
headers = {}
t = []
#countriesList = ['Argentina', 'Korea (South)', 'Slovakia', 'South Georgia and the South Sandwich Islands', 'Algeria', 'Falkland Islands (Malvinas)', 'Madagascar', 'Pitcairn', 'Venezuela (Bolivarian Republic)', 'Georgia', 'Estonia', 'Mauritania', 'Panama', 'South Africa', 'Svalbard and Jan Mayen Islands', 'Switzerland', 'Cayman Islands', 'Djibouti', 'Eritrea', 'Greece', 'Honduras', 'Moldova', 'Syrian Arab Republic (Syria)', 'Western Sahara', 'Bahrain', 'Botswana', 'Guyana', 'Jordan', 'Qatar', 'Solomon Islands', 'Japan', 'Lesotho', 'Cyprus', 'Spain', 'Tonga', 'Nigeria', 'Cuba', 'Denmark', 'Grenada', 'Holy See (Vatican City State)', 'Colombia', 'Namibia', 'Saudi Arabia', 'Ukraine', 'Gibraltar', 'Haiti', 'Montserrat', 'Singapore', 'Antarctica', 'Comoros', 'Bosnia and Herzegovina', 'Iran, Islamic Republic of', 'Kiribati', 'Tokelau', 'ALA Aland Islands', 'Angola', 'Belarus', 'Croatia', 'Italy', 'Nepal', 'Congo (Brazzaville)', 'Netherlands Antilles', 'Thailand', 'United States of America', 'Bangladesh', 'Cambodia', 'Libya', 'Sudan', 'Aruba', 'Azerbaijan', 'Lithuania', 'Sri Lanka', 'Iceland', 'Lao PDR', 'Macao, SAR China', 'Montenegro', 'Serbia', 'Tanzania, United Republic of', 'Morocco', 'San Marino', 'Tunisia', 'Afghanistan', 'Ethiopia', 'Niue', 'Cameroon', 'Congo (Kinshasa)', 'Réunion', 'Slovenia', 'Turks and Caicos Islands', 'Egypt', 'El Salvador', 'Malawi', 'Malta', 'Viet Nam', 'Jersey', 'Kenya', 'Swaziland', 'Turkey', 'Tuvalu', 'Anguilla', 'Australia', 'Burundi', 'Russian Federation', 'Sierra Leone', 'Cape Verde', 'Finland', 'Gambia', 'Romania', 'Fiji', 'Mozambique', 'Samoa', 'Saint Vincent and Grenadines', 'South Sudan', 'Armenia', 'Monaco', 'Nicaragua', 'Peru', 'French Guiana', 'Kazakhstan', 'Saint Kitts and Nevis', 'Saint Pierre and Miquelon', 'Timor-Leste', 'Bermuda', 'Vanuatu', 'American Samoa', 'Bahamas', 'Barbados', 'Kuwait', 'Liechtenstein', 'Malaysia', 'US Minor Outlying Islands', 'Uzbekistan', 'Zambia', 'Antigua and Barbuda', 'Canada', 'Netherlands', 'New Zealand', 'Norfolk Island', 'Oman', 'Austria', 'Central African Republic', 'Costa Rica', 'Turkmenistan', 'Poland', 'Virgin Islands, US', 'Hong Kong, SAR China', 'Niger', 'Northern Mariana Islands', 'Palestinian Territory', 'Philippines', 'Saint-Martin (French part)', 'Belize', 'Israel', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Ecuador', 'Jamaica', 'Luxembourg', 'Paraguay', 'United Arab Emirates', 'Dominican Republic', 'Guatemala', 'Macedonia, Republic of', 'Puerto Rico', 'Brazil', 'Brunei Darussalam', 'Iraq', 'Mali', 'Saint Helena', 'Bulgaria', 'Benin', 'Czech Republic', 'Indonesia', 'Suriname', 'Taiwan, Republic of China', 'Trinidad and Tobago', 'Belgium', 'British Virgin Islands', 'Burkina Faso', 'Greenland', 'Guam', 'Myanmar', 'Guinea', 'Martinique', 'Hungary', 'Norway', 'Lebanon', 'Nauru', 'Ghana', 'Guinea-Bissau', 'Ireland', 'Latvia', 'Chad', 'Germany', 'New Caledonia', 'Pakistan', 'Papua New Guinea', 'Senegal', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Heard and Mcdonald Islands', 'Republic of Kosovo', 'Togo', 'France', 'Maldives', 'Wallis and Futuna Islands', 'British Indian Ocean Territory', 'Chile', 'Cook Islands', 'Marshall Islands', 'Palau', 'Guadeloupe', 'Sao Tome and Principe', 'Uganda', 'Yemen', 'Andorra', 'Bhutan', 'Kyrgyzstan', 'Liberia', 'Mongolia', 'Zimbabwe', 'Christmas Island', 'Uruguay', 'Albania', 'Bouvet Island', 'Dominica', 'China', 'Isle of Man', 'Rwanda', 'Saint Lucia', 'Tajikistan', 'Bolivia', "Côte d'Ivoire", 'India', 'Mauritius', 'Cocos (Keeling) Islands', 'Faroe Islands', 'Equatorial Guinea', 'Portugal', 'Saint-Barthélemy', 'United Kingdom', 'Guernsey', 'Korea (North)', 'Seychelles', 'Somalia', 'Sweden']
countriesDataSet = np.array([[]])
for i in range(0, len(countries)):
    countryName = countries[i]
    #print("Currently in country: " + countryName)
    sys.stdout.write("Completed "+str(i+1/len(countries)) + "%")
    sys.stdout.write("Currently in country: " + countryName)
    for j in range(1, 5):
        sys.stdout.write("In the month: " + str(j)) #print("In the month: " + str(j))
        if(j == 1 or j == 3):
            l = 31
        elif(j == 2):
            l = 29
        else:
            l = 30
        for k in range(1, l+1): #change to l+1
            sys.stdout.write("In the day: " + str(k)) #print("In the day: " + str(k))
            if(j>10):
                finalUrl = url + countryName+urlMid+str(j)+dash+str(k)+timeVal
            else:
                finalUrl = url + countryName+urlMid+str(j)+dash+"0"+str(k)+timeVal
            response = requests.request("GET", finalUrl, headers=headers, data = payload)
            responseText = response.text
            #result=0
            resultConfirmed = responseText.find("\"Confirmed\": ")
            resultDeaths = responseText.find("\"Deaths\": ")
            resultRecovered = responseText.find("\"Recovered\": ")
            resultActive = responseText.find("\"Active\": ")
            numConfirmed = responseText[resultConfirmed+13:]
            subNumConfirmed = numConfirmed.find(",")
            subNumConfirmedText = numConfirmed[:subNumConfirmed]
            #deaths
            numDeaths = responseText[resultDeaths+10:]
            subNumDeaths = numDeaths.find(",")
            subNumDeathsText = numDeaths[:subNumDeaths]
            #recovered
            numRecovered = responseText[resultRecovered+13:]
            subNumRecovered = numRecovered.find(",")
            subNumRecoveredText = numRecovered[:subNumRecovered]
            #active
            numActive = responseText[resultActive+10:]
            subNumActive = numActive.find(",")
            subNumActiveText = numActive[:subNumActive]
            #storing in huge array
            startDate = finalUrl.find("2020")
            dateValue = finalUrl[startDate:]
            dateValue = dateValue[:len(dateValue)-len(timeVal)-1]
            t.append([countryName, subNumConfirmedText, subNumDeathsText, subNumRecoveredText, subNumActiveText, dateValue])
countriesDataSet = [list(item) for item in t]
sys.stdout.write(countriesDataSet) #print(countriesDataSet)       
            
            
