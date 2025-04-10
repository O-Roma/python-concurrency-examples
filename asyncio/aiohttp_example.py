import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = [
        "https://api.github.com",
        "https://jsonplaceholder.typicode.com/todos/1"
    ]
    
    #actually do the async requests
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        
        for i, response in enumerate(responses):
            print(f"\nResponse from URL {i+1}:\n{response[:200]}...")

if __name__ == "__main__":
    asyncio.run(main())