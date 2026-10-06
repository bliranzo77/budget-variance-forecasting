-- Fixes the 3 data problems in budget_data.csv.
-- Input: table "raw" (the CSV as loaded). Output: table "clean".
DROP TABLE IF EXISTS clean;

CREATE TABLE clean AS
SELECT DISTINCT                                                  -- 1. drop the duplicated row
       month,
       REPLACE(department, 'Marketng', 'Marketing') AS department, -- 2. fix the misspelled name
       budget,
       CASE WHEN actual IS NULL AND month <= '2026-09'           -- 3. a past month with no actual:
            THEN budget                                          --    assume it was on budget
            ELSE actual
       END AS actual
FROM raw;
