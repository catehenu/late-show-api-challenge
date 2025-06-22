from server.app import create_app, db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

app = create_app()
with app.app_context():
    db.create_all()
    # Sample Guests
    g1 = Guest(name="John Doe", occupation="Comedian")
    g2 = Guest(name="Jane Smith", occupation="Actor")
    db.session.add_all([g1, g2])
    # Sample Episodes
    e1 = Episode(date="2025-06-30", number=1)
    e2 = Episode(date="2025-07-07", number=2)
    db.session.add_all([e1, e2])
    db.session.commit()
    # Sample Appearances
    a1 = Appearance(rating=4, guest_id=g1.id, episode_id=e1.id)
    a2 = Appearance(rating=5, guest_id=g2.id, episode_id=e2.id)
    db.session.add_all([a1, a2])
    db.session.commit()
    print("Seed data inserted.")
