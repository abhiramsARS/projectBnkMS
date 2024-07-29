/* Creating Database */
Create Database bankms;

/* Using Database */
use bankms;

/* Creating Tables */
create table account(ac_no varchar(9) not null primary key,ac_holder varchar(20) not null,ph_no varchar(12) not null,ac_balance int,ac_status varchar(2) not null,ac_date date);
create table transaction(trans_id varchar(8) not null primary key,trns_date date not null,trans_ac varchar(9) not null,trans_method varchar(10) not null,amount integer not null ,trans_type varchar(2) not null);

/* Adding Trial Data to tables */
insert into account values("BAC-00001","Test","1234567890",0,'O',curdate());
insert into transaction values("2420001",curdate(),"BAC-10001","deposit",0,"c");
