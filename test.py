import asyncio

# async def boil_water():
#     print("🔵 Boiling...")
#     await asyncio.sleep(2)
#     print("✅ Done boiling")

# async def make_tea():
#     await boil_water()
#     print("🫖 Adding tea")
#     return "🍵 Tea ready"

# result = asyncio.run(make_tea())
# print("Result:", result)


# def boil_water():
#     print("🔵 Boiling...")
#     asyncio.sleep(2)
#     print("✅ Done boiling")

# def make_tea():
#     boil_water()
#     print("🫖 Adding tea")
#     return "🍵 Tea ready"

# result = asyncio.run(make_tea())
# print("Result:", result)

# import time

# def make_tea():
#     print("🔵 Boiling water...")
#     time.sleep(3)  # Pauses the whole program for 3 seconds
#     print("✅ Done boiling")
#     print("🫖 Adding tea")
#     return "🍵 Tea ready"

# result = make_tea()
# print("Result:", result)


async def hey():
    print('salam')
    await asyncio.sleep(2)
    print('salam2')

async def goodbye():
    print('hey')



async def main():
    await asyncio.gather(
        hey(),
        goodbye()
    )

asyncio.run(main())