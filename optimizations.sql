
/*1*/

SELECT EXTRACT(Year FROM release_date) "Year", COUNT(release_date) "Number of Movies"
FROM movie
GROUP BY EXTRACT(Year FROM release_date)
order by "Year"

/*2*/

SELECT g.name, count(mg.movie_id) "number of genres"
from movie_genres mg, genre g
where mg.genre_id = g.id
group by g.name

/*3*/

SELECT EXTRACT(Year FROM m.release_date) "Year", g.name, count(mg.movie_id) "number of genres"
from movie_genres mg, genre g, movie m
where mg.genre_id = g.id AND mg.movie_id = m.id
group by EXTRACT(Year FROM m.release_date), g.name
order by "Year"

/*4*/

SELECT EXTRACT(Year FROM release_date) "Year", max(budget) "Movie Budget"
FROM movie
GROUP BY EXTRACT(Year FROM release_date)
order by "Year"

/*5*/

SELECT EXTRACT(Year FROM m.release_date) "Year", sum(m.revenue) "Revenue"
FROM movie m, movie_cast2 mc
where mc.movie_id = m.id and mc.name = 'Johnny Depp'
GROUP BY EXTRACT(Year FROM release_date)
order by "Year"

/*6*/

SELECT user_id, avg(rating) "avg rating"
from ratings
group by user_id
order by user_id

/*7*/

SELECT user_id "user", count(rating) "count of ratings"
from ratings
group by user_id
order by user_id

/*8*/

SELECT sum(user_id) "user", avg(rating) "count of ratings"
from ratings
group by user_id
order by sum(user_id)

/*9*/

SELECT g.name "genre name", avg(r.rating) "avg rating"
from ratings r, movie_genres mg, genre g
where r.movie_id = mg.movie_id and mg.genre_id = g.id
group by g.name
