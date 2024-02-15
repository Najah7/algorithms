def collect_strings(obj):
    result = []
    for key in obj:
        if isinstance(obj[key], str):
            result += [obj[key]]
        if isinstance(obj[key], dict):
            result += collect_strings(obj[key])
    return result


sample_dict = {
    "stuff": "foo",
    "data": {
        "val": {
            "thing": {"info": "bar", "moreInfo": {"evenMoreInfo": {"weMadeIt": "baz"}}}
        }
    },
}

print(collect_strings(sample_dict) == ["foo", "bar", "baz"])
