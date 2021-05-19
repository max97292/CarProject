import getDriverBio
import formula1parser
from pprint import pprint as pp


class CompileParsed:
    drvbio = getDriverBio.GetDriverBio()
    ergast = list(drvbio.get_all_driver_data())
    formula = list(formula1parser.Formula1Parser.get_drivers())
    compiled = []

    @classmethod
    def to_dict(cls, name, team, birth, wins, podiums, points, entries, champships, nationality, fastest, bio):
        cls.compiled.append(
                        {
                            'name': name,
                            'team': team,
                            'birth_date': birth,
                            'wins': wins,
                            'podiums': podiums,
                            'points': points,
                            'entries': entries,
                            'championships': champships,
                            'nationality': nationality,
                            'fastest_laps': fastest,
                            'bio': bio
                        }
                    )

    # FIXME: need optimization, too much RAM use
    @classmethod
    def compile(cls):     
        for driver in cls.ergast:
            found = False

            # Checking if driver from ergast in drivers from formula,
            # And if it is - add to compiled list driver info from formula
            for driver2 in cls.formula:
                if driver['Name'] in driver2['name']:
                    found = True

                    cls.to_dict(driver2['name'],
                                driver2['team'],
                                driver2['date of birth'],
                                driver['Wins'],
                                driver2['podiums'],
                                driver2['points'],
                                driver2['grands prix entered'],
                                driver2['world championships'],
                                driver['Nationality'],
                                driver['Fastest laps'],
                                driver2['bio'])

                    break
            
            # Else add driver info from ergast
            if not found:
                cls.to_dict(driver['Name'],
                            driver['Teams'],
                            driver['dateOfBirth'],
                            driver['Wins'],
                            driver['Podiums'],
                            driver['Career points'],
                            driver['Entries'],
                            driver['Championships'],
                            driver['Nationality'],
                            driver['Fastest laps'],
                            'N/A')

        return cls.compiled


# pp(CompileParsed.compile())
