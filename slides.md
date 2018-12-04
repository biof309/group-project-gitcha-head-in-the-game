% Brief Analysis of Doggo Height & Weight by Breed
% Kaite Donahue, Micaela McCall, Libby Aliberti, Mia Sievers
% 12-11-2018

# We Like Dogs
So we analyzed data about dogs 

#Our Data
![AKC](https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/10/23104658/AKC_Horizontal_1884_blue.jpg)

- American Kennel Club dataset from data.world 
- Gives lowest and highest heights and weights for each of 150 dog breeds 

#Unicode Error Importing Our Data
- Used Pandas (pd.read.csv)
- But our csv file was a "Latin1" file or a "ISO-8859-1" file
- Converted to UTF-8, the standard file type 

#Our Data
dogs = pd.read_csv('https://query.data.world/s/wb2m35hoycwvieh3455mrac6l5ewjs', encoding="ISO-8859-1")


# I wanted a picture of a dog here
![dog](https://img.huffingtonpost.com/asset/5b7fdeab1900001d035028dc.jpeg?cache=sixpwrbb1s&ops=1910_1000)


# An interesting image from Wikipedia
![doggy](https://upload.wikimedia.org/wikipedia/commons/d/d9/Collage_of_Nine_Dogs.jpg)

# A local image
![coats](Dog_coat_variation.png)



