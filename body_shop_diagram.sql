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

