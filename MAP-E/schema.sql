drop table if exists ruleServer1;
    create table ruleServer1 (
        id integer primary key autoincrement,
        dmr VARCHAR(500),
        ipv6_fixlen VARCHAR(500),
        name VARCHAR(500),
        status VARCHAR(500),
        version VARCHAR(500),
        manufacturer_code VARCHAR(500),
        fmr JSON,
        UNIQUE (manufacturer_code)
    );

