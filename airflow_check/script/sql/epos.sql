select count(c.*) from (select distinct trans_date,rpc_code from dwd.mid_gtm_epos where banner in ('70000011','70000016')  )as c;
select count(*) from dwd.mid_gtm_epos  where banner = '70000013';
select count(*) from dwd.mid_gtm_epos  where banner = '70000014';
select count(*) from dwd.mid_gtm_epos  where banner = '70000015';
select count(*) from dwd.mid_gtm_epos where banner = '70000012';
select count(*) from dwd.mid_gtm_epos where banner = '70000010';
select count(*) from ods.gtm_epos_tmfs_trade where from_unixtime(unix_timestamp(created,'yyyy-MM-dd HH:mm:ss'),'yyyy-MM-dd') >=date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),59);
select count(*) from ods.gtm_epos_tmfs_order  where from_unixtime(unix_timestamp(created,'yyyy-MM-dd HH:mm:ss'),'yyyy-MM-dd') >=date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),59);
select count(*) from  ods.yd_jd_api_epos_byuser where dt >=date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),60);
select count(*) from
(
select
dim.cust_id,
dim.store_id,
from_unixtime(unix_timestamp(a.created,'yyyy-MM-dd HH:mm:ss'),'yyyy-MM-dd') as create_date,
from_unixtime(unix_timestamp(a.pay_time,'yyyy-MM-dd HH:mm:ss'),'yyyy-MM-dd') as trans_date,
-- coalesce(a.sku_id, a.num_iid) as rpc_code,
case when a.sku_id is null or a.sku_id='9999' or a.sku_id='N/A' then a.num_iid else a.sku_id end as rpc_code,
a.title as rpc_name,
a.sku_id as rpc_sku_id,
a.num_iid  as rpc_num_iid,
a.cid as rpc_first_category_id,
nvl(sum(a.total_fee/b.total_fee_sum*c.payment),0)  as offtake_value,
sum(a.num)  as offtake_qty,
count(a.oid)  as trans_volume,
count(distinct a.buyer_nick) consumer_cnt
from
ods.gtm_epos_tmfs_order a
inner join
(select
trade_id, sum(total_fee) as total_fee_sum
from ods.gtm_epos_tmfs_order  group by trade_id ) b
inner join ods.gtm_epos_tmfs_trade c
 on a.trade_id=b.trade_id  and a.trade_id=c.tid
left join dwd.tb_gtm_epos_store_man_dim dim
on upper(c.title) = upper(case when dim.hb_store_name_cn='skii官方旗舰店' then 'SK-II官方旗舰店' when dim.hb_store_name_cn='博朗蓝标旗舰店' then '博朗蓝色光标专卖店' else  dim.hb_store_name_cn end)
and dim.cust_id in ('70000011','70000016')
and from_unixtime(unix_timestamp(a.pay_time,'yyyy-MM-dd HH:mm:ss'),'yyyy-MM-dd') >= dim.dw_start_date
and from_unixtime(unix_timestamp(a.pay_time,'yyyy-MM-dd HH:mm:ss'),'yyyy-MM-dd') < dim.dw_end_date
 where  a.refund_status <> 'SUCCESS' and
case when a.status IN ('TRADE_FINISHED', 'WAIT_BUYER_CONFIRM_GOODS', 'WAIT_SELLER_SEND_GOODS','TRADE_CLOSED','PAID_FORBID_CONSIGN')
then 1 else 0 end = 1 and
case when c.status IN ('TRADE_FINISHED', 'WAIT_BUYER_CONFIRM_GOODS', 'WAIT_SELLER_SEND_GOODS','SELLER_CONSIGNED_PART','PAID_FORBID_CONSIGN')
then 1 else 0 end = 1  and from_unixtime(unix_timestamp(a.created,'yyyy-MM-dd HH:mm:ss'),'yyyy-MM-dd') >= date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),59)
 group by dim.cust_id,dim.store_id,from_unixtime(unix_timestamp(a.created,'yyyy-MM-dd HH:mm:ss'),'yyyy-MM-dd'),from_unixtime(unix_timestamp(a.pay_time,'yyyy-MM-dd HH:mm:ss'),'yyyy-MM-dd'),a.title,a.sku_id, a.num_iid,a.cid
)  h;
select count(*)  from (select ttt.*,row_number() over(partition by ttt.`日期`,ttt.`商品编码`  order by  ttt.dw_batch_num desc) rn  from stg.top_yhd_sale_detail_sku   ttt  where `日期`>= '2017-08-11') tt  where rn=1;
select count(*)  from  stg.sn_query_sale  where `statis_date`>= date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),60);
select count(*)  from ods.top_vip_productdetail_total  where `Date`>=date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),60);
select count(*) from
(select t1.* from
(select *
from stg.top_tmall_super_offtake super
) t1
inner join (
select `date`,max(dw_batch_num) as dw_batch_num
from stg.top_tmall_super_offtake super
group by `date`
) t2
on t1.`date` = t2.`date`
and t1.dw_batch_num = t2.dw_batch_num);

Select  count(*)  from ods.top_jd_epos_sz_offtake where `Date`  >=date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),60);
select count(*) from stg.yd_jd_api_epos_bysku where dt>=date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),60);

--target
select count(c.*) from
(select distinct trans_date,rpc_code from dwd.tb_gtm_epos_sale_rpc_daily_fact where banner in ('70000011','70000016') )as c;
select count(1) from dwd.tb_gtm_epos_sale_rpc_daily_fact where banner = '70000013' ;
select count(*) from dwd.tb_gtm_epos_sale_rpc_daily_fact  where banner = '70000014';
select count(*) from dwd.tb_gtm_epos_sale_rpc_daily_fact  where banner = '70000015';
select count(*) from dwd.tb_gtm_epos_sale_rpc_daily_fact where banner = '70000012';
select count(*) from dwd.tb_gtm_epos_sale_rpc_daily_fact where banner = '70000010';
select count(1) from dwd.tb_gtm_epos_tmfs_trade_daily_fact where dw_batch_num like '20191129%';
select count(1) from dwd.tb_gtm_epos_tmfs_order_daily_fact where order_date >= date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),59) ;
select count(1) from dwd.tb_gtm_epos_jd_api_byuser_daily_fact where dw_batch_num like '20191129%' ;
 select count(*) from dwd.mid_gtm_epos where banner in ('70000011','70000016')  and create_date>=date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),59);
select count(*) from dwd.mid_gtm_epos  where banner = '70000013' and trans_date >= '2017-08-11';
select count(*) from dwd.mid_gtm_epos  where banner = '70000014' and trans_date >= date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),60);
select count(*) from dwd.mid_gtm_epos  where banner = '70000015'  and trans_date >=date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),60);
select count(*) from dwd.mid_gtm_epos where banner = '70000012';
select count(*) from dwd.mid_gtm_epos where banner = '70000010' and trans_date >= date_sub(from_unixtime(unix_timestamp()+28800,'yyyy-MM-dd'),60) ;
