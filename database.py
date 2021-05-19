import sqlite3


class Database:
    def __init__(self):
        self.db = sqlite3.connect('database.db')
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
