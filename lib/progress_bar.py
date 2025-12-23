import sys

class ProgressBar:
    def __init__(self, iteration, total, label='', barLength=30):
        self.total = total
        self.barLength = barLength
        self.updateProgress(iteration, label)

    def updateProgress(self, iteration, label):
        """Updates the visual progress bar in the terminal."""
        percent = float(iteration) / self.total
        filledLength = int(self.barLength * percent)
        bar = '=' * filledLength + '-' * (self.barLength - filledLength)
        
        # Clear line and rewrite
        sys.stdout.write(f'\r{label} [{bar}] {percent*100:.1f}%')
        sys.stdout.flush()
        
        if iteration == self.total:
            sys.stdout.write('\n')
