from sqlalchemy import Column, Integer, String, DateTime,LargeBinary,ForeignKey
from sqlalchemy.orm import declarative_base, relationship, backref
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

engine = create_engine('postgresql://postgres.qzhfdmgnjughkplwfcem:&KUzW)~j&_XY7,z@aws-0-us-west-1.pooler.supabase.com:5432/postgres')
class User(Base):
  __tablename__ = 'User'

  id = Column(Integer(), primary_key=True)
  fullname = Column(String(100), nullable=False)
  email = Column(String(100), nullable=False)
  websiteurl = Column(String(100), nullable=False)
  phonenumber = Column(Integer(), nullable=True)
  qr_images = relationship('QRCode', back_populates='user')
  created_on = Column(DateTime(), default=datetime.now)


class QRCode(Base):
  __tablename__ = 'qr_codes'

  id = Column(Integer, primary_key=True)
  code_data = Column(LargeBinary)
  user_id = Column(Integer, ForeignKey('User.id'))
  user = relationship('User', back_populates ='qr_images')

def add_to_db(qrcode, user):
  try:
    with engine.connect() as connection_str:
      print('Successfully connected to the PostgreSQL database')
      Base.metadata.create_all(engine)
      Session = sessionmaker(bind=engine)
      session = Session()
      user_details = User(**user)
      session.add(user_details)
      session.commit()
      user1= QRCode(code_data=qrcode, user=user_details)
      session.add(user1)
      session.commit()
      print("added to db sucessfully")

  except Exception as ex:
    print(f'Sorry failed to connect: {ex}')

  
