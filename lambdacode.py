import json

import account_number_validation as accountValidationLayer

def lambda_handler(event, context):
    
    #print(event)
    
    if(accountValidationLayer.validateAccountNumber(event['accountNumber'])):
        print('Account created');

        return {
            'statusCode': 200,
            'body': json.dumps('Account created!')
        }
        
    else:
        
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid Account number!')
        }
