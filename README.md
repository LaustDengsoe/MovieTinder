# MovieTinder

## what is this?
This is MovieTinder, you create an a account, login in, at the homepage movies 
wil be represented to you witch you can like or dislike. In the top action bar 
you can see your liked movies under 'Likes', you can add friends(other accounts created on you local machine) under 'Friends',
change your account details under 'Account', logout and see which movies both you and your friends like under
'Matches'. 

The E/R diagram for the project is under 

## How to run

# step 1
Change the PATH to movies_shaved.csv in the file schema.sql to where you have it on your local machine(FULL PATH), the file movies_shaved.csv is a cut down version of the full data set movies.csv both of these files can be found in the folder 'static'. 

# step 2
Setting up the database, to create all the need tables run in terminal 'psql -d{database} -U{user} -W -f schema.sql' and then run '\i schema.sql'. Make sure to be inside the folder inner most MovieTinder folder. 

To use the example accounts we made run in terminal 'psql -d site -U postgres -W -f .\schema_ins.sql', still inside the inner most MovieTinder folder.

# step 3
Change the password for the psql user postgres under '__init__.py' to your own personal password. 

# step 4 
Run in terminal 'python run.py' and the app should run! else refer step 1, 2 and 3.

## What to do with MovieTinder

We have created 3 users 'Holger69', 'MIkkel420' and 'Laust42' with the Password: '123'. Each user have liked 15 movies and disliked 10 movies. 
# for you to do:
Login in to 'Holger69' and add 'Laust42' as a friend and se under 'Matches' to see the movies they both like.

Login to 'Mikkel420' and remove 'Holger69' as a friend under 'Friends'

Login in to 'Holger69' and remove the like under 'Likes' from "The dark knight", and check that it is no longer under 'Matches' with 'Mikkel420'

Create your own account and have a look around!

