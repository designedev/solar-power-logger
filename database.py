import pymysql
import config_loader as conf

def save_data(output, accum):
    db = conf.get_database_info()
    charset ='utf8'
    connection = pymysql.connect(host=db["host"], port=int(db["port"]), database=db["database"], user=db["user"], password=db["password"], charset=charset)
    cursor = connection.cursor()

    select_sql = "SELECT accumulated_output FROM solar_power_logs WHERE DATE(created_at) = DATE(NOW() - INTERVAL 1 DAY) order by id desc limit 1"
    cursor.execute(select_sql)
    res = cursor.fetchall()
    previous_accum = 0
    try:
        previous_accum = res[0][0]
    except IndexError:
        print("no previous accum data. set to 0")

    insert_sql = "INSERT INTO solar_power_logs (output, accumulated_output, daily_accumulated_output) VALUES (%s, %s, %s)"
    cursor.execute(insert_sql, (output, accum, accum-previous_accum))
    connection.commit()
    print("Checked Output: " + str(output) + "Kw, Accumulated Output : " + str(accum) + "Kw. Dailt Accumulated Output : " + str(accum-previous_accum) + "Kw.")
    connection.close()