import sqlite3


class Database:
    def __init__(self, connection='database.db'):
        self.db = sqlite3.connect(connection)
        self.cur = self.db.cursor()

    def add_value(self, data: dict):
        try:
            command = f'''
                INSERT INTO drivers
                (name, team, birth_date, wins, podiums, points, enteries, championships, nationality, fastest_laps, bio)
                VALUES ({data['name']},
                        {data['team']},
                        {data['birth_date']},
                        {data['wins']},
                        {data['podiums']},
                        {data['points']},
                        {data['enteries']},
                        {data['championships']},
                        {data['nationality']},
                        {data['fastest_laps']},
                        {data['bio']})
            '''
            self.cur.execute(command)
            self.cur.execute('COMMIT')
        except Exception:
            print('Error')

    def get_values(self):
        command = '''
            SELECT * FROM drivers
        '''

        self.cur.execute(command)
        return self.cur.fetchall()
