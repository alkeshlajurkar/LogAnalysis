
# Log File Analysis Project 🎯

This project processes a web server log file and provides useful analysis based on IP request counts, the most frequently accessed endpoint, and any suspicious login activity. The script outputs the analysis results to both the terminal and a CSV file. 

## Project Structure 📁

- **`log_analysis.py`**: The Python script that performs log analysis and outputs the results. 
- **`log_analysis_results.csv`**: The generated CSV file containing the analysis results. 
- **`sample.log`**: A sample log file used for testing the script. 
- **`README.md`**: Project documentation. 

## Requirements ⚙️

- **Python 3.x**: Make sure you have Python 3 installed. 
- No additional dependencies are required for this script to work. 

## Features ✨

1. **IP Request Count**: The script counts the number of requests made by each IP address. 
2. **Most Frequently Accessed Endpoint**: Identifies the most frequently accessed endpoint in the log file. 
3. **Suspicious Activity Detection**: Detects IP addresses that have made more than a specified number of failed login attempts (status code `401`). 

## Usage 🚀

### 1. Clone the repository 

Clone the repository to your local machine:

```bash
git clone https://github.com/alkeshlajurkar/LogAnalysis.git
cd LogAnalysis
```

### 2. Run the Python script 

Ensure the required log file (`sample.log`) is in the same directory as the script, or adjust the **`LOG_FILE`** path in the script to match your log file location.

Run the script with:

```bash
python log_analysis.py
```

### 3. View the results 

After running the script, the analysis results will be saved to a **CSV** file (**`log_analysis_results.csv`**). You will also see the output printed in the terminal.

### 4. Input Format 

The log file (**`sample.log`**) should have entries in the following format:

```
IP_ADDRESS - - [DATE] "METHOD ENDPOINT HTTP_VERSION" STATUS_CODE OTHER_DATA
```

Example:

```
192.168.0.1 - - [10/Oct/2024:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 2326
```

### 5. Output Format 

- **CSV File (`log_analysis_results.csv`)**: Contains three sections:
  1. **Requests per IP**: List of IP addresses and their request counts. 🖥
  2. **Most Accessed Endpoint**: The most frequently accessed endpoint and its access count. 
  3. **Suspicious Activity**: IP addresses with more than **5** failed login attempts (401 status). 

## Example Output 📈

### IP Address Requests 

```
IP Address           Request Count
192.168.0.1          50
192.168.0.2          42
```

### Most Accessed Endpoint 

```
/index.html (Accessed 30 times)
```

### Suspicious Activity 

```
IP Address           Failed Login Attempts
192.168.0.3          6
```

## Customization 🛠️

You can modify the following parameters in the script:

- **`FAILED_LOGIN_THRESHOLD`**: Threshold for the number of failed login attempts (default is `5`). 
- **`LOG_FILE`**: Path to the log file (default is `sample.log`). 
- **`OUTPUT_FILE`**: Path to the output CSV file (default is `log_analysis_results.csv`). 

## Contributing 

Feel free to fork the repository and submit pull requests. Contributions are always welcome! 

## Connect with Me 🤝

Feel free to connect with me for collaborations or any questions related to full-stack development, data management, or personal finance:

- **LinkedIn**: [alkeshlajurkar](https://www.linkedin.com/in/alkeshlajurkar) 
- **Email**: alkeshlajurkar@gmail.com 

**GitHub Repository**: [GitHub Repo Link](https://github.com/alkeshlajurkar/LogAnalysis) 

