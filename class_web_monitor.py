import requests

class WebappMonitor:
    def __init__(self):
        self.websites = []

    def add_website(self, website):
        if len(self.websites) >= 1000:
            return "Maximum number of websites (1000) reached. Cannot add more."
        
        if not website.startswith("http://") and not website.startswith("https://"):
            website = "https://" + website
        
        if website.endswith("/"):
            website = website[:-1]
        
        if website in self.websites:
            return f"Website {website} is already in the monitoring list"
        
        self.websites.append(website)
        return f"Website {website} added to the monitoring list"

    def remove_website(self, website):
        if not website.startswith("http://") and not website.startswith("https://"):
            website = "https://" + website
        
        if website.endswith("/"):
            website = website[:-1]

        if website in self.websites:
            self.websites.remove(website)
            return f"Website {website} removed from the monitoring list"
        else:
            return f"Website {website} not found in the monitoring list"

    def check_connectivity(self):
        if not self.websites:
            return "No websites in the monitoring list"

        results = []
        for website in self.websites:
            try:
                response = requests.get(website)
                if response.status_code == 200:
                    results.append(f"{website}: connected")
                else:
                    results.append(f"{website}: disconnected")
            except requests.ConnectionError:
                results.append(f"{website}: connection error")

        return "\n".join(results)

    def list_websites(self):
        if not self.websites:
            return "No websites in the monitoring list"
        
        return "\n".join(self.websites)
