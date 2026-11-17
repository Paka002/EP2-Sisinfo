-- 1. Todos os posts, do mais recente para o mais antigo.
SELECT * FROM blog_post ORDER BY published_at DESC;

-- 2. Comentários de um post específico.
SELECT * FROM blog_comment WHERE post_id = 2 ORDER BY created_at DESC;

-- 3. Comentários com título e data do post.
SELECT
    c.id, c.author_id, c.text, c.created_at,
    p.title, p.published_at AS post_date
FROM blog_comment AS c
JOIN blog_post AS p ON p.id = c.post_id
WHERE c.post_id = 2
ORDER BY c.created_at DESC;

-- 4. Posts de uma categoria, incluindo dados das duas tabelas.
SELECT
    c.id AS category_id, c.name,
    p.id AS post_id, p.title, p.content, p.published_at
FROM blog_category AS c
JOIN blog_post_categories AS pc ON pc.category_id = c.id
JOIN blog_post AS p ON p.id = pc.post_id
WHERE c.id = 1
ORDER BY p.published_at DESC;

-- 5. Categorias com um ou mais posts.
SELECT c.id, c.name, COUNT(pc.post_id) AS post_count
FROM blog_category AS c
JOIN blog_post_categories AS pc ON pc.category_id = c.id
GROUP BY c.id, c.name
HAVING COUNT(pc.post_id) > 0
ORDER BY c.name;
