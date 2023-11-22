import dns.resolver
import pandas as pd

# Function to check for MX records of a domain
def check_mx_record(domain):
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        return "Found", [record.to_text() for record in mx_records]
    except Exception as e:
        return "Not Found", str(e)

# Read domain names from the file
with open('Domain.txt', 'r') as file:
    domain_names = file.readlines()

# Remove leading and trailing whitespaces (e.g., newline characters)
domain_names = [domain.strip() for domain in domain_names if domain.strip() != '']

# Initialize a list to hold the results
results = []

# Check MX records for the domains (you can slice the list to check a subset)
for domain in domain_names:
    status, detail = check_mx_record(domain)
    results.append([domain, status, detail])

# Create a DataFrame to hold the results
df_results = pd.DataFrame(results, columns=['Domain Name', 'MX Record Status', 'Details'])

# Save the DataFrame to a CSV file
df_results.to_csv('MX_Record.csv', index=False)
