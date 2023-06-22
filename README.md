## WhatsApp Chat Analyzer

WhatsApp Chat Analyzer is a Python-based tool that allows users to analyze and visualize data from WhatsApp chat logs. It provides insights into message patterns, user activity, and trends within the chat group. With the help of interactive visualizations, users can gain a deeper understanding of their WhatsApp conversations and extract valuable information.

### Features

- **Upload Chat Logs**: Users can upload their WhatsApp chat log file in text format (.txt) using the intuitive file uploader interface.

- **Data Preprocessing**: The uploaded chat log is processed and converted into a structured format using the preprocessor module. The data is cleaned, and relevant information such as user names, timestamps, and messages are extracted.

- **User Analysis**: Users can explore the distribution of messages across different users in the chat. The tool provides visualizations such as bar charts, pie charts, scatter plots, area charts, bubble charts, and line charts to display the user-wise message counts.

- **Time Analysis**: Users can analyze message patterns over time. The tool offers visualizations such as bar charts, pie charts, scatter plots, area charts, bubble charts, and line charts to show the message counts across different months.

- **Month Vs User Analysis**: This feature enables users to visualize the distribution of messages across different months and users. It helps identify trends and patterns specific to individual users during different months.

- **Heatmap Analysis**: Users can explore the heatmap analysis to understand the distribution of messages throughout the week and different hours of the day. Heatmaps provide an easy-to-understand visualization of message activity.

- **Sunburst Analysis**: The tool offers a sunburst chart that shows the hierarchy of data from year to month to weekday to user. Users can explore the distribution of messages at each level and understand the overall message flow.

- **Word Cloud**: Users can generate a word cloud visualization that highlights the most frequently used words in the chat. This feature gives insights into the most common topics or themes discussed in the conversation.

### Getting Started

1. Clone the repository: `git clone https://github.com/your-username/whatsapp-chat-analyzer.git`

2. Install the required dependencies: `pip install -r requirements.txt`

3. Run the application: `streamlit run whatsapp_chat_analyzer.py`

4. Access the application in your web browser at `http://localhost:8501`

5. Upload your WhatsApp chat log file (.txt) and start exploring the analysis options.

### Technologies Used

- Python
- Pandas
- Streamlit
- Plotly
- Matplotlib

### Contributions

Contributions to the WhatsApp Chat Analyzer project are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request. Please make sure to follow the project's code of conduct and contribution guidelines.

### License

This project is licensed under the [MIT License](LICENSE).

### Acknowledgments

The WhatsApp Chat Analyzer project was inspired by the need to gain insights from WhatsApp chat logs and was developed as a learning project. Special thanks to the developers and contributors of the Pandas and Streamlit libraries for providing powerful tools for data analysis and web application development.
