from flask import Flask, render_template

app = Flask(__name__, static_folder='assets')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

if __name__ == '__main__':
    app.run()

    
# The 404 errors indicate that the requested assets are not found.
# To fix this issue, you need to make sure that the assets are properly configured and accessible in your Flask application.

# First, make sure that the assets folder is located in the correct directory relative to your app.py file.
# It should be in the same directory or a subdirectory.

# Next, you need to configure Flask to serve the static assets.
# Add the following line of code before the `if __name__ == '__main__':` line:


# This line tells Flask to serve static files from the 'assets' folder.

# Finally, make sure that the asset URLs in your HTML templates are correct.
# For example, if you have an image tag like this:
# <img src="/assets/images/hamburger.svg" alt="Hamburger">

# The 'src' attribute should match the relative path to the asset from the root URL of your Flask application.

# After making these changes, restart your Flask application and check if the assets are now being detected correctly. 

