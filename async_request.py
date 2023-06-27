import aiohttp
import asyncio
import json
import logging
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

async def async_requests(dataframe, extractor=None):
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
        async with caller[row.method.upper()](row.url, **options) as resp:
            length = 0 if pd.isnull(resp.content_length) else resp.content_length
            dataframe.at[index, "status"] = resp.status
            dataframe.at[index, "length"] = length
            dataframe.at[index, "target"] = resp.url
            dataframe.at[index, "headers"] = dict(resp.headers)
            dataframe.at[index, "response"] = await resp.read()

    timeout = aiohttp.ClientTimeout(total=None)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = (
            send_request(session, index, row)
            for index, row  in dataframe.iterrows()
        )
        await asyncio.gather(*tasks)

    if extractor is not None:
        dataframe.response = dataframe.response.apply(extractor)

    return dataframe.astype({"status": "Int16", "length": "Int64"})


def main():
    size = 100
    df = pd.read_csv("data.csv", keep_default_na=False).sample(size).astype({
        "SITE_NAME": "string",
        "LOC_CODE": "string",
        "SITE_LOCATIONS": "string"
    })
    df.columns = df.columns.str.lower()
    params = df.to_dict("records")
    df["url"] = "https://id.execute-api.region.amazonaws.com/stage/commands"
    df["method"] = "GET"
    df["params"] = params
    df["headers"] = [{"Content-Type": "application/json"}] * len(df)

    result = asyncio.run(async_requests(df, extractor=json.loads))
    print(result[["url", "status", "response"]])


if __name__ == "__main__":
    main()
