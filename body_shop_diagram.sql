-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/lm5ZNw
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "Customer" (
    "cust_id"  SERIAL  NOT NULL,
    "first_name" string   NOT NULL,
    "last_name" string   NOT NULL,
    CONSTRAINT "pk_Customer" PRIMARY KEY (
        "cust_id"
     )
);

CREATE TABLE "Car" (
    "car_id"  SERIAL  NOT NULL,
    "car_year" integer   NOT NULL,
    "car_make" string   NOT NULL,
    "car_model" string   NOT NULL,
    "drivable" boolean   NOT NULL,
    CONSTRAINT "pk_Car" PRIMARY KEY (
        "car_id"
     )
);

CREATE TABLE "Appt" (
    "date_and_time" timestamp   NOT NULL
);

