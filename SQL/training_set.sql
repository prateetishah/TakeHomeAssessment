WITH RankedImages AS (
    SELECT
        image_id,
        score,
        ROW_NUMBER() OVER (ORDER BY score DESC) as rank_desc,
        ROW_NUMBER() OVER (ORDER BY score ASC) as rank_asc
    FROM
        unlabeled_image_predictions
),
PositiveSamples AS (
    SELECT
        image_id,
        score AS weak_label
    FROM
        RankedImages
    WHERE
        rank_desc % 3 = 1
    LIMIT 10000
),
NegativeSamples AS (
    SELECT
        image_id,
        score AS weak_label
    FROM
        RankedImages
    WHERE
        rank_asc % 3 = 1
    LIMIT 10000
)
SELECT * FROM PositiveSamples
UNION ALL
SELECT * FROM NegativeSamples;