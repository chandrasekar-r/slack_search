# Slack Search App

The Slack Search App is a simple web application that allows users to search for questions and answers posted in their Slack workspace. The app fetches messages from all channels, processes and stores them in a SQLite database, and uses Elasticsearch to provide search functionality.

## Features

- Fetches messages from all channels in a Slack workspace
- Extracts questions and answers from messages
- Stores extracted data in a SQLite database
- Elasticsearch-based search functionality
- Web interface for submitting queries and displaying search results

## Installation

### Prerequisites

- Python 3.x
- Elasticsearch

### Steps

1. Clone the repository:
   ```python
   git clone https://github.com/yourusername/slack-search-app.git
   cd slack-search-app```

2. Set up a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate # On Windows, use venv\Scripts\activate
   ```

3. Install the required libraries:
    ```pip install -r requirements.txt```


4. Set up Slack API tokens:

- Create a Slack App and obtain the required API and App tokens (refer to [this guide](https://www.twilio.com/blog/how-to-build-a-slackbot-in-socket-mode-with-python)).
- Update the `config/config.py` file with your Slack API and App tokens:

  ```python
  SLACK_API_TOKEN = 'xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx'  # Replace with your Bot User OAuth Token
  SLACK_APP_TOKEN = 'xapp-xxxxxxxxxxxx-xxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx'  # Replace with your App Token
  ```

5. Set up Elasticsearch:

- Install and run Elasticsearch on your system or have access to a remote Elasticsearch instance.
- Update the `ELASTICSEARCH_HOST` and `ELASTICSEARCH_PORT` variables in `config/config.py` to match your Elasticsearch configuration.

## Usage

1. Navigate to the `app` directory in your project folder and run the following command:
   ```python app.py```

This will start the Flask development server on `http://localhost:5000/` or a similar URL. Open this URL in your web browser to access the search tool.

2. Enter a query in the search box and press the "Search" button. The search results should be displayed below the search box.

## Testing

1. Test the project with different queries, including edge cases and unexpected inputs, to identify any issues with the processing, storage, or search functionalities.

2. Add error handling for any potential errors that may arise, such as API rate limits, connection issues, or missing data.

3. (Optional) Use a testing framework like `pytest` to write test cases for the various functions and components of your project, such as Slack API integration, message processing, database storage, and Elasticsearch integration.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)



