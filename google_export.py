import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

def export_to_Google(my_list):
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name('skilled-mark-383315-2716c07d2268.json', scope)
    client = gspread.authorize(credentials)

    # Open the Google Sheet by name
    sheet_name = "1EGNI4kAzQD5XmOvdHzu2uS7br843fNCM4G16075Uwzw"
    worksheet_name = "1"
    sheet = client.open_by_key(sheet_name).worksheet(worksheet_name)


    records = sheet.get_all_values()
    records_no_first_column = [row[1:] for row in records]

    # print(records_no_first_column)




    if len(records) == 0:
        # write the header row
        header = ['date', 'phrase', 'text', 'link']
        sheet.insert_row(header, 1)

    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    # # write each row of data
    for row in my_list:
        data = [row['phrase'], row['text'], row['link']]

        if data not in records_no_first_column:
            data.insert(0, date)
            sheet.append_row(data)

    return f'https://docs.google.com/spreadsheets/d/{sheet_name}'