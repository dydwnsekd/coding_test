-- https://programmers.co.kr/learn/courses/30/lessons/59044
SELECT NAME, DATETIME
FROM ANIMAL_INS
WHERE ANIMAL_ID NOT IN (
    SELECT ANIMAL_ID
    FROM ANIMAL_OUTS
)
ORDER BY DATETIME
LIMIT 3;