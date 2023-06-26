import aiohttp
import asyncio
import json
import logging
import numpy as np
import pandas as pd


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s.%(msecs)03d:%(levelname)s:%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("responses.log"),
        logging.StreamHandler()
    ]
)

async def async_request(dataframe, extractor=None):
    async def send_request(session, index, row):
        if "url" not in row or "method" not in row:
            raise ValueError("Expected url and method columns")

        reqeust_params = {"params", "headers", "timeout", "data", "json"}
        options = {key: row[key] for key in reqeust_params if key in row}
        caller = {
            "GET": session.get,
            "POST": session.post,
            "PUT": session.put,
            "PATCH": session.patch,
            "DELETE": session.delete
        }

        logging.info({"id": index} | row.to_dict())
        async with caller[row.method](row.url, **options) as resp:
            length = 0 if pd.isnull(resp.content_length) else resp.content_length
            content = await resp.read()
            response = extractor(content) if extractor is not None else content
            dataframe.at[index, "status"] = resp.status
            dataframe.at[index, "length"] = length
            dataframe.at[index, "target"] = resp.url
            dataframe.at[index, "headers"] = json.dumps(dict(resp.headers))
            dataframe.at[index, "response"] = response

    timeout = aiohttp.ClientTimeout(total=None)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = (
            send_request(session, index, row)
            for index, row  in dataframe.iterrows()
        )
        await asyncio.gather(*tasks)
    return dataframe.astype({"status": "Int16", "length": "Int64"})


def main():
    size = 100
    df = pd.DataFrame(np.random.randint(1, 10e7-1, size=size).astype(str), columns=["url"])
    df["url"] = "https://stackoverflow.com/questions/" + df.url
    df["method"] = "GET"
    result = asyncio.run(async_request(df))
    print(result.info())


if __name__ == "__main__":
    main()
