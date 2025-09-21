INSERT INTO public.your_table_name (name, email, message, created_at)
SELECT
    'User ' || g AS name,
    'user' || g || '@example.com' AS email,
    'Dummy message ' || g AS message,
    NOW() - (floor(random() * 10000) || ' minutes')::interval AS created_at
FROM generate_series(1, 1000) g;
