"""
InnoDB is transactional. You need to call connection.commit() after inserts/deletes/updates.

"""
import pymysql


class manageDB():

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 3306
        self.database = 'dedsert-test'
        self.user = "root"
        self.password = "qwerty"
        # create table
        self.connection = pymysql.connect(self.host, self.user,
                                          self.password, self.database)
        self.cur = self.connection.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS dedsert_test(id INT NOT NULL AUTO_INCREMENT, name VARCHAR (40), age INT, job_title VARCHAR (40), PRIMARY KEY(id))ENGINE=InnoDB') 

    def __str__(self):
        pipeline = 'SELECT * FROM dedsert_test;'
        self.cur.execute(pipeline)
        info = [item for item in self.cur.fetchall()]
        return str(info)

    def add_user(self, name, age, job):
        pipeline = "INSERT INTO dedsert_test (name, age, job_title) VALUES('" + name + "'," + str(age) + ",'" + job + "');"
        self.cur.execute(pipeline)
        # InnoDB is transactional. You need to call connection.commit() after inserts/deletes/updates.
        self.connection.commit()
 
    def db_close(self):
        pipeline = 'Drop table dedsert_test;'
        self.cur.execute(pipeline)
        self.connection.commit()
        self.cur.close()
        self.connection.close()

if __name__ == "__main__":
    dedsert = manageDB()
    dedsert.add_user('bran14', 134, 'astronaut')
    print(dedsert)
    dedsert.db_close()
