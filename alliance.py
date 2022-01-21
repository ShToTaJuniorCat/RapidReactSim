from team import Team

class Alliance:
    def __init__(self, team1: Team, team2: Team, team3: Team):
        self.team1 = team1
        self.team2 = team2
        self.team3 = team3
        self.score = 0

    def __str__(self):
        return str(self.team1) + ", " + str(self.team2) + ", "  + str(self.team3)

    def raise_score(self, value: int):
        """
        Increases alliance's score by @value.

        @param value: The score to add to the alliance's score.\
        Negative to decrease.
        """
        self.score += value

    def get_teams(self):
        """
        @return: A list containing the three teams in the alliance.
        """
        return [self.team1, self.team2, self.team3]