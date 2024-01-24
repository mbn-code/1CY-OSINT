# 1CY-OSINT - Open Source Intelligence Tool

1CY-OSINT is a Python-based open-source intelligence tool designed for gathering information about various targets. It provides capabilities for obtaining details related to IP addresses, names/usernames, phone numbers, and email addresses. The tool utilizes external services and command-line tools to gather and present the information in an organized manner.

**Version:** BETA-V1.2

## Features

1. **IP Information:**
   - Retrieve information about a specific IP address.
   - Perform `whois`, `dig`, and `sslscan` operations on the provided IP.
   - Save the obtained information in text files for reference.

2. **Name/Username Scan:**
   - Conduct a scan based on a person's name or username.
   - Utilizes the `sherlock` tool to search for online profiles.
   - Outputs the results to a text file.

3. **Phone Number Information:**
   - Obtain basic information about a phone number using the `phonenumbers` library.
   - Includes carrier information, geolocation, and validity check.
   - Save the details in a text file.

4. **Email Information:**
   - Run an email OSINT scan.
   - Utilizes services like `emailrep` and `mailfy` to gather information.
   - Conducts an alternative email reputation check and saves the results.

5. **General Commands:**
   - Includes a few general commands for displaying the tool's version and help information.
   - Allows running arbitrary commands in the system.

## Usage

1. Run the script using Python 3.10:

    ```bash
    python3.10 1cy-osint.py
    ```

2. Follow the prompts and input the required information (e.g., IP, name, phone number, email).

## Dependencies

- Python 3.10
- `requests`, `phonenumbers` (install using `pip install requests phonenumbers`)
- External tools: `whois`, `dig`, `sslscan`, `lbd`, `sherlock`, `emailrep`, `mailfy` (make sure they are installed on your system)

## Notes

- The tool automatically checks for required Python modules and attempts to install them if missing.
- Some features require external tools, so ensure they are installed on your system.
- Be cautious when using the tool and respect privacy and legal boundaries.

**Disclaimer:** Use this tool responsibly and in accordance with applicable laws and ethical standards. The authors are not responsible for any misuse or unlawful activities conducted with this tool.
