
from personal_website import db


class Blogs(db.Model):
    __tablename__ = 'blogs'
    __table_args__ = {'extend_existing': True}

    # `id` int(11) NOT NULL,
    id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    # `title` varchar(255) DEFAULT NULL,
    title = db.Column(db.String, unique=True)
    # `link` varchar(255) DEFAULT NULL,
    link = db.Column(db.String, unique=True)
    # `created` date DEFAULT NULL,
    created = db.Column(db.Date)
    # `start_date` date DEFAULT NULL,
    start_date = db.Column(db.Date)
    # `end_date` date DEFAULT NULL,
    end_date = db.Column(db.Date)
    # `type` varchar(255) DEFAULT NULL,
    type = db.Column(db.String)
    # `description` text DEFAULT NULL,
    description = db.Column(db.Text)
    # `image` varchar(255) DEFAULT NULL,
    image = db.Column(db.String)
    # `content` text DEFAULT NULL,
    content = db.Column(db.Text)
    # `hidden` tinyint(1) NOT NULL DEFAULT
    hidden = db.Column(db.Boolean, nullable=False)
    last_updated = db.Column(db.Date)
