import asyncio
from fastmcp import Client

async def main():

    async with Client("mcpserver.py") as client:

        tools = await client.list_tools()
        print("Tools:", tools)

        result = await client.call_tool(
            "get_weather",
            {"city": "London"}
        )

        print(result.content[0].text)

if __name__ == "__main__":
    asyncio.run(main())