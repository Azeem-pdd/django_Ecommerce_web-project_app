--
-- PostgreSQL database dump
--

-- Dumped from database version 12.4
-- Dumped by pg_dump version 12.4

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO postgres;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: store_catagory; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.store_catagory (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.store_catagory OWNER TO postgres;

--
-- Name: store_catagory_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.store_catagory_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.store_catagory_id_seq OWNER TO postgres;

--
-- Name: store_catagory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.store_catagory_id_seq OWNED BY public.store_catagory.id;


--
-- Name: store_customer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.store_customer (
    id integer NOT NULL,
    first_name character varying(200) NOT NULL,
    last_name character varying(200) NOT NULL,
    email character varying(254) NOT NULL,
    phno bigint NOT NULL,
    password character varying(200) NOT NULL,
    confirm_password character varying(200) NOT NULL
);


ALTER TABLE public.store_customer OWNER TO postgres;

--
-- Name: store_customer_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.store_customer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.store_customer_id_seq OWNER TO postgres;

--
-- Name: store_customer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.store_customer_id_seq OWNED BY public.store_customer.id;


--
-- Name: store_order; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.store_order (
    id integer NOT NULL,
    date timestamp with time zone NOT NULL,
    price integer NOT NULL,
    customer_id integer NOT NULL,
    address character varying(100) NOT NULL,
    phno bigint NOT NULL,
    shipping_address character varying(100) NOT NULL,
    name character varying(20) NOT NULL,
    name_additional character varying(20),
    phno_additional bigint,
    email character varying(254) NOT NULL,
    payment_method_id integer NOT NULL,
    order_status character varying(20) NOT NULL
);


ALTER TABLE public.store_order OWNER TO postgres;

--
-- Name: store_order_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.store_order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.store_order_id_seq OWNER TO postgres;

--
-- Name: store_order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.store_order_id_seq OWNED BY public.store_order.id;


--
-- Name: store_order_products; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.store_order_products (
    id integer NOT NULL,
    order_id integer NOT NULL,
    products_id integer NOT NULL
);


ALTER TABLE public.store_order_products OWNER TO postgres;

--
-- Name: store_order_products_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.store_order_products_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.store_order_products_id_seq OWNER TO postgres;

--
-- Name: store_order_products_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.store_order_products_id_seq OWNED BY public.store_order_products.id;


--
-- Name: store_orderproduct; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.store_orderproduct (
    id integer NOT NULL,
    quantity integer NOT NULL,
    order_id integer NOT NULL,
    product_id integer NOT NULL
);


ALTER TABLE public.store_orderproduct OWNER TO postgres;

--
-- Name: store_orderproduct_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.store_orderproduct_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.store_orderproduct_id_seq OWNER TO postgres;

--
-- Name: store_orderproduct_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.store_orderproduct_id_seq OWNED BY public.store_orderproduct.id;


--
-- Name: store_payment_method; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.store_payment_method (
    id integer NOT NULL,
    name character varying(20) NOT NULL
);


ALTER TABLE public.store_payment_method OWNER TO postgres;

--
-- Name: store_payment_method_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.store_payment_method_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.store_payment_method_id_seq OWNER TO postgres;

--
-- Name: store_payment_method_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.store_payment_method_id_seq OWNED BY public.store_payment_method.id;


--
-- Name: store_products; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.store_products (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    "desc" character varying(200) NOT NULL,
    img character varying(100) NOT NULL,
    price integer NOT NULL,
    catagory_id integer NOT NULL,
    quantity integer NOT NULL,
    date timestamp with time zone NOT NULL,
    no_of_visits integer NOT NULL,
    featured boolean NOT NULL,
    CONSTRAINT store_products_no_of_visits_check CHECK ((no_of_visits >= 0))
);


ALTER TABLE public.store_products OWNER TO postgres;

--
-- Name: store_products_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.store_products_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.store_products_id_seq OWNER TO postgres;

--
-- Name: store_products_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.store_products_id_seq OWNED BY public.store_products.id;


--
-- Name: store_profile; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.store_profile (
    id integer NOT NULL,
    name character varying(20) NOT NULL,
    profession character varying(20) NOT NULL,
    img character varying(100),
    job_position character varying(40) NOT NULL,
    customer_id integer NOT NULL,
    home_address text NOT NULL,
    phno bigint NOT NULL,
    postal_address text NOT NULL,
    shipping_address text NOT NULL,
    zip_code integer
);


ALTER TABLE public.store_profile OWNER TO postgres;

--
-- Name: store_profile_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.store_profile_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.store_profile_id_seq OWNER TO postgres;

--
-- Name: store_profile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.store_profile_id_seq OWNED BY public.store_profile.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: store_catagory id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_catagory ALTER COLUMN id SET DEFAULT nextval('public.store_catagory_id_seq'::regclass);


--
-- Name: store_customer id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_customer ALTER COLUMN id SET DEFAULT nextval('public.store_customer_id_seq'::regclass);


--
-- Name: store_order id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_order ALTER COLUMN id SET DEFAULT nextval('public.store_order_id_seq'::regclass);


--
-- Name: store_order_products id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_order_products ALTER COLUMN id SET DEFAULT nextval('public.store_order_products_id_seq'::regclass);


--
-- Name: store_orderproduct id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_orderproduct ALTER COLUMN id SET DEFAULT nextval('public.store_orderproduct_id_seq'::regclass);


--
-- Name: store_payment_method id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_payment_method ALTER COLUMN id SET DEFAULT nextval('public.store_payment_method_id_seq'::regclass);


--
-- Name: store_products id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_products ALTER COLUMN id SET DEFAULT nextval('public.store_products_id_seq'::regclass);


--
-- Name: store_profile id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_profile ALTER COLUMN id SET DEFAULT nextval('public.store_profile_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add catagory	1	add_catagory
2	Can change catagory	1	change_catagory
3	Can delete catagory	1	delete_catagory
4	Can view catagory	1	view_catagory
5	Can add customer	2	add_customer
6	Can change customer	2	change_customer
7	Can delete customer	2	delete_customer
8	Can view customer	2	view_customer
9	Can add products	3	add_products
10	Can change products	3	change_products
11	Can delete products	3	delete_products
12	Can view products	3	view_products
13	Can add order	4	add_order
14	Can change order	4	change_order
15	Can delete order	4	delete_order
16	Can view order	4	view_order
17	Can add log entry	5	add_logentry
18	Can change log entry	5	change_logentry
19	Can delete log entry	5	delete_logentry
20	Can view log entry	5	view_logentry
21	Can add permission	6	add_permission
22	Can change permission	6	change_permission
23	Can delete permission	6	delete_permission
24	Can view permission	6	view_permission
25	Can add group	7	add_group
26	Can change group	7	change_group
27	Can delete group	7	delete_group
28	Can view group	7	view_group
29	Can add user	8	add_user
30	Can change user	8	change_user
31	Can delete user	8	delete_user
32	Can view user	8	view_user
33	Can add content type	9	add_contenttype
34	Can change content type	9	change_contenttype
35	Can delete content type	9	delete_contenttype
36	Can view content type	9	view_contenttype
37	Can add session	10	add_session
38	Can change session	10	change_session
39	Can delete session	10	delete_session
40	Can view session	10	view_session
41	Can add profile	11	add_profile
42	Can change profile	11	change_profile
43	Can delete profile	11	delete_profile
44	Can view profile	11	view_profile
45	Can add payment_method	12	add_payment_method
46	Can change payment_method	12	change_payment_method
47	Can delete payment_method	12	delete_payment_method
48	Can view payment_method	12	view_payment_method
49	Can add order product	13	add_orderproduct
50	Can change order product	13	change_orderproduct
51	Can delete order product	13	delete_orderproduct
52	Can view order product	13	view_orderproduct
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$216000$OXVKu75rI5X9$Jpa9gC8kZpN/Phjgc8vRXy77e4s/CdtgPpxQ5I+O2dg=	2021-09-16 20:10:13.947036+05	t	azeem			mazeemakramnns@gmail.com	t	t	2021-04-22 10:11:59.771889+05
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2021-04-22 10:12:55.404117+05	1	Catagory object (1)	1	[{"added": {}}]	1	1
2	2021-04-22 10:13:17.691939+05	2	Catagory object (2)	1	[{"added": {}}]	1	1
3	2021-04-22 10:13:33.042752+05	3	Catagory object (3)	1	[{"added": {}}]	1	1
4	2021-04-22 10:23:18.599785+05	1	Products object (1)	1	[{"added": {}}]	3	1
5	2021-04-22 10:31:54.421074+05	2	Products object (2)	1	[{"added": {}}]	3	1
6	2021-04-22 10:36:18.308201+05	3	Products object (3)	1	[{"added": {}}]	3	1
7	2021-04-22 11:02:17.837073+05	4	Catagory object (4)	1	[{"added": {}}]	1	1
8	2021-04-22 11:02:33.203669+05	5	Catagory object (5)	1	[{"added": {}}]	1	1
9	2021-04-22 11:24:03.732664+05	1	Products object (1)	2	[{"changed": {"fields": ["Price"]}}]	3	1
10	2021-04-22 11:24:11.420433+05	2	Products object (2)	2	[{"changed": {"fields": ["Price"]}}]	3	1
11	2021-04-22 11:38:34.592432+05	1	Products object (1)	2	[]	3	1
12	2021-04-22 11:40:40.514225+05	1	Products object (1)	2	[{"changed": {"fields": ["Name"]}}]	3	1
13	2021-04-22 11:59:12.314107+05	4	Products object (4)	1	[{"added": {}}]	3	1
14	2021-04-22 12:02:00.532988+05	5	Products object (5)	1	[{"added": {}}]	3	1
15	2021-04-22 12:06:22.493924+05	6	Products object (6)	1	[{"added": {}}]	3	1
16	2021-04-22 14:11:28.705858+05	7	Products object (7)	1	[{"added": {}}]	3	1
17	2021-04-22 14:14:38.133167+05	8	Products object (8)	1	[{"added": {}}]	3	1
18	2021-04-22 14:19:16.703573+05	9	Products object (9)	1	[{"added": {}}]	3	1
19	2021-04-23 15:32:23.617362+05	5	Customer object (5)	3		2	1
20	2021-05-16 09:12:28.98717+05	6	Catagory object (6)	1	[{"added": {}}]	1	1
21	2021-05-16 09:16:22.807492+05	10	Products object (10)	1	[{"added": {}}]	3	1
22	2021-05-16 09:19:14.137704+05	11	Products object (11)	1	[{"added": {}}]	3	1
23	2021-05-16 09:24:13.267578+05	12	Products object (12)	1	[{"added": {}}]	3	1
24	2021-05-16 09:25:48.050594+05	13	Products object (13)	1	[{"added": {}}]	3	1
25	2021-05-16 09:26:40.233455+05	14	Products object (14)	1	[{"added": {}}]	3	1
26	2021-08-13 08:40:13.49729+05	1	Order object (1)	1	[{"added": {}}]	4	1
27	2021-08-13 08:42:00.784838+05	1	Order object (1)	2	[{"changed": {"fields": ["Customer"]}}]	4	1
28	2021-08-15 17:40:00.163494+05	14	Products object (14)	2	[{"changed": {"fields": ["Date"]}}]	3	1
29	2021-08-15 17:41:00.780501+05	14	Products object (14)	2	[{"changed": {"fields": ["Date"]}}]	3	1
30	2021-08-16 14:44:19.729691+05	14	Products object (14)	2	[{"changed": {"fields": ["Date"]}}]	3	1
31	2021-08-16 14:44:59.765453+05	14	Products object (14)	2	[{"changed": {"fields": ["Date"]}}]	3	1
32	2021-08-16 14:45:41.811123+05	14	Products object (14)	2	[{"changed": {"fields": ["Date"]}}]	3	1
33	2021-08-16 14:47:05.012615+05	14	Products object (14)	2	[]	3	1
34	2021-08-16 14:47:23.520655+05	13	Products object (13)	2	[{"changed": {"fields": ["Date"]}}]	3	1
35	2021-08-16 14:47:31.899955+05	12	Products object (12)	2	[{"changed": {"fields": ["Date"]}}]	3	1
36	2021-08-16 14:47:42.337343+05	11	Products object (11)	2	[{"changed": {"fields": ["Date"]}}]	3	1
37	2021-08-16 14:47:53.659647+05	10	Products object (10)	2	[{"changed": {"fields": ["Date"]}}]	3	1
38	2021-08-16 14:48:05.22026+05	9	Products object (9)	2	[{"changed": {"fields": ["Date"]}}]	3	1
39	2021-08-16 14:48:15.45987+05	8	Products object (8)	2	[{"changed": {"fields": ["Date"]}}]	3	1
40	2021-08-16 14:48:30.300434+05	7	Products object (7)	2	[{"changed": {"fields": ["Date"]}}]	3	1
41	2021-08-16 15:08:27.7431+05	14	women white special dress	3		3	1
42	2021-08-16 15:27:40.757305+05	2	black colored  T-shirt	1	[{"added": {}}]	4	1
43	2021-08-16 15:30:35.624049+05	2	black colored  T-shirt	2	[{"changed": {"fields": ["Customer"]}}]	4	1
44	2021-08-16 15:31:03.070028+05	1		3		4	1
45	2021-08-17 12:04:09.434236+05	7	younasmughal	3		2	1
46	2021-08-18 12:12:29.196708+05	1	Muhammad Azeem Akram	1	[{"added": {}}]	11	1
47	2021-08-18 12:25:45.323332+05	1	azeem akram	3		2	1
48	2021-08-18 12:54:19.32573+05	1	Muhammad Azeem Akram	3		11	1
49	2021-08-18 13:12:39.55309+05	3	Muhammad Azeem Akram	3		11	1
50	2021-08-18 13:18:07.813881+05	4	Muhammad Azeem Akram	3		11	1
51	2021-08-18 13:25:47.429996+05	5	Muhammad Azeem Akram	3		11	1
52	2021-08-18 13:28:27.508988+05	6	Muhammad Azeem Akram	3		11	1
53	2021-08-18 13:31:07.017464+05	7	Muhammad Azeem Akram	3		11	1
54	2021-08-18 13:34:27.83304+05	8	Muhammad Azeem Akram	3		11	1
55	2021-08-18 13:36:13.480681+05	9	Muhammad Azeem Akram	3		11	1
56	2021-08-18 13:38:22.293562+05	10	Muhammad Azeem Akram	3		11	1
57	2021-08-18 13:39:04.48002+05	11	Muhammad Azeem Akram	1	[{"added": {}}]	11	1
58	2021-08-18 13:43:58.663869+05	11	Muhammad Azeem Akram	3		11	1
59	2021-08-18 19:08:39.566032+05	12	Muhammad Azeem Akram	3		11	1
60	2021-08-18 19:17:51.690587+05	13	Muhammad Azeem Akram	2	[{"changed": {"fields": ["Img"]}}]	11	1
61	2021-08-18 19:22:53.369921+05	13	Muhammad Azeem Akram	2	[{"changed": {"fields": ["Img"]}}]	11	1
62	2021-08-18 19:24:36.780033+05	13	Muhammad Azeem Akram	2	[{"changed": {"fields": ["Img"]}}]	11	1
63	2021-08-18 19:26:09.065905+05	13	Muhammad Azeem Akram	2	[{"changed": {"fields": ["Img"]}}]	11	1
64	2021-08-18 19:59:45.248269+05	13	Muhammad Azeem Akram	2	[{"changed": {"fields": ["Img"]}}]	11	1
65	2021-08-20 11:02:51.071737+05	14	younas Mughal	2	[{"changed": {"fields": ["Img"]}}]	11	1
66	2021-08-20 11:11:35.352072+05	14	younas Mughal	2	[{"changed": {"fields": ["Img"]}}]	11	1
67	2021-08-20 11:11:54.804226+05	14	younas Mughal	2	[{"changed": {"fields": ["Img"]}}]	11	1
68	2021-08-20 11:56:40.473865+05	14	younas Mughal	3		11	1
69	2021-08-21 10:40:45.646462+05	20	younas Mughal	2	[{"changed": {"fields": ["Img"]}}]	11	1
70	2021-08-21 10:45:40.492102+05	20	younas Mughal	3		11	1
71	2021-08-21 13:31:48.564785+05	2	black colored  T-shirt	3		4	1
72	2021-08-22 09:12:40.222776+05	1	Cash-on Delivery	1	[{"added": {}}]	12	1
73	2021-08-22 09:12:53.485829+05	2	jazz_cash	1	[{"added": {}}]	12	1
74	2021-08-22 09:45:05.415712+05	22	younas Mughal	3		11	1
75	2021-08-22 11:59:15.915363+05	3	faisal	3		4	1
76	2021-08-22 12:02:19.591495+05	5		3		4	1
77	2021-08-22 12:03:23.113164+05	6		3		4	1
78	2021-08-22 12:05:21.557344+05	7	younas Mughal	3		4	1
79	2021-08-22 13:26:56.177624+05	8	azeem akram	3		4	1
80	2021-08-22 13:27:27.795607+05	4	younas Mughal	3		4	1
81	2021-08-22 17:11:58.964848+05	10	azeem akram	3		4	1
82	2021-08-22 17:11:58.980834+05	9	azeem akram	3		4	1
83	2021-08-23 10:23:00.965647+05	6	Recent	3		1	1
84	2021-08-23 10:23:00.973669+05	5	New Arrivals	3		1	1
85	2021-08-23 10:23:00.981627+05	4	Best Selling	3		1	1
86	2021-08-25 19:38:08.229623+05	1	american accent dress shirt	2	[{"changed": {"fields": ["Featured"]}}]	3	1
87	2021-08-25 19:38:18.283302+05	1	american accent dress shirt	2	[]	3	1
88	2021-08-25 19:38:25.025352+05	1	american accent dress shirt	2	[]	3	1
89	2021-08-25 19:38:34.891508+05	3	fancy design dress shirt	2	[{"changed": {"fields": ["Featured"]}}]	3	1
90	2021-08-25 19:38:43.282288+05	8	offshore red dress	2	[{"changed": {"fields": ["Featured"]}}]	3	1
91	2021-08-25 19:38:53.433453+05	9	balck short with lightblue jeans	2	[{"changed": {"fields": ["Featured"]}}]	3	1
92	2021-08-25 19:39:32.008108+05	8	offshore red dress	2	[]	3	1
93	2021-08-25 19:42:12.060859+05	2	Multi-colored dress shirt	2	[{"changed": {"fields": ["Featured"]}}]	3	1
94	2021-08-25 20:21:54.360464+05	9	black short with lightblue jeans	2	[{"changed": {"fields": ["Name"]}}]	3	1
95	2021-08-26 13:25:06.739797+05	23	fancy design dress shirt	3		13	1
96	2021-08-26 13:25:06.755794+05	22	american accent dress shirt	3		13	1
97	2021-08-26 13:25:06.755794+05	21	black short with lightblue jeans	3		13	1
98	2021-08-26 13:25:06.755794+05	20	Multi-colored dress shirt	3		13	1
99	2021-08-26 13:25:06.763775+05	19	white sleeky dress	3		13	1
100	2021-08-26 13:25:06.763775+05	18	offshore red dress	3		13	1
101	2021-08-26 13:25:06.763775+05	17	fancy design dress shirt	3		13	1
102	2021-08-26 13:25:06.763775+05	16	american accent dress shirt	3		13	1
103	2021-08-26 13:25:06.763775+05	15	black colored  T-shirt	3		13	1
104	2021-08-26 13:25:06.771787+05	14	american accent dress shirt	3		13	1
105	2021-08-26 13:25:06.771787+05	13	white sleeky dress	3		13	1
106	2021-08-26 13:25:06.771787+05	12	fancy design dress shirt	3		13	1
107	2021-08-26 13:25:06.771787+05	11	fancy design dress shirt	3		13	1
108	2021-08-26 13:25:06.771787+05	10	fancy design dress shirt	3		13	1
109	2021-08-26 13:25:06.771787+05	9	fancy design dress shirt	3		13	1
110	2021-08-26 13:25:06.780366+05	8	fancy design dress shirt	3		13	1
111	2021-08-26 13:25:06.780366+05	7	fancy design dress shirt	3		13	1
112	2021-08-26 13:25:06.780366+05	5	black short with lightblue jeans	3		13	1
113	2021-08-26 13:25:06.780366+05	3	black short with lightblue jeans	3		13	1
114	2021-08-26 13:25:06.780366+05	1	black short with lightblue jeans	3		13	1
115	2021-08-26 13:25:36.975494+05	24	younas mughal	3		4	1
116	2021-08-26 13:25:36.975494+05	23	younas mughal	3		4	1
117	2021-08-26 13:25:36.983494+05	22	younas mughal	3		4	1
118	2021-08-26 13:25:36.983494+05	21	younas mughal	3		4	1
119	2021-08-26 13:25:36.983494+05	20	younas mughal	3		4	1
120	2021-08-26 13:25:36.983494+05	19	younas mughal	3		4	1
121	2021-08-26 13:25:36.983494+05	18	younas mughal	3		4	1
122	2021-08-26 13:25:36.991496+05	17	younas mughal	3		4	1
123	2021-08-26 13:25:36.991496+05	16	younas mughal	3		4	1
124	2021-08-26 13:25:36.991496+05	15	younas mughal	3		4	1
125	2021-08-26 13:25:36.991496+05	14	azeem akram	3		4	1
126	2021-08-26 13:25:36.991496+05	13	azeem akram	3		4	1
127	2021-08-26 13:25:36.991496+05	12	azeem akram	3		4	1
128	2021-08-26 13:25:36.999493+05	11	azeem akram	3		4	1
129	2021-08-26 13:27:06.849963+05	25	younas mughal	3		4	1
130	2021-08-26 14:03:54.854223+05	26	younas mughal	2	[{"changed": {"fields": ["Shipping address", "Completed"]}}]	4	1
131	2021-08-26 14:19:23.632691+05	30	younas mughal	3		4	1
132	2021-08-26 14:19:23.640709+05	29	younas mughal	3		4	1
133	2021-08-26 14:19:23.640709+05	28	younas mughal	3		4	1
134	2021-08-26 14:19:23.640709+05	27	younas mughal	3		4	1
135	2021-08-26 15:02:34.092217+05	26	younas mughal	2	[{"changed": {"fields": ["Order status"]}}]	4	1
136	2021-08-26 15:05:43.787959+05	26	younas mughal	2	[{"changed": {"fields": ["Order status"]}}]	4	1
137	2021-08-26 15:08:15.506517+05	26	younas mughal	2	[{"changed": {"fields": ["Order status"]}}]	4	1
138	2021-08-26 15:08:24.051879+05	26	younas mughal	2	[{"changed": {"fields": ["Order status"]}}]	4	1
139	2021-08-26 17:39:14.438925+05	8	azeem akram	2	[{"changed": {"fields": ["Email"]}}]	2	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	store	catagory
2	store	customer
3	store	products
4	store	order
5	admin	logentry
6	auth	permission
7	auth	group
8	auth	user
9	contenttypes	contenttype
10	sessions	session
11	store	profile
12	store	payment_method
13	store	orderproduct
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2021-04-22 10:09:51.30819+05
2	auth	0001_initial	2021-04-22 10:09:51.444178+05
3	admin	0001_initial	2021-04-22 10:09:51.580168+05
4	admin	0002_logentry_remove_auto_add	2021-04-22 10:09:51.612162+05
5	admin	0003_logentry_add_action_flag_choices	2021-04-22 10:09:51.636161+05
6	contenttypes	0002_remove_content_type_name	2021-04-22 10:09:51.684155+05
7	auth	0002_alter_permission_name_max_length	2021-04-22 10:09:51.708153+05
8	auth	0003_alter_user_email_max_length	2021-04-22 10:09:51.732152+05
9	auth	0004_alter_user_username_opts	2021-04-22 10:09:51.756151+05
10	auth	0005_alter_user_last_login_null	2021-04-22 10:09:51.77215+05
11	auth	0006_require_contenttypes_0002	2021-04-22 10:09:51.780148+05
12	auth	0007_alter_validators_add_error_messages	2021-04-22 10:09:51.804146+05
13	auth	0008_alter_user_username_max_length	2021-04-22 10:09:51.844159+05
14	auth	0009_alter_user_last_name_max_length	2021-04-22 10:09:51.86814+05
15	auth	0010_alter_group_name_max_length	2021-04-22 10:09:51.892139+05
16	auth	0011_update_proxy_permissions	2021-04-22 10:09:51.916136+05
17	auth	0012_alter_user_first_name_max_length	2021-04-22 10:09:51.940133+05
18	sessions	0001_initial	2021-04-22 10:09:51.964131+05
19	store	0001_initial	2021-04-22 10:09:52.044122+05
20	store	0002_remove_products_catagory	2021-04-22 10:09:52.116116+05
21	store	0003_auto_20210421_1805	2021-04-22 10:09:52.156112+05
22	store	0004_auto_20210421_1831	2021-04-22 10:09:52.260102+05
23	store	0005_catagory_customer_order_products	2021-04-22 10:09:52.348094+05
24	store	0006_auto_20210421_1839	2021-04-22 10:09:52.388093+05
25	store	0007_auto_20210422_0954	2021-04-22 10:09:52.420089+05
26	store	0008_auto_20210422_0956	2021-04-22 10:09:52.444087+05
27	store	0009_remove_products_catagory	2021-04-22 10:09:52.468085+05
28	store	0010_auto_20210422_1005	2021-04-22 10:09:52.500082+05
29	store	0011_auto_20210422_1014	2021-04-22 10:14:44.054279+05
30	store	0012_auto_20210423_1132	2021-04-23 11:32:20.659761+05
31	store	0013_auto_20210423_1134	2021-04-23 11:34:26.380748+05
32	store	0014_auto_20210423_1140	2021-04-23 11:41:03.51016+05
33	store	0015_auto_20210423_1211	2021-04-23 12:11:12.0355+05
34	store	0016_auto_20210423_1213	2021-04-23 12:13:27.444191+05
35	store	0017_profile	2021-08-13 07:35:58.653501+05
36	store	0018_auto_20210813_0743	2021-08-13 07:51:38.901843+05
37	store	0019_auto_20210815_1623	2021-08-15 16:24:00.458522+05
38	store	0020_remove_order_product_name	2021-08-16 15:07:32.426569+05
39	store	0021_order_product_name	2021-08-16 15:10:13.813025+05
40	store	0022_auto_20210816_1511	2021-08-16 15:11:18.685182+05
41	store	0023_auto_20210816_1511	2021-08-16 15:11:57.834966+05
42	store	0024_products_no_of_visits	2021-08-16 21:45:31.789142+05
43	store	0025_auto_20210817_1219	2021-08-17 12:19:55.513347+05
44	store	0026_auto_20210817_1220	2021-08-17 12:20:32.582488+05
45	store	0027_auto_20210818_1211	2021-08-18 12:11:45.971816+05
46	store	0028_auto_20210818_1211	2021-08-18 12:11:45.989081+05
47	store	0029_auto_20210818_1214	2021-08-18 12:14:42.230318+05
48	store	0030_auto_20210818_1312	2021-08-18 13:12:11.451418+05
49	store	0031_auto_20210818_1325	2021-08-18 13:25:12.008506+05
50	store	0032_auto_20210818_1328	2021-08-18 13:28:08.836739+05
51	store	0033_auto_20210818_1330	2021-08-18 13:30:18.620941+05
52	store	0034_auto_20210818_1334	2021-08-18 13:34:14.796859+05
53	store	0035_auto_20210818_1335	2021-08-18 13:35:58.132622+05
54	store	0036_auto_20210818_1959	2021-08-18 19:59:31.684815+05
55	store	0037_auto_20210820_1042	2021-08-20 10:42:34.175777+05
56	store	0038_auto_20210821_1427	2021-08-21 14:27:27.375015+05
57	store	0039_auto_20210821_1429	2021-08-21 14:29:57.345288+05
58	store	0040_auto_20210821_1515	2021-08-21 19:36:09.620618+05
59	store	0041_auto_20210821_2227	2021-08-21 22:27:17.351368+05
60	store	0042_auto_20210822_0910	2021-08-22 09:10:19.829614+05
61	store	0043_auto_20210822_1106	2021-08-22 11:06:35.190391+05
62	store	0044_auto_20210822_1132	2021-08-22 11:32:56.298505+05
63	store	0045_auto_20210822_1331	2021-08-22 13:31:12.744005+05
64	store	0046_orderproduct	2021-08-22 16:53:10.261908+05
65	store	0047_products_featured	2021-08-25 19:30:49.522738+05
66	store	0048_remove_order_quantity	2021-08-26 07:56:37.789032+05
67	store	0049_auto_20210826_0817	2021-08-26 08:17:49.078942+05
68	store	0050_auto_20210826_0829	2021-08-26 08:29:27.241491+05
69	store	0051_auto_20210826_1323	2021-08-26 13:24:01.743467+05
70	store	0052_auto_20210826_1330	2021-08-26 13:30:18.580223+05
71	store	0053_auto_20210826_1459	2021-08-26 14:59:40.32573+05
72	store	0054_auto_20210826_1749	2021-08-26 17:49:07.495738+05
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
k8u9j4nomieb3mwvjpqud7qvheavvdkd	.eJxVjDsOwyAQRO9CHSGMF1hSpvcZ0PILTiKQjF1FuXtsyUXSTDHvzbyZo20tbutpcXNkVzawy2_nKTxTPUB8UL03Hlpdl9nzQ-En7XxqMb1up_t3UKiXfe3HoIIJArPSWiZUnoTNAjRIQ9JIqYRB0npAFHtCgCzU6C16qwEyss8XvLk2Yw:1lZRdO:j_M-rOVmTrnuwr4G7bbWG3fhNjS1iHGGkyfUQlRAevg	2021-05-06 10:12:14.682528+05
9un4d7rw46zw60dfserbd8nnvkhfhw61	.eJxVjDsOwyAQRO9CHSGMF1hSpvcZ0PILTiKQjF1FuXtsyUXSTDHvzbyZo20tbutpcXNkVzawy2_nKTxTPUB8UL03Hlpdl9nzQ-En7XxqMb1up_t3UKiXfe3HoIIJArPSWiZUnoTNAjRIQ9JIqYRB0npAFHtCgCzU6C16qwEyss8XvLk2Yw:1mQt1h:CuFwLiOjY7fT3-R4EImJs0-7T33DFyCINnw1dwCa-EY	2021-09-30 20:10:13.959323+05
q01bqocy8qrgul8v0ld4yms1mcbbodgx	.eJxVjDsOwyAQRO9CHSGM-Swu0_sM1rJA7HxAMriKcvfYkoukmWLmzXuzCbc2T1uN67QENrCOXX47j_SI-RjCHfOtcCq5rYvnB8LPtfKxhPi8nuyfYMY672_fkyZLApI2RkbQHoVLQhklLUorpRYW0JgOQOypSCWhe-_AO6NUgl1KW23lFVc2dJ8vnJY6sA:1lZvVh:B7bLmQgf9bpUNUBId6sYVZYrJQ8KKK9t-xkK3r8hkio	2021-05-07 18:06:17.306089+05
otuj77dnco8tfcuywq0gjz97qu13hlrg	eyJjdXN0b21lciI6MX0:1lZveB:npXTAeQOCMFcXbM8UvTdjzz_2ouNbmqCCkUg8X5Xc3g	2021-05-07 18:15:03.585006+05
8q2ay70x7k4s4t2e31xifbg7aydrztiv	eyJjdXN0b21lciI6MX0:1lZvfq:9gS34TL8Jp4Y-aFeNPnox3sceHbJqC8mssOVWdkpjp4	2021-05-07 18:16:46.163421+05
g7kpqm2y0aw3eisrmjlggj6b704uhxoh	eyJjdXN0b21lciI6MX0:1lZvwz:_C-U7y-rmpd1Z8i-Xd1lX8SRV1bK8MTMqZVh4SKvXtM	2021-05-07 18:34:29.842145+05
qv48rt2lpr7xc36xwb3efhp01vnqqhy3	eyJjdXN0b21lciI6MX0:1laAra:OYDCzPf_Nq3u3oJ323YO1VcG1iHD3U4SqFDnuF0Gx0o	2021-05-08 10:29:54.308908+05
5g7hrk7on9ai4y4gmjv1ndjvxo2443oy	eyJjdXN0b21lciI6MX0:1laAv2:zVs-P2eKuXGqf9KYm7goKvipYQupIwmvQYMsObZOTr4	2021-05-08 10:33:28.739153+05
7v5sgdiehbzhyt19cujqen6ewf2fwrpm	eyJjdXN0b21lciI6MX0:1laAwB:WqPlMCFhT3QKub9EgN79fB44Cj-zbm0uF6kCTj7lxxs	2021-05-08 10:34:39.833083+05
ow2ystgm2usnvgqxsezrh9ucw92cndnb	eyJjYXJ0Ijp7InByb2R1Y3QiOjEsIjUiOjF9fQ:1laHl8:CSaBpiLzV_c2Ra2WFTrvX42VtRmX1Bnpu40j4URTMrA	2021-05-08 17:51:42.45513+05
l867dnk7mt5vah7t0lmmgmgtkrfexk2b	eyJjdXN0b21lciI6OH0:1mHiKP:bdz6HjZATkVfWu9H5A_X3ksqEOSmaMHM3C3cbf2M5nw	2021-09-05 12:55:37.492165+05
to4cqjw0umhbnvqyw1fjbiwfabd2tqtd	eyJjdXN0b21lciI6OH0:1mHiPR:frduvNRwfibr0-lVyB8zogC719B4cK0DKPRBBF3TMUY	2021-09-05 13:00:49.18993+05
rcaeg0i8hsxh6qoh795fz2lzi1bhlsay	eyJjYXJ0Ijp7IjQiOjEsIjUiOjIsIjkiOjEsIjciOjIsIjgiOjF9fQ:1laHuj:52MLJJph2ezv9poQFwBS8u85v6PKstP6YP2OrLQyg44	2021-05-08 18:01:37.345922+05
10p3qoqvbvdhukjzgpod6xyoz4jpj2mr	eyJjdXN0b21lciI6OH0:1mHiSV:-B5GFUCAam3p6QeB9f-RU_9XgbWjTDNOYM8NlG5rSAA	2021-09-05 13:03:59.736375+05
cvbouf3nf3nk45pog7ccn4sv7somj2hu	eyJjYXJ0Ijp7IjUiOjEsIjIiOjEsIjQiOjF9fQ:1laZu0:-VDOp5YPupGIzEk3NEZ-_3dEPlSXrW49Rf8xdwlre1g	2021-05-09 13:14:04.253044+05
x16xmk9ndeqfue7axwbq68sinndvui6j	eyJjdXN0b21lciI6MSwiY2FydCI6eyI0IjoxLCIxIjoxLCIzIjoxfX0:1laaok:dyyvOMnu4o1i9dVkRJhKbiMVMI7rV8XovUOtAxXu5m0	2021-05-09 14:12:42.662644+05
htkdfq8mymubxny6ha0sht1lom0mqq6j	eyJjYXJ0Ijp7IjQiOjEsIjEiOjF9fQ:1lbhBS:E9XBWpgVh4sLSAtLhDX9BsuMsMaEidBXFh1W_RtFSB8	2021-05-12 15:12:42.524942+05
vz46rcmbqld0p5h34b7nxkyyppf3aevc	eyJjdXN0b21lciI6OCwid2lzaGxpc3QiOnt9LCJjYXJ0Ijp7IjExIjoxLCI5IjoxfX0:1mHo4l:7ilUeu2cvaFXOcV7RMl71i3aBccXVuDXinwyfWyR-To	2021-09-05 19:03:51.727405+05
zvce05lgw73ypzuebjwfrt1exl5rzave	.eJxVjDsOwyAQRO-ydYQw5rOmTJ8zWAuGOD8jAa4s3z1YcpE0I828mdlgpLXO41pCHh8TWOjg8ps58q-wHGB60nJPzKel5odjR4WdtLBbmsL7enb_DmYqc1u73itvPMeotBYBlSM-RC61FIaEEUJxg6R1h8ibSi8jV70b0A1ayojt1FOuYDfowXZ7s2up6RMyWNy_IY4-5Q:1mI2wB:6j0mCiCyRidXlUOK_XUK_5Oi1qPPsc5SY0glu5YfLKA	2021-09-06 10:55:59.803233+05
mxdbejpdvr1bgirqejvw2cxeu9lsvhq4	.eJxVT0sKwyAUvIvrIsb4zbL7niHoi1bbNIIaugi9exWyyWZgvjAHApMrmg6k0TT8bugbS1hj6VJjs9lrmPfi8hwXNKEBXTRr4O22biwvsz0ThrTVHC3uEXy6BT_S4tb7mb0MBFNCa9sROEggynMhqFPcGqI9YYJRaaiklBOpjBCDUqQhA-YJH61WVgvGvGqjsJeaPi73F3_WSkP9:1mE5m8:_6_nj4WGMY00XqWB5soEESeakfAwVGj_IBKBe8-CeAA	2021-08-26 13:09:16.883278+05
fzw6fr4lakvveummq464h2ixdyivlml5	.eJxVjLkOhDAMRP_FNYqS4Byk3H6_ATkmWfYQSBwV4t83CBoaj-fN2BswTQuEDRCCrgCCqkCduzmNglAX0YXtFbS0Ln27zmlq3x0EUHBjkfibhiPoPjS8RsHjsEzvKI6KuNJZPMcu_R5X9_agp7kv17Fmw46lz8ZanbyJJJss0aJ2pJ3WRjpP1irvZZnImKWpY-NjYxGzh_0PWmZAPQ:1li9Dy:MeNgeqQQDLh22SVaJo9nLMLlLmq6eOIp490NzOHpOg8	2021-05-30 10:21:58.684661+05
8rpudgsv256rhjzetouotn6o199ap4fg	eyJjYXJ0Ijp7IjE0IjoxLCIxMCI6MSwiMiI6MX19:1luvte:rbXyNvLPeXKwlPPDM4gilz0v4lQcmoEv2XRRltw2JO8	2021-07-04 16:45:50.237163+05
p5p318filev5mvzsffgs9uzwyxzu161v	eyJjYXJ0Ijp7IjEyIjoyLCI0IjozfSwid2lzaGxpc3QiOnsiNCI6MSwiMTIiOjF9fQ:1m4d21:6iSez4riNp47x3Gksw4y2IydIxPMQNg_xTVIxGX4uNU	2021-07-31 10:38:33.823355+05
vdjv85zfyh3h127kuklqzdgm4gpx17bk	eyJjYXJ0Ijp7IjEiOjF9LCJ3aXNobGlzdCI6eyIxIjoxfX0:1m4dMj:r5GUhboSZGLyyRrIbHsXZWPgExkAFqoQ7v4-jrVk1eQ	2021-07-31 10:59:57.693363+05
8ikghk8ue9n4e4jas6mm7x67mkq5qfe9	.eJxVjrsOhCAURP_l1oYg8i63328wcIXVfUgCWBn_fTGxsZli5sxkdsCt1PQLGazpYHRbncethDwuE1jo4eZ5h5-wnsH0dusrEUxrzYsnJ0KutJBnmsL3cbG3gdmVubX9gAIVUh2FlCxo4R01kXLJmXJMMSao0k7KXmvalCOPVAzeaG8k51G3UXS5gt3bQ9t3oJoexx_NRT_2:1mJFtu:cYjTmXrr-azIFeRY4AbEsu5pw-sifi3Znft2UH9caPM	2021-09-09 18:58:38.925562+05
0f1u3q5nemxq2r238tmkin76ka0g3fln	.eJxVjDsOgzAQRO-ydWQZ48_aZfqcAa0XO5BEIGFTIe4ekGhoppj3ZjZgWiqEDVoIzf6AjtY6dGtJSzf2EKCBWxeJv2k6Qf-h6T0Lnqe6jFGcirhoEa-5T7_n5d4OBirDsY4tG3YsMRtrVUITSfostdXKkXJKGemQrG0Q5ZGadZamjR6jt1pnhP0PrgA6kQ:1mJqb7:WQG00oiHqVK7FLsfJJbwGtaozBI55Ah4YCR-ir_XGE8	2021-09-11 10:09:41.198642+05
asdvhkcliiur4xapyj3wc1mgerf1a1wo	.eJxVjDsOwyAQRO9CHSGMF1hSpvcZ0PILTiKQjF1FuXtsyUXSTDHvzbyZo20tbutpcXNkVzawy2_nKTxTPUB8UL03Hlpdl9nzQ-En7XxqMb1up_t3UKiXfe3HoIIJArPSWiZUnoTNAjRIQ9JIqYRB0npAFHtCgCzU6C16qwEyss8XvLk2Yw:1mEDEL:wHiVl_YauVFu_rwfySyvnlUwRZS9VeeUqibnRhMNzr0	2021-08-26 21:06:53.554117+05
5lc99pvfbqhizojz3dltw04m1w1fnz5k	.eJxVjDsOgzAQRO-yNbJs4x-U6TkDWi927ASBhEEpEHcPSBRJM8V7M7NDj9ua-q2Epc8DtCCg-mUe6R2mSwwvnJ4zo3lal-zZVWG3LaybhzA-7u7fQcKSzrWvSZMl7qI2RganPfImcmWUtCitlJpbh8YI5_iZilTkuvaN841RKrrzlHBZod1BCGjFUcEnlzTmcrHj-AKenD_Z:1mFt3Z:tmiVx5Re6WASAiiwelsAt-CawWMav3a1XpgoDkICGcs	2021-08-31 11:58:41.12351+05
\.


--
-- Data for Name: store_catagory; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.store_catagory (id, name) FROM stdin;
1	child & Babies
2	Men & Women
3	Fashion & Beauty
\.


--
-- Data for Name: store_customer; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.store_customer (id, first_name, last_name, email, phno, password, confirm_password) FROM stdin;
2	faisal	gulzar	faisal@gmail.com	3174042575	pbkdf2_sha256$216000$kdEXXAiazJY1$/tv9zTiXgH/qNT6516KUXHemxFJWdrMuVABOIVJHOcc=	123456
8	azeem	akram	mazeemakramnns@gmail.com	3047676571	pbkdf2_sha256$216000$MqhlqXddQ8W5$z8VFhCUuC+BiqhlI8tDvY3kD6sB/0tdIwz7TCl1m7eI=	123456
9	muh	ali	anon@gmail.com	12345678901	pbkdf2_sha256$216000$5Viu1RzPaIWm$5/4zWXirLJnOifQPWunpDebUfxmKg8I9gSqZimvTp/g=	pbkdf2_sha256$216000$t04pky6zSsjj$ynbSwe6MKkviDMQLJVDY0bjJcfu+pbwTFBCKXAm74/8=
6	younas	mughal	younas@gmail.com	3015656756	pbkdf2_sha256$216000$m0JOXqfXjT6Y$93A6o1BANnFKpdkVMoZcvM9FFKwleslbYnIjY70IHPM=	123456
\.


--
-- Data for Name: store_order; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.store_order (id, date, price, customer_id, address, phno, shipping_address, name, name_additional, phno_additional, email, payment_method_id, order_status) FROM stdin;
26	2021-08-26 13:31:56.221968+05	2437	6	ghazi road, lahore	3014848282	ghazi road, lahore	younas mughal	\N	\N	younas@gmail.com	1	approved
\.


--
-- Data for Name: store_order_products; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.store_order_products (id, order_id, products_id) FROM stdin;
49	26	8
50	26	3
\.


--
-- Data for Name: store_orderproduct; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.store_orderproduct (id, quantity, order_id, product_id) FROM stdin;
27	3	26	3
28	1	26	8
\.


--
-- Data for Name: store_payment_method; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.store_payment_method (id, name) FROM stdin;
1	Cash-on Delivery
2	jazz_cash
\.


--
-- Data for Name: store_products; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.store_products (id, name, "desc", img, price, catagory_id, quantity, date, no_of_visits, featured) FROM stdin;
3	fancy design dress shirt	Hey guys!! welcome to our amazing stock available try out this to flourish your character.	pics/Daco_4593156.png	549	2	4	2021-08-15 21:24:00+05	45	t
9	black short with lightblue jeans	Hey guys!! welcome to our amazing stock available try out this to flourish your character.	pics/ian-dooley-TT-ROxWj9nA-unsplash.jpg	599	3	2	2021-07-15 21:24:00+05	5	t
6	black slicky surfaced T-shirt	Here is our amazing stock available. You can choose anyone you like and you will feel proud to shop here	pics/dimitry-zub-0nkzBDzLXTI-unsplash.jpg	349	2	3	2021-08-15 21:24:00.444207+05	1	f
2	Multi-colored dress shirt	white balck and brown combination multi-colored dress shirt. Checkout to try our amazing offers and upraise your personality and amazing look.	pics/Daco_2047350.png	449	2	2	2021-08-15 21:24:00+05	19	t
7	white sleeky dress	Here is our amazing stock available. You can choose anyone you like and you will feel proud to shop here	pics/dmitry-zmiy-rD01mlJ5WUM-unsplash.jpg	699	3	2	2021-07-15 21:24:00+05	19	f
1	american accent dress shirt	It is an american culture dress shirt for people with glowing personalities. Checkout our amazing stock available with reasonable price and real quality. Shop it now to enrich your character.	pics/nimble-made-m2z2wJ1XX6Q-unsplash.jpg	499	2	3	2021-08-15 21:24:00+05	30	t
4	black colored  T-shirt	Hey guys!! welcome to our amazing stock available try out this to flourish your character.	pics/jose-pedro-ortiz-jXywvr0Odxg-unsplash.jpg	399	2	5	2021-08-15 21:24:00.444207+05	5	f
5	black flexible T-shirt	Hey guys!! welcome to our amazing stock available try out this to flourish your character.	pics/jade-scarlato-Pb7UGXyLcZs-unsplash.jpg	449	2	3	2021-08-15 21:24:00.444207+05	4	f
8	offshore red dress	Here is our amazing stock available. You can choose anyone you like and you will feel proud to shop here	pics/ussama-azam-xgNSlx7DjYM-unsplash.jpg	789	3	1	2021-07-15 21:24:00+05	33	t
\.


--
-- Data for Name: store_profile; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.store_profile (id, name, profession, img, job_position, customer_id, home_address, phno, postal_address, shipping_address, zip_code) FROM stdin;
23	younas Mughal	electonics	profile/21/My_Post_1_4ZH1Vym.jpg	technician	6	ghazi road, lahore	3014848282	ghazi road, lahore	kalma chowk, lahore	39100
13	Muhammad Azeem Akram	IT	My Post.jpg	Software Engineer	8	chandar nagar	3047676571	chandar nagar	chandar nagar	39100
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 52, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 139, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 13, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 72, true);


--
-- Name: store_catagory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.store_catagory_id_seq', 6, true);


--
-- Name: store_customer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.store_customer_id_seq', 9, true);


--
-- Name: store_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.store_order_id_seq', 30, true);


--
-- Name: store_order_products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.store_order_products_id_seq', 54, true);


--
-- Name: store_orderproduct_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.store_orderproduct_id_seq', 30, true);


--
-- Name: store_payment_method_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.store_payment_method_id_seq', 2, true);


--
-- Name: store_products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.store_products_id_seq', 14, true);


--
-- Name: store_profile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.store_profile_id_seq', 23, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: store_catagory store_catagory_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_catagory
    ADD CONSTRAINT store_catagory_pkey PRIMARY KEY (id);


--
-- Name: store_customer store_customer_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_customer
    ADD CONSTRAINT store_customer_email_key UNIQUE (email);


--
-- Name: store_customer store_customer_phno_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_customer
    ADD CONSTRAINT store_customer_phno_key UNIQUE (phno);


--
-- Name: store_customer store_customer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_customer
    ADD CONSTRAINT store_customer_pkey PRIMARY KEY (id);


--
-- Name: store_order store_order_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_order
    ADD CONSTRAINT store_order_pkey PRIMARY KEY (id);


--
-- Name: store_order_products store_order_products_order_id_products_id_b83d7379_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_order_products
    ADD CONSTRAINT store_order_products_order_id_products_id_b83d7379_uniq UNIQUE (order_id, products_id);


--
-- Name: store_order_products store_order_products_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_order_products
    ADD CONSTRAINT store_order_products_pkey PRIMARY KEY (id);


--
-- Name: store_orderproduct store_orderproduct_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_orderproduct
    ADD CONSTRAINT store_orderproduct_pkey PRIMARY KEY (id);


--
-- Name: store_payment_method store_payment_method_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_payment_method
    ADD CONSTRAINT store_payment_method_pkey PRIMARY KEY (id);


--
-- Name: store_products store_products_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_products
    ADD CONSTRAINT store_products_pkey PRIMARY KEY (id);


--
-- Name: store_profile store_profile_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_profile
    ADD CONSTRAINT store_profile_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: store_customer_email_1e001829_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX store_customer_email_1e001829_like ON public.store_customer USING btree (email varchar_pattern_ops);


--
-- Name: store_order_customer_id_13d6d43e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX store_order_customer_id_13d6d43e ON public.store_order USING btree (customer_id);


--
-- Name: store_order_payment_method_id_a77344fb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX store_order_payment_method_id_a77344fb ON public.store_order USING btree (payment_method_id);


--
-- Name: store_order_products_order_id_b344d9c7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX store_order_products_order_id_b344d9c7 ON public.store_order_products USING btree (order_id);


--
-- Name: store_order_products_products_id_5e4e167b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX store_order_products_products_id_5e4e167b ON public.store_order_products USING btree (products_id);


--
-- Name: store_orderproduct_order_id_87a00c28; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX store_orderproduct_order_id_87a00c28 ON public.store_orderproduct USING btree (order_id);


--
-- Name: store_orderproduct_product_id_1633886a; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX store_orderproduct_product_id_1633886a ON public.store_orderproduct USING btree (product_id);


--
-- Name: store_products_catagory_id_6c3abca6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX store_products_catagory_id_6c3abca6 ON public.store_products USING btree (catagory_id);


--
-- Name: store_profile_customer_id_55c892fe; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX store_profile_customer_id_55c892fe ON public.store_profile USING btree (customer_id);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: store_order store_order_customer_id_13d6d43e_fk_store_customer_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_order
    ADD CONSTRAINT store_order_customer_id_13d6d43e_fk_store_customer_id FOREIGN KEY (customer_id) REFERENCES public.store_customer(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: store_order store_order_payment_method_id_a77344fb_fk_store_pay; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_order
    ADD CONSTRAINT store_order_payment_method_id_a77344fb_fk_store_pay FOREIGN KEY (payment_method_id) REFERENCES public.store_payment_method(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: store_order_products store_order_products_order_id_b344d9c7_fk_store_order_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_order_products
    ADD CONSTRAINT store_order_products_order_id_b344d9c7_fk_store_order_id FOREIGN KEY (order_id) REFERENCES public.store_order(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: store_order_products store_order_products_products_id_5e4e167b_fk_store_products_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_order_products
    ADD CONSTRAINT store_order_products_products_id_5e4e167b_fk_store_products_id FOREIGN KEY (products_id) REFERENCES public.store_products(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: store_orderproduct store_orderproduct_order_id_87a00c28_fk_store_order_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_orderproduct
    ADD CONSTRAINT store_orderproduct_order_id_87a00c28_fk_store_order_id FOREIGN KEY (order_id) REFERENCES public.store_order(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: store_orderproduct store_orderproduct_product_id_1633886a_fk_store_products_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_orderproduct
    ADD CONSTRAINT store_orderproduct_product_id_1633886a_fk_store_products_id FOREIGN KEY (product_id) REFERENCES public.store_products(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: store_products store_products_catagory_id_6c3abca6_fk_store_catagory_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_products
    ADD CONSTRAINT store_products_catagory_id_6c3abca6_fk_store_catagory_id FOREIGN KEY (catagory_id) REFERENCES public.store_catagory(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: store_profile store_profile_customer_id_55c892fe_fk_store_customer_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.store_profile
    ADD CONSTRAINT store_profile_customer_id_55c892fe_fk_store_customer_id FOREIGN KEY (customer_id) REFERENCES public.store_customer(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

