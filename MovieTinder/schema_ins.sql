--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.users (id, username, password) OVERRIDING SYSTEM VALUE VALUES (1, 'Holger69', '$2b$12$QiuK9jNNJaQ8yeSbt0Xt7eTz8D6vUlh/QatYnt83CXXFbqoy019zy');
INSERT INTO public.users (id, username, password) OVERRIDING SYSTEM VALUE VALUES (2, 'Mikkel420', '$2b$12$yy2kYjOP0qRbobWmfHHPguhWLWX8VB21zSgHMKAzWUYfLHFVHvkC6');
INSERT INTO public.users (id, username, password) OVERRIDING SYSTEM VALUE VALUES (3, 'Laust42', '$2b$12$yb9WCJ5fBhAXPoWxoSMiXOysFjmkAR7pzzEXaVBi48c.ZmJJE7wOy');


--
-- Data for Name: dislikes; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.dislikes (user_id, movie_id) VALUES (3, 71);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (3, 25);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (3, 92);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (3, 84);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (3, 12);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (3, 56);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (3, 66);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (3, 63);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (3, 83);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (3, 80);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (1, 79);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (1, 27);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (1, 33);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (1, 17);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (1, 18);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (1, 47);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (1, 88);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (1, 24);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (1, 80);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (1, 15);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (2, 40);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (2, 67);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (2, 28);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (2, 57);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (2, 47);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (2, 78);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (2, 22);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (2, 75);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (2, 64);
INSERT INTO public.dislikes (user_id, movie_id) VALUES (2, 76);


--
-- Data for Name: hasfriends; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.hasfriends (id1, id2) VALUES (2, 1);


--
-- Data for Name: likes; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.likes (user_id, movie_id) VALUES (3, 7);
INSERT INTO public.likes (user_id, movie_id) VALUES (3, 3);
INSERT INTO public.likes (user_id, movie_id) VALUES (3, 2);
INSERT INTO public.likes (user_id, movie_id) VALUES (3, 98);
INSERT INTO public.likes (user_id, movie_id) VALUES (3, 87);
INSERT INTO public.likes (user_id, movie_id) VALUES (3, 72);
INSERT INTO public.likes (user_id, movie_id) VALUES (3, 49);
INSERT INTO public.likes (user_id, movie_id) VALUES (3, 70);
INSERT INTO public.likes (user_id, movie_id) VALUES (3, 27);
INSERT INTO public.likes (user_id, movie_id) VALUES (3, 6);
INSERT INTO public.likes (user_id, movie_id) VALUES (3, 96);
INSERT INTO public.likes (user_id, movie_id) VALUES (3, 86);
INSERT INTO public.likes (user_id, movie_id) VALUES (3, 77);
INSERT INTO public.likes (user_id, movie_id) VALUES (3, 35);
INSERT INTO public.likes (user_id, movie_id) VALUES (3, 97);
INSERT INTO public.likes (user_id, movie_id) VALUES (1, 29);
INSERT INTO public.likes (user_id, movie_id) VALUES (1, 37);
INSERT INTO public.likes (user_id, movie_id) VALUES (1, 4);
INSERT INTO public.likes (user_id, movie_id) VALUES (1, 72);
INSERT INTO public.likes (user_id, movie_id) VALUES (1, 26);
INSERT INTO public.likes (user_id, movie_id) VALUES (1, 23);
INSERT INTO public.likes (user_id, movie_id) VALUES (1, 16);
INSERT INTO public.likes (user_id, movie_id) VALUES (1, 19);
INSERT INTO public.likes (user_id, movie_id) VALUES (1, 34);
INSERT INTO public.likes (user_id, movie_id) VALUES (1, 89);
INSERT INTO public.likes (user_id, movie_id) VALUES (1, 39);
INSERT INTO public.likes (user_id, movie_id) VALUES (1, 11);
INSERT INTO public.likes (user_id, movie_id) VALUES (1, 82);
INSERT INTO public.likes (user_id, movie_id) VALUES (1, 28);
INSERT INTO public.likes (user_id, movie_id) VALUES (1, 38);
INSERT INTO public.likes (user_id, movie_id) VALUES (2, 25);
INSERT INTO public.likes (user_id, movie_id) VALUES (2, 52);
INSERT INTO public.likes (user_id, movie_id) VALUES (2, 99);
INSERT INTO public.likes (user_id, movie_id) VALUES (2, 4);
INSERT INTO public.likes (user_id, movie_id) VALUES (2, 71);
INSERT INTO public.likes (user_id, movie_id) VALUES (2, 48);
INSERT INTO public.likes (user_id, movie_id) VALUES (2, 82);
INSERT INTO public.likes (user_id, movie_id) VALUES (2, 2);
INSERT INTO public.likes (user_id, movie_id) VALUES (2, 14);
INSERT INTO public.likes (user_id, movie_id) VALUES (2, 43);
INSERT INTO public.likes (user_id, movie_id) VALUES (2, 16);
INSERT INTO public.likes (user_id, movie_id) VALUES (2, 49);
INSERT INTO public.likes (user_id, movie_id) VALUES (2, 39);
INSERT INTO public.likes (user_id, movie_id) VALUES (2, 92);
INSERT INTO public.likes (user_id, movie_id) VALUES (2, 38);


--
-- PostgreSQL database dump complete
--

