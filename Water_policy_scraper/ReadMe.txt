Texas Legislative Committee Scraper

This repository contains Python scripts that scrape historical and current committee membership data from the Texas Legislature website. The scripts extract member names, positions (Chair, Co-Chair, Vice Chair, Members), and associated City/County information, then organize the data into structured Excel files for analysis.

## Methods 

The scraping workflow is automated using Python and Selenium:

# Initialize WebDriver:
ChromeDriver is launched via webdriver_manager, with configurable Chrome options. The browser runs in normal (non-headless) mode to allow page loading.

# Iterate over URLs:
A list of committee URLs spanning multiple legislative sessions is provided. Each script targets either House or Senate committees for specific sessions.

# Extract Committee Members:

The script waits for the "Committee Members" section to load.

Each member link is visited to gather additional details, particularly City/County information from member profile tables.

# Determine Member Position:
Member names are parsed for titles (Chair, Co-Chair, Vice Chair). Remaining members are categorized as standard members. Up to two Vice Chairs and thirty members are captured per committee.

# Organize Data into Excel:
Each committee's data is compiled into a single row in a Pandas DataFrame with columns for Chair, Co-Chair, Vice Chairs, and Members, along with their respective cities. The DataFrame is exported as an Excel file for downstream use.

# Error Handling and Navigation:
The scripts handle missing data, table loading issues, and navigation back to the main committee page, with short delays to avoid overwhelming the server.