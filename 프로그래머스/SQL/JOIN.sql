-- 1 없어진 기록 찾기
SELECT OUTS.ANIMAL_ID, OUTS.NAME FROM ANIMAL_OUTS AS OUTS
LEFT OUTER JOIN ANIMAL_INS AS INS
ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
WHERE INS.ANIMAL_ID IS NULL
ORDER BY ANIMAL_ID

-- 2
SELECT INS.ANIMAL_ID, INS.NAME FROM ANIMAL_INS AS INS
INNER JOIN ANIMAL_OUTS AS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.DATETIME > OUTS.DATETIME
ORDER BY INS.DATETIME

-- 3
SELECT INS.NAME, INS.DATETIME FROM ANIMAL_INS AS INS
LEFT OUTER JOIN ANIMAL_OUTS AS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE OUTS.ANIMAL_ID IS NULL
ORDER BY INS.DATETIME
LIMIT 3

-- 4
SELECT OUTS.ANIMAL_ID, OUTS.ANIMAL_TYPE, OUTS.NAME FROM ANIMAL_OUTS AS OUTS
LEFT OUTER JOIN ANIMAL_INS AS INS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE (OUTS.SEX_UPON_OUTCOME LIKE "%Spayed%" or OUTS.SEX_UPON_OUTCOME LIKE "%Neutered%") AND (INS.SEX_UPON_INTAKE LIKE "%Intact%")
ORDER BY OUTS.ANIMAL_ID
