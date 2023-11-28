from PyQt6.QtWidgets import QMainWindow, QRadioButton
from gui import Ui_MainWindow


class Logic(QMainWindow, Ui_MainWindow):
    """Class set to program the voting system in the GUI."""

    def __init__(self):
        """Initializer to the Logic class."""
        super().__init__()
        self.amy_count: int = 0
        self.joseph_count: int = 0
        self.jenny_count: int = 0
        self.ben_count: int = 0
        self.setupUi(self)

        self.submit_button.clicked.connect(lambda: self.submit())
        self.result_button.clicked.connect(lambda: self.result())

    def submit(self) -> None:
        """The submit button on the GUI. Submits and collects the response data."""
        selected_button: QRadioButton = None
        candidate_name: str = ""

        if self.amy_button.isChecked():
            self.amy_count += 1
            selected_button = self.amy_button
            candidate_name = "Amy Dane"
        elif self.joseph_button.isChecked():
            self.joseph_count += 1
            selected_button = self.joseph_button
            candidate_name = "Joseph Strong"
        elif self.jenny_button.isChecked():
            self.jenny_count += 1
            selected_button = self.jenny_button
            candidate_name = "Jenny Apple"
        elif self.ben_button.isChecked():
            self.ben_count += 1
            selected_button = self.ben_button
            candidate_name = "Ben Dianca"

        if selected_button:
            self.result_label.setText(f'     Your response has been submitted.\n     You picked: {candidate_name}')
        else:
            self.result_label.setText(f'\tPlease select a candidate.')

    def result(self) -> None:
        """Displays the results from the voting process when pressing "View Results" in the GUI."""
        max_count: int = max(self.amy_count, self.joseph_count, self.jenny_count, self.ben_count)

        result_text: str = (f'Amy Dane -  {self.amy_count}\n'
                            f'Joseph Strong - {self.joseph_count}\n'
                            f'Jenny Apple - {self.jenny_count}\n'
                            f'Ben Dianca - {self.ben_count}\n\n'
                            f'TOTAL -  {self.amy_count + self.joseph_count + self.jenny_count + self.ben_count} Votes'
                            f'\n\n')

        winners = [candidate for candidate, count in
                   [('Amy Dane', self.amy_count),
                    ('Joseph Strong', self.joseph_count),
                    ('Jenny Apple', self.jenny_count),
                    ('Ben Dianca', self.ben_count)]
                   if count == max_count]

        if len(winners) == 1:
            result_text += f'{winners[0]} WINS!'
        else:
            result_text += 'It\'s a TIE between:\n' + '\nand '.join(winners) + '!'

        self.result_label.setText(result_text)
