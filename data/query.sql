select "Station Name", "Measurement Day", "min_temp", "max_temp", "first_temp", "last_temp" FROM 
(
  SELECT
	"Station Name"
    ,CAST("Measurement Timestamp" AS DATE) AS "Measurement Day"
    ,MIN("Air Temperature") OVER (PARTITION BY "Station Name" ,CAST("Measurement Timestamp" AS DATE)) AS min_temp
  	,MAX("Air Temperature") OVER (PARTITION BY "Station Name" ,CAST("Measurement Timestamp" AS DATE)) AS max_temp
	,FIRST_VALUE("Air Temperature") OVER (PARTITION BY  "Station Name",cast("Measurement Timestamp" AS date) ORDER BY "Measurement Timestamp" ASC) AS first_temp
	/* for the life of me I can't figure out why the last_value function doesn't work list the first_value function ... using first_value and reverse order */
	,FIRST_VALUE("Air Temperature") OVER (PARTITION BY  "Station Name", cast("Measurement Timestamp" AS date) ORDER BY "Measurement Timestamp" DESC) AS last_temp,
ROW_NUMBER() OVER (PARTITION BY "Station Name", CAST("Measurement Timestamp" AS DATE) ORDER BY "Measurement Timestamp" DESC) as row_num
FROM
	weather
) x
WHERE x.row_num = 1;

