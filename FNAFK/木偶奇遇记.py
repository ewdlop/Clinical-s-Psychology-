```python
from psychopy import visual, core, event, data, gui
import random
import json

class PinocchioExperiment:
    def __init__(self):
        # Initialize experiment window
        self.win = visual.Window(
            size=[1024, 768],
            units="pix",
            fullscr=False,
            color="white"
        )
        
        # Create stimuli
        self._setup_stimuli()
        
        # Setup data storage
        self.data = []
        self.participant_info = self._get_participant_info()
        
    def _get_participant_info(self):
        """Get participant information through dialog box"""
        dlg = gui.DlgFromDict(
            dictionary={
                'Participant ID': '',
                'Age': '',
                'Gender': ['M', 'F', 'Other'],
            },
            title='Pinocchio Experiment'
        )
        
        if dlg.OK:
            return dlg.dictionary
        else:
            core.quit()

    def _setup_stimuli(self):
        """Setup all visual stimuli"""
        # Face base
        self.face = visual.ImageStim(
            win=self.win,
            image="face.png",  # Need base face image
            pos=(0, 0),
            size=(200, 200)
        )
        
        # Nose (will be manipulated)
        self.nose = visual.Line(
            win=self.win,
            start=(0, 0),
            end=(50, 0),
            lineWidth=5,
            lineColor="black"
        )
        
        # Questions
        self.question_text = visual.TextStim(
            win=self.win,
            text="",
            height=30,
            color="black",
            pos=(0, 200)
        )
        
        # Response options
        self.truth_option = visual.TextStim(
            win=self.win,
            text="Truth (T)",
            height=20,
            color="green",
            pos=(-200, -200)
        )
        
        self.lie_option = visual.TextStim(
            win=self.win,
            text="Lie (L)",
            height=20,
            color="red",
            pos=(200, -200)
        )
        
        # Feedback
        self.feedback = visual.TextStim(
            win=self.win,
            text="",
            height=30,
            color="black",
            pos=(0, -100)
        )

    def _load_questions(self):
        """Load experimental questions"""
        return [
            {
                "question": "Have you ever cheated on a test?",
                "type": "personal",
                "social_desirability": "low"
            },
            {
                "question": "Do you always wash your hands after using the bathroom?",
                "type": "personal",
                "social_desirability": "high"
            },
            # Add more questions...
        ]

    def run_trial(self, question_data):
        """Run a single trial"""
        # Show question
        self.question_text.text = question_data["question"]
        self.question_text.draw()
        self.face.draw()
        self.nose.draw()
        self.truth_option.draw()
        self.lie_option.draw()
        self.win.flip()
        
        # Get response
        response = event.waitKeys(keyList=['t', 'l'])[0]
        
        # Record response time
        response_time = core.getTime()
        
        # Process response and show feedback
        if response == 'l':  # Lie
            # Grow nose
            for length in range(50, 150, 10):
                self.nose.end = (length, 0)
                self._draw_all()
                core.wait(0.1)
        
        return {
            "question": question_data["question"],
            "question_type": question_data["type"],
            "social_desirability": question_data["social_desirability"],
            "response": response,
            "response_time": response_time
        }

    def _draw_all(self):
        """Draw all stimuli"""
        self.face.draw()
        self.nose.draw()
        self.question_text.draw()
        self.truth_option.draw()
        self.lie_option.draw()
        self.win.flip()

    def run_experiment(self):
        """Run the full experiment"""
        # Load questions
        questions = self._load_questions()
        random.shuffle(questions)
        
        # Instructions
        instructions = visual.TextStim(
            win=self.win,
            text="Welcome to the experiment!\n\n" +
                 "You will be asked several questions.\n" +
                 "Press 'T' for truth or 'L' for lie.\n\n" +
                 "Press SPACE to begin.",
            height=30,
            color="black"
        )
        instructions.draw()
        self.win.flip()
        event.waitKeys(keyList=['space'])
        
        # Run trials
        for question in questions:
            trial_data = self.run_trial(question)
            self.data.append(trial_data)
            
            # Inter-trial interval
            self.win.flip()
            core.wait(1.0)
            
            # Reset nose
            self.nose.end = (50, 0)
        
        # Save data
        self._save_data()
        
    def _save_data(self):
        """Save experimental data"""
        output = {
            'participant': self.participant_info,
            'trials': self.data
        }
        
        filename = f"pinocchio_data_{self.participant_info['Participant ID']}.json"
        with open(filename, 'w') as f:
            json.dump(output, f)
    
    def cleanup(self):
        """Clean up resources"""
        self.win.close()
        core.quit()

if __name__ == "__main__":
    exp = PinocchioExperiment()
    try:
        exp.run_experiment()
    finally:
        exp.cleanup()
```
