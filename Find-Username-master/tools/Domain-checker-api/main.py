from fastapi import FastAPI
import os
import subprocess
import tldsGenerator


app = FastAPI()

code = """
import dns.resolver
import  socket
import whois

def domain_valid(domain):
    for _ in range(3):
        try:
            w = whois.whois(domain)
            if w.domain_name:
                return domain, True
        except Exception:
            pass  # WHOIS failed, retrying

    try:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ["8.8.8.8"]  # Use Google DNS
        resolver.resolve(domain, 'NS')  # Resolves if domain exists
        return domain, True
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.LifetimeTimeout, dns.resolver.NoNameservers):
        pass  # If DNS lookup fails, continue

    try:
        socket.gethostbyname(domain)
        return domain, True
    except socket.gaierror:
        return domain, False  # Final fallback

def process_domain_check(name, tlds):

    valid_domains = ''  
    available_domains = '' 

    for tld in tlds:
        domain, exists = domain_valid(name+'.'+tld)
        if exists:
            valid_domains+= '\\n'+domain
        else:
            available_domains+= '\\n'+domain
    
    f1 = name+'domainValid.txt'
    f2 = name+'domainAvailable.txt'

    with open(f1, 'a') as file:
        file.write(valid_domains)
    
    with open(f2, 'a') as file:
        file.write(available_domains)
    
if __name__=='__main__':
    process_domain_check(name, tlds)
"""   


@app.get("/checkDomain")
def checkDomain(name: str, type: str):
    if type=='M':
        tlds = tldsGenerator.get_tlds()
    else:
        tlds = [
            "net", "me", "org", "us", "info", "la", "asia", "biz", "tv", "ws", "nyc", "okinawa", "online", "network", "ninja", "photo", "photography", "photos", "pics", "pictures", "pink", "pizza", "place", "plumbing", "press","productions", "reisen", "repair", "report", "republican", "rest", "restaurant", "reviews", "rich", "rip", "rocks", "paris", "partners", "sale", "sarl", "schule", "shiksha", "shoes", "singles", "social", "solar", "solutions", "space", "support", "surgery", "systems", "tattoo", "tax", "services", "sexy", "technology", "tips", "tires", "land", "juegos", "kaufen", "kim", "kitchen", "kiwi", "immo", "immobilien", "jetzt", "ink", "institute", "insure", "international", "investments", "guide", "guitars", "guru", "haus", "help", "hiphop", "holdings", "holiday", "host", "hosting", "house", "lawyer", "lease", "legal", "life", "lighting", "limited", "limo", "link", "loans", "london", "luxury", "maison", "management", "market", "marketing", "nagoya", "navy", "media", "memorial", "menu", "moda", "money", "mortgage", "blackfriday", "blue", "boutique", "builders", "business", "buzz", "bz", "auction", "audio", "band", "bar", "bid", "bike", "bio", "associates", "attorney", "agency", "airforce", "academy", "accountants", "coach", "codes", "coffee", "bargains", "bayern", "archi", "cab", "camera", "camp", "capital", "cards", "care", "careers", "casa", "cash", "catering", "cc", "center", "ceo", "cheap", "christmas", "church", "city", "claims", "company", "construction", "consulting", "contractors", "cool", "deals", "degree", "delivery", "democrat", "dental", "dentist", "desi"
        ]
    processes = []  # Store subprocesses

    for index in range(0, len(tlds), 5):
        n_tlds = tlds[index:index+5]
        filename = f'subFile{index}.py'
        
        # Create the Python file
        with open(filename, "w") as file:
            file.write(f"name='{name}'\ntlds={n_tlds}\n{code}")
        
        # Start the script (non-blocking)
        process = subprocess.Popen(["python", filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        processes.append((filename, process))  # Store process with filename

    for filename, process in processes:
        process.wait()  # Wait for each script to complete
        os.remove(filename)  # Now delete the file safely

    with open(f'{name}domainValid.txt', 'r') as f1:
        domainsV = f1.read().split()
       
    with open(f'{name}domainAvailable.txt', 'r') as f1:
        domainsA = f1.read().split()

    os.remove(f'{name}domainValid.txt')
    os.remove(f'{name}domainAvailable.txt')

    return {'Valid Domains': domainsV, 'Available Domains': domainsA}