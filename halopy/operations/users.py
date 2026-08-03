from halopy.paths import Users

def delete_users(client,user_ids):
    for user_id in user_ids:
        client.delete(Users,id=user_id)
