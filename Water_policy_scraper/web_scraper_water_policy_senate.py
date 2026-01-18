import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options (no headless mode)
options = Options()

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# List of URLs to scrape
urls = [
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=1586&session=58-0&from=session&passsearchparams=session=58**subcommittees=1&minutes=0&chamber=S&from=search",  #58th
    "Uhttps://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=2408&session=57-0&from=session&passsearchparams=subcommittees=1**minutes=0&chamber=S&session=57&from=search",  #57th
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=1773&session=56-0&from=session&passsearchparams=minutes=0**session=56&subcommittees=1&chamber=S&from=search",     #56th
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=1797&session=55-0&from=session&passsearchparams=subcommittees=1**chamber=S&session=55&minutes=0&from=search",  #55th
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=1911&session=54-0&from=session&passsearchparams=minutes=0**session=54&chamber=S&subcommittees=1&from=search", #54th
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=2022&session=53-0&from=session&passsearchparams=minutes=0**chamber=S&subcommittees=1&session=53&from=search", #53rd
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=2225&session=52-0&from=session&passsearchparams=minutes=0**subcommittees=1&chamber=S&session=52&from=search", #52nd
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=2456&session=51-0&from=session&passsearchparams=session=51**chamber=S&minutes=0&subcommittees=1&from=search",     #51st
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=2577&session=47-0&from=session&passsearchparams=subcommittees=1**chamber=S&session=47&minutes=0&from=search", #47th
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=2938&session=46-0&from=session&passsearchparams=session=46**chamber=S&minutes=0&subcommittees=1&from=search", #46th
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=2702&session=45-0&from=session&passsearchparams=subcommittees=1**chamber=S&session=45&minutes=0&from=search", #45th
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=2740&session=44-0&from=session&passsearchparams=minutes=0**subcommittees=1&chamber=S&session=44&from=search", #44th
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3185&session=43-0&from=session&passsearchparams=chamber=S**subcommittees=1&minutes=0&session=43&from=search",#43rd
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=2991&session=42-0&from=session&passsearchparams=session=42**minutes=0&subcommittees=1&chamber=S&from=search",#42nd
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3110&session=41-0&from=session&passsearchparams=session=41**minutes=0&chamber=S&subcommittees=1&from=search",#41st
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3221&session=40-0&from=session&passsearchparams=chamber=S**minutes=0&session=40&subcommittees=1&from=search",#40th
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3295&session=39-0&from=session&passsearchparams=minutes=0**session=39&subcommittees=1&chamber=S&from=search",#39th
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3555&session=38-0&from=session&passsearchparams=minutes=0**chamber=S&subcommittees=1&session=38&from=search",#38th
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3407&session=37-0&from=session&passsearchparams=subcommittees=1**chamber=S&session=37&minutes=0&from=search",#37th
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3479&session=36-0&from=session&passsearchparams=session=36**subcommittees=1&chamber=S&minutes=0&from=search",#36th
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3771&session=35-0&from=search&passsearchparams=session=35**committeename=Mining%2C%20Irrigation%20and%20Drainage&chamber=S&minutes=0&subcommittees=1&from=search",#35th
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3587&session=34-0&from=session&passsearchparams=session=34**chamber=S&minutes=0&subcommittees=1&from=search",#34th
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3801&session=33-0&from=search&passsearchparams=chamber=S**minutes=0&session=33&subcommittees=1&committeename=%09Mining%20and%20Irrigation&from=search",#33rd
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3882&session=32-0&from=search&passsearchparams=minutes=0**session=32&chamber=S&subcommittees=1&committeename=%09Mining%20and%20Irrigation&from=search",#32nd
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3916&session=31-0&from=search&passsearchparams=minutes=0**subcommittees=1&chamber=S&committeename=%09Mining%20and%20Irrigation&session=31&from=search",#31st
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=4004&session=30-0&from=search&passsearchparams=committeename=%09Mining%20and%20Irrigation**subcommittees=1&session=30&chamber=S&minutes=0&from=search",#30th
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=4152&session=29-0&from=search&passsearchparams=session=29**minutes=0&chamber=S&committeename=%09Mining%20and%20Irrigation&subcommittees=1&from=search",#29th
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=4167&session=28-0&from=search&passsearchparams=committeename=%09Mining%20and%20Irrigation**chamber=S&minutes=0&subcommittees=1&session=28&from=search",#28th
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=4355&session=27-0&from=search&passsearchparams=minutes=0**subcommittees=1&session=27&committeename=%09Mining%20and%20Irrigation&chamber=S&from=search",#27th
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=4285&session=26-0&from=search&passsearchparams=minutes=0**chamber=S&subcommittees=1&session=26&committeename=%09Mining%20and%20Irrigation&from=search",#26th
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=4579&session=25-0&from=search&passsearchparams=chamber=S**committeename=%09Mining%20and%20Irrigation&subcommittees=1&session=25&minutes=0&from=search",#25th
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=4464&session=24-0&from=search&passsearchparams=minutes=0**chamber=S&subcommittees=1&committeename=%09Mining%20and%20Irrigation&session=24&from=search",#24th
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=5530&session=23-0&from=search&passsearchparams=chamber=S**minutes=0&subcommittees=1&committeename=%09Mining%20and%20Irrigation&session=23&from=search",#23rd
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=4500&session=22-0&from=search&passsearchparams=committeename=%09Mining%20and%20Irrigation**chamber=S&session=22&minutes=0&subcommittees=1&from=search",#22nd
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=4653&session=21-0&from=search&passsearchparams=session=21**committeename=%09Mining%20and%20Irrigation&subcommittees=1&chamber=S&minutes=0&from=search",#21st
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=11780&session=20-0&from=session&passsearchparams=minutes=0**subcommittees=1&session=20&chamber=S&from=search",#20th

    
]

