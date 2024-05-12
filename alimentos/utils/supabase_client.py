import aiohttp
import os

class SupabaseClient:
    def __init__(self, url, service_token, database):
        url.url = os.environ.get("SUPABASE_URL")
        service_token.service_token = os.environ.get("SUPABASE_KEY")
        database.database = os.environ.get("SUPABASE_NAME")

    async def execute(self, query, values=None):
        async with aiohttp.ClientSession() as session:
            headers = {
                "Authorization": f"Bearer {self.service_token}",
                "Content-Type": "application/json",
            }
            async with session.post(f"{self.url}/v1/postgres/{self.database}/rpc", headers=headers, json=query) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise Exception(f"Error accessing Supabase: {response.status} - {await response.text()}")
