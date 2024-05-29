class TaskDetailsManager:
    def __init__(self, br_task_details, br_task_info):
        self.taskInfo = br_task_info
        self.taskDetails = br_task_details
        self.font_size = 14
        self.column_values = {}

    def display_task_details(self):
        if len(self.column_values) == 0:
            return

        self.taskDetails.clear()

        style_label = 'style=\" background-color: #E2E9EE; text-align: center; vertical-align: middle; color: #145479; font-size: ' + str(self.font_size) + 'px; font-weight: bold; padding-left : 3px; padding-right : 3px;\"'
        style_text = 'style=\" vertical-align: middle; color: #050C4B; font-size: ' + str(self.font_size) + 'px; font-weight: normal; padding-left : 3px; padding-right : 3px\"'
        SAP_style_text = 'style=\" vertical-align: middle; color: #F50A77; font-size: ' + str(self.font_size) + 'px; font-weight: bold; padding-left : 3px; padding-right : 3px\"'

        html_task = f'''
        <table width = 100%><tbody>
          <tr>
            <td colspan = 8><p style = "font-size: 2px; text-align: center; vertical-align: middle; background-color: #E8E8E8;"></p></td>
        </tr>
        <tr>
            <td width = 100 {style_label}><p>Segment:</p></td><td {style_text}><b>{self.column_values['Segment']}<b></td>
            <td width = 100 {style_label}><p>Teczka:</p></td><td {style_text}><b>{self.column_values['Teczka']}<b></td>
            <td width = 100 {style_label}><p>Nr SAP:</p></td><td {SAP_style_text}>{self.column_values['Nr SAP']}</td>
            <td width = 100 {style_label}><p>Status:</p></td><td {self.set_style('Status', self.font_size)}>{self.set_symbol('Status', self.font_size)}</td>
        </tr>
         <tr>
            <td colspan = 8><p style = "font-size: 2px; text-align: center; vertical-align: middle; background-color: #E8E8E8;"></p></td>
        </tr>
        <tr>
            <td {style_label}><p>Wpływ:</p></td><td {style_text}>{self.column_values['Wpływ']}</td>
            <td {style_label}><p>Inżynier:</p></td><td {style_text}>{self.column_values['Inżynier']}</td>
            <td {style_label}><p>Zadanie:</p></td><td {style_text}>{self.column_values['Zadanie']}</td>
            <td {style_label}><p>Priorytet:</p></td><td {self.set_style('Priorytet', self.font_size)}>{self.column_values['Priorytet']}</td>
        </tr>
          <tr>
            <td colspan = 8><p style = "font-size: 2px; text-align: center; vertical-align: middle; background-color: #E8E8E8;"></p></td>
        </tr>
        <tr>
            <td {style_label}><p>Kategoria:</p></td><td  {style_text}>{self.column_values['Kategoria']}</td>
            <td {style_label}><p>Aktywność:</p></td><td {style_text}>{self.column_values['Aktywność']}</td>
            <td {style_label}><p>Termin do:</p></td><td {style_text}>{self.column_values['Termin do']}</td>
            <td {style_label}><p>Sygn. obca:</p></td><td {style_text}>{self.column_values['Sygnatura obca']}</td>
        </tr>
          <tr>
            <td colspan = 8><p style = "font-size: 2px; text-align: center; vertical-align: middle; background-color: #E8E8E8;"></p></td>
        </tr>
        </tbody></table>
        '''
        self.taskDetails.append(html_task)

        if self.column_values['Link'] != '-':
            style_href = 'style=\" color: #890D0D; font-size: ' + str(self.font_size) + 'px; font-weight: normal; padding-left : 3px; padding-right : 3px \"'''
            html_link = f'''
                          <table style = \" margin-top: 6px \"><tbody>
                          <tr>
                          <td width = 100 {style_label}><p>Link:</p></td>
                          <td {style_href}><a {style_href} href={self.column_values['Link']}>{self.column_values['Link']}</a></td>
                          </tr>
                            </tbody></table>
                      '''
            self.taskDetails.append(html_link)

        self.taskInfo.clear()

        html_info = f'''
            <table><tbody>
            <tr>
                <td width = 100 {style_label} ><p>Uwagi:</p></td>
                <td {style_text}>{self.column_values['Uwagi']}</td>
            </tr>
            </tbody></table>
            '''
        self.taskInfo.append(html_info)

    def set_symbol(self, field_name, font_size):
        match self.column_values[field_name]:
            case "Przygotowanie":
                return '<span style = "font-size: ' + str(font_size) + 'px; vertical-align: bottom;" > &#9835;</span> Przygotowanie'
            case "Realizacja":
                return '<span style = "font-size: ' + str(font_size) + 'px; vertical-align: bottom;" > &#9728;</span> Realizacja'
            case "Wykonany":
                return '<span style = "font-size: ' + str(font_size) + 'px; vertical-align: bottom;" > &#10004;</span> Wykonany'
            case "Rezygnacja":
                return '<span style = "font-size: ' + str(font_size) + 'px; vertical-align: bottom;" > &#10008;</span> Rezygnacja'
            case "Zawieszenie":
                return '<span style = "font-size: ' + str(font_size) + 'px; vertical-align: bottom;" > &#9729;</span> Zawieszenie'
            case "Przekazanie":
                return '<span style = "font-size: ' + str(font_size) + 'px; vertical-align: bottom;" > &#9755;</span> Przekazanie'

    def set_style(self, field_name, font_size):
        match self.column_values[field_name]:
            case "Przygotowanie":
                return 'style=\" vertical-align: top; color: #3E7309; font-size: ' + str(
                    font_size) + 'px; font-weight: bold; padding-left : 3px; padding-right : 3px\"'''
            case "Realizacja":
                return 'style=\" vertical-align: top; color: #663399; font-size: ' + str(
                    font_size) + 'px; font-weight: bold; padding-left : 3px; padding-right : 3px\"'''
            case "Wykonany":
                return 'style=\" vertical-align: top; color: #646161; font-size: ' + str(
                    font_size) + 'px; font-weight: bold; padding-left : 3px; padding-right : 3px\"'''
            case "Rezygnacja":
                return 'style=\" vertical-align: top; color: #813800; font-size: ' + str(
                    font_size) + 'px; font-weight: bold; padding-left : 3px; padding-right : 3px\"'''
            case "Zawieszenie":
                return 'style=\" vertical-align: top; color: #6C5A41; font-size: ' + str(
                    font_size) + 'px; font-weight: bold; padding-left : 3px; padding-right : 3px\"'''
            case "Przekazanie":
                return 'style=\" vertical-align: top; color: #7400DA; font-size: ' + str(
                    font_size) + 'px; font-weight: bold; padding-left : 3px; padding-right : 3px\"'''
            case "Tak":
                return 'style=\" vertical-align: middle; color: #EF0B0B; font-size: ' + str(
                    font_size) + 'px; font-weight: bold; padding-left : 3px; padding-right : 3px\"'''
            case "Nie":
                return 'style=\" vertical-align: middle; color: #000000; font-size: ' + str(
                    font_size) + 'px; font-weight: normal; padding-left : 3px; padding-right : 3px\"'''