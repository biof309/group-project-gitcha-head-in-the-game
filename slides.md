% Brief Analysis of Doggo Height & Weight by Breed
% Kaite Donahue, Micaela McCall, Libby Aliberti, Mia Sievers
% 12-11-2018

# We Like Dogs
So we analyzed data about dogs 

# Our Data
![AKC](https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/10/23104658/AKC_Horizontal_1884_blue.jpg)

- American Kennel Club dataset from data.world 
- Gives lowest and highest heights and weights for each of 150 dog breeds 

# Unicode Error Importing Our Data
- Used Pandas (pd.read_csv())
- But our csv file was a "Latin1" file or a "ISO-8859-1" file
- Added an argument to our read_csv() function that included the encoding information and eliminated the error

# Our Data

# Added New Columns for Average Height and Weight

#Found Average Height
- Using np.mean(average_height), we found the average height to be 19.5 inches
- Which is equivalent to the average heights of these good bois:

#Kerry Blue Terrior
![beardbois](https://minepuppy.com/wp-content/uploads/2018/03/Kerry-Blue-Terrier-breed-silver-minepuppy.jpg)

#Chesapeake Bay Retriever
![frens](https://vetstreet.brightspotcdn.com/dims4/default/3e810eb/2147483647/crop/0x0%2B0%2B0/resize/645x380/quality/90/?url=https%3A%2F%2Fvetstreet-brightspot.s3.amazonaws.com%2F96%2F97e4009e9411e0a2380050568d634f%2Ffile%2FChesapeake-Bay-Retriever-4-645mk062111.jpg)

#Found Average Weight
- Using np.mean(average_weight), we found the average weight to be 50.35lbs
- Which is equivalent to the average weights of these doggos:

#Samoyed
![floof](https://cdn1-www.dogtime.com/assets/uploads/gallery/samoyed-dogs-and-puppies/samoyed-dogs-puppies-5.jpg)

#Dalmation
![spottyboi](https://vetstreet-brightspot.s3.amazonaws.com/ee/140380a73111e0a0d50050568d634f/file/Dalmatian-2-645mk062311.jpg)

#Chinese Shar Pei
![rollyboi](https://www2.vet.cornell.edu/sites/default/files/styles/nodecontent_default/public/Shar_pei_puppy_%28age_2_months%29.jpg?itok=qk5oS0PP)


# Generated an Exploratory Pear Plot
- Wanted to take a closer look at the scatter plot and histograms

#Scatter Plot of Average Height & Weight

#Histogram of Average Height

#Histogram of Average Weight


# I wanted a picture of a dog here
![dog](https://img.huffingtonpost.com/asset/5b7fdeab1900001d035028dc.jpeg?cache=sixpwrbb1s&ops=1910_1000)


# An interesting image from Wikipedia
![doggy](https://upload.wikimedia.org/wikipedia/commons/d/d9/Collage_of_Nine_Dogs.jpg)

# A local image
![coats](Dog_coat_variation.png)
´


