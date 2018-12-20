# Author: Rosalba Monterrosas
# Description: Initializes the statistics of the game (scores, level, and ship left)..

class GameStats():
	"""Track statistics for the game."""

	def __init__(self, ai_settings):
		"""Initialize statistics."""
		self.ai_settings = ai_settings
		self.reset_stats()

		# Start the game in an inactive state.
		self.game_active = False

		# High score should never be reset.
		with open('high_score.txt') as file_object:
		 	self.high_score = int(file_object.read())

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1