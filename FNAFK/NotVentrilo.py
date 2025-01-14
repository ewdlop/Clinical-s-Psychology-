```python
from psychopy import visual, core, event, sound
import numpy as np

class VentriloquismExperiment:
    def __init__(self):
        # Initialize window
        self.win = visual.Window(
            size=[1024, 768],
            units="pix",
            fullscr=False,
            color="gray"
        )
        
        # Create stimuli
        self.face = visual.ImageStim(
            self.win,
            image="face.png",  # Need a face image
            size=(200, 200)
        )
        
        # Audio setup for different positions
        self.audio_left = sound.Sound("voice.wav")  # Need voice audio
        self.audio_center = sound.Sound("voice.wav")
        self.audio_right = sound.Sound("voice.wav")
        
        # Parameters
        self.positions = np.linspace(-300, 300, 7)  # 7 positions across screen
        self.visual_delay = 0.0  # Visual delay in seconds
        self.audio_delay = 0.0  # Audio delay in seconds
        
    def run_trial(self, visual_pos, audio_pos, duration=2.0):
        """Run a single trial with given visual and audio positions"""
        # Set positions
        self.face.pos = (visual_pos, 0)
        
        # Show face
        core.wait(self.visual_delay)
        self.face.draw()
        self.win.flip()
        
        # Play sound
        core.wait(self.audio_delay)
        if audio_pos < -100:
            self.audio_left.play()
        elif audio_pos > 100:
            self.audio_right.play()
        else:
            self.audio_center.play()
            
        # Wait for duration
        core.wait(duration)
        
        # Get response
        response = event.waitKeys(keyList=['left', 'right', 'space'])
        
        return response[0] if response else None

    def run_experiment(self, n_trials=50):
        """Run the full experiment"""
        results = []
        
        # Create trial list
        visual_positions = np.random.choice(self.positions, n_trials)
        audio_positions = np.random.choice(self.positions, n_trials)
        
        # Instructions
        instructions = visual.TextStim(
            self.win,
            text="観察者に合わせた指示を入れてください\n\nスペースキーで開始",
            height=30
        )
        instructions.draw()
        self.win.flip()
        event.waitKeys(keyList=['space'])
        
        # Run trials
        for v_pos, a_pos in zip(visual_positions, audio_positions):
            response = self.run_trial(v_pos, a_pos)
            results.append({
                'visual_pos': v_pos,
                'audio_pos': a_pos,
                'response': response
            })
            
            # Break between trials
            self.win.flip()
            core.wait(0.5)
            
        return results
        
    def save_results(self, results, filename):
        """Save results to file"""
        import json
        with open(filename, 'w') as f:
            json.dump(results, f)
            
    def cleanup(self):
        """Clean up resources"""
        self.win.close()
        core.quit()

# Extended version with additional features
class AdvancedVentriloquismExperiment(VentriloquismExperiment):
    def __init__(self):
        super().__init__()
        
        # Additional parameters
        self.fixation = visual.TextStim(
            self.win,
            text="+",
            height=30
        )
        
        # Progress bar
        self.progress = visual.Rect(
            self.win,
            width=0,
            height=10,
            fillColor="white",
            pos=(-400, -300)
        )
        
    def show_fixation(self, duration=0.5):
        """Show fixation cross"""
        self.fixation.draw()
        self.win.flip()
        core.wait(duration)
        
    def update_progress(self, current, total):
        """Update progress bar"""
        width = (current / total) * 800
        self.progress.width = width
        self.progress.pos = (-400 + width/2, -300)
        self.progress.draw()
        
    def run_trial(self, visual_pos, audio_pos, duration=2.0):
        """Enhanced trial with fixation and progress"""
        # Show fixation
        self.show_fixation()
        
        # Regular trial
        response = super().run_trial(visual_pos, audio_pos, duration)
        
        return response

if __name__ == "__main__":
    # Create and run experiment
    exp = AdvancedVentriloquismExperiment()
    try:
        results = exp.run_experiment()
        exp.save_results(results, "ventriloquism_results.json")
```
    finally:
        exp.cleanup()
