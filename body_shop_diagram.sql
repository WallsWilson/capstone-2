-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/lm5ZNw
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "CustomerReview" (
    "id" SERIAL NOT NULL,
    "name" VARCHAR(50) NOT NULL,
    "rating" FLOAT NOT NULL,
    "review_text" VARCHAR(500) NOT NULL,
    "created_at" TIMESTAMP NOT NULL
);

CREATE TABLE "Customer" (
    "cust_id"  SERIAL  NOT NULL,
    "first_name" VARCHAR(255)   NOT NULL,
    "last_name" VARCHAR(255)   NOT NULL,
    CONSTRAINT "pk_Customer" PRIMARY KEY ("cust_id")
);

CREATE TABLE "Car" (
    "car_id"  SERIAL  NOT NULL,
    "car_year" integer   NOT NULL,
    "car_make" VARCHAR(255)   NOT NULL,
    "car_model" VARCHAR(255)   NOT NULL,
    "drivable" boolean   NOT NULL,
    "cust_id" integer,
    CONSTRAINT "pk_Car" PRIMARY KEY ("car_id"),
    CONSTRAINT "fk_Car_Customer" FOREIGN KEY ("cust_id") REFERENCES "Customer" ("cust_id")
);

CREATE TABLE "Appt" (
    "date_and_time" timestamp   NOT NULL,
    "car_id" integer,
    CONSTRAINT "fk_Appt_Car" FOREIGN KEY ("car_id") REFERENCES "Car" ("car_id")
);

