-- 코드를 작성해주세요
SELECT
COUNT(*) FISH_COUNT
,FN.FISH_NAME
FROM FISH_INFO FI
LEFT JOIN FISH_NAME_INFO FN
ON FI.FISH_TYPE=FN.FISH_TYPE
GROUP BY FN.FISH_NAME
ORDER BY FISH_COUNT DESC