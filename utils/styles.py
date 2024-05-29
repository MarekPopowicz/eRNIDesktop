QHeaderView_qss = """
        QTableView::item {border: 0px; color: #050C4B; padding-left: 5px; padding-right: 5px; }
        QTableView::item:hover {color: #FF4D00;}
        QHeaderView::section {
                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                        stop:0 #EEEEEE, stop: 0.5 #DADDE1,
                                        stop: 0.6 #D2D5D8, stop:1 #D6D9DC);
                        border: 1px solid #D2D2D2; 
                        font-weight: bold;
                        padding-top: 3px; 
                        padding-bottom: 3px; 
                        padding-left: 5px; 
                        padding-right: 5px}

        QTableView::item:selected {
                        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, 
                         stop:0 #F3F4FF, stop: 0.5 #DEE0F5,
                         stop: 0.6 #CACDEC, stop:1 #DFE1F5);}
                        
        QTableView QTableCornerButton::section {background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                        stop:0 #EEEEEE, stop: 0.5 #DADDE1,
                                        stop: 0.6 #D2D5D8, stop:1 #D6D9DC);}
        """

QTabBar_qss = """
QTabWidget::tab-bar {left: 5px; }
QTabBar::tab {
    border: 1px solid #C4C4C3;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    min-width: 50ex;
    padding-left: 10px; padding-top: 5px; padding-bottom: 5px}
QTabBar::tab:selected { background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #EEEEEE, stop: 0.5 #DADDE1,
                                            stop: 0.6 #D2D5D8, stop:1 #D6D9DC);}
QTabBar::tab:selected { border-color: #9B9B9B;}
QTabBar::tab:!selected { margin-top: 2px; }
"""

