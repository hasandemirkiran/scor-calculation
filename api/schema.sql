drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  kimlikNo integer not null,
  adSoyad text not null,
  aylikGelir integer not null,
  telNo integer not null,
  ikamet text not null
);