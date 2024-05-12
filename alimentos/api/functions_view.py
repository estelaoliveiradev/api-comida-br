from supabase import SupabaseClient
import os
import asyncio

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_SERVICE_TOKEN = os.environ.get("SUPABASE_KEY")
SUPABASE_DATABASE = os.environ.get("SUPABASE_NAME")
supabase = SupabaseClient(
    SUPABASE_URL, SUPABASE_SERVICE_TOKEN, SUPABASE_DATABASE)


async def get_almoco():
    try:
        # Assuming you have a configured supabase client
        response = await supabase.rpc("getalmoco")
        data = response.data
    except Exception as error:
        print(f"An error occurred: {error}")  # Use print for logging
    else:
        print(data)  # Use print for logging

asyncio.run(get_almoco())


async def get_janta():
    try:
        # Assuming you have a configured supabase client
        response = await supabase.rpc("getjanta")
        data = response.data
    except Exception as error:
        print(f"An error occurred: {error}")  # Use print for logging
    else:
        print(data)  # Use print for logging

asyncio.run(get_janta())
