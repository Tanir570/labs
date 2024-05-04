import psycopg2 as pgsql
import csv

conn=pgsql.connect(host='localhost', 
    dbname='PhoneBook', 
    user='postgres', 
    password='1234')
cur = conn.cursor()


# Delete table
cur.execute('DROP TABLE phones_data CASCADE;')

conn.commit()

#1
# Create a new table
cur.execute("""CREATE TABLE phones_data (
            name VARCHAR(255),
            surname VARCHAR(255),
            phone_number VARCHAR(20)
);
""")

conn.commit()

#2
#upload data from csv file
filename = r'C:\Users\Танир\Desktop\lab1\lab 11\people.csv'

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        name, surname, phone_number = row
        
        # Create new students
        cur.execute(f"""INSERT INTO phones_data (name, surname, phone_number) VALUES 
                    ('{name}', '{surname}', '{phone_number}');
        """)

        conn.commit()

#PROCEDURES & functions
#1 searching by name
cur.execute("""CREATE OR REPLACE FUNCTION search_from_pb_byname(a character varying)
  RETURNS SETOF phones_data
AS
$$
SELECT * 
FROM phones_data 
WHERE name=a;
$$
language sql;
""")
#2 updating if exist inserting if not
cur.execute("""CREATE OR REPLACE PROCEDURE insert_to_pb(a character varying, b character varying, c integer)
LANGUAGE plpgsql
AS $$
DECLARE v_exists INTEGER;
BEGIN
    SELECT into v_exists (SELECT count(*) FROM public.phones_data WHERE surname = b AND name=a);
    IF v_exists=0 THEN
        INSERT INTO public.phones_data (name, surname, phone_number) values(a, b, c);
    END IF;
	IF v_exists IS NOT NULL THEN
        UPDATE public.phones_data
		SET phone_number = c
		WHERE name = a AND surname=b;
    END IF;
END;
$$;
""")
#3 inserting in loop

cur.execute("""CREATE OR REPLACE PROCEDURE insert_loop()
LANGUAGE plpgsql
AS $$
DECLARE
   m   text[];
   num int;
   arr text[] := '{{bichpaket,kuandyk,22222},{oralgazy,tair, 09099},{omarbayev, alen, 33333}}'; 
BEGIN
   FOREACH m SLICE 1 IN ARRAY arr
   LOOP
      SELECT INTO num CAST(m[3] AS INTEGER);
      INSERT INTO phones_data (name, surname, phone_number) values(m[1],m[2],num);
   END LOOP;
END
$$;""")

#4pagination
cur.execute("""CREATE OR REPLACE FUNCTION paginating(a integer, b integer)
RETURNS SETOF phones_data
AS $$
    SELECT * FROM phones_data 
	ORDER BY surname
	LIMIT a OFFSET b;
$$
language sql;""")

#5deleting
cur.execute("""CREATE OR REPLACE PROCEDURE delete_from_pb(a character varying, b character varying)
LANGUAGE plpgsql
AS $$
DECLARE v_exists INTEGER;
BEGIN
    SELECT into v_exists (SELECT count(*) FROM public.phones_data WHERE surname = b AND name=a);
	IF v_exists IS NOT NULL THEN
        DELETE FROM phones_data
		WHERE name=a AND surname=b;
    END IF;
END;
$$;""")

#executing
cur.execute("""CALL insert_to_pb('pessi','maladec',465465654);
""")
cur.execute("""SELECT *
FROM search_from_pb_byname('lol');""")
print(cur.fetchall())
cur.execute("""CALL insert_to_pb('hop', 'poh', 777);""")
cur.execute("""SELECT *
FROM paginating(5, 2);""")
print(cur.fetchall())
cur.execute("""CALL delete_from_pb('pessi', 'maladec');""")
cur.execute("""CALL insert_loop();""")


conn.commit()
cur.close()
conn.close()