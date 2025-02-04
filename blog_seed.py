from app.database import db
from app.models import Blogs
from app import create_app

# Initialize the Flask app
app = create_app()


# Seed the database
with app.app_context():
    new_post = Blogs(
        title="Asphalt vs. Concrete: Which is Best for Your Driveway?", # type: ignore
        slug="asphalt-vs-concrete", # type: ignore
    )

    # Add and commit the post to the database
    db.session.add(new_post)
    db.session.commit()

    print("Blog post added successfully!")
