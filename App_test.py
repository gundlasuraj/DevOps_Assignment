import unittest
from unittest.mock import MagicMock, patch
import tkinter as tk
from ACEest_Fitness import FitnessTrackerApp

class TestFitnessTrackerApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main window during tests
        self.app = FitnessTrackerApp(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch('tkinter.messagebox.showerror')
    def test_add_workout_empty_fields(self, mock_showerror):
        self.app.workout_entry.delete(0, tk.END)
        self.app.duration_entry.delete(0, tk.END)
        self.app.add_workout()
        mock_showerror.assert_called_with("Error", "Please enter both workout and duration.")

    @patch('tkinter.messagebox.showerror')
    def test_add_workout_invalid_duration(self, mock_showerror):
        """Tests that an error is shown if the duration is not a valid integer."""
        self.app.workout_entry.insert(0, "Pushups")
        self.app.duration_entry.insert(0, "abc")
        self.app.add_workout()
        mock_showerror.assert_called_with("Error", "Duration must be a number.")
        self.assertEqual(len(self.app.workouts), 0)
        #self.root.destroy()

    @patch('tkinter.messagebox.showerror')
    def test_add_workout_only_workout_filled(self, mock_showerror):
        """Tests that an error is shown if only the workout name is provided."""
        # Arrange: Insert text only into the workout field.
        # The duration field is empty by default from setUp.
        self.app.workout_entry.insert(0, "Running")

        # Act: Call the method to be tested.
        self.app.add_workout()

        # Assert: Check that the correct error was shown and no workout was added.
        mock_showerror.assert_called_with("Error", "Please enter both workout and duration.")
        self.assertEqual(len(self.app.workouts), 0)
        #self.root.destroy()

    @patch('tkinter.messagebox.showinfo')
    def test_add_workout_with_valid_data(self, mock_messagebox):
        """Tests that a valid workout is successfully added to the list."""
        # Arrange: Set up the inputs for a valid workout.
        workout_name = "Squats"
        duration = "45"
        self.app.workout_entry.insert(0, workout_name)
        self.app.duration_entry.insert(0, duration)

        # Act: Call the method to be tested.
        self.app.add_workout()

        mock_messagebox.assert_called_with("Success", f"'{workout_name}' added successfully!")

        # Assert: Check that the application's internal state is correct.
        self.assertEqual(len(self.app.workouts), 1)
        self.assertEqual(self.app.workouts[0]['workout'], workout_name)
        self.assertEqual(self.app.workouts[0]['duration'], int(duration))

    @patch('tkinter.messagebox.showerror')
    def test_add_workout_zero_duration(self, mock_showerror):
        """Tests that an error is shown for a workout with zero duration."""
        workout_name = "Stretching"
        duration = "0"
        self.app.workout_entry.insert(0, workout_name)
        self.app.duration_entry.insert(0, duration)
        self.app.add_workout()
        mock_showerror.assert_called_with("Error", "Duration must be a positive number.")
        self.assertEqual(len(self.app.workouts), 0)

    @patch('tkinter.messagebox.showerror')
    def test_add_workout_negative_duration(self, mock_showerror):
        """Tests that an error is shown for a workout with a negative duration."""
        self.app.workout_entry.insert(0, "Time Travel")
        self.app.duration_entry.insert(0, "-10")
        self.app.add_workout()
        mock_showerror.assert_called_with("Error", "Duration must be a positive number.")
        self.assertEqual(len(self.app.workouts), 0)
    
    @patch('tkinter.messagebox.showinfo')
    def test_view_workouts_empty(self, mock_showinfo):
        """Tests that the correct message is shown when viewing an empty workout list."""
        # Arrange: The workout list is empty by default after setUp, but we can be explicit.
        self.app.workouts = []

        # Act: Call the method to be tested.
        self.app.view_workouts()

        # Assert: Verify the message box was shown with the "no workouts" message.
        mock_showinfo.assert_called_with("Workouts", "No workouts logged yet.")

    @patch('tkinter.messagebox.showinfo')
    def test_view_workouts_with_entries(self, mock_showinfo):
        """Tests that the view_workouts method correctly formats and displays a list of workouts."""
        # Arrange: Manually set the workouts list to a known state
        self.app.workouts = [
            {"workout": "Pushups", "duration": 30},
            {"workout": "Squats", "duration": 20}
        ]
        expected_text = "Logged Workouts:\n1. Pushups - 30 minutes\n2. Squats - 20 minutes\n"

        # Act: Call the method to be tested
        self.app.view_workouts()
        # Assert: Verify the message box was shown with the correctly formatted string
        mock_showinfo.assert_called_with("Workouts", expected_text)

if __name__ == '__main__':
    unittest.main()