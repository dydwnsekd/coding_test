-- https://programmers.co.kr/learn/courses/30/lessons/59043
SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_OUTS OUTS
JOIN ANIMAL_INS INS
ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
WHERE OUTS.DATETIME < INS.DATETIME
ORDER BY INS.DATETIME;