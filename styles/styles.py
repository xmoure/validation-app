styles_table_files = '''
    QTableWidget {
        gridline-color:#d4d9d7 ;
    }
    QHeaderView::section {
        border-style: solid;
        border-width: 1px;
        border-color: #d4d9d7;
        padding: 4px;
        background-color: #009879;
        color: #ffffff;
        text-align: left;

    }

    QTableWidget::item:selected {
        background-color: transparent;
    }

    QTableWidget::item {
        border-bottom: 1px solid #dddddd; /* Horizontal line */
        border-right: 1px solid #dddddd;  /* Vertical line */
        padding-left: 10px
    }

    QHeaderView::section:first {
            /* Specific style for the first header */
            border-top-left-radius: 10px;
            border-bottom-left-radius: 10px;
    }
    QHeaderView::section:last {
            /* Specific style for the last header */
            border-top-right-radius: 10px;
            border-bottom-right-radius: 10px;
    }
'''


styles_table_test = '''
    QTableWidget {
        border-radius: 10px;
        selection-background-color: #FFFFFF;
        alternate-background-color: #FFFFFF;
        background:#cfc6cb;
    }
    QHeaderView::section {
        background-color: #324960;
        color: white;
        padding-left: 4px; /* Align text to the left */
        border: none;
        border-bottom: 1px solid white;
    }
    QHeaderView::section:first {
        border-top-left-radius: 10px;
    }
    QHeaderView::section:last:horizontal {
        border-top-right-radius: 10px;
    }

    QHeaderView::section:last:vertical {
        border-bottom-left-radius: 10px;
    }


'''

styles_btn_disabled = '''
    QPushButton:disabled {
        background-color: #C0C0C0;
        color: white;
    }
'''

styles_btn_enabled = '''
    QPushButton:enabled {
        background-color: #ff6e40;
        color: white;
    }
'''