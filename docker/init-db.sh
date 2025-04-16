set -e

psql -v ON_ERROR_STOP=1 --username "${DB_USER}" <<-EOSQL
    CREATE DATABASE "tron_app_tests";
    CREATE DATABASE "tron_app";
EOSQL