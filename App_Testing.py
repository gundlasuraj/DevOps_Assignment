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
        self.app.workout_entry.insert(0, "Pushups")
        self.app.duration_entry.insert(0, "abc")
        self.app.add_workout()
        mock_showerror.assert_called_with("Error", "Duration must be a number.")

    @patch('tkinter.messagebox.showinfo')
    def test_add_workout_success(self, mock_showinfo):
        self.app.workout_entry.insert(0, "Pushups")
        self.app.duration_entry.insert(0, "30")
        self.app.add_workout()
        mock_showinfo.assert_called_with("Success", "'Pushups' added successfully!")
        self.assertEqual(len(self.app.workouts), 1)
        self.assertEqual(self.app.workouts[0]['workout'], "Pushups")
        self.assertEqual(self.app.workouts[0]['duration'], 30)

    @patch('tkinter.messagebox.showinfo')
    def test_view_workouts_empty(self, mock_showinfo):
        self.app.workouts = []
        self.app.view_workouts()
        mock_showinfo.assert_called_with("Workouts", "No workouts logged yet.")

    @patch('tkinter.messagebox.showinfo')
    def test_view_workouts_with_entries(self, mock_showinfo):
        self.app.workouts = [
            {"workout": "Pushups", "duration": 30},
            {"workout": "Squats", "duration": 20}
        ]
        self.app.view_workouts()
        expected = "Logged Workouts:\n1. Pushups - 30 minutes\n2. Squats - 20 minutes\n"
        mock_showinfo.assert_called_with("Workouts", expected)

if __name__ == '__main__':
    unittest.main()