from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
@app.route('/entry1')
def entry_page():
    return render_template('entry.html', the_title='Welcome to Search4Letters!', the_title2='Search4Letters')


@app.route('/search4', methods=['POST'])
def search4()->'html':
    phrase = set(request.form['phrase'].lower())
    chars = set(request.form['letters'].lower())
    #If letters is blank search set('aeiou')
    if bool(chars)==False:
        chars = set('aeiou')

    title='Here are your results: '
    title2='Results'
    results = phrase.intersection(chars)
    if bool(results) == False:
        results2 = "None"
    else:
        results2 = str(phrase.intersection(chars)).upper()
    return render_template('results.html', the_phrase=request.form['phrase'], the_letters=request.form['letters'], the_title=title, the_title2=title2, the_results=results2)

app.run(debug=True)