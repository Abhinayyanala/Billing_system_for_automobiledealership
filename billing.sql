#Database for an automobile dealership to manage billing.
create database tata;
use tata;
create table login(
    id int,
    user_name char(25),
    pwd varchar(20)
);

  insert into login(id,user_name, pwd) value(1,'abhinay','abhi@123');

create table cars(
    id int AUTO INCREMENT NOT NULL,
    carname char(25),
    price int,
    PRIMARY KEY(id)
);
  
  insert into cars(carname, price) values (1, 'Nano', 200000),
    (2, 'Tiago', 450000),
    (3, 'Zest', 525000),
    (4, 'Altroz', 575000),
    (5, 'Punch', 625000),
    (6, 'Tigor', 715000),
    (7, 'Nexon', 785000),
    (8, 'Safari', 1000000),
    (9, 'Harrier', 1300000),
    (10, 'NexonEV', 1400000);

    create table bills(
    billid INT PRIMARY KEY AUTO_INCREMENT,
    customer CHAR(30) NULL,
    phone VARCHAR(20) NULL,
    billdate DATE NULL
  );
  create table transac(
    id int PRIMARY KEY AUTO_INCREMENT,
    car char(30),
    dpamt int,
    billid int,
    paymode char(20),
    emi_period int
  );

    

