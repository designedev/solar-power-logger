import pymysql
import config_loader as conf

def save_data(output, accum):
    db = conf.get_database_info()
    charset ='utf8'
    connection = pymysql.connect(host=db["host"], port=int(db["port"]), database=db["database"], user=db["user"], password=db["password"], charset=charset)
    cursor = connection.cursor()

    # calculate daily output accum.
    prev_day_output_sql = "SELECT accumulated_output FROM solar_power_logs WHERE DATE(created_at) = DATE(NOW() - INTERVAL 1 DAY) order by id desc limit 1"
    cursor.execute(prev_day_output_sql)
    prev_daily_res = cursor.fetchall()
    prev_daily_accum = 0
    try:
        prev_daily_accum = prev_daily_res[0][0]
    except IndexError:
        print("no previous daily accum data. set to 0")

    #calculate monthly output accum.
    prev_month_output_sql = "SELECT accumulated_output from solar_power_logs where created_at between (LAST_DAY(DATE(NOW() - INTERVAL 2 MONTH)) + INTERVAL 1 DAY) AND LAST_DAY(DATE(NOW() - INTERVAL 1 MONTH)) order by id desc limit 1"
    cursor.execute(prev_month_output_sql)
    prev_monthly_res = cursor.fetchall()
    prev_monthy_accum = 0
    try:
        prev_daily_accum = prev_monthly_res[0][0]
    except IndexError:
        print("no previous monthly accum data. set to 0")

    insert_sql = "INSERT INTO solar_power_logs (output, accumulated_output, daily_accumulated_output, monthly_accumulated_output) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_sql, (output, accum, accum-prev_daily_accum, accum-prev_monthy_accum))
    connection.commit()
    print("Checked Output: " + str(output) + "Kw, Accumulated Output : " + str(accum) + "Kw. Daily Accumulated Output : " + str(accum-prev_daily_accum) + "Kw. Monthly Accumulated Output : " + str(accum-prev_monthy_accum) + "Kw.")
    connection.close()