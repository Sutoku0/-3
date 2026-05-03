users = ['Admin', 'Guest', 'User', 'Bot']

index_user = users.index('User')
users[index_user] = 'Moderator'

users[-1] = 'SuperAdmin'

users.append('Newbie')

print(f"Обновленный список пользователей: {users}")