import string, random 

#Function to genreate random shortcode. 
def generate_shortcode(lenghth=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(lenghth))