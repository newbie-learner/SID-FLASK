drop table if exists ruleServer2;
    create table ruleServer2 (
    id integer primary key autoincrement,
    DMR nvarchar(500),
    IPV6_length nvarchar(500),
    FMR1 nvarchar(15),
    IPV6 nvarchar(500),
    IPV4 nvarchar(32),
    EA_bit int,
    PSID int
);

