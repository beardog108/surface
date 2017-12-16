create table sites(
    id integer primary key AUTOINCREMENT not null,
    name text not null,
    onion text,
    zeronet text,
    i2p text,
    i2pHostname text,
    freenet text,
    ipfs text,
    dat text,
    keywords text,
    category text
);

create table files(
    id integer primary key AUTOINCREMENT not null,
    name text not null,
    hash text not null
);