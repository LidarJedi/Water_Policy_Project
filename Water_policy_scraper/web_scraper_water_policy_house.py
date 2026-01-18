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
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=12192&session=88-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",  #88th
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=12106&session=87-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=12004&session=86-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=11859&session=85-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=11624&session=84-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=11494&session=83-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=11394&session=82-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=10315&session=81-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=9718&session=80-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=9284&session=79-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=8780&session=78-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=502&session=77-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=713&session=76-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=1063&session=75-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=593&session=74-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=765&session=73-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=1311&session=72-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=835&session=71-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=882&session=70-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=938&session=69-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=971&session=68-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=1126&session=67-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=1224&session=66-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=1378&session=65-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=1430&session=64-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=1344&session=63-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=1534&session=62-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=9135&session=62-0&from=search&passsearchparams=minutes=0**chamber=H&subcommittees=1&committeename=natural%20resources&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=2759&session=61-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=7327&session=61-0&from=search&passsearchparams=chamber=H**committeename=desalination%20of&subcommittees=1&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=1611&session=60-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=7233&session=60-0&from=search&passsearchparams=subcommittees=1**chamber=H&committeename=water&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=2050&session=59-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=7198&session=59-0&from=search&passsearchparams=subcommittees=1**minutes=0&committeename=water%20resources&chamber=H&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=1690&session=58-0&from=session&passsearchparams=chamber=H**subcommittees=1&session=58&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=7159&session=58-0&from=session&passsearchparams=chamber=H**subcommittees=1&session=58&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=1865&session=57-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=2113&session=56-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=7093&session=56-0&from=search&passsearchparams=subcommittees=1**chamber=H&committeename=local%20water%20districts&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=1818&session=55-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=1955&session=54-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=2070&session=53-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=2265&session=52-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=2428&session=51-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=2319&session=50-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=2846&session=49-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=2512&session=48-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=2594&session=47-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3973&session=46-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=2636&session=45-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=2805&session=44-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3056&session=43-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3011&session=42-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3130&session=41-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3241&session=40-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3314&session=39-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3426&session=38-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3351&session=37-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3499&session=36-0&from=search&passsearchparams=committeename=conservation%20and**subcommittees=1&chamber=H&minutes=0&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3731&session=35-0&from=search&passsearchparams=subcommittees=1**committeename=irrigation&minutes=0&chamber=H&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3636&session=34-0&from=search&passsearchparams=subcommittees=1**committeename=irrigation&minutes=0&chamber=H&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3720&session=33-0&from=search&passsearchparams=subcommittees=1**committeename=irrigation&minutes=0&chamber=H&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3848&session=32-0&from=search&passsearchparams=subcommittees=1**committeename=irrigation&minutes=0&chamber=H&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=3963&session=31-0&from=search&passsearchparams=subcommittees=1**committeename=irrigation&minutes=0&chamber=H&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=4071&session=30-0&from=search&passsearchparams=subcommittees=1**committeename=irrigation&minutes=0&chamber=H&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=4123&session=29-0&from=search&passsearchparams=subcommittees=1**committeename=irrigation&minutes=0&chamber=H&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=4228&session=28-0&from=search&passsearchparams=subcommittees=1**committeename=irrigation&minutes=0&chamber=H&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=4268&session=27-0&from=search&passsearchparams=subcommittees=1**committeename=irrigation&minutes=0&chamber=H&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=4338&session=26-0&from=search&passsearchparams=subcommittees=1**committeename=irrigation&minutes=0&chamber=H&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=4636&session=25-0&from=search&passsearchparams=subcommittees=1**committeename=irrigation&minutes=0&chamber=H&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=4409&session=24-0&from=search&passsearchparams=subcommittees=1**committeename=irrigation&minutes=0&chamber=H&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=4913&session=23-0&from=search&passsearchparams=subcommittees=1**committeename=irrigation&minutes=0&chamber=H&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=4541&session=22-0&from=search&passsearchparams=subcommittees=1**committeename=irrigation&minutes=0&chamber=H&from=search",
    "https://lrl.texas.gov/committees/cmtesDisplay.cfm?cmteID=4729&session=21-0&from=search&passsearchparams=subcommittees=1**committeename=irrigation&minutes=0&chamber=H&from=search"


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
excel_file_path = r"Add Path\for\output"
df.to_excel(excel_file_path, index=False)

# Close the driver after the operation
driver.quit()
