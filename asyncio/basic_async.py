import asyncio

async def say_after(delay, message):
    await asyncio.sleep(delay)
    print(message)
    
async def main():
    await asyncio.gather(
        say_after(3,"Hello"),
        say_after(2, "World")
    )

if __name__ == "__main__":
    asyncio.run(main())