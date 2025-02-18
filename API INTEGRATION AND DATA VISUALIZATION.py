import requests
import json
import matplotlib.pyplot as plt
import pandas as pd

# --- API Integration ---

def fetch_data_from_api(api_url, params=None):
    """Fetches data from a given API endpoint.

    Args:
        api_url: The URL of the API.
        params: (Optional) A dictionary of query parameters.

    Returns:
        A JSON object containing the API response, or None if an error occurs.
    """
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return None



# Example API (replace with your actual API)
# I'm using a placeholder here, you'll have to find a suitable public API
# that returns data that's appropriate for visualization.
# Many options exist, like APIs for weather, stock prices, etc.

api_url = "https://jsonplaceholder.typicode.com/todos" # Example: Replace with your API URL
# If your API requires parameters, create a dictionary:
# params = {"userId": 1}  # Example
params = None # Or keep it None if no params needed


api_data = fetch_data_from_api(api_url, params)

if api_data is None:
    exit()  # Exit the script if API call fails


# --- Data Processing ---

# Example:  (Adapt this section based on your API's data structure)
# The JSONPlaceholder API returns a list of dictionaries.
# We'll create a Pandas DataFrame for easier manipulation.

df = pd.DataFrame(api_data)

# Example data cleaning/transformation (adapt as needed)
# Let's just select a few columns for this example

if 'completed' in df.columns and 'userId' in df.columns: # Check if columns exists before using them
    df_viz = df[['userId', 'completed']].groupby('userId')['completed'].sum().reset_index()
else:
    print("Required columns not found in data.  Adjust data processing.")
    exit() # Exit if essential data is missing


# --- Data Visualization ---

def create_bar_chart(data, x_label, y_label, title):
    """Creates a bar chart using matplotlib.

    Args:
        data: A Pandas DataFrame containing the data.
        x_label: Label for the x-axis.
        y_label: Label for the y-axis.
        title: Title of the chart.
    """
    plt.figure(figsize=(8, 6))  # Adjust figure size as needed
    plt.bar(data[x_label], data[y_label])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels if needed
    plt.tight_layout() # Adjust layout to prevent labels from overlapping
    plt.show()



# Example: Create a bar chart
create_bar_chart(df_viz, 'userId', 'completed', 'Number of Completed Todos per User')




# --- More Visualization Examples (Add as needed) ---

# You can add more visualizations based on your data and requirements.
# Examples:
# - Line charts (for time series data)
# - Scatter plots (for relationships between two variables)
# - Pie charts (for proportions)
# - Histograms (for distributions)

# Example: saving the plot to a file
# plt.savefig("my_chart.png") # Uncomment if you want to save

print("Data visualization complete.")
