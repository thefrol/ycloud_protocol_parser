import logging

from protocol_parsers import MosffParser, MosffPlayerParser, MosffTeamParser,YflParser 

from stack_log import StackLogger


PROTOCOL_URL_PARAMETER_NAME='protocol_url'
MATCH_TIME_PARAMETER_NAME='match_time'
PLAYER_URL_PARAMETER_NAME='player_url'
TEAM_URL_PARAMETER_NAME='team_url'


def check_input(event):
    if event['queryStringParameters'].get(PROTOCOL_URL_PARAMETER_NAME):
        if event['queryStringParameters'].get(MATCH_TIME_PARAMETER_NAME) is not None:
            try:
                int(event['queryStringParameters'].get(MATCH_TIME_PARAMETER_NAME))
            except Exception:
                return False
        return 'protocol'
    elif event['queryStringParameters'].get(PLAYER_URL_PARAMETER_NAME):
        return 'player'
    elif event['queryStringParameters'].get(TEAM_URL_PARAMETER_NAME):
        return 'team'
    else:
        return False
    

def handler(event, context):
    log_stack=StackLogger()
    logger=logging.getLogger()
    logger.addHandler(log_stack)

    input_type=check_input(event)
    if not input_type:
            return {
        'statusCode': 400,
        'body': f'Bad input, maybe field {PROTOCOL_URL_PARAMETER_NAME} or {PLAYER_URL_PARAMETER_NAME} or {TEAM_URL_PARAMETER_NAME} not specified. or {MATCH_TIME_PARAMETER_NAME} cant be converted to int',
    }

    protocol_URL=event['queryStringParameters'].get(PROTOCOL_URL_PARAMETER_NAME)
    player_URL=event['queryStringParameters'].get(PLAYER_URL_PARAMETER_NAME)
    team_URL=event['queryStringParameters'].get(TEAM_URL_PARAMETER_NAME)
    match_time=event['queryStringParameters'].get(MATCH_TIME_PARAMETER_NAME)



    if input_type=='protocol':
        try:
            if match_time:
                match_time=int(match_time)
            
            if 'mosff' in protocol_URL:
                result=MosffParser(protocol_URL,match_time).to_rbdata()
            elif 'yfl' in protocol_URL:
                result=YflParser(protocol_URL).to_rbdata()
            else:
                raise Exception('Unknown url')


            return {
            'statusCode': 200,
                'body': {
                    'protocol':result,
                    'log':log_stack.collect(),
                },
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': 'parsing protocol failed',
                'err': str(e)
            }
    if input_type=='player':
        try:
            result=MosffPlayerParser(player_URL).to_rbdata()

            return {
            'statusCode': 200,
                'body': {
                    'player':result,
                    'log':log_stack.collect()
                },
            }
        except:
            return {
                'statusCode': 500,
                'body': f'parsing player {player_URL} failed',
            }
    if input_type=='team':
        try:
            result=MosffTeamParser(team_URL).to_rbdata()

            return {
            'statusCode': 200,
                'body': {
                    'team':result,
                    'log':log_stack.collect()
                },
            }
        except:
            return {
                'statusCode': 500,
                'body': f'parsing team {team_URL} failed',
            }
