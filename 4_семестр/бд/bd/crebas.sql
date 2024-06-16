/*==============================================================*/
/*Ivan Kazakevich */
/*==============================================================*/




drop table S_CUSTOMER cascade constraints;

drop table S_DEPT cascade constraints;

drop table S_EMP cascade constraints;

drop table S_ITEM cascade constraints;

drop table S_ORD cascade constraints;

drop table S_PRODUCT cascade constraints;

drop table S_REGION cascade constraints;




/*==============================================================*/
/* Table: S_CUSTOMER                                            */
/*==============================================================*/
create table S_CUSTOMER 
(
   ID                   NUMBER(7)       ,
   NAME                 VARCHAR2(50) constraint  S_Cus_Name_nn not null,
   PHONE                VARCHAR2(25),
   ADDRESS              VARCHAR2(400),
   CITY                 VARCHAR2(30),
   STATE                VARCHAR2(20),
   COUNTRY              VARCHAR2(30),
   ZIP_CODE             VARCHAR2(75),
   CREDIT_RATING        VARCHAR2(9),
   SALES_REP_ID         NUMBER(7),
   REGION_ID            NUMBER(7),
   COMMENTS             VARCHAR2(255),
   constraint PK_S_CUSTOMER primary key (ID)
);
/*==============================================================*/
/* Table: S_DEPT                                                */
/*==============================================================*/
create table S_DEPT 
(
   ID                   NUMBER(7)       ,
   NAME                 VARCHAR2(25)constraint S_de_name_nn not null,
   REGION_ID            NUMBER(7),
   constraint PK_S_DEPT primary key (ID)
);

/*==============================================================*/
/* Table: S_EMP                                                 */
/*==============================================================*/
create table S_EMP 
(
   ID                   NUMBER(7)      , 
   LAST_NAME            VARCHAR2(25)constraint S_em_l_n_nn not null,
   FIRST_NAME           VARCHAR2(25),
   USERID               VARCHAR2(8)constraint S_em_us_nn not null,
   START_DATE           DATE,
   COMMENTS             VARCHAR2(25),
   MANAGER_ID           NUMBER(7),
   TITLE                VARCHAR2(25),
   DEPT_ID              NUMBER(7),
   SALARY               NUMBER(11,2),
   COMMISSION_PCT       NUMBER(4,2),
   constraint PK_S_EMP primary key (ID)
);
/*==============================================================*/
/* Table: S_ITEM                                                */
/*==============================================================*/
create table S_ITEM 
(
   ORD_ID               NUMBER(7) ,
   ITEM_ID              NUMBER(7),
   PRODUCT_ID           NUMBER(7), 
   PRICE                NUMBER(11,2),
   QUANTITY             NUMBER(9),
   QUANTITY_SHIPPED     NUMBER(9),
constraint PK_S_ITEM primary key (ORD_ID,PRODUCT_ID)
);
   
/*==============================================================*/
/* Table: S_ORD                                                 */
/*==============================================================*/
create table S_ORD 
(
	ID                             NUMBER(7),
    CUSTOMER_ID                    NUMBER(7),
    DATE_ORDERED                   DATE,
    DATE_SHIPPED                   DATE,
    SALES_REP_ID                   NUMBER(7),
    TOTAL                          NUMBER(11,2),
    PAYMENT_TYPE                   VARCHAR2(6),
    ORDER_FILLED                   VARCHAR2(1),
   constraint PK_S_ORD primary key (ID)
   );
   

/*==============================================================*/
/* Table: S_PRODUCT                                             */
/*==============================================================*/
create table S_PRODUCT 
(
   ID                   NUMBER(7) ,
   NAME                 VARCHAR2(50) constraint S_pr_na_nn not null,
   SHORT_DESC           VARCHAR2(255),
   LONGTEXT_ID          NUMBER(7),
   SUGGESTED_WHLSL_PRICE NUMBER(11,2),
   WHLSL_UNITS          VARCHAR2(25),
      constraint PK_S_PRODUCT primary key (ID)
   );
/*==============================================================*/
/* Table: S_REGION                                              */
/*==============================================================*/
create table S_REGION 
(
   ID                   NUMBER(7)            ,
   NAME                 VARCHAR2(50)  constraint S_re_na_nn not null,
   constraint PK_S_REGION primary key (ID)
);


alter table S_CUSTOMER
   add constraint FK_S_CUSTOM_REFERENCE_S_EMP foreign key (SALES_REP_ID)
      references S_EMP (ID);

alter table S_CUSTOMER
   add constraint FK_S_CUSTOM_REFERENCE_S_REGION foreign key (REGION_ID)
      references S_REGION (ID);

alter table S_DEPT
   add constraint FK_S_DEPT_VHH_S_REGION foreign key (REGION_ID)
      references S_REGION (ID);

alter table S_EMP               
   add constraint FK_S_EMP_REFERENCE_S_DEPT foreign key (DEPT_ID)
      references S_DEPT (ID);
	  
alter table S_EMP
   add constraint FK_S_EMP_REFERENCE_S_EMP foreign key (MANAGER_ID)
      references S_EMP (ID);

alter table S_ITEM
   add constraint FK_S_ITEM_REFERENCE_S_PRODUC foreign key (PRODUCT_ID)
      references S_PRODUCT (ID);
	  
alter table S_ITEM
   add constraint FK_S_ORD_REFERENCE_S_ITEM foreign key (ORD_ID)
      references S_ORD(ID);
	  
alter table S_ORD
   add constraint FK_S_ORD_REFERENCE_S_CUSTOM foreign key (CUSTOMER_ID)
      references S_CUSTOMER (ID);

alter table S_ORD
   add constraint FK_S_ORD_REFERENCE_S_EMP foreign key (SALES_REP_ID)
      references S_EMP (ID); 