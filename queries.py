# SQL Queries

query_1 = """Select title, views from (SELECT count(main.id) as views, path
from (SELECT id, path, status from log where status = '200 OK' and path!='/')
as main GROUP BY path) as allviews JOIN articles as art on
(allviews.path = CONCAT('/article/', art.slug))
ORDER  BY views DESC LIMIT 3;"""

query_2 = """SELECT auth.name, sum(views) as totalviews FROM articles AS art
JOIN authors AS auth ON (art.author = auth.id)
JOIN (SELECT count(id) as views, path
from (SELECT id, path, status from log where status = '200 OK' and path!='/')
as main GROUP BY path ORDER BY views DESC)
as pre on CONCAT('/article/', art.slug) = pre.path GROUP BY auth.name ORDER
BY totalviews DESC;"""

query_3 = """SELECT day, round(cast(badreq AS NUMERIC )*100/CAST
(allreq AS  NUMERIC ), 2) as percentage FROM
(SELECT COUNT (id) as badreq , date(time) as day
from (SELECT * FROM log WHERE status != '200 OK') AS foo GROUP BY day)
AS request
JOIN (SELECT COUNT (id) AS allreq, date(time) as fullday
from log GROUP BY fullday) as totalreq ON (request.day = totalreq.fullday)
WHERE round(cast(badreq AS NUMERIC )*100/CAST
(allreq AS  NUMERIC ), 2) > 1.0 ORDER BY percentage DESC;"""
