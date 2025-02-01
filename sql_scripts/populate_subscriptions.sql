INSERT INTO subscriptions_details (
    subscription_name, subscription_type, cost_rubles, cost_stars, duration,
    is_active, models_count, photos_by_prompt_count, photos_by_image_count
) VALUES
    ('monthly_small',            'monthly',       900,   375,   30,     TRUE, 1, 50,  50),
    ('monthly_middle',           'monthly',       1200,  495,  30,     TRUE, 1, 150, 150),
    ('monthly_large',            'monthly',       5300,  2200,  30,     TRUE, 2, 500, 500),

    ('models_small_pack',        'models',        900,   375,   NULL,   TRUE, 1, 0, 0),
    ('models_midlle_pack',       'models',        1600,  666,  NULL,   TRUE, 2, 0, 0),
    ('models_large_pack',        'models',        3600,  1500,  NULL,   TRUE, 5, 0, 0),

    ('generations_bomz_pack',    'generations',   400,   165,   NULL,   TRUE, 0, 50,   50),
    ('generations_small_pack',   'generations',   1000,  415,   NULL,   TRUE, 0, 150,  150),
    ('generations_middle_pack',  'generations',   1800,  750,  NULL,   TRUE, 0, 300,  300),
    ('generations_large_pack',   'generations',   5500,  2290,  NULL,   TRUE, 0, 1000, 1000);


