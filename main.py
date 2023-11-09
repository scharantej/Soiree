 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create a list of parties
parties = []

# Home page
@app.route('/')
def index():
    return render_template('index.html', parties=parties)

# Create a new party
@app.route('/create_party', methods=['GET', 'POST'])
def create_party():
    if request.method == 'GET':
        return render_template('create_party.html')
    else:
        name = request.form['name']
        date = request.form['date']
        time = request.form['time']
        location = request.form['location']
        party = {'name': name, 'date': date, 'time': time, 'location': location}
        parties.append(party)
        return redirect(url_for('index'))

# Edit an existing party
@app.route('/edit_party/<int:party_id>', methods=['GET', 'POST'])
def edit_party(party_id):
    if request.method == 'GET':
        party = parties[party_id]
        return render_template('edit_party.html', party=party)
    else:
        name = request.form['name']
        date = request.form['date']
        time = request.form['time']
        location = request.form['location']
        party = parties[party_id]
        party['name'] = name
        party['date'] = date
        party['time'] = time
        party['location'] = location
        return redirect(url_for('index'))

# Delete an existing party
@app.route('/delete_party/<int:party_id>')
def delete_party(party_id):
    party = parties[party_id]
    parties.remove(party)
    return redirect(url_for('index'))

# Invite friends to a party
@app.route('/invite_friends/<int:party_id>', methods=['GET', 'POST'])
def invite_friends(party_id):
    if request.method == 'GET':
        party = parties[party_id]
        return render_template('invite_friends.html', party=party)
    else:
        friends = request.form.getlist('friends')
        party = parties[party_id]
        party['friends'] = friends
        return redirect(url_for('index'))

# Manage RSVPs for a party
@app.route('/manage_rsvps/<int:party_id>', methods=['GET', 'POST'])
def manage_rsvps(party_id):
    if request.method == 'GET':
        party = parties[party_id]
        return render_template('manage_rsvps.html', party=party)
    else:
        rsvps = request.form.getlist('rsvps')
        party = parties[party_id]
        party['rsvps'] = rsvps
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


main.py


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create a list of parties
parties = []

# Home page
@app.route('/')
def index():
    return render_template('index.html', parties=parties)

# Create a new party
@app.route('/create_party', methods=['GET', 'POST'])
def create_party():
    if request.method == 'GET':
        return render_template('create_party.html')
    else:
        name = request.form['name']
        date = request.form['date']
        time = request.form['time']
        location = request.form['location']
        party = {'name': name, 'date': date, 'time': time, 'location': location}
        parties.append(party)
        return redirect(url_for('index'))

# Edit an existing party
@app.route('/edit_party/<int:party_id>', methods=['GET', 'POST'])
def edit_party(party_id):
    if request.method == 'GET':
        party = parties[party_id]
        return render_template('edit_party.html', party=party)
    else:
        name = request.form['name']
        date = request.form['date']
        time = request.form['time']
        location = request.form['location']
        party = parties[party_id]
        party['name'] = name
        party['date'] = date
        party['time'] = time
        party['location'] = location
        return redirect(url_for('index'))

# Delete an existing party
@app.route('/delete_party/<int:party_id>')
def delete_party(party_id):
    party = parties[party_id]
    parties.remove(party)
    return redirect(url_for('index'))

# Invite friends to a party
@app.route('/invite_friends/<int:party_id>', methods=['GET', 'POST'])
def invite_friends(party_id):
    if request.method == 'GET':
        party = parties[party_id]
        return render_template('invite_friends.html', party=party)
    else:
        friends = request.form.getlist('friends')
        party = parties[party_id]
        party['friends'] = friends
        return redirect(url_for('index'))

# Manage RSVPs for a party
@app.route('/manage_rsvps/<int:party_id>', methods=['GET', 'POST'])
def manage_rsvps(party_id):
    if request.method == 'GET':
        party = parties[party_id]
        return render_template('manage_rsvps.html', party=party)
    else:
        rsvps = request.form.getlist('rsvps')
        party = parties[party_id]
        party['rsvps'] = rsvps
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
