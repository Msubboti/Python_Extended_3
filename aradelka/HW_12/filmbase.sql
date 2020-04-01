--
-- PostgreSQL database dump
--

-- Dumped from database version 10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: actor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actor (
    id integer NOT NULL,
    surname text NOT NULL,
    name text NOT NULL
);


ALTER TABLE public.actor OWNER TO postgres;

--
-- Name: actor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.actor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actor_id_seq OWNER TO postgres;

--
-- Name: actor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.actor_id_seq OWNED BY public.actor.id;


--
-- Name: correct_film_table; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.correct_film_table (
    id integer NOT NULL,
    film_year integer NOT NULL,
    film_name text NOT NULL,
    genre text NOT NULL,
    director text,
    actor text
);


ALTER TABLE public.correct_film_table OWNER TO postgres;

--
-- Name: orig_film_list; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.orig_film_list (
    id integer NOT NULL,
    release_year integer NOT NULL,
    film_title text NOT NULL,
    genre text NOT NULL,
    director_name_surname text NOT NULL,
    director_birth_year integer NOT NULL,
    actor_name_surname text NOT NULL
);


ALTER TABLE public.orig_film_list OWNER TO postgres;

--
-- Name: orig_film_list_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.orig_film_list_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.orig_film_list_id_seq OWNER TO postgres;

--
-- Name: orig_film_list_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.orig_film_list_id_seq OWNED BY public.orig_film_list.id;


--
-- Name: producer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.producer (
    id integer NOT NULL,
    surname text NOT NULL,
    name text NOT NULL,
    birth_year integer NOT NULL
);


ALTER TABLE public.producer OWNER TO postgres;

--
-- Name: producer_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.producer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.producer_id_seq OWNER TO postgres;

--
-- Name: producer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.producer_id_seq OWNED BY public.producer.id;


--
-- Name: right_film_list_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.right_film_list_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.right_film_list_id_seq OWNER TO postgres;

--
-- Name: right_film_list_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.right_film_list_id_seq OWNED BY public.correct_film_table.id;


--
-- Name: actor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actor ALTER COLUMN id SET DEFAULT nextval('public.actor_id_seq'::regclass);


--
-- Name: correct_film_table id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.correct_film_table ALTER COLUMN id SET DEFAULT nextval('public.right_film_list_id_seq'::regclass);


--
-- Name: orig_film_list id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orig_film_list ALTER COLUMN id SET DEFAULT nextval('public.orig_film_list_id_seq'::regclass);


--
-- Name: producer id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producer ALTER COLUMN id SET DEFAULT nextval('public.producer_id_seq'::regclass);


--
-- Data for Name: actor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actor (id, surname, name) FROM stdin;
1	Craig	Daniel
2	Evans	Chris
3	Merad	Kad
4	Jugnot	Gerard
5	Wood	Elijha
6	Mckellen	Ian
7	Annezeder	Nora
8	Freeman	Martin
9	Sheen	Michael
10	Tennant	David
11	Tornton	Billy Bob
12	Lillis	Sophia
13	Swinton	Tilda
14	Fenn	Sherilyn
15	Johnson	Dakota
16	Nance	Jack
\.


--
-- Data for Name: correct_film_table; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.correct_film_table (id, film_year, film_name, genre, director, actor) FROM stdin;
3	2004	The Chorus	drama	\N	\N
4	2001	lotr 1	fantasy	\N	\N
5	2002	lotr 2	fantasy	\N	\N
6	2003	lotr 3	fantasy	\N	\N
7	2012	Maniac	horror	\N	\N
8	2005	Sin City	neonoir	\N	\N
9	2013	The Hobbit 2	fantasy	\N	\N
10	2019	The Good Omens	comedy	\N	\N
11	2014	Fargo 1	crime drama	\N	\N
12	2017	Ghost stories	horror	\N	\N
13	2020	Gretel and Hansel	horror	\N	\N
14	1977	Eraserhead	horror	\N	\N
15	1993	Boxing Helena	thriller	\N	\N
16	2018	Suspiria	horror	\N	\N
2	2019	Knives Out	mystery	1	1
\.


--
-- Data for Name: orig_film_list; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orig_film_list (id, release_year, film_title, genre, director_name_surname, director_birth_year, actor_name_surname) FROM stdin;
3	2019	Knives Out	mystery	Rian Johnson	1973	Daniel Craig, Chris Evans
4	2004	The Chorus	drama	Christophe Barratier	1963	Gerard Jugnot, Kad Merad
6	2001	lotr 1	fantasy	Peter Jackson	1961	Ian Mckellen, Elijha Wood
7	2002	lotr 2	fantasy	Peter Jackson	1961	Ian Mckellen, Elijha Wood
8	2003	lotr 3	fantasy	Peter Jackson	1961	Ian Mckellen, Elijha Wood
9	2012	Maniac	horror	Frank Khalfaun	1968	Nora Annezeder, Elijha Wood
10	2005	Sin City	neonoir	Robert Rodriguez	1968	Elijha Wood
11	2013	The Hobbit 2	fantasy	Peter Jackson	1961	Ian McKellen, Martin Freeman
12	2019	The Good Omens	comedy	Douglas Mackinnon	1970	Michael Sheen, David Tennant
13	2014	Fargo 1	crime drama	Noah Hawley	1967	Billy Bob Tornton, Martin Freeman
14	2017	Ghost stories	horror	Jeremy Dyson	1966	Martin Freeman
2	2020	Gretel and Hansel	horror	Oz Perkins	1983	Sophia Lillis
15	1977	Eraserhead	horror	David Lynch	1946	Jack Nance
16	1993	Boxing Helena	thriller	Jennifer Lynch	1968	Sherilyn Fenn
17	2018	Suspiria	horror	Luca Guadagnino	1971	Tilda Swinton, Dakota Johnson
\.


--
-- Data for Name: producer; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.producer (id, surname, name, birth_year) FROM stdin;
1	Johnson	Rian	1973
2	Barratier	Cristophe	1963
3	Jackson	Peter	1961
4	Khalfaun	Frank	1968
5	Rodriguez	Robert	1961
6	Mackinnon	Douglas	1970
7	Hawley	Noah	1967
8	Dyson	Jeremy	1966
9	Perkins	Oz	1983
10	Lynch	David	1946
11	Lynch	Jennifer	1968
12	Guadagnino	Luca	1971
\.


--
-- Name: actor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.actor_id_seq', 16, true);


--
-- Name: orig_film_list_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.orig_film_list_id_seq', 17, true);


--
-- Name: producer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.producer_id_seq', 12, true);


--
-- Name: right_film_list_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.right_film_list_id_seq', 18, true);


--
-- PostgreSQL database dump complete
--

