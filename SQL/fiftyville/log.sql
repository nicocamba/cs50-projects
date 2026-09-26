-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Una idea general del crimen
SELECT description FROM crime_scene_reports WHERE(year = 2021 AND month = 7 AND day = 28 AND street="Humphrey Street");
-- Siguiendo el hilo de la descripción, veremos lo que dicen los testigos
SELECT * FROM interviews WHERE(year = 2021 AND month = 7 AND day = 28 AND transcript LIKE "%bakery%");
-- Vamos a mirar las cámaras de seguridad del establecimiento, según lo que nos ha comentado Ruth y a juntar las matriculas con sus respectivos conductores
SELECT name FROM people JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE(year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute > 14 AND minute < 26 AND activity = "exit");
-- Utilicemos ahora las pruebas otorgadas por el segundo sospechoso
SELECT name FROM people JOIN bank_accounts ON bank_accounts.person_id = people.id JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE(year = 2021 AND month = 7 AND day = 28 AND transaction_type = "withdraw" AND atm_location = "Leggett Street");
-- Si ahora comparamos ambos conjuntos solo nos quedan 4 sospechosos
SELECT name FROM people JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE(year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute > 14 AND minute < 26 AND activity = "exit")
INTERSECT
SELECT name FROM people JOIN bank_accounts ON bank_accounts.person_id = people.id JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE(year = 2021 AND month = 7 AND day = 28 AND transaction_type = "withdraw" AND atm_location = "Leggett Street");
-- Vamos ahora a consultar el primer vuelo del dia siguiente
SELECT name FROM people JOIN passengers ON passengers.passport_number = people.passport_number WHERE passengers.flight_id =
(SELECT id FROM flights WHERE(year = 2021 AND month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville"))
ORDER BY hour, minute
LIMIT 1);
-- Intersequemos ahora nuestros tres conjuntos de sospechosos
SELECT name FROM people JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE(year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute > 14 AND minute < 26 AND activity = "exit")
INTERSECT
SELECT name FROM people JOIN bank_accounts ON bank_accounts.person_id = people.id JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE(year = 2021 AND month = 7 AND day = 28 AND transaction_type = "withdraw" AND atm_location = "Leggett Street")
INTERSECT
SELECT name FROM people JOIN passengers ON passengers.passport_number = people.passport_number WHERE passengers.flight_id =
(SELECT id FROM flights WHERE(year = 2021 AND month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville"))
ORDER BY hour, minute
LIMIT 1);
-- Como ya solo nos quedan dos sospechosos, podemos consultar las llamadas realizadas
SELECT name FROM people JOIN phone_calls ON phone_calls.caller = people.phone_number WHERE(year = 2021 AND month = 7 AND day = 28 AND duration < 60);
-- Podemos confirmar que el culpable es Bruce
-- Si queremos averiguar quién es el cómplice basta con ver quien es el que recive la llamada de Bruce
SELECT name FROM people JOIN phone_calls ON phone_calls.receiver = people.phone_number WHERE(year = 2021 AND month = 7 AND day = 28 AND duration < 60 AND caller = (SELECT phone_number FROM people WHERE name = "Bruce"));
-- El cómplice es Robin
-- Finalmente falta por averiguar la ciudad de huida
SELECT city FROM airports WHERE id = (SELECT destination_airport_id FROM flights WHERE(year = 2021 AND month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville"))
ORDER BY hour, minute
LIMIT 1);
-- La ciudad es NYC