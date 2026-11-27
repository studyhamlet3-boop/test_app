from src.data.main_db import Database
from exceptions import UserAlreadyExistsError

async def insert_user_db(email: str, password: str): # Inserts a new user record into the users table: returns None: raises UserAlreadyExistsError
    async with Database.pool.acquire() as conn:
        # Pass the record_id variable into the query
        async with conn.transaction(): # Start a transaction
            existing_user = await conn.fetchrow('SELECT email FROM users WHERE email = $1', email) # Check if the email already exists
            if existing_user:
                # Handle the case where the user already exists
                raise UserAlreadyExistsError()
            
            await conn.execute(
                '''
                INSERT INTO users (email, password_hash)
                VALUES ($1, $2)
                ''',
                email,
                password
            )
async def get_user_info_by_email(email: str): #Returns users everything by email: returns dict or None
    async with Database.pool.acquire() as conn:
        user = await conn.fetchrow('SELECT * FROM users WHERE email = $1', email)
        return {'id': user['id'], 'email': user['email'], 'password': user['password_hash'], 'verified': user['is_verified']} if user else None #?<---------------Pattern
