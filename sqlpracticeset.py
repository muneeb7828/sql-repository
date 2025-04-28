
# use munebdb4;

# create table employee4(
# EmpID int not null,
# firstname varchar(200),
# lastname varchar(200),
# Empzone varchar(250),
# primary key(EmpID)
# );

# desc employee4;

# insert into employee4(EmpID,firstname,lastname,Empzone,Empsalary) values(1,"Tom","hanks","east",7000);
# insert into employee4(EmpID,firstname,lastname,Empzone,Empsalary) values(2,"Tom","hanks","east",7000);
# insert into employee4(EmpID,firstname,lastname,Empzone,Empsalary) values(3,"Tom","hanks","east",7000);
# insert into employee4(EmpID,firstname,lastname,Empzone,Empsalary) values(4,"Tom","hanks","east",7000);
# insert into employee4(EmpID,firstname,lastname,Empzone,Empsalary) values(5,"Tom","hanks","east",7000);

# alter table employee4 add column Empsalary int;

# select * from employee4;

# update employee4 set firstname="abdur",lastname="rehman",Empzone="south" where EmpID=2;
# update employee4 set firstname="muneeb",lastname="ur rehman",Empzone="south" where EmpID=3;
# update employee4 set firstname="saad",lastname="ali khan",Empzone="north" where EmpID=4;
# update employee4 set firstname="abdullah",lastname="ahmed",Empzone="north" where EmpID=5;
# update employee4 set firstname="hamza",lastname="ahmed",Empzone="north" where EmpID=6;


# create table Department(
# DeptID int not null,
# DeptName varchar(200),
# primary key (DeptID),
# EmpID int,
# foreign key(EmpID) references employee4(EmpID) on delete cascade on update cascade
# );

# desc Department;

# select * from Department;

# insert into Department(DeptID,DeptName,EmpID) values(10,"marketing",2);
# insert into Department(DeptID,DeptName,EmpID) values(11,"operations",3);
# insert into Department(DeptID,DeptName,EmpID) values(12,"finance",4);


# update Department set EmpID=5 where EmpID=2;


# insert into employee4(EmpID,firstname,lastname,Empzone,Empsalary) values(6,"sahil","ifthekhar","north",7000);


# insert into Department(DeptID,DeptName,EmpID) values(14,"IT sector",6);


# update employee4 set EmpID=10 where EmpID=6;


# alter table Department add constraint foreign key(EmpID) references employee4(EmpID) on update cascade;



# create table employee5(
# EmpID int not null,
# firstname varchar(200),
# lastname varchar(200),
# unique(EmpID)
# );

# desc employee5;

# create table employee6(
# EmpID int not null,
# firstname varchar(200),
# lastname varchar(200),
# unique(EmpID),
# unique(firstname)
# );

# desc employee6;


# alter table employee6 add column PID int not null;

# alter table employee6 add constraint foreign key(PID) references employee5(EmpID) on delete cascade on update cascade;

# create table employee9(
# EmpID int not null,
# firstname varchar(200) default "operations",
# lastname varchar(200),
# unique(EmpID),
# unique(firstname)
# );

# desc employee9;
 
# alter table employee9 add column age int;

# alter table employee9 add constraint check(age>20);

# insert into employee9(EmpID,lastname,age) values(1,"rehman",24);

# select * from employee9;

# update employee9 set firstname="muneeb",lastname="ur rehman" where age=24;

# set SQL_SAFE_UPDATES=0;
 


# select * from employee4 where empzone="south" and empsalary=7000;

# select * from employee4 where empzone="south" or empsalary=7000;

# select * from employee4 where not empzone="south";

# select * from employee4 where empzone in("south","east");

# select * from employee4 where firstname like ("%a%");

# select * from employee4 where empzone like("___t");

# alter table employee4 add column age int;

# update employee4 set age=24 where firstname="muneeb";

# set sql_safe_updates=0;

# alter table employee4 modify column age int not null;

# update employee4 set age=24 where firstname="muneeb";
# update employee4 set age=21 where firstname="abdur";
# update employee4 set age=21 where firstname="abdullah";
# update employee4 set age=30 where firstname="Tom";
# update employee4 set age=26 where firstname="saad";
# update employee4 set age=24 where firstname="sahil";


# insert into employee4(EmpID,firstname,lastname,Empzone,empsalary,age) values(14,"hamza","ali","west",7000,20);

# desc employee4;

# select * from employee4 where age between 24 and 30;

























