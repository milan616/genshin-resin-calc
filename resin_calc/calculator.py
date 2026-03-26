from datetime import datetime, timedelta

class ResinCalculator:
    def __init__(self):
        self.MAX_RESIN = 200
        self.REGEN_RATE_MINUTES = 8
        self.REGEN_RATE_SECONDS = 60 * self.REGEN_RATE_MINUTES

    def calculate_current_resin(self, last_resin: int, last_updated_time: datetime) -> int:
        """
        Takes the resin count from the last time the user saved it
        and calculates how much they have 'now' based on elapsed time.
        """
        pass

    def time_to_target(self, current_resin: int, target_resin: int) -> datetime:
        """
        Calculates the specific clock time (HH:MM) when a user 
        will reach a target amount (like 160 or 200).
        """
        pass

    def decrement_resin(self, current_resin: int, amount: int) -> int:
        """
        Simple helper to subtract resin (20, 40, 60, etc.) 
        and ensure it doesn't go below 0.
        """
        pass

    def get_remaining_time_string(self, current_resin: int) -> str:
        """
        Returns a human-readable string: "Full in 14h 20m"
        Useful for your future Web GUI.
        """
        pass
