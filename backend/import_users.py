import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.models.users import User, Role, ActivationKey
from app.core.config import settings
from datetime import datetime
import traceback

# Database connection setup
DATABASE_URL = settings.SQL_URL
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# CSV File Path (Change accordingly)
CSV_FILE_PATH = "user_dump.csv"

# Function to parse CSV file
def parse_csv(file_path):
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        users_data = []
        for row in reader:
            users_data.append({
                "username": row["username"],
                "password": row["password"],  # Assume it's hashed
                "email": row["email"],
                "user_role": row["role"],
                "joining_date": datetime.strptime(row["joining_date"], "%Y-%m-%d"),
                "last_login": datetime.strptime(row["last_login"], "%Y-%m-%d") if row["last_login"] else None,
                "account_status": row["account_status"].lower() == "active",
                "activation_key": row.get("activation_key")  # Can be None
            })
    return users_data

# Function to insert records using transactions
def insert_users(users_data):
    session = Session()
    try:
        for user_data in users_data:
            # Check if role exists, create if not
            role = session.query(Role).filter_by(name=user_data["user_role"]).first()
            if not role:
                role = Role(name=user_data["user_role"])
                session.add(role)
                session.commit()  # Commit to get role ID

            # Create user object
            new_user = User(
                username=user_data["username"],
                password=user_data["password"],
                email=user_data["email"],
                user_role=role.id,  # Foreign key
                joining_date=user_data["joining_date"],
                last_login=user_data["last_login"],
                account_status=user_data["account_status"]
            )
            session.add(new_user)
            session.commit()  # Commit to get user ID

            # Insert Activation Key if available
            if user_data["activation_key"]:
                activation_key = ActivationKey(
                    user_id=new_user.id,
                    key=user_data["activation_key"],
                    created_at=datetime.now(),
                    expires_at=datetime.now().replace(year=datetime.now().year + 1),
                    used=False
                )
                session.add(activation_key)

        session.commit()  # Final commit after inserting all users
        print("✅ User data successfully inserted!")

    except Exception as e:
        session.rollback()  # Rollback transaction on error
        print("❌ Error inserting data:", str(e))
        traceback.print_exc()
    finally:
        session.close()

# Main execution
if __name__ == "__main__":
    users_data = parse_csv(CSV_FILE_PATH)
    insert_users(users_data)
