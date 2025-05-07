from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('aboutus.html')

@app.route('/about-brenda')
def bp_about():
    return render_template('about-brenda.html')

@app.route('/about-jake')
def jake_about():
    return render_template('about-jake.html')

@app.route('/about-nash')
def nash_about():
    return render_template('about-nash.html') 

@app.route('/about-laine')
def laine_about():
    return render_template('about-laine.html')

@app.route('/contact')
def contact():
    return render_template('contactus.html')

@app.route('/employer-contact')
def employer_contact():
    return render_template('employer-contact.html')

@app.route('/candidate-contact')
def candidate_contact():
    return render_template('candidate-contact.html')

@app.route('/jobs')
def jobs():
    return render_template('jobs.html')

@app.route('/employers')
def employers():
    return render_template('employers.html')

@app.route('/candidates')
def candidates():
    return render_template('candidates.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog1')
def blog1():
    return render_template('blog1.html')

@app.route('/blog2')
def blog2():
    return render_template('blog2.html')

@app.route('/blog3')
def blog3():
    return render_template('blog3.html')

@app.route('/norest')
def norest():
    return render_template('norest.html')

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy-policy.html')

@app.route('/cookie-policy')
def cookie_policy():
    return render_template('cookie-policy.html')

if __name__ == '__main__':
    app.run(debug=True)
