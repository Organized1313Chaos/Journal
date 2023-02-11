- query to show row number along with row_number
  ```
  SET @row_num = 0;
  SELECT @row_num := @row_num + 1 AS row_number, t.* FROM tablename t;
  ``` 