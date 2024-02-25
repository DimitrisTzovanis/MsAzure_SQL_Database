import psycopg2
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

# Update connection string information
host = "floppyfish.postgres.database.azure.com"
dbname = "postgres"
user = "examiner@floppyfish"
password = "Aueb555"
sslmode = "require"

# Construct connection string


conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()

x = []
y = []

xVal = []
yVal = []
zVal = []


#1

cursor.execute('SELECT EXTRACT(Year FROM release_date)"year" , COUNT(release_date)  FROM movie GROUP BY EXTRACT(Year FROM release_date) order by "year";')
row = cursor.fetchone()
while row:
    x.append(str(row[0]))
    y.append(row[1])
    row = cursor.fetchone() 
plt.xlabel('year')
plt.ylabel('number of movies')
plt.bar(x,y)
plt.show()

x = []
y = []


#2

cursor.execute('SELECT g.name, count(mg.movie_id) from movie_genres mg, genre g where mg.genre_id = g.id group by g.name;')
row = cursor.fetchone()
while row:
    x.append(str(row[0]))
    y.append(row[1])
    row = cursor.fetchone() 
plt.xlabel('genre')
plt.ylabel('number of movies')
plt.bar(x,y)
plt.show()


x = []
y = []


#3

cursor.execute('SELECT g.name, EXTRACT(Year FROM m.release_date) "Year", count(mg.movie_id) "number of genres" from movie_genres mg, genre g, movie m where mg.genre_id = g.id AND mg.movie_id = m.id AND EXTRACT(Year FROM m.release_date) <2014 group by EXTRACT(Year FROM m.release_date), g.name order by "Year";')
row = cursor.fetchone()
while row:
    if(row[1]!="None" and row[1]!= 'None' and row[1]!=None):
        xVal.append(str(row[0]))
        yVal.append(int(row[1]))
        zVal.append(int(row[2]))
    row = cursor.fetchone()
# Initializing Figure
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
ax1.set_facecolor((1.0, 1.0, 1.0))
# Creating a dictionary from categories to x-axis coordinates
xCategories = xVal
i=0
xDict = {}
x=[]
for category in xCategories:
  if category not in xDict:
    xDict[category]=i
    x.append(i)
    i+=1
  else:
    x.append(xDict[category])
# Defining the starting position of each bar (x is already defined)
z = np.zeros(len(x))
# Defining the length/width/height of each bar.
dx = np.ones(len(x))*0.1
dy = np.ones(len(x))
dz = zVal
ax1.bar3d(x, yVal, z, dx, dy, dz)
ax1.set_zlim([0, max(zVal)])
plt.xticks(range(len(xDict.values())), xDict.keys())
plt.show()




x = []
y = []

#4

cursor.execute('SELECT EXTRACT(Year FROM release_date) "Year", max(budget) "Movie Budget" FROM movie GROUP BY EXTRACT(Year FROM release_date) order by "Year";')
row = cursor.fetchone()
while row:
    x.append(str(row[0]))
    y.append(row[1])
    row = cursor.fetchone() 
plt.xlabel('year')
plt.ylabel('max movie budget')
plt.bar(x,y)
plt.show()

x = []
y = []

#5

cursor.execute("SELECT EXTRACT(Year FROM m.release_date), sum(m.revenue)  FROM movie m, movie_cast2 mc where mc.movie_id = m.id and mc.name = 'Johnny Depp' GROUP BY EXTRACT(Year FROM release_date) order by EXTRACT(Year FROM m.release_date);")
row = cursor.fetchone()
while row:
    x.append(str(row[0]))
    y.append(int(row[1]))
    row = cursor.fetchone() 
plt.xlabel('year')
plt.ylabel('movies of johnny depp')
plt.bar(x,y)
plt.show()


x = []
y = []

#6

cursor.execute('SELECT user_id, avg(rating) "avg rating" from ratings group by user_id order by user_id;')
row = cursor.fetchone()
while row:
    x.append(str(row[0]))
    y.append(row[1])
    row = cursor.fetchone() 
plt.xlabel('user')
plt.ylabel('avg rating')
plt.scatter(x, y,s=1)
plt.show()


x = []
y = []

#7

cursor.execute('SELECT user_id "user", count(rating) "count of ratings" from ratings group by user_id order by user_id;')
row = cursor.fetchone()
while row:
    x.append(str(row[0]))
    y.append(row[1])
    row = cursor.fetchone() 
plt.xlabel('user')
plt.ylabel('sum of ratings')
plt.scatter(x, y,s=1)
plt.show()


x = []
y = []

#8

cursor.execute('SELECT sum(user_id) "user", avg(rating) "count of ratings" from ratings group by user_id order by sum(user_id);')
row = cursor.fetchone()
while row:
    x.append(str(row[0]))
    y.append(row[1])
    row = cursor.fetchone() 
plt.xlabel('sum of ratings')
plt.ylabel('avg ratings')
plt.scatter(x, y,s=1)
plt.show()


x = []
y = []

#9

cursor.execute('SELECT g.name "genre name", avg(r.rating) "avg rating" from ratings r, movie_genres mg, genre g where r.movie_id = mg.movie_id and mg.genre_id = g.id group by g.name;')
row = cursor.fetchone()
while row:
    x.append(str(row[0]))
    y.append(row[1])
    row = cursor.fetchone() 
plt.xlabel('genre')
plt.ylabel('avg rating')
plt.bar(x,y)
plt.show()





# Clean up
            
cursor = conn.cursor()

conn.commit()
cursor.close()
conn.close()
