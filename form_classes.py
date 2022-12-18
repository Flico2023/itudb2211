#these classes are used for creating forms with WTForms
from wtforms import Form,StringField,validators,IntegerField,DecimalField


class TeamsForm(Form):
   team_name = StringField("Team name:", validators=[validators.InputRequired()])


class AttackForm(Form):
   team_name = StringField("Team name:", validators=[validators.InputRequired()])
   matches = IntegerField("Matches: ", validators=[validators.InputRequired()])
   total_corners = IntegerField("Total Corners: ", validators=[validators.InputRequired()])
   average_corners = DecimalField("Average Corners: ", validators=[validators.InputRequired()])
   crosses_attempted = IntegerField("Crosses Attempted: ", validators=[validators.InputRequired()])
   crossing_accuracy = IntegerField("Crossing Accuracy: ", validators=[validators.InputRequired()])

class AttemptsForm(Form):
   team_name = StringField("Team name:", validators=[validators.InputRequired()])
   matches = IntegerField("Matches: ", validators=[validators.InputRequired()])
   attempts = IntegerField("Attempts: ", validators=[validators.InputRequired()])
   attempts_on_target =IntegerField("Attempts On Target: ", validators=[validators.InputRequired()])
   attempts_off_target = IntegerField("Attempts Off Target: ", validators=[validators.InputRequired()])
   attempts_blocked = IntegerField("Attempts Blocked: ", validators=[validators.InputRequired()])

class GoalsForm(Form):
   team_name = StringField("Team name:", validators=[validators.InputRequired()])
   matches = IntegerField("Matches: ", validators=[validators.InputRequired()])
   total_goals = IntegerField("Total Goals: ", validators=[validators.InputRequired()])
   average_goals = DecimalField("Average Goals: ", validators=[validators.InputRequired()])
   goals_conceded =IntegerField("Goals Conceded: ", validators=[validators.InputRequired()])
   average_conceded = DecimalField("Average Conceded: ", validators=[validators.InputRequired()])
   goal_difference = IntegerField("Goal Difference: ", validators=[validators.InputRequired()])

class GoalTypeForm(Form):
   team_name = StringField("Team name:", validators=[validators.InputRequired()])
   goals = IntegerField("Goals: ", validators=[validators.InputRequired()])
   left_foot = IntegerField("Left Foot: ", validators=[validators.InputRequired()])
   right_foot = IntegerField("Right Foot: ", validators=[validators.InputRequired()])
   header =IntegerField("Header: ", validators=[validators.InputRequired()])
   own_goals = IntegerField("Own Goals: ", validators=[validators.InputRequired()])
   penalties = IntegerField("Penalties: ", validators=[validators.InputRequired()])


class DefenceForm(Form):
   team_name = StringField("Team name:", validators=[validators.InputRequired()])
   saves_made = IntegerField("Saves Made: ", validators=[validators.InputRequired()])
   blocks = IntegerField("Blocks: ", validators=[validators.InputRequired()])
   total_clearances = IntegerField("Total Clearances: ", validators=[validators.InputRequired()])
   interceptions = IntegerField("Interceptions: ", validators=[validators.InputRequired()])
   recoveries = IntegerField("Recoveries: ", validators=[validators.InputRequired()])
   goals_conceded = IntegerField("Goals Conceded: ", validators=[validators.InputRequired()])

class DisciplineForm(Form):
   team_name = StringField("Team name:", validators=[validators.InputRequired()])
   matches = IntegerField("Matches: ", validators=[validators.InputRequired()])
   fouls_won = IntegerField("Fouls Won: ", validators=[validators.InputRequired()])
   fouls_conceded =IntegerField("Fouls Conceded: ", validators=[validators.InputRequired()])
   yellow_cards = IntegerField("Yellow Cards: ", validators=[validators.InputRequired()])
   red_cards = IntegerField("Red Cards: ", validators=[validators.InputRequired()])

