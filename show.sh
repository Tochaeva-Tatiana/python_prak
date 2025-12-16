#!/usr/bin/env bash

ST_A="Точаева Татьяна"
ST_B="Стрелкина Ирина"
TOML_PATH="/path/to/personal.toml"

hworker $TOML_PATH -c update
hworker $TOML_PATH -c "show result" > test_data

cat test_data | grep "ID=${ST_A}.*USER_ID=${ST_A}" | head -n 1 || echo "Проверки тестов $ST_A на задачах $ST_A не было"
cat test_data | grep "ID=${ST_A}.*USER_ID=${ST_B}" | head -n 1 || echo "Проверки тестов $ST_B на задачах $ST_A не было"
cat test_data | grep "ID=${ST_B}.*USER_ID=${ST_A}" | head -n 1 || echo "Проверки тестов $ST_A на задачах $ST_B не было"
cat test_data | grep "ID=${ST_B}.*USER_ID=${ST_B}" | head -n 1 || echo "Проверки тестов $ST_B на задачах $ST_B не было"
