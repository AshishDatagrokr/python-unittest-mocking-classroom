import mysql.connector

class DbHelper:

    def get_connection():    
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host=hostip,
                                       database=database,
                                       user=user,
                                       password=pswd)
        if conn.is_connected():
            print('Connected to MySQL database')
 
    except Error as e:
        print(e)
    return conn




    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        query = 'select max(salary) as max_salary from salaries'
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0]

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        query = 'select min(salary) as min_salary from salaries'
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0]
    
    def max_salary_is_greater_than_min(self):
        max_salary = self.get_maximum_salary()
        min_salary = self.get_minimum_salary()
        if max_salary > min_salary:
            return True
        else:
            return False

if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)
