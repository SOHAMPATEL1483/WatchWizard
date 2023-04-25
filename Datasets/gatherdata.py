import numpy as np
import pandas as pd
import httpx
import asyncio
import time
import json
import pickle


l = pickle.load(open("imdb_list", "rb"))

df2 = pd.DataFrame()
print(len(l))


async def fetch(df2):
    j = 0
    async with httpx.AsyncClient() as client:
        reqs = []
        for i in range(0, 500):
            query = l[i]
            reqs.append(
                client.get(
                    url=f"https://api.themoviedb.org/3/movie/{query}?api_key="
                )
            )
        results = await asyncio.gather(*reqs)
        for result in results:
            temp = result.json()
            if temp.get("id") is None:
                continue
            for key in temp.keys():
                temp[key] = [json.dumps(temp[key])]
            df = pd.DataFrame().from_dict(temp)
            print(df)
            df2 = pd.concat([df2, df], ignore_index=True)
            print(j)
            j += 1
        df2.to_csv("movieinfo_final.csv", index=False)


start = time.perf_counter()
asyncio.run(fetch(df2))
end = time.perf_counter()
print(end - start)