# Initialize lists to store the data
chair = []
co_chair = []
vice_chairs = []
members = []

# Initialize a list to store all rows of data for the Excel file
all_rows_data = []

# Iterate over all the URLs
for url in urls:
    # Open the URL
    driver.get(url)
    
    # Wait for the page to load and the "Committee Members" section to appear
    try:
        # Wait until the "Committee Members" section is visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Committee Members']"))
        )
        
        # Find the committee members' hyperlinks under the "Committee Members" section
        committee_members = driver.find_elements(By.XPATH, "//h2[text()='Committee Members']/following::ul[1]//a")
        
        # Reset lists for each URL
        chair = []
        co_chair = []
        vice_chairs = []
        members = []

        # Loop through the links and navigate to each member's page
        for member_link in committee_members:
            name = member_link.text
            link = member_link.get_attribute('href')
            
            # Print the committee member's name and hyperlink
            print(f"Name: {name}, Link: {link}")
            
            # Click the hyperlink to go to the committee member's page
            member_link.click()
            
            # Wait for the new page to load and the 'top' anchor to appear
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "top"))
            )
            
            # Try to find the City/County information using the table row
            try:
                # Wait for the entire table to load properly
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//table"))
                )
                
                # Find all rows in the table
                rows = driver.find_elements(By.XPATH, "//table//tr")

                # Loop through all rows and get the City/County from the 6th <td> element (index 5)
                city_county_value = ""
                for row in rows:
                    columns = row.find_elements(By.TAG_NAME, "td")
                    
                    if len(columns) > 5:  # Ensure there are enough columns
                        city_county_value = columns[5].text.strip()  # 6th <td> (index 5) is City/County
                        if city_county_value:
                            # Clean up any extra spaces
                            city_county_value = ' '.join(city_county_value.split())
                            print(f"City/County: {city_county_value}")
                            break  # We only need the first valid City/County
                        
            except Exception as e:
                print(f"Error while extracting city/county: {e}")
            
            # Determine position (Chair, Co Chair, Vice Chair, Member) and store the data
            if "Chair" in name:
                if not chair:
                    chair = [name, city_county_value]
            elif "Co Chair" in name:
                if not co_chair:
                    co_chair = [name, city_county_value]
            elif "Vice Chair" in name:
                if len(vice_chairs) < 2:  # We want only 2 Vice Chairs
                    vice_chairs.append([name, city_county_value])
            else:
                members.append([name, city_county_value])

            # Go back to the committee members list
            driver.back()
            
            # Add a small delay to prevent overwhelming the server with requests
            time.sleep(2)
    
    except Exception as e:
        print(f"Error: {e}")
    
    # Collect data for the current URL into the row
    row_data = []

    # Add the chair, co-chair, vice chairs, and members to the row
    row_data.extend([chair[0] if chair else '', chair[1] if chair else ''])
    row_data.extend([co_chair[0] if co_chair else '', co_chair[1] if co_chair else ''])
    
    for i in range(2):
        if i < len(vice_chairs):
            row_data.extend([vice_chairs[i][0], vice_chairs[i][1]])
        else:
            row_data.extend(['', ''])
    
    for i in range(30):  # We are assuming there are up to 30 members
        if i < len(members):
            row_data.extend([members[i][0], members[i][1]])
        else:
            row_data.extend(['', ''])

    # Append the row data for this URL to the list of all rows
    all_rows_data.append(row_data)

# Convert to DataFrame
df = pd.DataFrame(all_rows_data, columns=[
    'Chair', 'Chair City',
    'Co Chair', 'Co Chair City',
    'Vice Chair 1', 'Vice Chair 1 City',
    'Vice Chair 2', 'Vice Chair 2 City',
    'Member 1', 'Member 1 City', 
    'Member 2', 'Member 2 City', 
    'Member 3', 'Member 3 City', 
    'Member 4', 'Member 4 City', 
    'Member 5', 'Member 5 City', 
    'Member 6', 'Member 6 City',
    'Member 7', 'Member 7 City', 
    'Member 8', 'Member 8 City',
    'Member 9', 'Member 9 City', 
    'Member 10', 'Member 10 City', 
    'Member 11', 'Member 11 City', 
    'Member 12', 'Member 12 City', 
    'Member 13', 'Member 13 City', 
    'Member 14', 'Member 14 City', 
    'Member 15', 'Member 15 City', 
    'Member 16', 'Member 16 City', 
    'Member 17', 'Member 17 City', 
    'Member 18', 'Member 18 City', 
    'Member 19', 'Member 19 City', 
    'Member 20', 'Member 20 City', 
    'Member 21', 'Member 21 City', 
    'Member 22', 'Member 22 City', 
    'Member 23', 'Member 23 City', 
    'Member 24', 'Member 24 City',
    'Member 25', 'Member 25 City', 
    'Member 26', 'Member 26 City', 
    'Member 27', 'Member 27 City', 
    'Member 28', 'Member 28 City', 
    'Member 29', 'Member 29 City',
    'Member 30', 'Member 30 City'
])

# Write to Excel file
excel_file_path = r"change to Path\for\output"
df.to_excel(excel_file_path, index=False)

# Close the driver after the operation
driver.quit()
