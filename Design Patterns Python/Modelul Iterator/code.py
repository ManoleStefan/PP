class FootbalTeamIterator:
    def __init__(self,members):
        self.members = members
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.members):
            val = self.members[self.index]
            self.index += 1
            return val
        raise StopIteration()

class FootbalTeam:
    def __init__(self,members):
        self.members = members

    def __iter__(self):
        return FootbalTeamIterator(self.members)

members = []
for x in range(1,23):
    members.append(f'jucator_nr_{str(x)}')
members.append('antrenor principal')
members.append('antrenor secund')
members.append('antrenor cu cafele')

team = FootbalTeam(members)
team_it = iter(team)

while True:
    try:
        print(next(team_it))
    except StopIteration:
        break