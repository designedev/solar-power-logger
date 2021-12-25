import pymysql
import config_loader as conf

def save_data(output, accum):
    db = conf.get_database_info()
    charset ='utf8'
    connection = pymysql.connect(host=db["host"], port=int(db["port"]), database=db["database"], user=db["user"], password=db["password"], charset=charset)
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    sql = "INSERT INTO solar_power_logs (output, accumulated_output) VALUES (%s, %s)"
    values = (output, accum)
    cursor.execute(sql, values)
    connection.commit()
    print("Checked Output: " + str(output) + "Kw, Accumulated Output : " + str(accum) + "Kw.")
    connection.close()