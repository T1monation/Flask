from blog.app import create_app

app = create_app()


@app.cli.command("create-admin")
def create_admin():
    from blog.models import User
    from blog.extensions import db

    user_email = input("Input user email: ")
    admin_candidate = User.query.filter_by(email=user_email).one_or_none()
    print(admin_candidate)
    if admin_candidate:
        db.session.query(User).filter(User.email == user_email).update(
            {User.is_admin: True}, synchronize_session=False
        )
    else:
        print("User dosn't exist!")
