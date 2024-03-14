from discord.ext import commands
import discord
import os

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())
client.remove_command("help")


@client.event
async def on_ready():
    print("Geoffrey's ready to go!")


@client.command(pass_context=True, aliases=['t'])
async def test(ctx):
    await ctx.send('$wotd')
    await ctx.send('$cd 00:02')
    await ctx.send('$meme')
    await ctx.send('$psv')


@client.command(pass_context=True, aliases=['i'])
async def info(ctx, *, arg):
    try:
        if arg not in [str(member.name) for member in ctx.guild.members]:
            await ctx.send("Member not found")
            return
        
        member = discord.utils.get(ctx.guild.members, name=arg)

        embed = discord.Embed(title="User Information", color=discord.Color(0xFFFFFF))
        embed.set_thumbnail(url=member.avatar)
        embed.add_field(name="Username", value=member.name, inline=True)
        embed.add_field(name="Discriminator", value=member.discriminator, inline=True)
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Status", value=member.status, inline=True)
        embed.add_field(name="Top Role", value=member.top_role.name, inline=True)
        embed.add_field(name="Joined Server", value=member.joined_at.strftime("%A, %B %d %Y %I:%M %p"), inline=True)
        embed.add_field(name="Joined Discord", value=member.created_at.strftime("%A, %B %d %Y %I:%M %p"), inline=True)
        await ctx.send(embed=embed)

    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")


@client.command()
async def members(ctx):
    members = ctx.guild.members
    member_list = ''
    for member in members:
        member_list += str(member.name) + ' (' + str(member.display_name) + ')' + '\n'
    embed = discord.Embed(title="Members", color=discord.Color(0xFFFFFF), description=member_list)
    await ctx.send(embed=embed)



@client.command(pass_context=True)
async def help(ctx):
    em = discord.Embed(
        title="Help",
        description=
        "***$info*** *member*\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0member info\n\n***$members***\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0member list"
    )
    await ctx.send(embed=em)


client.run(os.environ["TOKEN"])