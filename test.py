import getDriverBio
import formula1parser
from pprint import pprint as pp


class CompileParsed:
    drvbio = getDriverBio.GetDriverBio()
    ergast = list(drvbio.get_all_driver_data())
    formula = list(formula1parser.Formula1Parser.get_drivers())
    compiled = []

    @classmethod
    def compile(cls):
        for driver in cls.ergast:
            found = False

            for driver2 in cls.formula:
                if driver['Name'] in driver2['name']:
                    found = True

                    cls.compiled.append(
                        {
                            'name': driver2['name'],
                            'team': driver2['team'],
                            'birth_date': driver2['date of birth'],
                            'wins': driver['Wins'],
                            'podiums': driver2['podiums'],
                            'points': driver2['points'],
                            'entries': driver2['grands prix entered'],
                            'championships': driver2['world championships'],
                            'nationality': driver['Nationality'],
                            'fastest_laps': driver['Fastest laps'],
                            'bio': driver2['bio']
                        }
                    )

                    break

            if not found:
                cls.compiled.append(
                    {
                        'name': driver['Name'],
                        'team': driver['Teams'],
                        'birth_date': driver['dateOfBirth'],
                        'wins': driver['Wins'],
                        'podiums': driver['Podiums'],
                        'points': driver['Career points'],
                        'entries': driver['Entries'],
                        'championships': driver['Championships'],
                        'nationality': driver['Nationality'],
                        'fastest_laps': driver['Fastest laps'],
                        'bio': 'N/A'
                    }
                )

        return cls.compiled


# pp(CompileParsed.compile())