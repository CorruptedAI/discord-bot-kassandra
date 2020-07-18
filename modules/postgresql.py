DEFAULT_VALUES = """
    INSERT INTO users (user_id, guild_id, level, exp, coins, tickets, daily, description, background, language)
    VALUES ($1, $2, 1, 0, 100, 20, '1945-05-08 21:43:10', 'No information given', 'https://cdn.discordapp.com/avatars/708690846735663184/2d5960c88a4169535d9796dba86b3739.webp?size=1024', 'en')
    RETURNING *
"""

SELECT = """
    SELECT *
    FROM users
    WHERE user_id = $1
    AND guild_id = $2
"""

COINS = """
    UPDATE users 
    SET coins = $3
    WHERE user_id = $1 AND guild_id = $2
"""

TICKETS_COINS = """
    UPDATE users 
    SET tickets = $3
    WHERE user_id = $1 AND guild_id = $2
"""
