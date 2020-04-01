select * from orig_film_list;

select film_title, genre from orig_film_list where actor_name_surname like '%Wood%';

select genre, count(genre) from orig_film_list group by genre;



select distinct director_name_surname from orig_film_list;


select release_year, film_title from orig_film_list order by release_year desc;

select release_year, film_title from orig_film_list where director_name_surname like '%Lynch' order by release_year desc;

select release_year, film_title from orig_film_list where release_year >=2000 order by release_year asc;

 select release_year, film_title from orig_film_list where release_year >=2000 order by release_year asc limit 5;

select release_year, film_title from orig_film_list where release_year >=2000 order by release_year asc limit 5 offset 1;

select release_year, film_title from orig_film_list where release_year >=2000 order by release_year asc fetch first 6 rows only;

select film_title, actor_name_surname from orig_film_list where actor_name_surname like '%in%';

