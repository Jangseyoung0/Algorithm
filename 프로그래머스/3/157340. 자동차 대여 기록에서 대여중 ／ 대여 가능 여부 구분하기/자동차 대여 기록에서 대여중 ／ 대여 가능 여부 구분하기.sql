SELECT CAR_ID,
       CASE 
           -- 대여 중인 차량이 0대이면 '대여 가능'
           WHEN COUNT(CASE 
                       WHEN START_DATE <= '2022-10-16' AND END_DATE >= '2022-10-16'
                       THEN 1 
                       ELSE NULL 
                    END) = 0 
           THEN '대여 가능'
           -- 그 외는 '대여 중'
           ELSE '대여중'
       END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;
