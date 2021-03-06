from discord.ext import commands
from gyoji.commands import log

class Slohyo(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    
    # Commands
    
    @commands.command(
        name='submit_slohyo',
        aliases=['slohyo'],
        description='Submit a Slohyo form in discord. Requires you to mention your opponent. GyojiBot will direct message you to complete the form.'
    )
    async def submit_slohyo(self, ctx):
        author = ctx.author
        opponent = 'nil'
        response_message = f'User {author} is submitting a Slohyo for their bout against {opponent}'
        log.info(response_message)
        await ctx.send(response_message)
        # TODO: Implement direct messaging logic, filling out of the slohyo form
        pass

# Cog registration

def setup(client):
    client.add_cog(Slohyo(client))
