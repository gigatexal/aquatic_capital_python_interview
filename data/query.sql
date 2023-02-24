explain analyze select
	--row_number() over (partition by "Station Name", cast("Measurement Timestamp" as date) order by "Measurement Timestamp" desc) as row_num
	"Station Name"
    ,cast("Measurement Timestamp" as DATE) as "Measurement Day"
    ,min("Air Temperature") OVER (partition by "Station Name" ,CAST("Measurement Timestamp" AS DATE)) as min_temp
  	,max("Air Temperature") OVER (partition by "Station Name" ,CAST("Measurement Timestamp" AS DATE)) as max_temp
	,first_value("Air Temperature") OVER (partition by  "Station Name",cast("Measurement Timestamp" as date) ORDER BY "Measurement Timestamp" ASC) as first_temp
	/* for the life of me I can't figure out why the last_value function doesn't work list the first_value function ... using first_value and reverse order */
	,first_value("Air Temperature") OVER (partition by  "Station Name", cast("Measurement Timestamp" as date) ORDER BY "Measurement Timestamp" DESC) as last_temp
from
	weather
	qualify row_number() over (partition by "Station Name", cast("Measurement Timestamp" as date) order by "Measurement Timestamp" desc) = 1
order by 2 asc,1
	

--create index ix_foo on weather ("Station Name", "Measurement Timestamp", "Air Temperature");
