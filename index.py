from protocol_parsers import MosffParser

POST_URL_PARAMETER_NAME='protocol_url'
POST_MATCH_TIME_PARAMETER_NAME='match_time'

def check_input(event):
    if event['queryStringParameters'].get(POST_URL_PARAMETER_NAME) is None:
        return False
    if event['queryStringParameters'].get(POST_MATCH_TIME_PARAMETER_NAME) is not None:
        try:
            int(event['queryStringParameters'].get(POST_MATCH_TIME_PARAMETER_NAME))
        except Exception:
            return False
    return True

def handler(event, context):
    if not check_input(event):
            return {
        'statusCode': 400,
        'body': f'Bad input, maybe field {POST_URL_PARAMETER_NAME} not specified. or {POST_MATCH_TIME_PARAMETER_NAME} cant be converted to int',
    }

    protocol_URL=event['queryStringParameters'].get(POST_URL_PARAMETER_NAME)
    match_time=event['queryStringParameters'].get(POST_MATCH_TIME_PARAMETER_NAME)

    if match_time:
        match_time=int(match_time)

    try:
        result=MosffParser(protocol_URL,match_time).to_rbdata()

        return {
           'statusCode': 200,
            'body': {
                'protocol':result,
                'log':None
            },
        }
    except:
        return {
            'statusCode': 500,
            'body': 'parsing failed',
         }

