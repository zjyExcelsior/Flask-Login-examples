from myapp import create_app, db

def create_all_db(app):
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    app = create_app()
    create_all_db(app)
    app.run(debug=True)
