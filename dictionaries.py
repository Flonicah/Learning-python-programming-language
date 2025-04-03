#dictionaries in python
# special structure for storing ky value pairs to be accessed using the key
#jan-> january convertions
#mar -> march etc

print("Dictionaries in python MONTH CONVERTION")
print()
monthConversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" :"April",
    "May" :"May",
    "Jun" :"June",
    "Jul" :"July",
    "Aug" :"August",
    "Sep" :"September",
    "Oct" :"Octeber",
    "Nov" :"November", 
    "Dec" :"December"
    }

#accessing a specific value
print(monthConversions["Mar"])
print()
print(monthConversions.get("Dec"))#used a get function
#trying a invalid key
print()
print(monthConversions.get("LUV","Not a valid key"))
# the keys can be number as well


