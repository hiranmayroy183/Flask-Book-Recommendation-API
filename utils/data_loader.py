import pandas as pd

class DataLoader:
    def __init__(self, csv_path1, csv_path2):
        try:
            # Load the CSV files with error handling
            self.df1 = pd.read_csv(csv_path1, on_bad_lines='skip')
            self.df2 = pd.read_csv(csv_path2, on_bad_lines='skip')
        except Exception as e:
            print(f"Error reading CSV files: {e}")
            raise

    def get_combined_data(self):
        # Merge the two dataframes on 'bookID' and 'bookId'
        combined_df = pd.merge(self.df1, self.df2, left_on='bookID', right_on='bookId', how='inner')
        return combined_df

    def filter_by_author(self, author):
        # Filter books by author name
        combined_df = self.get_combined_data()
        return combined_df[combined_df['authors'].str.contains(author, case=False, na=False)]

    def get_recommendations(self, author=None):
        # Get book recommendations, optionally filtered by author
        combined_df = self.get_combined_data()
        if author:
            combined_df = self.filter_by_author(author)
        return combined_df.sort_values(by='average_rating', ascending=False).reset_index(drop=True)
