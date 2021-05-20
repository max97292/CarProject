import getDriverBio
import formula1parser
from pprint import pprint as pp


class CompileParsed:
    compiled = []

    @classmethod
    def to_dict(cls,
                name,
                team,
                birth,
                wins,
                podiums,
                points,
                entries,
                champships,
                nationality,
                fastest,
                bio):
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
    def compile(cls, limit=1000):
        drvbio = getDriverBio.GetDriverBio()
        for ergast_driver in drvbio.get_all_driver_data(limit):
            cls.to_dict(ergast_driver['Name'] if 'Name' in ergast_driver else 'N/A',
                        ergast_driver['Teams'] if 'Teams' in ergast_driver else 'N/A',
                        ergast_driver['dateOfBirth'] if 'dateOfBirth' in ergast_driver else 'N/A',
                        ergast_driver['Wins'] if 'Wins' in ergast_driver else 'N/A',
                        ergast_driver['Podiums'] if 'Podiums' in ergast_driver else 'N/A',
                        ergast_driver['Career points'] if 'Career points' in ergast_driver else 'N/A',
                        ergast_driver['Entries'] if 'Entries' in ergast_driver else 'N/A',
                        ergast_driver['Championships'] if 'Championships' in ergast_driver else 'N/A',
                        ergast_driver['Nationality'] if 'Nationality' in ergast_driver else 'N/A',
                        ergast_driver['Fastest laps'] if 'Fastest laps' in ergast_driver else 'N/A',
                        ergast_driver['Bio'] if 'Bio' in ergast_driver else 'N/A')

        for formula_driver in formula1parser.Formula1Parser.get_drivers():
            for compiled_driver in cls.compiled:
                if formula_driver['name'] in compiled_driver['name']:
                    break
                else:
                    cls.to_dict(formula_driver['name'],
                                formula_driver['team'],
                                formula_driver['date of birth'],
                                formula_driver['highest race finish'],
                                formula_driver['podiums'],
                                formula_driver['points'],
                                formula_driver['grands prix entered'],
                                formula_driver['world championships'],
                                formula_driver['country'],
                                'N/A',
                                formula_driver['bio'])
                    break

        return cls.compiled


# pp(CompileParsed.compile())
