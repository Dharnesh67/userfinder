# Install the dependencies
pip install -r requirements.txt

# Running API
uvicorn main:app --reload

# API Endpoint
/checkDomain

# Pass Attributes
/checkDomain?name=value&type=value
Type-> M for detailed search(Avg 2.5 mins)
Type-> F for quick search(Avg 1.5 mins)

# Intermediatory files Generated
1- subFileIndex.py 
2- namedomainAvailable.txt
3- namedomainValid.txt
Once processessed; these are deleted automatically