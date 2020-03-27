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
    name text NOT NULL,
    birth_year integer NOT NULL
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
-- Name: orig_film_list; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.orig_film_list (
    id integer NOT NULL,
    film_year integer NOT NULL,
    film_name text NOT NULL,
    genre text NOT NULL,
    producer_name_surname text NOT NULL,
    producer_birth_year integer NOT NULL,
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
-- Name: right_film_list; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.right_film_list (
    id integer NOT NULL,
    film_year integer NOT NULL,
    film_name text NOT NULL,
    genre text NOT NULL,
    producer integer NOT NULL,
    actor text NOT NULL
);


ALTER TABLE public.right_film_list OWNER TO postgres;

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

ALTER SEQUENCE public.right_film_list_id_seq OWNED BY public.right_film_list.id;


--
-- Name: actor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actor ALTER COLUMN id SET DEFAULT nextval('public.actor_id_seq'::regclass);


--
-- Name: orig_film_list id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orig_film_list ALTER COLUMN id SET DEFAULT nextval('public.orig_film_list_id_seq'::regclass);


--
-- Name: producer id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producer ALTER COLUMN id SET DEFAULT nextval('public.producer_id_seq'::regclass);


--
-- Name: right_film_list id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.right_film_list ALTER COLUMN id SET DEFAULT nextval('public.right_film_list_id_seq'::regclass);


--
-- Data for Name: actor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actor (id, surname, name, birth_year) FROM stdin;
\.


--
-- Data for Name: orig_film_list; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orig_film_list (id, film_year, film_name, genre, producer_name_surname, producer_birth_year, actor_name_surname) FROM stdin;
\.


--
-- Data for Name: producer; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.producer (id, surname, name, birth_year) FROM stdin;
\.


--
-- Data for Name: right_film_list; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.right_film_list (id, film_year, film_name, genre, producer, actor) FROM stdin;
\.


--
-- Name: actor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.actor_id_seq', 1, false);


--
-- Name: orig_film_list_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.orig_film_list_id_seq', 1, false);


--
-- Name: producer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.producer_id_seq', 1, false);


--
-- Name: right_film_list_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.right_film_list_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

