from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db
import json


views = Blueprint('views', __name__)

@views.route('/',methods=['GET', 'POST'])
@login_required
def home():
	if request.method == 'POST':
		note=request.form.get('note')

		if len(note) < 1:
			flash('Note is too short!', category='error')
		else:
			new_note = Note(data=note, user_id=current_user.id)
			db.session.add(new_note)
			db.session.commit()
			flash('Note added!', category='success')
	return render_template("home.html", user=current_user)


@views.route("/edit_note/<int:note_id>", methods=['GET', 'POST'])
@login_required
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)
    if request.method == "POST":
        note.data = request.form['note']
        db.session.commit()
        flash('Your post has been updated!')
        return redirect(url_for('views.home'))
    
    return render_template('edit_note.html', note=note)

@views.route("/demo", methods=['GET'])
def demo():
    return render_template('demo.html')

@views.route('/delete-note',methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('Your note has been deleted!')
    return jsonify({})

# @views.route("/edit-note", methods=['GET', 'POST'])
# @login_required
# def edit_note():
# 	note = json.loads(request.data)
# 	noteId = note['noteId']
# 	note = Note.query.get(noteId)
# 	if note:
# 		if note.user_id == current_user.id:
# 			note.data = request.form['notes']
# 			db.session.commit()
# 			flash('Your note has been updated!')
# 			return redirect(url_for('views.home'))
# 	return render_template('edit_note.html', note=note)


