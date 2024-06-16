SELECT author, COUNT(*) с
FROM reviews
GROUP BY author
HAVING с = (
    SELECT COUNT(*) cc 
        FROM reviews 
        GROUP BY author
        order by cc desc
        limit 1
);

SELECT round(sum(r.score)) s, a.artist from reviews r
left join artists a on a.reviewid = r.reviewid
group by a.artist
order by s desc
limit 10;
