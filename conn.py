import psycopg2

db = psycopg2.connect(user="postgres", database="sensor", port=5432, password="admin")

def insert(s):
    cur = db.cursor()
    #Insert into datagrama values('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36');
    str_Sql = "Insert into datagrama (col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18, col19, col20, col21, col22, col23, col24, col25, col26, col27, col28, col29, col30, col31, col32, col33, col34, col35, col36) values("
    for i in range(0,36):
        if(i<35):
            str_Sql+="%s,"
        else:
            str_Sql+="%s);"
    
    print(str_Sql %(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8],s[9],s[10],s[11],s[12],s[13],s[14],s[15],s[16],s[17],s[18],s[19],s[20],s[21],s[22],s[23],s[24],s[25],s[26],s[27],s[28],s[29],s[30],s[31],s[32],s[33],s[34],s[35]))
    
    cur.execute(str_Sql, (s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8],s[9],s[10],s[11],s[12],s[13],s[14],s[15],s[16],s[17],s[18],s[19],s[20],s[21],s[22],s[23],s[24],s[25],s[26],s[27],s[28],s[29],s[30],s[31],s[32],s[33],s[34],s[35]))
    db.commit()
    #db.close()
    

