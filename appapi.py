from fastapi import FastAPI

# Create a FastAPI app instance
app = FastAPI()

# Define the richest_people_list dictionary
richest_people_list = {
    "Elon Musk": "280 Billion USD",
    "Jeff Bezos": "250 Billion USD",
    "Bill Gates": "190 Billion USD",
    "Mark Zuckerberg": "150 Billion USD"
}

# Define the endpoint for retrieving the richest people list
@app.get("/richest-people")
def get_richest_people():
    return richest_people_list
