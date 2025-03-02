import gspread
from google.oauth2.service_account import Credentials
from books import books
#import share_book
#import ping_user

# Define the correct scopes
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

try:
    creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
    client = gspread.authorize(creds)
    
    sheet_id = "1Mthh3RTYPiov3WLM-JvrV6zTI8rlaKssv0djRkw6PZE"
    workbook = client.open_by_key(sheet_id)

except FileNotFoundError:
    print("Error: credentials.json file not found. Please ensure it exists in the correct location.")
    exit(1)
except Exception as e:
    print(f"Error connecting to Google Sheets: {str(e)}")
    exit(1)

def main():
    # Create an instance of the books class
    book_manager = books()
    tyler_Lib = workbook.worksheet("Tyler's Lib")
    #tyler_Lib.update_title("Tyler's Lib")

    
    #books call here for inputs
    print("What is the title of the book?")
    title = input()
    print("Who is the author?")
    author = input()
    print("how would you rate this book from 1 - 5?")
    rating = int(input())  # Convert the rating input to an integer

    book_data = book_manager.book_inputs(title, author, rating)

    try:
        # Get the next empty row
        values = tyler_Lib.get_all_values()
        next_row = len(values) + 1
        
        # Update the cells in the next empty row
        tyler_Lib.update_cell(next_row, 1, book_data['title'])
        tyler_Lib.update_cell(next_row, 2, book_data['author'])
        tyler_Lib.update_cell(next_row, 3, book_data['rating'])
        
        print(f"Book added successfully to row {next_row}")
        
    except Exception as e:
        print(f"Error accessing spreadsheet: {str(e)}")

    #share the book using SQL or google sheets
    #ping the other user if book is of interest

if __name__ == "__main__":
    main()