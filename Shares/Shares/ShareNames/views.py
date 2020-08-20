from flask import Flask,Blueprint,render_template,redirect,url_for
from Shares import db
from Shares.ShareNames.forms import AddForm,DeleteForm
from Shares.models import Company

shares_blueprint = Blueprint('Shares',__name__,template_folder='templates/ShareNames')





@shares_blueprint.route('/add',methods=['GET','POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        quantity = form.quantity.data
        Total = price * quantity

        sha = Company(name,price,quantity,Total)
        db.session.add(sha)
        db.session.commit()

        return redirect(url_for('Shares.list'))

    return render_template('add.html',form=form)

@shares_blueprint.route('/list')
def list():
    shar = Company.query.all()
    return render_template('list.html',shar=shar)

@shares_blueprint.route('/delete',methods=['GET','POST'])
def delete():
    form = DeleteForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Company.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('Shares.list'))
    return render_template('delete.html',form=form)
