--source
select count(*)  from (select ttt.*,row_number() over(partition by ttt.`Date`,ttt.productcode

order by  ttt.dw_batch_num desc) rn  from  stg.top_jd_epos_sz_offtake  ttt  where ttt.`Date`>=date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),60)

) tt where rn=1;

select count(1) from (select oid,Row_Number() OVER (partition by oid order by modified desc) as num_par
from stg.mid_gtm_epos_tmfs_order where substr(created,1,10) >= date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),59)) as c where c.num_par = 1;

select count(1) from
(select t1.date,t1.dw_batch_num from
from stg.top_vip_productdetail_total t1
inner join
(select `date`,max(dw_batch_num) as max_dw_batch_num from stg.top_vip_productdetail_total
 where `date`>=date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),60) group  by `date`
)  s
on t1.`date`=s.`date` and t1.dw_batch_num=s.max_dw_batch_num
);

Select count(*) from
(select *, Row_Number() OVER (partition by skuid,parentordid,sonordid order by dt desc )
as num_par from  stg.yd_jd_api_epos_byuser where dt >=date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),60)) c  where c.num_par = 1;

Select count(c.*) from
(select *, Row_Number() OVER (partition by skuid,parentordid,sonordid order by dt desc ) as num_par from  stg.yd_jd_api_epos_refund
where   dt >=date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),60) ) c  where c.num_par = 1;

select count(*) from
(select tid,Row_Number() OVER (partition by tid order by modified desc ) as num_par from stg.mid_gtm_epos_tmfs_trade
where substr(created,1,10) >=date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),59)) as c where c.num_par = 1;

--target

Select  count(*)  from ods.top_jd_epos_sz_offtake where `Date`  >=date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),60);
select count(1) from ods.gtm_epos_tmfs_order where substr(created,1,10) >= date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),59);
Select  count(*) from ods.top_vip_productdetail_total where `date` >=date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),60);
Select count(*) from  ods.yd_jd_api_epos_byuser where dt >= date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),60);
Select count(*) from  ods.yd_jd_api_epos_refund where dt >= date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),60);
Select count(*) from  ods.gtm_epos_tmfs_trade where substr(created,1,10) >=date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),59);